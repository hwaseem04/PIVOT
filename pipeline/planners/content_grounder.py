import json
from pathlib import Path
from pipeline import prompts
from utils.textwork import _load_json_dict, _is_truncated_json

class ContentGrounder:
    def __init__(self, planner_func, workflow_logger):
        self.planner = planner_func
        self.workflow_logger = workflow_logger

    def content_extract_by_llm(self, pdf_path, scene_idx, part_plan, past_contents=None) -> dict:
        """Stage 1: Extract relevant content from the paper for this scene."""
        memory_context = ""
        if past_contents:
            memory_context = "## Previous Scenes Memory\n"
            memory_context += "The following content was extracted for the immediately preceding scenes. **This is provided as a memory of what the audience has JUST seen.**\n"
            memory_context += "You MUST NOT repeat the claims, figures, tables, or equations from these previous scenes in your current extraction, to ensure the presentation maintains forward momentum without redundant slides.\n"
            memory_context += "If you must reference the exactly same figure/table, the 'relevance' MUST be clearly unique to avoid narrative duplication.\n\n"
            for past in past_contents:
                subset = {
                    "extracted_content": past.get("extracted_content", ""),
                    "key_figures": past.get("key_figures", []),
                    "key_tables": past.get("key_tables", []),
                    "key_equations": past.get("key_equations", [])
                }
                memory_context += json.dumps(subset, indent=2) + "\n"

        prompt = prompts.content_extraction_prompt.format(
            scene_json=json.dumps(part_plan, indent=2),
            memory_context=memory_context
        )
        
        max_retries = 3
        for attempt in range(max_retries):
            _response = self.planner(
                prompt=prompt,
                pdf_path=Path(pdf_path),
            )
            try:
                raw = eval(_response)
            except Exception:
                raw = _response  # eval failed; _load_json_dict handles raw strings
            self.workflow_logger.info(f"  Content extraction scene {scene_idx} (Attempt {attempt+1}): {raw[:200] if isinstance(raw, str) else str(raw)[:200]}")
            
            parsed = _load_json_dict(raw)
            if parsed and isinstance(parsed, dict):
                return parsed
            
            self.workflow_logger.warning(f"Content extraction parsing failed for scene {scene_idx} on attempt {attempt+1}. Retrying...")
            if _is_truncated_json(raw):
                prompt += (
                    "\n\nERROR: Your previous response was cut off mid-JSON — it hit the output "
                    "token limit. Please produce a SHORTER version: use brief text values, omit "
                    "optional/redundant fields, and if there are many elements reduce their count. "
                    "The entire JSON must fit in a single response."
                )
            else:
                prompt += "\n\nERROR: The previous response was not valid JSON. Please ensure you output ONLY valid JSON without any truncated strings or formatting errors."
            
        raise ValueError(f"Content extraction failed for scene {scene_idx} after {max_retries} attempts.")
