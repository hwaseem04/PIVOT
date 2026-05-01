"""
Gemini VLM-based frame comparison for slide extraction.

Uses Gemini to compare consecutive video frames and determine:
- Same slide (build) vs. different slide transitions
- Detailed layout analysis for style agent reference

This module does NOT modify any existing code.
"""

import sys
from pathlib import Path
import logging
import json
import base64
import time
import random
from typing import Optional, Dict, List, Tuple
from io import BytesIO

import cv2
import numpy as np
from PIL import Image

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

import google.generativeai as genai
import yaml

from utils.logger import get_logger


class GeminiFrameComparator:
    """
    Uses Gemini VLM to compare video frames for slide extraction.
    
    Key features:
    - Compare two frames to determine same-slide vs different-slide
    - Analyze slide layout with rich textual descriptions
    - Exponential backoff for API rate limiting
    """

    # Prompt for comparing two consecutive frames
    COMPARE_PROMPT = """You are analyzing two consecutive frames from an academic paper presentation video.

Your task: Determine if these two frames belong to the **same slide** or **different slides**.

**Rules for classification:**
1. **SAME SLIDE (build)**: The slide title/heading stays the same. Only minor additions appear:
   - New bullet points appearing incrementally
   - A figure or image being added to existing content
   - An animation or video playing within the slide area
   - Text highlighting or emphasis changes
   - A progress indicator changing
   - Minor visual artifacts or compression differences
   
2. **DIFFERENT SLIDE (new slide)**: The slide title/heading changes, OR there is a major layout restructuring:
   - The title text at the top of the slide is different
   - Complete change of content layout (e.g., from text to full-screen figure)
   - Transition effects (fade, slide-in, etc.)
   - Moving from one topic/section to another

**CRITICAL**: Videos or animations playing *within* a slide do NOT constitute a new slide. If the overall slide structure (title, layout positioning) remains the same, it is the SAME slide even if an embedded video is playing.

Respond in exactly this JSON format:
```json
{
    "same_slide": true/false,
    "confidence": 0.0-1.0,
    "reason": "Brief explanation of why you classified this way"
}
```"""

    # Prompt for detailed layout analysis
    LAYOUT_PROMPT = """You are analyzing an academic presentation slide. Provide a **detailed description** of its visual layout structure.

Describe the following aspects in natural language (NO coordinates, only descriptive text):

1. **Overall Layout Type**: e.g., "single column with title", "two-column layout", "full-screen figure", "title slide", "comparison layout", "grid layout"

2. **Title/Heading**: Where is the title? What style? (e.g., "Large bold title at top-left with colored accent bar", "Centered title with subtitle below")

3. **Content Structure**: 
   - Are there bullet points? How are they organized? (e.g., "hierarchical bullets with 2 levels of indentation", "numbered list with 5 items")
   - Are there columns? How many? What's in each? (e.g., "left column has text bullets, right column has a figure")
   - Are there figures/images? How are they positioned? (e.g., "large figure centered below title", "two side-by-side comparison images")
   
4. **Equations/Math**: Are there equations? Where? (e.g., "centered equation block between text paragraphs", "equations on left with explanatory text on right")

5. **Visual Elements**: 
   - Tables, charts, diagrams, flowcharts
   - Color scheme / background style
   - Logos, watermarks, page numbers
   - Icons or decorative elements

6. **Text Density**: Light, moderate, or dense

7. **Slide Section**: Classify this slide into exactly one of these standard academic categories:
   - "title": Presentation title slide (paper title, authors).
   - "introduction": Introduction, motivation, problem statement, or background context.
   - "method": Methodology, approach, proposed method, architecture, or foundational related work.
   - "experiments": Experimental setup, datasets, implementation details, or benchmarks.
   - "results": Quantitative results, qualitative findings, analysis, discussion, or tables/charts.
   - "conclusion": Conclusion, future work, limitations, or summary.
   - "other": Anything that doesn't fit the above (e.g., Q&A, extra references).

Respond in exactly this JSON format:
```json
{
    "layout_type": "short layout type name",
    "title_text": "exact title text visible on the slide",
    "slide_section": "one of the section categories listed above",
    "layout_description": "Detailed multi-sentence description covering all the aspects above. Be specific about positioning (top, bottom, left, right, centered), hierarchy, and visual relationships between elements."
}
```"""

    def __init__(
        self,
        config_path: Path = Path("config.yml"),
        logger: Optional[logging.Logger] = None,
        max_retries: int = 2,
        initial_delay: float = 2.0
    ):
        self.logger = logger or get_logger("GeminiFrameComparator")
        self.max_retries = max_retries
        self.initial_delay = initial_delay

        # Load config
        config_path = Path(config_path)
        if not config_path.exists():
            raise FileNotFoundError(f"Config file not found: {config_path}")

        with open(config_path, "r") as f:
            cfg = yaml.safe_load(f)


        self.api_key = cfg["GEMINI"]["API_KEY"]
        self.model_name = cfg["GEMINI"]["MODEL"]
        self.temperature = cfg["GEMINI"].get("TEMPERATURE", 0.0)

        # Configure Gemini
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(self.model_name)

        self.logger.info(f"GeminiFrameComparator initialized with model: {self.model_name}")

    def _encode_frame_to_image_part(self, frame: np.ndarray) -> Dict:
        """Convert an OpenCV BGR frame to a Gemini API-compatible image part."""
        # Convert BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(rgb_frame)

        # Resize to reduce token usage (max 1024px on longest side)
        max_dim = 1024
        w, h = pil_image.size
        if max(w, h) > max_dim:
            scale = max_dim / max(w, h)
            pil_image = pil_image.resize(
                (int(w * scale), int(h * scale)), Image.LANCZOS
            )

        # Encode to JPEG bytes
        buffer = BytesIO()
        pil_image.save(buffer, format="JPEG", quality=85)
        b64_str = base64.b64encode(buffer.getvalue()).decode("utf-8")

        return {"mime_type": "image/jpeg", "data": b64_str}

    def _query_gemini(self, content: list, parse_json: bool = True) -> Dict:
        """
        Send a query to Gemini with exponential backoff.
        
        Args:
            content: List of content parts (images + text prompt)
            parse_json: If True, parse the response as JSON
            
        Returns:
            Parsed JSON dict or raw text
        """
        delay = self.initial_delay

        for attempt in range(self.max_retries):
            try:
                response = self.model.generate_content(
                    content,
                    generation_config=genai.GenerationConfig(
                        max_output_tokens=8192,
                        temperature=self.temperature
                    )
                )

                if response and response.text:
                    text = response.text.strip()

                    if parse_json:
                        # Extract JSON from possible markdown code block
                        if "```json" in text:
                            text = text.split("```json")[1].split("```")[0].strip()
                        elif "```" in text:
                            text = text.split("```")[1].split("```")[0].strip()

                        return json.loads(text)
                    else:
                        return {"text": text}

            except json.JSONDecodeError as e:
                self.logger.warning(f"JSON parse error (attempt {attempt+1}): {e}")
                self.logger.warning(f"Raw response: {text[:200]}...")
            except Exception as e:
                self.logger.warning(
                    f"Gemini API error (attempt {attempt+1}/{self.max_retries}): "
                    f"{type(e).__name__}: {e}"
                )

            # Exponential backoff with jitter
            jitter = random.uniform(0.5, 1.5)
            sleep_time = delay * jitter
            self.logger.info(f"Retrying in {sleep_time:.1f}s...")
            time.sleep(sleep_time)
            delay *= 2

        self.logger.error("All retries exhausted for Gemini query")
        raise RuntimeError("Gemini API retries exhausted (check for JSON truncation or rate limits)")

    def compare_frames(
        self,
        frame_a: np.ndarray,
        frame_b: np.ndarray
    ) -> Dict:
        """
        Compare two frames using Gemini VLM.
        
        Args:
            frame_a: First frame (OpenCV BGR)
            frame_b: Second frame (OpenCV BGR)
            
        Returns:
            Dict with keys: same_slide (bool), confidence (float), reason (str)
        """
        img_a = self._encode_frame_to_image_part(frame_a)
        img_b = self._encode_frame_to_image_part(frame_b)

        content = [img_a, img_b, self.COMPARE_PROMPT]

        result = self._query_gemini(content, parse_json=True)

        # Ensure required fields
        return {
            "same_slide": result.get("same_slide", True),
            "confidence": result.get("confidence", 0.0),
            "reason": result.get("reason", "unknown")
        }

    def analyze_slide_layout(self, frame: np.ndarray) -> Dict:
        """
        Analyze the layout of a single slide frame using Gemini VLM.
        
        Returns detailed textual description of the layout — NO coordinates,
        only rich descriptions suitable for style agent reference.
        
        Args:
            frame: Slide frame (OpenCV BGR)
            
        Returns:
            Dict with keys: layout_type, title_text, layout_description
        """
        img_part = self._encode_frame_to_image_part(frame)

        content = [img_part, self.LAYOUT_PROMPT]

        result = self._query_gemini(content, parse_json=True)

        return {
            "layout_type": result.get("layout_type", "unknown"),
            "title_text": result.get("title_text", ""),
            "slide_section": result.get("slide_section", "other"),
            "layout_description": result.get("layout_description", "")
        }

    # Prompt for batch classification of multiple frames
    BATCH_CLASSIFY_PROMPT_TEMPLATE = """You are analyzing {n_frames} consecutive frames (labeled Frame_0 through Frame_{last_idx}) extracted at 1 fps from an academic paper presentation video.

Your task: Assign a **slide number** and **build number** to each frame.

**Rules:**
1. **SAME SLIDE, SAME BUILD**: Visually identical or near-identical frames (no informative change). Same slide_number, same build_number. Also applies to video playback where the overall content is the same.
2. **SAME SLIDE, NEW BUILD**: Same title/heading, but **meaningful new content** is added:
   - New bullet points or lines of text appearing.
   - New arrows, boxes, or annotations explaining concepts.
   - Significant new figures or images being added.
   - **CRITICAL**: Do NOT increment build_number for simple video/animation playback or highlighting unless it introduces new explanatory text/elements.
3. **NEW SLIDE**: Title changes, complete layout restructuring, topic transition. Increment slide_number, reset build_number to 0.
4. **BLANK/TRANSITION**: A mostly black/blank frame gets slide_number 0, build_number 0 (will be filtered out).
5. Slide numbers should start from 1 and increase sequentially.
6. Build numbers start from 0 for each new slide and increase when new content appears on the same slide.

Respond in exactly this JSON format:
```json
{{
    "frames": [
        {{"frame_id": 0, "slide_number": 1, "build_number": 0, "is_blank": false, "title": "slide title text"}},
        {{"frame_id": 1, "slide_number": 1, "build_number": 1, "is_blank": false, "title": "slide title text"}},
        {{"frame_id": 2, "slide_number": 2, "build_number": 0, "is_blank": false, "title": "new slide title"}},
        ...
    ]
}}
```"""

    def classify_frame_batch(
        self,
        frames: List[np.ndarray],
        batch_start_idx: int = 0
    ) -> List[Dict]:
        """
        Classify a batch of frames in one Gemini call.
        
        Sends all frames in the batch to Gemini and asks it to assign
        slide_number and build_number to each frame.
        
        Args:
            frames: List of OpenCV BGR frames
            batch_start_idx: Global index of the first frame (for logging)
            
        Returns:
            List of dicts, one per frame:
            {frame_id, slide_number, build_number, is_blank, title}
        """
        n = len(frames)
        prompt = self.BATCH_CLASSIFY_PROMPT_TEMPLATE.format(
            n_frames=n,
            last_idx=n - 1
        )

        # Build content: interleave frame labels and images
        content = []
        for i, frame in enumerate(frames):
            content.append(f"Frame_{i}:")
            content.append(self._encode_frame_to_image_part(frame))
        content.append(prompt)

        result = self._query_gemini(content, parse_json=True)

        # Parse and validate
        frame_labels = result.get("frames", [])

        # If Gemini returned fewer results, fill in defaults
        while len(frame_labels) < n:
            frame_labels.append({
                "frame_id": len(frame_labels),
                "slide_number": 0,
                "build_number": 0,
                "is_blank": True,
                "title": ""
            })

        self.logger.info(
            f"Batch {batch_start_idx}-{batch_start_idx + n - 1}: "
            f"classified {n} frames"
        )

        return frame_labels

    def batch_compare_frames(
        self,
        frame_pairs: List[Tuple[np.ndarray, np.ndarray]],
        delay_between: float = 0.5
    ) -> List[Dict]:
        """
        Compare multiple frame pairs sequentially with rate limiting.
        
        Args:
            frame_pairs: List of (frame_a, frame_b) tuples
            delay_between: Seconds to wait between API calls
            
        Returns:
            List of comparison results
        """
        results = []
        for i, (frame_a, frame_b) in enumerate(frame_pairs):
            self.logger.info(f"Comparing frame pair {i+1}/{len(frame_pairs)}")
            result = self.compare_frames(frame_a, frame_b)
            results.append(result)

            if i < len(frame_pairs) - 1:
                time.sleep(delay_between)

        return results
