"""
Asset Analyser Agent

Responsible for independently analyzing auxiliary files (images and videos)
provided in the `<pdf_name> assets/` directory and mapping them to visual
components or summarizing them for the high-level planner, entirely decoupled
from the PDF.
"""
from pathlib import Path
import json
import logging
from PIL import Image

from utils.logger import get_logger
from pipeline import prompts
from utils.textwork import _load_json_dict

class AssetAnalyser:
    def __init__(self, work_dir: Path, pdf_path: Path, llm_instance, logger: logging.Logger = None):
        self.work_dir = work_dir
        self.pdf_path = pdf_path
        self.assets_dir = self.pdf_path.parent / f"{self.pdf_path.stem} assets"
        self.llm = llm_instance
        self.logger = logger or get_logger("AssetAnalyser", self.work_dir / "asset_analyser.log")

    def _get_files_by_ext(self, extensions):
        if not self.assets_dir.exists() or not self.assets_dir.is_dir():
            return []
        
        files = []
        for ext in extensions:
            files.extend(list(self.assets_dir.glob(f"*{ext}")))
            files.extend(list(self.assets_dir.glob(f"*{ext.upper()}")))
        return files

    def analyze_images(self) -> dict:
        """
        Scans exactly for one conference logo and multiple affiliation logos based on visuals.
        """
        img_exts = [".png", ".jpg", ".jpeg", ".svg", ".avif", ".webp"]
        image_files = self._get_files_by_ext(img_exts)


        result = {"conference": None, "affiliations": []}

        if not image_files:
            self.logger.info("No images found in assets directory for logos.")
            return result
        
        self.logger.info(f"AssetAnalyser found {len(image_files)} image(s) for logo resolution.")

        loaded_images = []
        file_mapping = {}
        for idx, img_path in enumerate(image_files):
            try:
                img = Image.open(img_path)
                # Convert to RGB if needed to avoid format issues with Gemini API
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                loaded_images.append(img)
                file_mapping[f"image_{idx}"] = img_path
            except Exception as e:
                self.logger.warning(f"Could not load image {img_path}: {e}")

        if not loaded_images:
            return result

        prompt = prompts.asset_analyser_image_prompt.format(
            num_images=len(loaded_images)
        )

        try:
            # Query Gemini
            _, raw_out = self.llm.query(
                prompt=prompt,
                img_path_lst=loaded_images
            )
            parsed = _load_json_dict(raw_out)

            if parsed and isinstance(parsed, dict):
                # Map back to paths
                conf_idx = parsed.get("conference_logo")
                if conf_idx in file_mapping:
                    result["conference"] = file_mapping[conf_idx]
                
                for aff_idx in parsed.get("affiliation_logos", []):
                    if aff_idx in file_mapping:
                        result["affiliations"].append(file_mapping[aff_idx])
            else:
                self.logger.warning("AssetAnalyser image parsing failed formatting. Returning raw fallback.")
                return result

        except Exception as e:
            self.logger.error(f"AssetAnalyser image analysis failed: {e}")

        return result

    def analyze_videos(self) -> dict:
        """
        Uploads local video files in the assets dir, asks Gemini what they are,
        and returns a dict mapping video filename to a text summary.
        """
        vid_exts = [".mp4", ".mov", ".mkv", ".avi"]
        video_files = self._get_files_by_ext(vid_exts)

        summary_dict = {}

        if not video_files:
            self.logger.info("No videos found in assets directory.")
            return summary_dict

        self.logger.info(f"AssetAnalyser found {len(video_files)} video(s). Starting analysis...")

        for vid_path in video_files:
            try:
                # Query Gemini using file API specifically
                # We expect the unified LLM or Gemini class to expose `query_video` 
                # or handle video Paths gracefully in `query`. For now, use `query_video`.
                if hasattr(self.llm, "query_video"):
                    prompt = prompts.asset_analyser_video_prompt.format(filename=vid_path.name)
                    _, raw_out = self.llm.query_video(
                        prompt=prompt,
                        video_path=vid_path
                    )
                    parsed = _load_json_dict(raw_out)
                    if parsed and isinstance(parsed, dict):
                        # Store structural info
                        summary_dict[vid_path.name] = {
                            "description": parsed.get("description", "A video clip."),
                            "relevance": parsed.get("relevance", "Unknown"),
                            "path": str(vid_path)
                        }
                    else:
                        summary_dict[vid_path.name] = {"description": "A video clip.", "relevance": "Unknown", "path": str(vid_path)}
                else:
                    self.logger.warning("LLM does not support `query_video`. Skipping video analysis.")
            except Exception as e:
                self.logger.error(f"AssetAnalyser failing on video {vid_path.name}: {e}")

        # Cache results in log_dir for traceability
        cache_path = self.work_dir / "asset_video_analysis.json"
        with open(cache_path, "w") as f:
            json.dump(summary_dict, f, indent=4)

        return summary_dict
