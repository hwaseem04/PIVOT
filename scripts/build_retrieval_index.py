import sys
from pathlib import Path
import logging

# Add project root to sys.path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from tools.retriever import PaperRetriever
from utils.logger import get_logger

def main():
    logger = get_logger("IndexBuilder")
    
    data_ref_dir = project_root / "data_reference"
    index_save_path = data_ref_dir / "paper_index"
    
    if not data_ref_dir.exists():
        logger.error(f"Data reference directory not found: {data_ref_dir}")
        return
        
    logger.info(f"Scanning for PDFs in {data_ref_dir}...")
    
    # Initialize retriever
    retriever = PaperRetriever(logger=logger)
    
    try:
        # Scan and build
        # We search recursively just in case
        pdf_paths = list(data_ref_dir.rglob("*.pdf"))
        
        if not pdf_paths:
            logger.warning(f"No PDFs found in {data_ref_dir} or subdirectories.")
            return
            
        logger.info(f"Found {len(pdf_paths)} PDFs. Building index...")
        
        retriever.build_index(pdf_paths, save_path=index_save_path)
        logger.info(f"Successfully built index at {index_save_path}")
        
    except Exception as e:
        logger.error(f"Failed to build index: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
