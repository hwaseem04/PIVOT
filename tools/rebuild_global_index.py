import logging
from pathlib import Path
import sys

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from tools.retriever import PaperRetriever
from utils.logger import get_logger

def rebuild_global_index():
    logger = get_logger("RebuildGlobalIndex")
    logger.info("Initializing PaperRetriever with OpenAI support...")
    
    # Initialize with OpenAI support
    retriever = PaperRetriever(use_openai=True, logger=logger)
    
    # Paths
    data_ref_dir = project_root / "data_reference"
    output_dir = data_ref_dir / "faiss" / "global"
    
    # Find all PDFs in data_reference (excluding those in faiss/ subdirs)
    pdf_paths = list(data_ref_dir.glob("*.pdf"))
    # Also check subdirectories but exclude 'faiss'
    for item in data_ref_dir.iterdir():
        if item.is_dir() and item.name != "faiss" and item.name != "style_db_refined_final":
             pdf_paths.extend(list(item.rglob("*.pdf")))
    
    # Filter duplicates
    pdf_paths = list(set(pdf_paths))
    
    if not pdf_paths:
        logger.error("No PDFs found in data_reference directory.")
        return

    logger.info(f"Found {len(pdf_paths)} papers to index.")
    
    # Build and save
    try:
        retriever.build_index(pdf_paths, save_path=output_dir)
        logger.info(f"Global index successfully built and saved to {output_dir}")
    except Exception as e:
        logger.error(f"Failed to build index: {e}")
        import traceback
        logger.error(traceback.format_exc())

if __name__ == "__main__":
    rebuild_global_index()
