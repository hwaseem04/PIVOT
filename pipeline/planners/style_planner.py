import json
from pathlib import Path
from pipeline import prompts
from utils.textwork import _load_json_dict, _is_truncated_json
from utils.grid_image import make_grid_image

class StylePlanner:
    def __init__(self, planner_func, workflow_logger):
        self.planner = planner_func
        self.workflow_logger = workflow_logger

    def style_plan_by_llm(self, pdf_path, scene_idx, part_plan, content_summary, style_context) -> dict:
        """Stage 2: Decide layout using content + structured LayoutSpec examples.

        Args:
            style_context: dict returned by retrieve_scene_style(), containing:
                - layout_specs: list of LayoutSpec v1 dicts from similar papers
                - layout_descriptions: list of fallback verbose description strings
                - durations: dict with min/max/avg duration stats
        """
        prompt = prompts.style_planning_prompt(
            content_summary=json.dumps(content_summary, indent=2),
            scene_context=json.dumps(part_plan, indent=2),
            style_context=style_context,
        )

        # Pass the grid overlay image so Gemini can pick precise grid-cell IDs
        # instead of free-form floats — eliminates most coordinate overlap issues.
        grid_img = make_grid_image()

        max_retries = 3
        for attempt in range(max_retries):
            _response = self.planner(
                prompt=prompt,
                pdf_path=Path(pdf_path),
                img_path=[grid_img],   # ← list of images (base_llm requires a list)
            )
            try:
                raw = eval(_response)
            except Exception:
                raw = _response  # eval failed; _load_json_dict handles raw strings
            self.workflow_logger.info(f"  Style plan scene {scene_idx} (Attempt {attempt+1}): {raw[:200] if isinstance(raw, str) else str(raw)[:200]}")

            parsed = _load_json_dict(raw)
            if parsed and isinstance(parsed, dict):
                return parsed

            self.workflow_logger.warning(f"Style planning parsing failed for scene {scene_idx} on attempt {attempt+1}. Retrying...")
            if _is_truncated_json(raw):
                prompt += (
                    "\n\nERROR: Your previous response was cut off mid-JSON — it hit the output "
                    "token limit. Please produce a SHORTER version: use brief text values, omit "
                    "optional/redundant fields, and if there are many elements reduce their count. "
                    "The entire JSON must fit in a single response."
                )
            else:
                prompt += "\n\nERROR: The previous response was not valid JSON. Please ensure you output ONLY valid JSON without any truncated strings or formatting errors."

        raise ValueError(f"Style planning failed for scene {scene_idx} after {max_retries} attempts.")
