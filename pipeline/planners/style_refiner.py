import json
from pathlib import Path
from pipeline import prompts
from utils.textwork import _load_json_dict, _is_truncated_json


# ── LaTeX escape repair ──────────────────────────────────────────────────────
# Python's eval() (used to parse LLM responses) converts single-backslash LaTeX
# escape sequences to control characters, e.g. \approx → \x07pprox (BEL).
# We repair them here so that refine_k.json contains valid LaTeX strings.

_CONTROL_TO_LATEX = {
    '\x07': '\\a',   # BEL       → \a  (e.g. \alpha, \approx)
    '\x08': '\\b',   # backspace → \b  (e.g. \beta, \bar, \begin)
    '\x09': '\\t',   # tab       → \t  (e.g. \theta, \tau)
    '\x0b': '\\v',   # vert-tab  → \v  (e.g. \vdots, \vee)
    '\x0c': '\\f',   # form-feed → \f  (e.g. \frac, \forall)
    '\x0d': '\\r',   # CR        → \r  (e.g. \right, \rho)
}


def _repair_latex_escapes(text: str) -> str:
    """Map eval()-introduced control chars back to LaTeX backslash sequences."""
    for ctrl, repl in _CONTROL_TO_LATEX.items():
        text = text.replace(ctrl, repl)
    return text


def _repair_equations_in_dict(d: dict) -> None:
    """In-place repair of LaTeX escape corruption in a refiner output dict.

    Walks the 'elements.equations' list and repairs any control-char corruption
    produced by eval() during LLM response parsing.
    """
    elements = d.get("elements")
    if not isinstance(elements, dict):
        return
    eqs = elements.get("equations")
    if not isinstance(eqs, list):
        return
    elements["equations"] = [
        _repair_latex_escapes(eq) if isinstance(eq, str) else eq
        for eq in eqs
    ]


class StyleRefiner:
    def __init__(self, planner_func, workflow_logger):
        self.planner = planner_func
        self.workflow_logger = workflow_logger

    def style_refine_by_llm(self, pdf_path, scene_idx, content_draft, style_plan) -> dict:
        """Stage 4: Decide builds from scratch, assign drafted content to build steps."""
        total_time_sec = content_draft.get("duration_sec", 8.0)
        prompt = prompts.style_refinement_prompt.format(
            content_draft=json.dumps(content_draft, indent=2),
            layout_info=json.dumps({
                "layout_template": style_plan.get("layout_template", ""),
                "layout_regions": style_plan.get("layout_regions", {}),
                "has_figure": style_plan.get("has_figure", False),
                "total_time_sec": total_time_sec,
            }, indent=2),
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
            self.workflow_logger.info(f"  Style refinement scene {scene_idx} (Attempt {attempt+1}): {raw[:200] if isinstance(raw, str) else str(raw)[:200]}")
            
            parsed = _load_json_dict(raw)
            if parsed and isinstance(parsed, dict):
                # Repair any LaTeX control-char corruption produced by eval()
                # so that refine_k.json contains valid LaTeX strings (e.g. \frac
                # not \x0crac, \approx not \x07pprox).
                _repair_equations_in_dict(parsed)
                return parsed

            self.workflow_logger.warning(f"Style refinement parsing failed for scene {scene_idx} on attempt {attempt+1}. Retrying...")
            if _is_truncated_json(raw):
                prompt += (
                    "\n\nERROR: Your previous response was cut off mid-JSON — it hit the output "
                    "token limit. Please produce a SHORTER version: use brief text values, omit "
                    "optional/redundant fields, and if there are many elements reduce their count. "
                    "The entire JSON must fit in a single response."
                )
            else:
                prompt += "\n\nERROR: The previous response was not valid JSON. Please ensure you output ONLY valid JSON without any truncated strings or formatting errors."
            
        raise ValueError(f"Style refinement failed for scene {scene_idx} after {max_retries} attempts.")
