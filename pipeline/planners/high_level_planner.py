import json
from pathlib import Path
from pipeline import prompts
from utils.textwork import merge_dict_keys_values, classify_response

class HighLevelPlanner:
    def __init__(self, planner_func, evaluator_func, workflow_logger):
        self.planner = planner_func
        self.evaluator = evaluator_func
        self.workflow_logger = workflow_logger

    def high_planning(self, pdf_path, high_plan_path, with_reflection, with_example, high_example, max_high_plan_iteration, video_summaries_context) -> str:
        """Sets the initial plan."""

        style_context = ""#self.retrieve_global_style()
        if with_reflection:
            high_planning_success=False
            iter=0
            eval_results=None
            high_plan=None
            while high_planning_success == False and (iter < max_high_plan_iteration):
                high_plan = self.high_plan_by_llm(pdf_path, style_context, video_summaries_context, with_example, high_example, eval_results, high_plan)
                high_planning_success, eval_results = self.high_evaluate_by_llm(pdf_path, high_plan)
                iter += 1
        else:
            high_plan = self.high_plan_by_llm(pdf_path, style_context, video_summaries_context, with_example, high_example)
        self.workflow_logger.info(f"High Level Plan: {high_plan}")
        # with open(self.high_plan_path, 'w') as file:
        #     file.write(high_plan)

        with open(high_plan_path, 'w', encoding='utf-8') as f:
            json.dump(high_plan, f, ensure_ascii=False, indent=2)
        return high_plan
    
    def high_plan_by_llm(self, pdf_path, style_context, video_summaries_context, with_example, high_example, eval_results=None, high_plan=None) -> str:
        if eval_results:
            prompt = high_plan + ' \n '+ prompts.high_level_replanning_prompt + eval_results + ' \n ' + style_context + ' \n ' + video_summaries_context
        else:
            # Inject style context into the placeholder
            # Note: prompts.high_level_planning_prompt has {style_context} and {video_assets_context} placeholders now
            try:
                base_prompt = prompts.high_level_planning_prompt.format(
                    style_context=style_context,
                    video_assets_context=video_summaries_context
                )
            except Exception as e:
                 # Fallback if format fails (e.g. if prompt doesn't have placeholder or has other braces)
                 self.workflow_logger.warning(f"Formatting failed: {e}")
                 base_prompt = prompts.high_level_planning_prompt + "\n\n" + style_context

            prompt = base_prompt
            if with_example :
                prompt += ' \n '+ merge_dict_keys_values(high_example) 
        high_plan = eval(
            self.planner(
                prompt=prompt,
                pdf_path=Path(pdf_path),
            )
        )
        self.workflow_logger.info(f"High_plan: {high_plan}")
        return  high_plan
    
    def high_evaluate_by_llm(self, pdf_path, high_plan) -> str:
        prompt = prompts.high_level_evaluate_prompt + ' \n '+ high_plan
        eval_results = eval(
            self.evaluator(
                prompt = prompt,
                pdf_path=Path(pdf_path),
                ))
        success = classify_response(eval_results)
        self.workflow_logger.info(f"Eval_Results: {eval_results}")
        return success, eval_results
