from pathlib import Path
from PIL import Image
import yaml
import logging
from time import localtime, strftime
import json
import random
from typing import Optional
import re
import os 
import fitz # PyMuPDF
from llms import GPT4, DepictQA, GPT4_AZ, GEMINI,QWEN
from . import prompts
from utils.slides import create_ppt_style_image, get_specific_element
from utils.logger import get_logger
from utils.custom_types import *
from utils.textwork import merge_dict_keys_values, classify_response, text_to_list, extract_code,replace_animate,extract_dict,extract_list_from_text, _load_json_dict
from utils                                                                                                                                                .videowork import extract_key_frames, merge_video_audio, image_to_images, image_to_video, concatenate_videos
from utils.math_vis import render_video
from moviepy.editor import VideoFileClip
from tools import Wanxiang_video, Wanxiang_image, Qwentts
from utils.misc import download_file, name_to_pdb_ids, download_pdb
from utils.mol import generate_mol_animation
from tools.retriever import PaperRetriever
from tools.renderer import SlideRenderer
from tools.logo_manager import format_authors_display, format_affiliations_display, format_authors_with_superscripts
from tools.asset_analyser import AssetAnalyser
from .planners.high_level_planner import HighLevelPlanner
from .planners.content_grounder import ContentGrounder
from .planners.style_planner import StylePlanner
from .planners.low_level_planner import LowLevelPlanner
from .planners.style_refiner import StyleRefiner
import random
import json

class Preacher:
    """
    Args:
        input_path (Path): Path to the input image.
        output_dir (Path): Path to the output directory, in which a directory will be created.
        llm_config_path (Path, optional): Path to the config file of LLM. Defaults to Path("config.yml").
        plan_by (str, optional): The method of degradation evaluation, "depictqa" or "gpt4v". Defaults to "depictqa".
        with_retrieval (bool, optional): Whether to schedule with retrieval. Defaults to True.
        schedule_example_path (Path | None, optional): Path to the example hub. Defaults to Path( "memory/schedule_example.json").
        with_reflection (bool, optional): Whether to reflect on the results of tools. Defaults to True.
        eval_by (str, optional): The method of reflection on results of tools, "depictqa" or "gpt4v". Defaults to "depictqa".
        with_rollback (bool, optional): Whether to roll back when failing in one subtask. Defaults to True.
        silent (bool, optional): Whether to suppress the console output. Defaults to False.
    """

    def __init__(
        self,
        input_path: Path,
        output_dir: Path,
        llm_config_path: Path ,
        plan_by: str,
        eval_by: str,
        art_work: str,
        with_example: bool = True,
        schedule_example_path: Optional[Path] = Path(
            "memory/schedule_example.json"
        ),
        with_reflection: bool = True,
        with_rollback: bool = True,
        silent: bool = False,
        max_high_plan_iteration: int = 15,
        max_low_plan_iteration: int = 30,
        max_generate_iteration: int = 10,
        general_video_work: str = "wanx",
        captioning_work: str = "wanx",
        slides_work: str = "xinghuo",
        audio_work: str = "qwentts",
    ) -> None:
        # paths
        self.pdf_path = input_path
        self.low_plan_order = ["style","audio_content","source","prompt"]
        self._prepare_dir(input_path, output_dir)
        # config
        self._config(
            plan_by,
            with_example,
            with_reflection,
            eval_by,
            with_rollback,
            max_high_plan_iteration,
            max_low_plan_iteration,
            max_generate_iteration,
            art_work,
            general_video_work,
            captioning_work,
            slides_work,
            audio_work,
        )
        # components
        self._create_components(llm_config_path, schedule_example_path, silent)
        # constants
        self._set_constants()

    def _config(
        self,
        plan_by: str,
        with_example: bool,
        with_reflection: bool,
        eval_by: str,
        with_rollback: bool,
        max_low_plan_iteration:int,
        max_high_plan_iteration:int,
        max_generate_iteration:int,
        art_work: str,
        general_video_tool: str ,
        captioning_tool: str  ,
        slides_tool: str ,
        audio_tool: str ,
    ) -> None:
        #assert plan_by in {"GPT4v", "depictqa", "GPT4_AZ", "GEMINI"}
        self.plan_by = plan_by
        self.with_example = with_example
        
        self.eval_by = eval_by
        #assert eval_by in {"GPT4v", "depictqa", "GPT4_AZ", "GEMINI"}
        self.art_work = art_work
        self.with_reflection = with_reflection
        
        self.with_rollback = with_rollback
        self.max_high_plan_iteration=max_high_plan_iteration
        self.max_low_plan_iteration=max_low_plan_iteration
        
        self.general_video_tool = general_video_tool
        self.captioning_tool= captioning_tool
        self.slides_tool = slides_tool
        self.audio_tool = audio_tool
        self.max_generate_iteration =max_generate_iteration

    def _create_components(
        self,
        llm_config_path: Path,
        schedule_example_path: Optional[Path],
        silent: bool,
    ) -> None:
        # Load config
        with open(llm_config_path, "r", encoding="utf-8") as f:
            self.cfg = yaml.safe_load(f)

        # logger
        self.qa_logger = get_logger(
            logger_name="QA",
            log_file=self.qa_path,
            console_log_level=logging.WARNING,
            file_format_str="%(message)s",
            silent=silent,
        )
        workflow_format_str = "%(asctime)s - %(levelname)s\n%(message)s\n"
        self.workflow_logger: logging.Logger = get_logger(
            logger_name="Workflow",
            log_file=self.workflow_path,
            console_format_str=workflow_format_str,
            file_format_str=workflow_format_str,
            silent=silent,
        )

        # LLM
        if self.plan_by == "GPT4v":
            self.planner = GPT4(
                config_path=llm_config_path,
                logger=self.qa_logger,
                silent=silent,
                system_message=prompts.system_message,
            )
        elif self.plan_by == "depictqa" or self.eval_by == "depictqa":
            self.planner = DepictQA(logger=self.qa_logger, silent=silent)
        elif self.plan_by == "GPT4_AZ":
            self.planner = GPT4_AZ(
                config_path=llm_config_path,
                logger=self.qa_logger,
                silent=silent,
                system_message=prompts.system_message,
            )
        elif self.plan_by == "GEMINI":
            self.planner = GEMINI(
                config_path=llm_config_path,
                logger=self.qa_logger,
                silent=silent,
                system_message=prompts.system_message,
            )
        elif self.plan_by == "QWEN":
            self.planner = QWEN(
                config_path=llm_config_path,
                logger=self.qa_logger,
                silent=silent,
                system_message=prompts.system_message,
            )
        
        # LLM evaluator
        if self.eval_by == "GPT4v":
            self.evaluator = GPT4(
                config_path=llm_config_path,
                logger=self.qa_logger,
                silent=silent,
                system_message=prompts.system_message,
            )
        elif self.eval_by == "depictqa" :
            self.evaluator = DepictQA(logger=self.qa_logger, silent=silent)
        elif self.eval_by== "GPT4_AZ":
            self.evaluator = GPT4_AZ(
                config_path=llm_config_path,
                logger=self.qa_logger,
                silent=silent,
                system_message=prompts.system_message,
            )
        elif self.eval_by == "GEMINI":
            self.evaluator = GEMINI(
                config_path=llm_config_path,
                logger=self.qa_logger,
                silent=silent,
                system_message=prompts.system_message,
            )
        elif self.eval_by == "QWEN":
            self.evaluator = QWEN(
                config_path=llm_config_path,
                logger=self.qa_logger,
                silent=silent,
                system_message=prompts.system_message,
            )
        #Generator
        if self.art_work == "GPT4_AZ":
            self.art_agent = GPT4_AZ(
                config_path=llm_config_path,
                logger=self.qa_logger,
                silent=silent,
                system_message=prompts.system_message,
            )
        elif self.art_work == "GEMINI":
            self.art_agent = GEMINI(
                config_path=llm_config_path,
                logger=self.qa_logger,
                silent=silent,
                system_message=prompts.system_message,
            )
        elif self.art_work == "QWEN":
            self.art_agent = QWEN(
                config_path=llm_config_path,
                logger=self.qa_logger,
                silent=silent,
                system_message=prompts.system_message,
            )
        if self.audio_tool== "qwentts":
            self.audio_tool = Qwentts(config_path=llm_config_path)
        if self.general_video_tool == "wanx":
            self.general_video_tool = Wanxiang_video(config_path=llm_config_path)
        if self.captioning_tool == "wanx":
            self.captioning_tool = Wanxiang_image(config_path=llm_config_path)

        # SlideRenderer
        try:
            self.slide_renderer = SlideRenderer(
                self.work_dir, self.pdf_path,
                tts_engine=self.audio_tool,
                planner_func=self.planner,
            )
        except Exception as e:
            self.workflow_logger.warning(f"Failed to initialize SlideRenderer: {e}")
            self.slide_renderer = None

        
        # Retriever & Style DB
        try:
            # Check for pre-computed index in data_reference first
            openai_global_index = Path("data_reference/faiss/global")
            data_ref_index = Path("data_reference/paper_index")
            legacy_index = Path("output/test_index")
            
            if openai_global_index.exists():
                index_path = openai_global_index
                use_openai = True
                self.workflow_logger.info(f"Using OpenAI global index at {index_path}")
            elif data_ref_index.exists():
                index_path = data_ref_index
                use_openai = False
                self.workflow_logger.info(f"Using pre-computed index at {index_path}")
            else:
                # Fallback: try to build from dataset if no index found
                self.workflow_logger.info("No index found. Attempting to build from 'dataset' directory...")
                index_path = legacy_index # Default save location for auto-build
                use_openai = False
                source_dir = Path("dataset")
                if source_dir.exists():
                    temp_retriever = PaperRetriever(logger=self.workflow_logger)
                    try:
                        temp_retriever.build_from_dir(source_dir, save_path=index_path)
                        self.workflow_logger.info("Index built successfully.")
                    except Exception as e:
                         self.workflow_logger.error(f"Failed to build index: {e}")
                else:
                     self.workflow_logger.warning("'dataset' directory not found. Cannot build index.")

            self.retriever = PaperRetriever(index_path=index_path, use_openai=use_openai)
            
            # Retrieval Configuration
            self.retrieval_top_k = self.cfg.get("GEMINI", {}).get("retrieval_top_k", 5)
            
            self.style_db = {}
            style_db_path = Path("data_reference/style_db_refined_final/db_summary.json")
            if style_db_path.exists():
                with open(style_db_path, "r") as f:
                    summary = json.load(f)
                    for item in summary:
                        self.style_db[item["video_id"]] = item["path"]
            else:
                self.workflow_logger.warning("Style DB not found. Retrieval will be limited.")
        except Exception as e:
            self.workflow_logger.warning(f"Failed to init retrieval: {e}")


        # example
        if self.with_example:
            assert (
                schedule_example_path is not None
            ), "Example should be provided."
            with open(schedule_example_path, "r") as f:
                examples = json.load(f)
            self.high_example = examples["high_examples"]
            self.low_example = examples["low_examples"]
            self.manim_example = examples["MANIM_examples"]
        random.seed(0)

        # Asset Analyser Initialization
        self.asset_analyser = AssetAnalyser(
            work_dir=self.work_dir,
            pdf_path=self.pdf_path,
            llm_instance=self.planner,  # Pass the main planner for Gemini tasks
            logger=self.workflow_logger
        )

        # Instantiate Disentangled Planners
        self.high_level_planner = HighLevelPlanner(self.planner, self.evaluator, self.workflow_logger)
        self.content_grounder = ContentGrounder(self.planner, self.workflow_logger)
        self.style_planner = StylePlanner(self.planner, self.workflow_logger)
        self.low_level_planner = LowLevelPlanner(self.planner, self.evaluator, self.workflow_logger)
        self.style_refiner = StyleRefiner(self.planner, self.workflow_logger)

        self.workflow_logger.info("Preacher components (and planners) successfully created.")
        """
        Retrieve context for high-level planning.
        """
        context = []
        try:
            # 1. Retrieve similar papers
            k = self.retrieval_top_k
            similar_papers = self.retriever.retrieve_similar_papers(pdf_path=self.pdf_path, k=k)
            self.workflow_logger.info(f"Retrieved {len(similar_papers)} papers for global style context. Top-k={k}")
            
            print(f"\n[USER LOG] Top {len(similar_papers)} similar papers found for global planning:")
            context.append("## Similar Papers found in specific domain:")
            for p in similar_papers:
                title = p.get('paper_name', 'Unknown')
                print(f" - {title}")
                context.append(f"- {title}")
                
            # 2. Retrieve style examples
            style_matches = []
            for p in similar_papers:
                paper_title = p.get('paper_name', '')
                if paper_title in self.style_db:
                    style_matches.append((paper_title, self.style_db[paper_title]))
            
            total_slides_list = []
            if style_matches:
                context.append("\n## Reference Presentation Styles (from existing videos):")
                for title, path in style_matches:
                    meta_path = Path(path)
                    if meta_path.exists():
                        with open(meta_path, "r") as f:
                            meta = json.load(f)
                            total_slides = meta.get("total_slides", len(meta.get("slides", [])))
                            total_slides_list.append(total_slides)
                            context.append(f"- Paper '{title}': total {total_slides} slides.")
                
                if total_slides_list:
                    avg_slides = sum(total_slides_list) / len(total_slides_list)
                    min_slides = min(total_slides_list)
                    max_slides = max(total_slides_list)
                    
                    # Heuristic for recommendation based on content density
                    try:
                        doc = fitz.open(self.pdf_path)
                        page_count = len(doc)
                        
                        # Analyze content density
                        text_len = sum(len(p.get_text()) for p in doc)
                        num_figs = sum(len(p.get_images()) for p in doc)
                        
                        # Heuristic: 
                        # - Baseline: 1.2 scenes per page
                        # - Complexity: Adjust based on average chars per page (baseline 3000)
                        # - Figures: Each figure adds ~0.3 scene weight
                        chars_per_page = text_len / max(1, page_count)
                        complexity_factor = max(0.8, min(1.5, chars_per_page / 3000))
                        
                        content_estimated_slides = (page_count * 1.2 + num_figs * 0.3) * complexity_factor
                        content_estimated_slides = max(5, int(content_estimated_slides))
                        
                        # Weighted average: 60% content density, 40% style reference
                        final_recommendation = int(0.6 * content_estimated_slides + 0.4 * avg_slides)
                        
                        context.append(f"\nRECOMMENDATION: Target approximately {final_recommendation} scenes.")
                        context.append(f"  - Analysis: {page_count} pages, {num_figs} figures, high density factor {complexity_factor:.1f}x.")
                        context.append(f"  - Reference Range: similar papers used {min_slides}-{max_slides} slides.")
                    except Exception as e:
                         self.workflow_logger.warning(f"Failed to analyze PDF content for planning: {e}")
                         context.append(f"\nRECOMMENDATION: Target approximately {int(avg_slides)} scenes.")

        except Exception as e:
            self.workflow_logger.warning(f"Global retrieval failed: {e}")
            import traceback
            self.workflow_logger.error(traceback.format_exc())
            
        return "\n".join(context)

    def retrieve_scene_style(self, scene_plan: dict) -> dict:
        """
        Retrieve layout context for style planning (scene specific).
        Uses section-wise retrieval and queries style_db_refined_final.

        Returns a dict with:
          "layout_specs"        — list of LayoutSpec v1 dicts from metadata_v2.json (preferred)
          "layout_descriptions" — list of fallback verbose strings for slides without layout_spec
          "durations"           — duration statistics dict {min, max, avg}
        """
        narrative_role = scene_plan.get('narrative_role', '').lower()
        if not narrative_role or narrative_role not in ['introduction', 'method', 'experiments', 'results']:
            raise ValueError(f"Invalid narrative_role: {narrative_role}")

        layout_specs = []
        layout_descriptions = []
        durations = []

        try:
            # 1. Section-wise retrieval
            k = self.retrieval_top_k
            index_dir = Path("data_reference/faiss") / narrative_role
            if not index_dir.exists():
                self.workflow_logger.warning(f"FAISS index directory for section '{narrative_role}' at {index_dir} not found. Falling back.")
                return self._fallback_scene_style(scene_plan)

            section_retriever = PaperRetriever(logger=self.workflow_logger, use_openai=True)
            section_retriever.load_index(index_dir, index_name=f"{narrative_role}.faiss", meta_name="metadata.json")

            similar_papers = section_retriever.retrieve_similar_papers(
                pdf_path=self.pdf_path,
                k=k
            )

            print(f"\n[USER LOG] Top {len(similar_papers)} papers for section '{narrative_role}':")
            for p in similar_papers:
                print(f" - {p.get('paper_name', 'Unknown')}")

            # 2. Extract layouts from metadata (prefer metadata_v2.json if it exists)
            for p in similar_papers:
                paper_title = p.get('paper_name', '')
                if paper_title not in self.style_db:
                    continue
                meta_path = Path(self.style_db[paper_title])
                if not meta_path.exists():
                    continue

                # Prefer LayoutSpec v1 from metadata_v2.json
                v2_path = meta_path.parent / "metadata_v2.json"
                load_path = v2_path if v2_path.exists() else meta_path

                with open(load_path, "r") as f:
                    meta = json.load(f)

                for slide in meta.get("slides", []):
                    if slide.get("slide_section", "").lower() != narrative_role:
                        continue

                    # Accumulate duration stats
                    dur = slide.get("t_end", 0) - slide.get("t_start", 0)
                    if dur > 0:
                        durations.append(dur)

                    ls = slide.get("layout_structure", {})

                    # Try LayoutSpec v1 first
                    spec = ls.get("layout_spec")
                    if (
                        spec
                        and isinstance(spec, dict)
                        and spec.get("version") == 1
                        and spec.get("elements")
                    ):
                        layout_specs.append(spec)
                    else:
                        # Fall back to verbose description
                        desc = ls.get("layout_description", "")
                        if desc:
                            layout_descriptions.append(desc)

            if not layout_specs and not layout_descriptions:
                self.workflow_logger.warning(f"No layout data found in style DB for section '{narrative_role}'. Falling back.")
                return self._fallback_scene_style(scene_plan)

            # Sample to avoid overwhelming the prompt (max 5 specs, max 3 descriptions)
            import random as _random
            sampled_specs = _random.sample(layout_specs, min(5, len(layout_specs)))
            sampled_descs = _random.sample(layout_descriptions, min(3, len(layout_descriptions)))

            # On-the-fly conversion: turn sampled verbose descriptions into LayoutSpec v1
            # (used when metadata_v2.json doesn't exist yet — before running style_db_migrate.py)
            if sampled_descs and not sampled_specs:
                self.workflow_logger.info(
                    f"  No pre-migrated LayoutSpecs found. Converting {len(sampled_descs)} "
                    "descriptions on-the-fly via LLM..."
                )
                for desc in sampled_descs:
                    converted = self._desc_to_layout_spec(desc)
                    if converted:
                        sampled_specs.append(converted)
                sampled_descs = []  # consumed — don't send as fallback too

            duration_stats = {}
            if durations:
                duration_stats = {
                    "min": round(min(durations), 1),
                    "max": round(max(durations), 1),
                    "avg": round(sum(durations) / len(durations), 1),
                }

            self.workflow_logger.info(
                f"  Retrieved {len(sampled_specs)} LayoutSpec examples + "
                f"{len(sampled_descs)} fallback descriptions for '{narrative_role}'."
            )

            return {
                "layout_specs": sampled_specs,
                "layout_descriptions": sampled_descs,
                "durations": duration_stats,
            }

        except Exception as e:
            self.workflow_logger.warning(f"Scene retrieval failed: {e}")
            import traceback
            self.workflow_logger.error(traceback.format_exc())
            return self._fallback_scene_style(scene_plan)

    def _fallback_scene_style(self, scene_plan: dict) -> dict:
        """Standard template fallback when retrieval fails.
        Returns the same dict format as retrieve_scene_style().
        """
        self.workflow_logger.info("Falling back to standard description-based style hints.")
        scene_desc = f"{scene_plan.get('summary', '')} {scene_plan.get('title', '')}".lower()

        if any(w in scene_desc for w in ['result', 'performance', 'accuracy', 'table', 'chart', 'graph']):
            desc = "Two-column layout: results table on the left, supporting chart on the right. Clean white background, title at top."
        elif any(w in scene_desc for w in ['method', 'architecture', 'model', 'diagram', 'pipeline']):
            desc = "Two-column layout: architecture diagram on the left, bullet-point explanations on the right."
        else:
            desc = "Single-column layout: title at top, bullet points below covering the main points."

        return {
            "layout_specs": [],
            "layout_descriptions": [desc],
            "durations": {},
        }

    # ── Conversion prompt (kept here to avoid importing migration script) ─────
    _LAYOUT_SPEC_CONVERSION_PROMPT = """\
You are a slide layout expert. Convert this layout description to a LayoutSpec v1 JSON.

layout_description:
{layout_description}

## Element Types
T=title, ST=subtitle, B=bullets, P=paragraph, EQ=equation, L=sub-label,
META=logos/authors, F=figure/image, D=diagram, CH=chart, TAB=table, QR=qr-code

## Layout Signature
Use | for vertical rows and - for horizontal groups. E.g. T|F-B, F, T|TAB-CH

## Required JSON format (version must be integer 1):
{{
  "version": 1,
  "layout_type": "<short label>",
  "layout_tags": ["<tag1>", "<tag2>"],
  "layout_signature": "<sig>",
  "background_color": "#FFFFFF",
  "elements": [
    {{"id": "title", "type": "T", "content_ref": "elements.title",
      "box": {{"x": 0.05, "y": 0.03, "w": 0.90, "h": 0.10}},
      "style": {{"font_size": 40, "bold": true}}}}
  ],
  "global_constraints": {{"no_overlap": true, "no_overflow": true, "min_font_size": 14}}
}}

Return ONLY valid JSON. No markdown fences. No explanation.
"""

    def _desc_to_layout_spec(self, layout_description: str) -> dict | None:
        """Convert a verbose layout_description string to a LayoutSpec v1 dict via LLM.

        Uses self.planner (the same LLM client used by all other planners).
        Returns None if conversion fails.
        """
        prompt = self._LAYOUT_SPEC_CONVERSION_PROMPT.format(
            layout_description=layout_description
        )
        max_retries = 2
        for attempt in range(max_retries):
            try:
                raw = self.planner(prompt=prompt)
                # Strip Python triple-quote wrappers the LLM sometimes adds
                raw = raw.strip().strip('"""').strip("'''").strip()
                parsed = _load_json_dict(raw)
                if parsed and isinstance(parsed, dict):
                    if str(parsed.get("version", "")) == "1":
                        parsed["version"] = 1
                        if "elements" in parsed and isinstance(parsed["elements"], list):
                            return parsed
            except Exception as e:
                self.workflow_logger.warning(
                    f"  _desc_to_layout_spec attempt {attempt+1} failed: {e}"
                )
        self.workflow_logger.warning("  _desc_to_layout_spec: conversion failed. Skipping this description.")
        return None

    def _set_constants(self) -> None:
        self.degra_subtask_dict: dict[Degradation, Subtask] = {
            "low resolution": "super-resolution",
            "noise": "denoising",
            "motion blur": "motion deblurring",
            "defocus blur": "defocus deblurring",
            "haze": "dehazing",
            "rain": "deraining",
            "dark": "brightening",
            "jpeg compression artifact": "jpeg compression artifact removal",
        }
        self.subtask_degra_dict: dict[Subtask, Degradation] = {
            v: k for k, v in self.degra_subtask_dict.items()
        }
        self.degradations = set(self.degra_subtask_dict.keys())
        self.subtasks = set(self.degra_subtask_dict.values())
        self.levels: list[Level] = ["very low", "low", "medium", "high", "very high"]

        # Examples (initialized to None, loaded in _create_components if with_example)
        self.high_example = None
        self.low_example = None
        self.manim_example = None
        
    def _ensure_audio(self, content: str, return_url=False) -> Path:
        target = self.curr_scene_dir / "audio.wav"
        if target.exists():
            return target
        url = self.audio_tool.return_audio(content)
        if return_url:
            return url 
        return Path(download_file(url, target)) 
    def run(self, high_plan: Optional[list[Subtask]]=None) -> None:
        # 1. High Planning
        self.workflow_logger.info("=" * 50)
        self.workflow_logger.info("Step 1: High-level planning...")
        self.workflow_logger.info("=" * 50)

        if high_plan is not None:
            self.workflow_logger.info(f"Loading pre-generated high plan from {high_plan}")
            with open(high_plan, 'r') as file:
                self.high_plan = file.read()
        elif self.high_plan_path.exists():
            self.workflow_logger.info(f"High plan already cached at {self.high_plan_path}. Loading...")
            with open(self.high_plan_path, 'r') as file:
                self.high_plan = file.read()
        else:
            # 1a. Pre-process assets (videos) to feed into high_planning
            # self.workflow_logger.info("=" * 50)
            # self.workflow_logger.info("Step 1a: Pre-processing Assets...")
            # self.workflow_logger.info("=" * 50)

            # video_summaries = self.asset_analyser.analyze_videos()
            self.video_summaries_context = "" # Temporarily disabled
            # if video_summaries:
            #     for v_name, v_data in video_summaries.items():
            #         self.video_summaries_context += f"Filename: {v_name}\nDescription: {v_data['description']}\nRelevance: {v_data['relevance']}\n\n"
            # else:
            #     self.video_summaries_context = "No video assets provided."

            # self.workflow_logger.info(f"Video assets context identified:\n{self.video_summaries_context}")

            self.high_plan = self.high_planning()
            
        # 2. Parse High Plan
        self.workflow_logger.info("=" * 50)
        self.workflow_logger.info("Step 2: Parsing high-level plan...")
        self.workflow_logger.info("=" * 50)

        # Parse string into list using the formalized parser
        self.high_plan_list = self.setting_plan_format(self.high_plan, step="high")

        self.workflow_logger.info(f"Parsed {len(self.high_plan_list)} scenes from high plan.")

        # TODO: Should be done as part of high level plan. and title details should be decided in subseqeunt stages accordingly
        # 2b. Build and prepend title scene
        self.workflow_logger.info("=" * 50)
        self.workflow_logger.info("Step 2b: Building title page scene...")
        self.workflow_logger.info("=" * 50)

        title_metadata = self.extract_title_metadata()
        title_scene = self.build_title_scene(title_metadata)
        self.high_plan_list.insert(0, title_scene)
        self.workflow_logger.info(f"Title scene prepended. Total scenes: {len(self.high_plan_list)}")

        # 3. Low Planning
        self.workflow_logger.info("=" * 50)
        self.workflow_logger.info("Step 3: Low-level planning...")
        self.workflow_logger.info("=" * 50)

        self.final_plan = []
        for i in range(len(self.high_plan_list)):
            self.final_plan.append({})
            self.scene_idx = i
            self.low_planning(self.high_plan_list[i])

        # 4. Video Generation
        self.workflow_logger.info("=" * 50)
        self.workflow_logger.info("Step 4: Generating scene videos...")
        self.workflow_logger.info("=" * 50)

        # Clean up previous scene outputs so videos are always regenerated
        import shutil
        for i in range(len(self.high_plan_list)):
            scene_dir = self.work_dir / f"scene_{i}"
            if scene_dir.exists():
                self.workflow_logger.info(f"Removing previous scene directory: {scene_dir}")
                shutil.rmtree(scene_dir)

        self.video_list = []
        for i in range(len(self.high_plan_list)):
            self.scene_idx = i
            self.workflow_logger.info(f"Generating scene {i}...")
            self.generate_(i)

            video_path = self.work_dir / f"scene_{i}" / f"scene{i}.mp4"
            if video_path.exists():
                self.workflow_logger.info(f"Scene {i} video generated at {video_path}")
                self.video_list.append(video_path)
            else:
                self.workflow_logger.error(f"Scene {i} video NOT found at {video_path}")

        # 5. Concatenation
        self.workflow_logger.info("=" * 50)
        self.workflow_logger.info("Step 5: Concatenating final video...")
        self.workflow_logger.info("=" * 50)

        if not self.video_list:
            raise RuntimeError("No scene videos were generated. Cannot concatenate.")

        concatenate_videos(self.video_list, self.final_video_path_)
        self.workflow_logger.info(f"Final video saved at {self.final_video_path_}")


    def extract_title_metadata(self) -> dict:
        """Extract title, authors, affiliations, venue from the PDF's first page."""
        cache_path = self.log_dir / "title_metadata.json"
        
        if cache_path.exists():
            self.workflow_logger.info(f"Title metadata already cached at {cache_path}. Loading.")
            with open(cache_path, "r") as f:
                return json.load(f)
        
        self.workflow_logger.info("Extracting title metadata from PDF...")
        prompt = prompts.title_extraction_prompt
        raw = eval(self.planner(
            prompt=prompt,
            pdf_path=Path(self.pdf_path),
        ))
        self.workflow_logger.info(f"Title metadata raw: {str(raw)[:300]}")
        
        parsed = _load_json_dict(raw)
        if not parsed or not isinstance(parsed, dict):
            # Fallback: minimal metadata
            self.workflow_logger.warning(f"Title metadata extraction failed. Using fallback.")
            parsed = {
                "paper_title": self.input_path.stem.replace("_", " ").replace("-", " ").title(),
                "authors": [],
                "affiliations": [],
                "venue": "",
            }
        
        with open(cache_path, "w") as f:
            json.dump(parsed, f, indent=4)
        return parsed
    
    def build_title_scene(self, metadata: dict) -> dict:
        """Build a fully-specified title scene plan from extracted metadata."""
        authors = metadata.get("authors", [])
        affiliations = metadata.get("affiliations", [])
        venue = metadata.get("venue", "")
        paper_title = metadata.get("paper_title", "Untitled Paper")
        
        # --- Resolve logos via AssetAnalyser ---
        logos = self.asset_analyser.analyze_images()
        
        # Build available_logos description for the style prompt
        available_logos_desc = []
        if logos.get("conference"):
            conf_path = Path(logos['conference'])
            available_logos_desc.append(f"conference_logo: {conf_path.name}")
        for i, aff_logo in enumerate(logos.get("affiliations", [])):
            if aff_logo:
                aff_path = Path(aff_logo)
                aff_name = affiliations[i].get("name", f"Affiliation {i+1}") if i < len(affiliations) else f"Affiliation {i+1}"
                available_logos_desc.append(f"affiliation_{i+1}_logo: {aff_path.name} ({aff_name})")
        
        if not available_logos_desc:
            available_logos_str = "No logos available."
        else:
            available_logos_str = "\n".join(available_logos_desc)
        
        # --- LLM decides layout ---
        style_prompt = prompts.title_style_prompt.format(
            metadata_json=json.dumps(metadata, indent=2),
            available_logos=available_logos_str,
        )
        raw = eval(self.planner(
            prompt=style_prompt,
            pdf_path=Path(self.pdf_path),
        ))
        self.workflow_logger.info(f"Title style layout: {str(raw)[:300]}")
        
        style_plan = _load_json_dict(raw)
        if not style_plan or not isinstance(style_plan, dict):
            # Fallback layout
            self.workflow_logger.warning("Title style planning failed. Using default layout.")
            style_plan = {
                "layout_template": "title_page",
                "background_color": "#FFFFFF",
                "layout_regions": {
                    "conference_logo": {"x": 0.03, "y": 0.03, "w": 0.15, "h": 0.12},
                    "affiliation_logos": {"x": 0.55, "y": 0.03, "w": 0.42, "h": 0.12},
                    "title": {"x": 0.05, "y": 0.25, "w": 0.9, "h": 0.25},
                    "authors": {"x": 0.1, "y": 0.55, "w": 0.8, "h": 0.12},
                    "affiliations": {"x": 0.1, "y": 0.72, "w": 0.8, "h": 0.08},
                    "venue": {"x": 0.3, "y": 0.82, "w": 0.4, "h": 0.06},
                },
            }
        
        # --- Format display strings ---
        authors_display = format_authors_with_superscripts(authors)
        affiliations_display = format_affiliations_display(authors, affiliations)
        
        # --- Build elements ---
        elements = {
            "title": paper_title,
            "authors": authors_display,
            "affiliations": affiliations_display,
            "venue": venue,
        }
        
        # Add logo paths to elements
        if logos.get("conference"):
            elements["conference_logo"] = {"type": "logo", "path": str(logos["conference"])}
        
        aff_logos_list = []
        for logo_path in logos.get("affiliations", []):
            if logo_path:
                aff_logos_list.append({"type": "logo", "path": str(logo_path)})
        if aff_logos_list:
            elements["affiliation_logos"] = aff_logos_list
        
        # --- Audio ---
        # Short intro narration
        if authors:
            first_author = authors[0].get("name", "the authors")
            if len(authors) > 1:
                audio = f"This paper, titled {paper_title}, is by {first_author} and colleagues."
            else:
                audio = f"This paper, titled {paper_title}, is by {first_author}."
        else:
            audio = f"This paper is titled {paper_title}."
        if venue:
            audio += f" Presented at {venue}."
        
        # --- Assemble scene plan ---
        regions = style_plan.get("layout_regions", {})
        
        # Remove logo regions if no logos available
        if not logos.get("conference") and "conference_logo" in regions:
            del regions["conference_logo"]
        if not aff_logos_list and "affiliation_logos" in regions:
            del regions["affiliation_logos"]
        
        scene = {
            "scene_id": 0,
            "title": paper_title,
            "summary": f"Title page for: {paper_title}",
            "paper_section": "Title",
            "narrative_role": "title",
            "time_allocation_sec": 5,
            "style": "Slides",
            "layout": {
                "template": "title_page",
                "background_color": style_plan.get("background_color", "#FFFFFF"),
                "regions": regions,
            },
            "elements": elements,
            "builds": [
                {
                    "step_index": 0,
                    "time_offset_sec": 0.0,
                    "actions": [{"type": "show", "target": "all"}],
                    "audio_segment": audio,
                }
            ],
            "expected_build_steps": 1,
            "time_cost": "5",
            "audio_content": audio,
            "prompt": f"Title page showing paper title, authors, and logos for: {paper_title}",
        }
        
        # Cache title scene
        with open(self.log_dir / "title_scene.json", "w") as f:
            json.dump(scene, f, indent=4)
        
        self.workflow_logger.info(f"Title scene built: {paper_title}")
        return scene

    def high_planning(self) -> str: # Changed return type to str
        """Sets the initial plan."""
        return self.high_level_planner.high_planning(
            pdf_path=self.pdf_path,
            high_plan_path=self.high_plan_path,
            with_reflection=self.with_reflection,
            with_example=self.with_example,
            high_example=self.high_example,
            max_high_plan_iteration=self.max_high_plan_iteration,
            video_summaries_context=self.video_summaries_context
        )
    
    def high_plan_by_llm(self, style_context, video_summaries_context, eval_results=None, high_plan=None) -> str:
        return self.high_level_planner.high_plan_by_llm(self.pdf_path, style_context, video_summaries_context, self.with_example, self.high_example, eval_results, high_plan)
    
    def high_evaluate_by_llm(self, high_plan) -> str:
        return self.high_level_planner.high_evaluate_by_llm(self.pdf_path, high_plan)
    
    def low_planning(self, part_plan):
        """Orchestrate the 4-stage low-level planning pipeline."""
        plan_file = self.log_dir / f"file_{self.scene_idx}.json"
        
        # Check if final plan already cached
        if os.path.exists(plan_file):
            self.workflow_logger.info(f"Scene {self.scene_idx}: Low plan already exists at {plan_file}. Skipping.")
            with open(plan_file, "r") as file:
                self.final_plan[self.scene_idx] = json.load(file)
                return None
        
        # Title scenes skip the 4-stage pipeline — they are already fully specified
        if part_plan.get("narrative_role") == "title":
            self.workflow_logger.info(f"Scene {self.scene_idx}: Title scene — skipping 4-stage pipeline.")
            self.final_plan[self.scene_idx] = part_plan.copy()
            with open(plan_file, "w") as file:
                json.dump(self.final_plan[self.scene_idx], file, indent=4)
            return None
        
        self.workflow_logger.info(f"Scene {self.scene_idx}: Starting 4-stage low-level planning...")
        self.final_plan[self.scene_idx] = part_plan.copy()
        
        # ── Stage 1: Content Extraction ──
        content_file = self.log_dir / f"content_{self.scene_idx}.json"
        if os.path.exists(content_file):
            self.workflow_logger.info(f"  Stage 1: Content already cached. Loading.")
            with open(content_file, "r") as f:
                content_summary = json.load(f)
        else:
            self.workflow_logger.info(f"  Stage 1: Extracting content from paper...")
            past_contents = []
            for past_idx in range(max(0, self.scene_idx - 2), self.scene_idx):
                past_file = self.log_dir / f"content_{past_idx}.json"
                if os.path.exists(past_file):
                    try:
                        with open(past_file, "r") as f:
                            past_contents.append(json.load(f))
                    except Exception:
                        pass
            content_summary = self.content_grounder.content_extract_by_llm(self.pdf_path, self.scene_idx, part_plan, past_contents)
            with open(content_file, "w") as f:
                json.dump(content_summary, f, indent=4)
        
        # ── Stage 2: Style Planning (Layout) ──
        style_file = self.log_dir / f"style_{self.scene_idx}.json"
        if os.path.exists(style_file):
            self.workflow_logger.info(f"  Stage 2: Style plan already cached. Loading.")
            with open(style_file, "r") as f:
                style_plan = json.load(f)
        else:
            self.workflow_logger.info(f"  Stage 2: Planning style/layout...")
            style_advice = self.retrieve_scene_style(part_plan)
            style_plan = self.style_planner.style_plan_by_llm(self.pdf_path, self.scene_idx, part_plan, content_summary, style_advice)
            with open(style_file, "w") as f:
                json.dump(style_plan, f, indent=4)

        # Augment LayoutSpec v1 with backward-compatible fields needed by Stage 3 and Stage 4.
        # Stage 3 (low_level_planning_prompt) checks has_figure / has_video to decide whether
        # to include a figure/video block. Stage 4 (style_refiner) reads layout_template,
        # layout_regions, and has_figure directly. Without these, figures are silently dropped.
        if style_plan.get("version") == 1:
            elem_types = {e.get("type", "") for e in style_plan.get("elements", [])}
            elem_ids   = {e.get("id", "")   for e in style_plan.get("elements", [])}
            style_plan.setdefault("has_figure", bool(elem_types & {"F", "D", "TAB", "CH"}))
            style_plan.setdefault("has_video",  "video" in elem_ids)
            style_plan.setdefault("layout_template", style_plan.get("layout_type", "custom"))
            style_plan.setdefault("layout_regions",  {
                e["id"]: e["box"] for e in style_plan.get("elements", [])
            })

        # ── Stage 3: Low-Level Content Drafting (and Duration) ──
        low_file = self.log_dir / f"low_{self.scene_idx}.json"
        if os.path.exists(low_file):
            self.workflow_logger.info(f"  Stage 3: Low-level draft already cached. Loading.")
            with open(low_file, "r") as f:
                content_draft = json.load(f)
        else:
            self.workflow_logger.info(f"  Stage 3: Drafting content and deciding flexible duration...")
            duration_stat = part_plan.get("duration_stat", {"min": 5.0, "max": 15.0, "avg": 8.0})
            
            # Fetch past content draft to avoid repetition in drafting
            past_contents = []
            if self.scene_idx > 0:
                past_file = self.log_dir / f"low_{self.scene_idx - 1}.json"
                if os.path.exists(past_file):
                    try:
                        with open(past_file, "r") as f:
                            past_contents.append(json.load(f))
                    except Exception:
                        pass

            # ── Introspective QA Loop (wired via low_planning) ──────────────
            # When self.with_reflection is True this runs the full
            #   draft → Self-QA → "No, Revise" → ... loop from the diagram.
            # When False it falls through to a single draft call (fast path).
            content_draft = self.low_level_planner.low_planning(
                self.pdf_path, self.scene_idx, part_plan, content_summary,
                style_plan, duration_stat, past_contents,
                with_reflection=self.with_reflection,
                max_iterations=self.max_low_plan_iteration,
            )
            with open(low_file, "w") as f:
                json.dump(content_draft, f, indent=4)
        
        # ── Stage 4: Style Refinement (assign content to builds) ──
        refine_file = self.log_dir / f"refine_{self.scene_idx}.json"
        if os.path.exists(refine_file):
            self.workflow_logger.info(f"  Stage 4: Refined plan already cached. Loading.")
            with open(refine_file, "r") as f:
                final_refined = json.load(f)
        else:
            self.workflow_logger.info(f"  Stage 4: Assigning content to builds...")
            final_refined = self.style_refiner.style_refine_by_llm(self.pdf_path, self.scene_idx, content_draft, style_plan)
            # Ensure duration_sec is carried over
            final_refined["time_allocation_sec"] = content_draft.get("duration_sec", 8.0)
            with open(refine_file, "w") as f:
                json.dump(final_refined, f, indent=4)
        
        # ── Merge everything into final plan ──
        merged_plan = part_plan.copy()
        merged_plan["extracted_content"] = content_summary.get("extracted_content", "")

        # Handle both LayoutSpec v1 output and old layout_template/layout_regions format
        if style_plan.get("version") == 1:
            # New LayoutSpec v1 format from style planner
            from .layout.layout_compile import spec_to_layout_dict
            from .layout.layout_spec import LayoutSpec
            spec = LayoutSpec.from_dict(style_plan)
            merged_plan["layout"] = spec_to_layout_dict(spec)
        else:
            # Legacy format (backward compatibility)
            merged_plan["layout"] = {
                "template": style_plan.get("layout_template", "one_col_bullets"),
                "background_color": style_plan.get("background_color", "#FFFFFF"),
                "regions": style_plan.get("layout_regions", {}),
            }
        # Merge refined output (elements, builds, style, audio_content, etc.)
        merged_plan.update(final_refined)
        # Add source, audio_content, prompt and duration from content draft
        merged_plan["source"] = content_draft.get("source", [])
        merged_plan["time_allocation_sec"] = content_draft.get("duration_sec", merged_plan.get("time_allocation_sec", 8.0))
        merged_plan["audio_content"] = content_draft.get("audio_content", "")
        merged_plan["prompt"] = content_draft.get("prompt", "")
        
        self.final_plan[self.scene_idx] = merged_plan
        
        # Save final combined plan
        with open(plan_file, "w") as file:
            json.dump(self.final_plan[self.scene_idx], file, indent=4)
        self.workflow_logger.info(f"  Scene {self.scene_idx}: All 4 stages complete. Saved to {plan_file}")
    
    def low_evaluate_by_llm(self, low_plan_str) -> tuple:
        return self.low_level_planner.low_evaluate_by_llm(self.pdf_path, self.scene_idx, low_plan_str)
    
    def generate_(self, scene_idx):
        self.curr_scene_dir = self.work_dir / "scene_{}".format(scene_idx)
        if not os.path.isdir(self.curr_scene_dir):
            self.curr_scene_dir.mkdir()
        style = self.final_plan[scene_idx]["style"].lower()
        if hasattr(self, 'slide_renderer') and self.slide_renderer:
            try:
                video_path = self.slide_renderer.render_scene(self.final_plan[scene_idx], scene_idx)
            except Exception as e:
                raise Exception(f"SlideRenderer failed: {e}")
        else:
            raise Exception("SlideRenderer not found. Cannot generate video.")

        return video_path

    def math_single_work(self, plan, eval_results=None, code_str=None):
        eval_prompt = "Please check if the above code follows the rules mentioned. If not, modify it: "+\
            "The first line should be 'def animate(self):\n'; the last line should be in the format 'self.wait(X)', where X is a positive integer;"+\
                " does the code have a strong mathematical nature? Does it align with theme {}? Directly output the modified code (Code should be easy). Error message:".format(plan["prompt"])
        if eval_results==None:
            prompt = " Please write a python function named animate at the letf-bottom part in the bottom left corner of the screen about {}. ".format(plan["source"])+\
                "The requirements are: "+\
                "Use the MANIM package function should be part of the Scene class in MANIM , NO NEED TO IMPORT package"+\
                "The first line SHOULD be 'def animate(self):\n '; the last line should be in the format 'self.wait(X)'"+\
                " The function product visual content such as intuitive function graphs."+\
                " Should conform to {} and {}.".format(plan["source"], plan["prompt"]) +\
                " Only output the function defnition code. Example:"
            prompt_r = "Rewrite this promptso as A WHOLE sentence to make it fits as acaption in a video. Keep the word with around 5 words perline"+\
                " using \"\n\" to separate lines. JUST A MEANINGFUL sentence!"
            plan["prompt"] = eval(
                self.art_agent(
                    prompt=prompt_r+"\n" + plan["prompt"],
                ))
            code_str = eval(
                self.art_agent(
                    prompt=prompt+self.manim_example,
                    pdf_path=Path(self.pdf_path),
                    ))
        else:
            code_str = eval(
                self.art_agent(
                    prompt=  eval_results+ "\n"+code_str,
                    pdf_path=Path(self.pdf_path),
                    ))
        code_str = eval(
                self.art_agent(
                    prompt=prompts.pro_format_prompt+"\n" + code_str,
                    ))
        code_str = extract_code(code_str)
        video_path = None
        while video_path == None:
            try:
                replace_animate(self.animate_path, code_str)
                print("CHECKING CODE-2")
                video_path = render_video(self.curr_scene_dir,plan)
                print("CHECKING CODE-3")
            except Exception as e:
                error_msg = str(e)  # Capture the actual error message
                code_str = eval(
                self.evaluator(
                    prompt= code_str+ "\n"+ eval_prompt + f"\nError message: {error_msg}",
                ))
                code_str = eval(
                    self.evaluator(
                prompt=prompts.pro_format_prompt+"\n" + code_str,
                ))
                code_str = extract_code(code_str)
        return code_str, video_path

    def video_evaluate_by_mllm(self, plan, video_path, type='video'):
        if type=='video':
            img_list = extract_key_frames(video_path)
        elif type=='image':
            img_list = image_to_images(video_path)
        else:
            img_list = None
        if "general" in plan["style"].lower():
            prompt_e = plan["prompt"] + ' \n '+ prompts.gen_vis_eval
        elif "professional" in plan["style"].lower():
            prompt_e =  plan["scenario"] + ' \n '+   plan["prompt"] + ' \n '+ prompts.pro_vis_eval 
        elif "captioning" in plan["style"].lower():
            prompt_e = prompts.gen_vis_eval
        elif "slides" in plan["style"].lower():
            # Use summary or audio_content as the text to evaluate against since 'prompt' is missing for slides
            text_desc = plan.get('summary', plan.get('audio_content', ''))
            prompt_e = prompts.slides_vis_eval + text_desc
        else: print("error: Please check the style file of"+plan["scenario"])
        eval_results = eval(
            self.evaluator(
                prompt = prompt_e,
                img_path=img_list,
                ))
        success = classify_response(eval_results)
        return success, eval_results
    
    def setting_plan_format(self, plan, step="low"):
        if step == "high":
            # Parse the raw string into a list of scenes
            parsed_plan = _load_json_dict(plan)

            # Handle double-serialized cache: json.dump wraps a string in quotes
            if parsed_plan is None or isinstance(parsed_plan, str):
                try:
                    unwrapped = json.loads(plan) if isinstance(plan, str) else plan
                    parsed_plan = _load_json_dict(unwrapped)
                except Exception:
                    pass

            # Handle dict-wrapped plans (e.g. {"scenes": [...]})
            if isinstance(parsed_plan, dict):
                for v in parsed_plan.values():
                    if isinstance(v, list):
                        parsed_plan = v
                        break

            if not isinstance(parsed_plan, list):
                raise ValueError(f"High plan parsing failed: expected list, got {type(parsed_plan)}. Raw: {str(plan)[:200]}")
                
            return parsed_plan
        return plan


    def _prepare_dir(self, input_path, output_dir) -> None:

        pdf_name = input_path.stem
        self.input_path = input_path
        self.work_dir = output_dir / pdf_name
        if not os.path.isdir(self.work_dir):
            self.work_dir.mkdir(parents=True)

        self.log_dir = self.work_dir / "logs"
        if not os.path.isdir(self.log_dir):
            self.log_dir.mkdir()
        self.qa_path = self.log_dir / "llm_qa.md"
        self.workflow_path = self.log_dir / "workflow.log"
        self.high_plan_path = self.log_dir / "highplan.txt"
        self.final_video_path_= self.log_dir / "final_video.mp4"
        self.animate_path =  Path("utils/math_vis.py").resolve()
        #self.plan_path = self.log_dir


    # def tolist(self, high_plan: str) -> list:
    #     if self.plan_by=='GEMINI':
    #         return text_to_list(high_plan)

