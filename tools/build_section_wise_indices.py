import json
import logging
from pathlib import Path
import sys
from typing import List, Dict, Any, Optional
import numpy as np
import os

# Add parent directory to path to import utils
sys.path.append(str(Path(__file__).parent.parent))

from utils.logger import get_logger

try:
    from openai import OpenAI
    import faiss
except ImportError:
    print("Please install: pip install openai faiss-cpu")
    sys.exit(1)

class SectionIndexBuilder:
    """Builds FAISS indices for specific paper sections derived from Gemini summaries."""
    
    SECTIONS = ["introduction", "method", "experiments", "results"]

    def __init__(
        self,
        summaries_dir: Path,
        output_base_dir: Path,
        model_name: str = "text-embedding-3-small",
        logger: Optional[logging.Logger] = None
    ):
        self.summaries_dir = Path(summaries_dir)
        self.output_base_dir = Path(output_base_dir)
        self.logger = logger or get_logger("SectionIndexBuilder")
        self.model_name = model_name
        self.client = OpenAI() # Assumes OPENAI_API_KEY is in environment
        
        # Storage for each section
        self.section_data = {sec: {"texts": [], "metadata": []} for sec in self.SECTIONS}

    def load_summaries(self):
        """Load and categorize text from the JSON summary files."""
        json_files = list(self.summaries_dir.glob("*.json"))
        self.logger.info(f"Found {len(json_files)} summary files.")

        for json_path in json_files:
            try:
                with open(json_path, 'r') as f:
                    data = json.load(f)
                
                paper_name = data.get("paper_name", json_path.stem)
                sections = data.get("sections", {})
                
                for sec_key in self.SECTIONS:
                    content = sections.get(sec_key)
                    if content and isinstance(content, str):
                        self.section_data[sec_key]["texts"].append(content)
                        self.section_data[sec_key]["metadata"].append({
                            "paper_name": paper_name,
                            "section": sec_key,
                            "source_file": str(json_path)
                        })
            except Exception as e:
                self.logger.error(f"Error processing {json_path}: {e}")

    def get_embeddings(self, texts: List[str]) -> np.ndarray:
        """Get embeddings from OpenAI API."""
        self.logger.info(f"Requesting embeddings for {len(texts)} texts from OpenAI...")
        response = self.client.embeddings.create(
            input=texts,
            model=self.model_name
        )
        embeddings = [data.embedding for data in response.data]
        return np.array(embeddings).astype('float32')

    def build_and_save_indices(self):
        """Build and save FAISS indices for each section."""
        for sec_key in self.SECTIONS:
            texts = self.section_data[sec_key]["texts"]
            metadata = self.section_data[sec_key]["metadata"]
            
            if not texts:
                self.logger.warning(f"No content found for section: {sec_key}")
                continue
                
            self.logger.info(f"Building index for section '{sec_key}' with {len(texts)} entries...")
            
            # Create embeddings
            embeddings_np = self.get_embeddings(texts)
            
            # Normalize for cosine similarity (Inner Product on normalized vectors is cosine similarity)
            faiss.normalize_L2(embeddings_np)
            
            # Build index
            dimension = embeddings_np.shape[1]
            index = faiss.IndexFlatIP(dimension)
            index.add(embeddings_np)
            
            # Prepare output directory
            output_dir = self.output_base_dir / sec_key
            output_dir.mkdir(parents=True, exist_ok=True)
            
            # Save index and metadata
            index_filename = f"{sec_key}.faiss"
            faiss.write_index(index, str(output_dir / index_filename))
            with open(output_dir / "metadata.json", "w") as f:
                json.dump(metadata, f, indent=2)
                
            self.logger.info(f"Saved {sec_key} index to {output_dir}")

def main():
    logging.basicConfig(level=logging.INFO)
    
    # Paths based on user request and project structure
    project_root = Path(__file__).parent.parent
    summaries_dir = project_root / "data_reference" / "categorised_section_summary_extraction_gemini"
    # Store all indices in a 'faiss' parent folder
    output_base_dir = project_root / "data_reference" / "faiss"
    
    builder = SectionIndexBuilder(summaries_dir, output_base_dir)
    builder.load_summaries()
    builder.build_and_save_indices()

if __name__ == "__main__":
    main()
