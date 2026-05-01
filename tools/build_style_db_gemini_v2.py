"""
Builds a style database using Gemini VLM (V2).

Features:
1. Extracts frames at 1 fps (or custom fps).
2. Uses Gemini 1.5 Flash to classify frames in batches (same slide vs new slide vs build).
3. Uses Gemini to analyze layout of each unique slide.
4. Saves high-quality slide images and rich metadata.
5. Optimized for speed (batch processing) and cost.

Usage12:     python tools/build_style_db_gemini_v2.py --input-dir data_reference/final --output-dir data_reference/style_db_refined_final
"""

import sys
import argparse
from pathlib import Path
import logging
import json
import cv2
import numpy as np
import re
from typing import List, Dict, Tuple, Optional
from tqdm import tqdm

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from tools.gemini_frame_comparator import GeminiFrameComparator
from utils.logger import get_logger


class GeminiStyleDBBuilderV2:
    def __init__(
        self,
        output_dir: Path,
        config_path: str = "config.yml"
    ):
        self.output_dir = Path(output_dir)
        self.logger = get_logger("GeminiStyleDBBuilderV2")
        
        # Initialize Gemini client
        self.gemini = GeminiFrameComparator(config_path=Path(config_path), logger=self.logger)
        
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Processing metrics
        self.batch_calls = 0
        self.layout_calls = 0
        self.total_frames_sampled = 0
        self.batch_size = 15 # Default

    def process_video(
        self,
        video_path: Path,
        output_dir: Path,
        skip_if_exists: bool = True
    ) -> Dict:
        """
        Process a single video to extract slides and builds.
        
        Args:
            video_path: Path to the mp4 video
            output_dir: Directory to save output (images + metadata)
            skip_if_exists: Skip if metadata.json already exists
            
        Returns:
            Metadata dict
        """
        video_path = Path(video_path)
        output_dir = Path(output_dir)

        if skip_if_exists and (output_dir / "metadata.json").exists():
            self.logger.info(f"Skipping {video_path.name} (already processed)")
            with open(output_dir / "metadata.json", "r") as f:
                return json.load(f)

        # Step 1: Extract frames
        self.logger.info(f"=== Processing: {video_path.name} ===")
        frames, duration = self._extract_frames(video_path)
        self.logger.info(f"Extracted {len(frames)} frames (sampled at 1.0 fps)")

        if len(frames) < 2:
            self.logger.warning(f"Too few frames in {video_path.name}")
            return {}

        # Step 2: Classify all frames with batch Gemini calls
        all_labels = self._classify_all_frames(frames)

        # Step 3: Assemble slides and builds
        slides = self._assemble_slides(frames, all_labels)
        self.logger.info(f"Detected {len(slides)} slides")

        # Step 4: Analyze layouts
        layouts = self._analyze_layouts(frames, slides)

        # Step 5: Find title slide
        title_slide_idx = self._find_title_slide(slides, layouts)

        # Step 6: Save images
        self._save_images(frames, slides, layouts, output_dir, title_slide_idx)

        # Step 7: Build and save metadata
        metadata = self._build_metadata(
            video_path, duration, slides, layouts, all_labels, title_slide_idx, fps=1.0
        )

        output_dir.mkdir(parents=True, exist_ok=True)
        with open(output_dir / "metadata.json", "w") as f:
            json.dump(metadata, f, indent=2)

        self.logger.info(
            f"✓ {video_path.stem}: {len(slides)} slides, "
            f"{sum(len(s['builds']) for s in slides)} total builds"
        )

        return metadata

    def _extract_frames(self, video_path: Path, fps: float = 1.0) -> Tuple[List[Tuple[float, np.ndarray]], float]:
        """Extract frames at 1 fps. Returns list of (timestamp, frame)."""
        cap = cv2.VideoCapture(str(video_path))
        if not cap.isOpened():
            self.logger.error(f"Could not open video: {video_path}")
            return [], 0.0

        frames = []
        fps_in = cap.get(cv2.CAP_PROP_FPS)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = total_frames / fps_in if fps_in > 0 else 0

        interval = int(fps_in / fps) if fps_in > 0 else 30
        
        for i in range(0, total_frames, interval):
            cap.set(cv2.CAP_PROP_POS_FRAMES, i)
            ret, frame = cap.read()
            if ret:
                timestamp = i / fps_in
                frames.append((timestamp, frame))
        
        cap.release()
        self.total_frames_sampled = len(frames)
        return frames, duration

    def _classify_all_frames(self, frames: List[Tuple[float, np.ndarray]]) -> List[Dict]:
        """Classify frames with adaptive batch sizes (15 -> 10 -> 5 -> 1)."""
        raw_frames = [f[1] for f in frames]
        all_labels = [None] * len(frames)
        
        # Queue of ranges to process: (start_idx, end_idx, batch_size)
        pending_ranges = [(0, len(raw_frames), self.batch_size)]
        
        while pending_ranges:
            start, end, current_batch_size = pending_ranges.pop(0)
            if start >= end:
                continue
                
            idx = start
            while idx < end:
                sub_end = min(idx + current_batch_size, end)
                batch = raw_frames[idx : sub_end]
                self.batch_calls += 1
                
                try:
                    labels = self.gemini.classify_frame_batch(batch, batch_start_idx=idx)
                    
                    # Fill labels
                    for j, label in enumerate(labels):
                        if idx + j < len(all_labels):
                            all_labels[idx + j] = label
                    
                    self.logger.info(f"Batch {idx}-{sub_end-1}: classified {len(batch)} frames (batch_size={current_batch_size})")
                    idx = sub_end # Move forward
                except Exception as e:
                    self.logger.warning(f"Batch {idx}-{sub_end-1} failed with batch_size={current_batch_size}: {e}")
                    
                    # Determine next fallback size
                    if current_batch_size > 10: next_size = 10
                    elif current_batch_size > 5: next_size = 5
                    elif current_batch_size > 1: next_size = 1
                    else: next_size = 0 # No more fallbacks
                    
                    if next_size > 0:
                        self.logger.info(f"Retrying range {idx}-{sub_end-1} with smaller batch_size={next_size}")
                        # Immediately process this sub-range with smaller size
                        # We don't increment idx; we'll retry the same spot with next_size
                        current_batch_size = next_size
                    else:
                        self.logger.error(f"Batch {idx}-{sub_end-1} failed even with batch_size=1. Marking as unknown.")
                        for j in range(idx, sub_end):
                            all_labels[j] = {"is_blank": True, "slide_number": -1, "build_number": 0}
                        idx = sub_end # Skip and move on
            
        # Backfill any missed frames (sanity check)
        for i in range(len(all_labels)):
            if all_labels[i] is None:
                all_labels[i] = {"is_blank": True, "slide_number": -1, "build_number": 0}

        return all_labels

    def _assemble_slides(self, frames: List, labels: List[Dict]) -> List[Dict]:
        """Group frames into slides based on slide_number."""
        slides = []
        current_slide_num = -1
        current_slide = None
        
        for i, label in enumerate(labels):
            s_num = label.get("slide_number", 0)
            b_num = label.get("build_number", 0)
            is_blank = label.get("is_blank", False)
            title = label.get("title", "")
            
            if is_blank or s_num == 0:
                continue

            if s_num != current_slide_num:
                # New slide
                if current_slide:
                    slides.append(current_slide)
                
                current_slide = {
                    "slide_number": s_num,
                    "title": title,
                    "builds": [],
                    "start_time": frames[i][0]
                }
                current_slide_num = s_num
            
            # Add build info
            # Check if this build is already recorded?
            # We want unique builds. If consecutive frames have same build_number, skip.
            if current_slide:
                existing_builds = [b["build_number"] for b in current_slide["builds"]]
                if b_num not in existing_builds:
                    current_slide["builds"].append({
                        "build_number": b_num,
                        "frame_idx": i,
                        "timestamp": frames[i][0]
                    })
                    
        # Append last
        if current_slide:
            slides.append(current_slide)
            
        return slides

    def _analyze_layouts(self, frames: List, slides: List[Dict]) -> List[Dict]:
        """Analyze layout of the LAST build of each slide (most complete)."""
        layouts = []
        for slide in tqdm(slides, desc="Analyzing Layouts"):
            if not slide["builds"]:
                layouts.append({})
                continue
                
            # Use last build frame
            last_build = slide["builds"][-1]
            frame_idx = last_build["frame_idx"]
            frame = frames[frame_idx][1]
            
            try:
                layout = self.gemini.analyze_slide_layout(frame)
                self.layout_calls += 1
                layouts.append(layout)
            except Exception as e:
                self.logger.error(f"Layout analysis failed for slide {slide['slide_number']}: {e}")
                layouts.append({})
                
        return layouts

    def _find_title_slide(self, slides: List[Dict], layouts: List[Dict]) -> int:
        """Find title slide index."""
        for i, layout in enumerate(layouts):
            section = layout.get("slide_section", "").lower()
            ltype = layout.get("layout_type", "").lower()
            if "title" in section or "title" in ltype:
                return i
        
        # Fallback to first slide
        return 0 if slides else -1

    def _save_images(
        self,
        frames: List,
        slides: List[Dict],
        layouts: List[Dict],
        output_dir: Path,
        title_slide_idx: int
    ):
        """Save representative images for slides."""
        output_dir.mkdir(parents=True, exist_ok=True)
        
        content_counter = 0
        for i, slide in enumerate(slides):
            # Skip if blank heuristics?
            # Just create folder structure
            
            # Save extracted frames for each build
            # Naming convention: slide_N_build_M.jpg
            # Note: We use continuous numbering for content slides if user wants
            # But here we just use the slide index
            
            slide_idx = i + 1
            
            for build in slide["builds"]:
                b_num = build["build_number"]
                f_idx = build["frame_idx"]
                frame = frames[f_idx][1]
                
                filename = f"slide_{slide_idx}_build_{b_num}.jpg"
                cv2.imwrite(str(output_dir / filename), frame)

    def _build_metadata(self, video_path, duration, slides, layouts, labels, title_idx, fps):
        """Construct final metadata dict following requested structure."""
        
        final_slides = []
        slides_with_builds = 0
        total_build_steps = 0

        for i, slide in enumerate(slides):
            layout = layouts[i] if i < len(layouts) else {}
            
            num_builds = len(slide["builds"])
            total_build_steps += num_builds
            if num_builds > 1:
                slides_with_builds += 1

            # Extract slide_section from layout or default
            slide_section = layout.pop("slide_section", "other")
            
            # Restructure builds
            restructured_builds = []
            for b in slide["builds"]:
                restructured_builds.append({
                    "build_id": b["build_number"],
                    "timestamp": round(b["timestamp"], 2),
                    "image": f"slide_{i+1}_build_{b['build_number']}.jpg"
                })

            # Start and End times
            t_start = round(slide["start_time"], 2)
            if i < len(slides) - 1:
                t_end = round(slides[i+1]["start_time"], 2)
            else:
                t_end = round(duration, 2)

            slide_data = {
                "slide_id": i + 1,
                "slide_section": slide_section,
                "t_start": t_start,
                "t_end": t_end,
                "num_builds": num_builds,
                "builds": restructured_builds,
                "layout_structure": layout
            }
            
            final_slides.append(slide_data)
            
        return {
            "video_id": video_path.stem,
            "duration": round(duration, 2),
            "fps_sampled": fps,
            "total_slides": len(slides),
            "slides_with_builds": slides_with_builds,
            "total_build_steps": total_build_steps,
            "slides": final_slides,
            "processing_info": {
                "gemini_batch_calls": self.batch_calls,
                "gemini_layout_calls": self.layout_calls,
                "total_gemini_calls": self.batch_calls + self.layout_calls,
                "total_frames_sampled": self.total_frames_sampled,
                "batch_size": self.batch_size
            }
        }

def build_style_db(
    input_dir: str,
    output_dir: str,
    config_path: str = "config.yml",
    batch_size: int = 15,
    fps: float = 1.0
):
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    videos = list(input_path.glob("*.mp4"))
    if not videos:
        print(f"No .mp4 files found in {input_path}")
        return

    builder = GeminiStyleDBBuilderV2(output_path, config_path)
    
    print(f"Found {len(videos)} videos. Processing...")
    
    # Store summary list
    summary_list = []
    
    for vid in videos:
        # Create safe subfolder name
        vid_id = vid.stem
        safe_id = re.sub(r'[^\w\-]', '_', vid_id)
        vid_out = output_path / safe_id
        
        try:
            builder.process_video(vid, vid_out, skip_if_exists=True)
            summary_list.append({
                "video_id": vid_id,
                "path": str(vid_out / "metadata.json") # Preacher expects "path"
            })
        except Exception as e:
            logging.error(f"Failed to process {vid.name}: {e}")
            
    # Save db_summary.json
    output_path.mkdir(parents=True, exist_ok=True)
    with open(output_path / "db_summary.json", "w") as f:
        json.dump(summary_list, f, indent=2)
    print(f"Saved db_summary.json to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build Style DB with Gemini V2")
    parser.add_argument("--input-dir", required=True, help="Directory containing .mp4 videos")
    parser.add_argument("--output-dir", required=True, help="Directory to save style DB")
    parser.add_argument("--config", default="config.yml", help="Path to config.yml")
    parser.add_argument("--batch-size", type=int, default=15, help="Batch size for Gemini")
    parser.add_argument("--fps", type=float, default=1.0, help="Frames per second to extract")
    
    args = parser.parse_args()
    
    build_style_db(
        args.input_dir,
        args.output_dir,
        args.config,
        args.batch_size,
        args.fps
    )
