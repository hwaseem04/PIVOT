import json
from pathlib import Path
from pipeline import prompts
from utils.textwork import _load_json_dict, classify_response, _is_truncated_json

class LowLevelPlanner:
    def __init__(self, planner_func, evaluator_func, workflow_logger):
        self.planner = planner_func
        self.evaluator = evaluator_func
        self.workflow_logger = workflow_logger

    def low_planning(
        self,
        pdf_path,
        scene_idx,
        part_plan,
        content_summary,
        style_plan,
        duration_stat,
        past_contents=None,
        with_reflection: bool = False,
        max_iterations: int = 3,
    ) -> dict:
        """Orchestrate Stage 3 with an optional Introspective QA Loop.

        Mirrors the pattern in HighLevelPlanner.high_planning():
          - with_reflection=False  → single call (same as before, no extra LLM cost)
          - with_reflection=True   → draft → evaluate → revise loop up to max_iterations
        """
        if not with_reflection:
            # Fast path: no reflection — single draft call (previous behaviour)
            return self.low_plan_by_llm(
                pdf_path, scene_idx, part_plan, content_summary,
                style_plan, duration_stat, past_contents,
            )

        # ── Introspective QA Loop (diagram: "Self QA: Key Info Present?") ────
        self.workflow_logger.info(
            f"  Stage 3 (scene {scene_idx}): Introspective QA Loop "
            f"(max_iterations={max_iterations})..."
        )
        content_draft = None
        eval_results = None
        success = False
        iteration = 0

        while not success and iteration < max_iterations:
            self.workflow_logger.info(
                f"  Stage 3 QA — iteration {iteration + 1}/{max_iterations}"
            )

            # Build memory context: include QA feedback on re-draft iterations
            if eval_results is not None and iteration > 0:
                # Inject evaluator feedback so the planner knows what to fix
                revision_note = [{
                    "_qa_feedback": str(eval_results),
                    "_instruction": prompts.low_level_replanning_prompt,
                }]
                effective_past = (past_contents or []) + revision_note
            else:
                effective_past = past_contents

            # Step 1 (and "No, Revise"): Draft / re-draft content
            content_draft = self.low_plan_by_llm(
                pdf_path, scene_idx, part_plan, content_summary,
                style_plan, duration_stat, effective_past,
            )

            # Step 2: Self-QA evaluation ("Key Info Present?")
            try:
                success, eval_results = self.low_evaluate_by_llm(
                    pdf_path, scene_idx, json.dumps(content_draft, indent=2)
                )
            except Exception as e:
                self.workflow_logger.warning(
                    f"  Stage 3 QA eval error on iter {iteration + 1}: {e}. "
                    "Accepting draft to avoid infinite loop."
                )
                success = True  # fail-safe: never loop forever on eval errors

            self.workflow_logger.info(
                f"  Stage 3 QA scene {scene_idx} iter {iteration + 1}: "
                f"{'PASS — finalising ✓' if success else 'FAIL — revising...'}"
            )
            iteration += 1

        if not success:
            self.workflow_logger.warning(
                f"  Stage 3 QA Loop hit max_iterations={max_iterations} "
                f"for scene {scene_idx}. Using last draft as-is."
            )

        return content_draft

    def low_plan_by_llm(self, pdf_path, scene_idx, part_plan, content_summary, style_plan, duration_stat, past_contents=None) -> dict:
        """Stage 3: Draft content (bullets, audio, figures) within the decided layout."""
        
        memory_context = ""
        if past_contents:
            memory_context = "## Previous Content\n"
            memory_context += "The following content was drafted for the immediately preceding scenes.\n"
            memory_context += "You MUST NOT repeat the exact text content or claims from these previous scenes in your current draft.\n\n"
            for past in past_contents:
                subset = {
                    "bullets": past.get("bullets", []),
                    "audio_content": past.get("audio_content", "")
                }
                memory_context += json.dumps(subset, indent=2) + "\n"

        prompt = prompts.low_level_planning_prompt.format(
            content_summary=json.dumps(content_summary, indent=2),
            style_plan=json.dumps(style_plan, indent=2),
            scene_context=json.dumps(part_plan, indent=2),
            duration_stat=json.dumps(duration_stat, indent=2),
            memory_context=memory_context,
            canvas_constraints=self._compute_canvas_constraints(style_plan),
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
            self.workflow_logger.info(f"  Content draft scene {scene_idx} (Attempt {attempt+1}): {raw[:200] if isinstance(raw, str) else str(raw)[:200]}")
            
            parsed = _load_json_dict(raw)
            if parsed and isinstance(parsed, dict):
                return parsed
                
            self.workflow_logger.warning(f"Content drafting parsing failed for scene {scene_idx} on attempt {attempt+1}. Retrying...")
            if _is_truncated_json(raw):
                prompt += (
                    "\n\nERROR: Your previous response was cut off mid-JSON — it hit the output "
                    "token limit. Please produce a SHORTER version: use brief text values, omit "
                    "optional/redundant fields, and if there are many elements reduce their count. "
                    "The entire JSON must fit in a single response."
                )
            else:
                prompt += "\n\nERROR: The previous response was not valid JSON. Please ensure you output ONLY valid JSON without any truncated strings or formatting errors."
            
        raise ValueError(f"Content drafting failed for scene {scene_idx} after {max_retries} attempts.")

    @staticmethod
    def _compute_canvas_constraints(style_plan: dict) -> str:
        """
        Derive a human-readable canvas constraints hint from the LayoutSpec.

        Returns a formatted string injected into the prompt that tells the LLM:
        - how many bullets physically fit in the bullet region
        - what font size will be used
        - max recommended words per bullet
        """
        SLIDE_HEIGHT_PX = 1080
        LINE_SPACING    = 1.15
        BULLET_GAP_PX   = 10
        WORDS_PER_LINE  = 8   # approximate average words per wrapped line at typical font

        # Find the B-type (bullets) element in the spec
        bullet_elem = None
        elements = style_plan.get("elements", [])
        for elem in elements:
            if elem.get("type") == "B":
                bullet_elem = elem
                break

        if bullet_elem is None:
            return ""  # no bullet region — no constraints needed

        # Region height in pixels
        box = bullet_elem.get("box", {})
        region_h_norm = box.get("h", 0.8)
        region_h_px   = region_h_norm * SLIDE_HEIGHT_PX

        # Fixed bullet font size used by the renderer (36px).
        # We deliberately ignore the spec's font_size here so the constraint
        # matches what the renderer will actually render.
        font_size = 36

        # Approximate line height with spacing
        line_h_px = int(font_size * LINE_SPACING)

        # Assume ~1.5 lines per bullet on average (one wrap)
        avg_lines_per_bullet = 1.5
        px_per_bullet = avg_lines_per_bullet * line_h_px + BULLET_GAP_PX

        max_bullets = max(1, int(region_h_px / px_per_bullet))

        # Max words per bullet so it stays within 1–2 wrapped lines
        max_words_per_bullet = 10  # enforced as hard rule in low_level_planning_prompt

        # Check whether the layout also has an EQ element
        has_eq = any(elem.get("type") == "EQ" for elem in elements)

        # Count figure-type elements (F, D, CH, TAB)
        _FIGURE_TYPES = {"F", "D", "CH", "TAB"}
        figure_count = sum(1 for elem in elements if elem.get("type") in _FIGURE_TYPES)

        lines = [
            "## Canvas Constraints (MUST FOLLOW)",
            f"The bullet region is {region_h_norm:.0%} of the slide height "
            f"({region_h_px:.0f}px) at font_size={font_size}px.",
            f"- **Maximum bullets that fit: {max_bullets}** — do NOT write more than this.",
            f"- Each bullet must be ≤ {max_words_per_bullet} words so it fits on 1–2 lines without shrinking.",
            "- Prefer 2–3 punchy bullets over 4–5 verbose ones.",
        ]
        if has_eq:
            eq_max = max(1, max_bullets - 1)
            lines.append(
                f"- This layout has an EQ element: include 1–2 equations and write at most {eq_max} bullets."
            )
        if figure_count == 1:
            lines.append(
                "- This layout has **1 figure region** — assign exactly 1 figure to the `figure` key."
            )
        elif figure_count >= 2:
            slot_names = ", ".join(
                f"`figure`" if i == 0 else f"`figure_{i + 1}`"
                for i in range(figure_count)
            )
            lines.append(
                f"- This layout has **{figure_count} figure regions** — you MUST populate all "
                f"{figure_count} figure slots: {slot_names}. "
                f"Assign a distinct key figure from the paper to each slot."
            )
        return "\n".join(lines)

    def low_evaluate_by_llm(self, pdf_path, scene_idx, low_plan_str) -> tuple:
        prompt = prompts.low_level_evaluate_prompt + ' \n ' + low_plan_str
        eval_results = eval(
            self.evaluator(
                prompt=prompt,
                pdf_path=Path(pdf_path),
            )
        )
        success = classify_response(eval_results)
        self.workflow_logger.info(f"Low eval scene {scene_idx}: {eval_results}")
        return success, eval_results
