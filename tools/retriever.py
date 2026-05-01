from pathlib import Path
import json
import logging
import fitz 
import numpy as np
from typing import List, Dict, Optional, Tuple, Any

# Optional imports for embeddings and faiss
try:
    from sentence_transformers import SentenceTransformer
    import faiss
    from openai import OpenAI
except ImportError:
    SentenceTransformer = None
    faiss = None
    OpenAI = None

from utils.logger import get_logger

class PaperRetriever:
    """
    Retrieves similar papers based on content embeddings.
    """
    def __init__(
        self,
        index_path: Optional[Path] = None,
        use_openai: bool = True,
        openai_model: str = "text-embedding-3-small",
        model_name: str = "all-MiniLM-L6-v2",
        logger: Optional[logging.Logger] = None
    ):
        self.logger = logger or get_logger("Retriever")
        self.use_openai = use_openai
        self.openai_model = openai_model
        
        if faiss is None:
            self.logger.warning("faiss not installed. Retrieval will fail.")
            self.index = None
        else:
            self.index = None

        if self.use_openai:
            if OpenAI is None:
                raise ImportError("openai package not installed but use_openai=True")
            self.client = OpenAI()
            self.model = None
        else:
            if SentenceTransformer is None:
                self.logger.warning("sentence-transformers not installed. Local retrieval will fail.")
                self.model = None
            else:
                self.model = SentenceTransformer(model_name)

        self.papers_metadata: List[Dict] = []
        if index_path and index_path.exists():
            self.load_index(index_path)

    def extract_paper_text(self, pdf_path: Path) -> Dict[str, Any]:
        """
        Extract key sections from a PDF for embedding.
        Returns a dict with 'title', 'abstract', 'content'.
        """
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        
        # Simple heuristic extraction (can be improved with docling/LLM)
        # For now, we treat the first page text as high signal (title/abstract)
        # and the rest as content.
        first_page_text = doc[0].get_text()
        doc.close()
        
        return {
            "paper_name": pdf_path.stem.replace("_", " ").replace("-", " ").title(),
            "abstract": first_page_text[:1000],
            "content": text,
            "path": str(pdf_path)
        }

    def build_index(self, pdf_paths: List[Path], save_path: Optional[Path] = None):
        """
        Builds a FAISS index from a list of PDF paths.
        """
        if not self.use_openai and not self.model:
            raise ImportError("sentence-transformers not installed and use_openai=False")

        self.logger.info(f"Building index for {len(pdf_paths)} papers using {'OpenAI' if self.use_openai else 'Local'} embeddings...")
        
        embeddings = []
        self.papers_metadata = []

        for i, pdf_path in enumerate(pdf_paths):
            try:
                data = self.extract_paper_text(pdf_path)
                # Embed a combination of paper_name and abstract/start of content
                text_to_embed = f"{data.get('paper_name', '')} {data.get('abstract', '')}"
                
                if self.use_openai:
                    response = self.client.embeddings.create(
                        input=[text_to_embed],
                        model=self.openai_model
                    )
                    embedding = response.data[0].embedding
                else:
                    embedding = self.model.encode(text_to_embed)
                
                embeddings.append(embedding)
                
                # Store metadata
                self.papers_metadata.append({
                    "id": i,
                    "path": str(pdf_path),
                    "paper_name": data.get("paper_name", ""),
                    "excerpt": data.get("abstract", "")[:200]
                })
            except Exception as e:
                self.logger.error(f"Failed to process {pdf_path}: {e}")

        if not embeddings:
            self.logger.warning("No embeddings created.")
            return

        embeddings_np = np.array(embeddings).astype('float32')
        dimension = embeddings_np.shape[1]
        
        if self.use_openai:
            # Normalize for cosine similarity
            faiss.normalize_L2(embeddings_np)
            self.index = faiss.IndexFlatIP(dimension)
        else:
            self.index = faiss.IndexFlatL2(dimension)
            
        self.index.add(embeddings_np)
        
        if save_path:
            self.save_index(save_path)
            
        self.logger.info(f"Index built with {self.index.ntotal} documents.")

    def build_from_dir(self, source_dir: Path, save_path: Optional[Path] = None):
        """
        Builds index from all PDFs in a directory.
        """
        source_dir = Path(source_dir)
        if not source_dir.exists():
            raise FileNotFoundError(f"Source directory {source_dir} not found")
            
        pdf_paths = list(source_dir.glob("*.pdf"))
        if not pdf_paths:
            self.logger.warning(f"No PDFs found in {source_dir}")
            return
            
        self.build_index(pdf_paths, save_path)

    def save_index(self, path: Path):
        path = Path(path)
        path.mkdir(parents=True, exist_ok=True)
        
        # Save FAISS index
        faiss.write_index(self.index, str(path / "paper_index.faiss"))
        
        # Save metadata
        with open(path / "paper_metadata.json", "w") as f:
            json.dump(self.papers_metadata, f, indent=2)

    def load_index(self, path: Path, index_name: str = "paper_index.faiss", meta_name: str = "paper_metadata.json"):
        path = Path(path)
        if not (path / index_name).exists():
            raise FileNotFoundError(f"Index {index_name} not found at {path}")
            
        self.index = faiss.read_index(str(path / index_name))
        
        meta_file = path / meta_name
        if meta_file.exists():
            with open(meta_file, "r") as f:
                self.papers_metadata = json.load(f)
                # Normalize metadata keys: verify paper_name exists
                # Section indices use 'paper_name', global index might have 'title' if old
                for item in self.papers_metadata:
                    if 'paper_name' not in item and 'title' in item:
                        item['paper_name'] = item['title']
        else:
            self.logger.warning(f"Metadata file {meta_name} not found at {path}")
            self.papers_metadata = []

    def retrieve_similar_papers(self, query: str = None, pdf_path: Path = None, k: int = 5) -> List[Dict]:
        """
        Retrieve top-k similar papers. query can be text string or a PDF path to use as query.
        """
        if not self.index or (not self.use_openai and not self.model):
            raise RuntimeError("Index not loaded or dependencies missing.")

        query_text = ""
        if pdf_path:
            data = self.extract_paper_text(pdf_path)
            query_text = f"{data.get('paper_name', '')} {data.get('abstract', '')}"
        elif query:
            query_text = query
        else:
            raise ValueError("Must provide either query string or pdf_path")

        if self.use_openai:
            response = self.client.embeddings.create(
                input=[query_text],
                model=self.openai_model
            )
            query_embedding = np.array([response.data[0].embedding]).astype('float32')
        else:
            query_embedding = self.model.encode([query_text]).astype('float32')
            
        D, I = self.index.search(query_embedding, k)
        
        results = []
        for dist, idx in zip(D[0], I[0]):
            if idx < len(self.papers_metadata) and idx >= 0:
                item = self.papers_metadata[idx].copy()
                item['distance'] = float(dist)
                results.append(item)
                
        return results

if __name__ == "__main__":
    # Test stub
    logging.basicConfig(level=logging.INFO)
    retriever = PaperRetriever()
    print("Retriever initialized.")
