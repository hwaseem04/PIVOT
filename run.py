"""
Unified entry point for Paper2Video pipeline.

Steps:
  1. Check/build FAISS retrieval index from PDFs in data_reference/
  2. Check/build style DB from videos in data_reference/final/
  3. Run Preacher agent on the given input PDF

Usage:
  python run.py <input_pdf>
  python run.py <input_pdf> --output_dir output --llm GEMINI --reflection --examples
  python run.py <input_pdf> --high_plan path/to/highplan.txt --noreflection
"""

import sys
import logging
from pathlib import Path

import fire

project_root = Path(__file__).resolve().parent
sys.path.append(str(project_root))

from tools.retriever import PaperRetriever
from tools.build_style_db_gemini_v2 import build_style_db
from pipeline.preacher import Preacher
from utils.logger import get_logger


def ensure_faiss_index(logger):
    """Build FAISS index if it doesn't already exist."""
    index_path = project_root / "data_reference" / "paper_index"
    
    if index_path.exists() and any(index_path.iterdir()):
        logger.info(f"FAISS index already exists at {index_path}. Skipping build.")
        return index_path
    
    data_ref_dir = project_root / "data_reference"
    if not data_ref_dir.exists():
        raise FileNotFoundError(f"Data reference directory not found: {data_ref_dir}")
    
    pdf_paths = list(data_ref_dir.rglob("*.pdf"))
    if not pdf_paths:
        raise FileNotFoundError(f"No PDFs found in {data_ref_dir}. Cannot build FAISS index.")
    
    logger.info(f"Building FAISS index from {len(pdf_paths)} PDFs...")
    retriever = PaperRetriever(logger=logger)
    retriever.build_index(pdf_paths, save_path=index_path)
    logger.info(f"FAISS index built at {index_path}")
    return index_path


def ensure_style_db(logger):
    """Build style DB if it doesn't already exist."""
    style_db_dir = project_root / "data_reference" / "style_db_refined_final"
    style_db_summary = style_db_dir / "db_summary.json"
    
    if style_db_summary.exists():
        logger.info(f"Style DB already exists at {style_db_summary}. Skipping build.")
        return style_db_summary
    
    video_dir = project_root / "data_reference" / "final"
    if not video_dir.exists():
        raise FileNotFoundError(f"Video reference directory not found: {video_dir}. Cannot build style DB.")
    
    videos = list(video_dir.rglob("*.mp4"))
    if not videos:
        raise FileNotFoundError(f"No videos found in {video_dir}. Cannot build style DB.")
    
    logger.info(f"Building style DB from {len(videos)} videos...")
    
    # ensure output dir
    style_db_dir.mkdir(parents=True, exist_ok=True)
    
    # Call builder
    build_style_db(
        input_dir=str(video_dir),
        output_dir=str(style_db_dir)
    )
    
    logger.info(f"Style DB built at {style_db_summary}")
    return style_db_summary


def main(
    input_pdf: str,
    output_dir: str = "output",
    config: str = "config.yml",
    llm: str = "GEMINI",
    examples: bool = False,    
    reflection: bool = False,
    rollback: bool = False,
    high_plan: str = None,
):
    """
    Run the Paper2Video pipeline.

    Args:
        input_pdf: Path to the input PDF file.
        output_dir: Output directory.
        config: Path to LLM config YAML.
        llm: LLM backend (GEMINI, GPT4_AZ, GPT4v, QWEN).
        reflection: Enable reflection loops for planning.
        examples: Enable few-shot examples in prompts.
        high_plan: Path to a pre-generated high-level plan file.
    """
    logger = get_logger("Paper2Video", console_log_level=logging.INFO)

    input_path = Path(input_pdf).resolve()
    output_dir = Path(output_dir).resolve()
    llm_config_path = Path(config).resolve()

    if not input_path.exists():
        logger.error(f"Input PDF not found: {input_path}")
        sys.exit(1)

    # Step 1: Ensure FAISS index
    # logger.info("=" * 50)
    # logger.info("Step 1: Checking FAISS retrieval index...")
    # logger.info("=" * 50)
    # ensure_faiss_index(logger) #TODO: it should also check for section wise faiss index which will be created soon.

    # Step 2: Ensure Style DB
    # logger.info("=" * 50)
    # logger.info("Step 2: Checking style database...")
    # logger.info("=" * 50)
    # ensure_style_db(logger) #TODO: it should also check for style_db_refined_final

    # Step 3: Run Preacher agent
    logger.info("=" * 50)
    logger.info("Step 3: Running Preacher agent...")
    logger.info("=" * 50)


    # TODO: change code structure of Preacher. 
    agent = Preacher(
        input_path=input_path,
        output_dir=output_dir,
        llm_config_path=llm_config_path,
        plan_by=llm,
        eval_by=llm,
        art_work=llm,
        with_example=examples,
        with_reflection=reflection,
        with_rollback=rollback,
        silent=False,
    )

    high_plan_path = Path(high_plan).resolve() if high_plan else None
    agent.run(high_plan=high_plan_path)

    logger.info("=" * 50)
    logger.info("Pipeline complete!")
    logger.info("=" * 50)


if __name__ == "__main__":
    fire.Fire(main)
