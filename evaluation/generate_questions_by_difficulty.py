#!/usr/bin/env python
"""
Generate ground truth Q&A organized by difficulty level for all PDFs in a directory.

Output structure:
  evaluation/questions/easy.json    — 5 questions per paper (1 per category)
  evaluation/questions/medium.json  — 10 questions per paper (2 per category)
  evaluation/questions/hard.json    — 20 questions per paper (4 per category)

Skip logic: papers already present in a difficulty file are not regenerated.

Usage: python -u evaluation/generate_questions_by_difficulty.py <pdf_directory>
"""

import json
import os
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional

sys.stdout.reconfigure(line_buffering=True)
sys.stderr.reconfigure(line_buffering=True)

import fitz  # PyMuPDF

sys.path.append(str(Path(__file__).parent.parent))
from llms.gemini import GEMINI


# ---------------------------------------------------------------------------
# Difficulty configs
# ---------------------------------------------------------------------------

CATEGORIES = [
    "core_contribution",
    "methodology",
    "experimental_results",
    "limitations",
    "negative_traps",
]

DIFFICULTY_CONFIGS = {
    "easy": {
        "questions_per_paper": 5,
        "per_category": 1,
        "guidelines": (
            "Easy questions should test surface-level understanding. "
            "Answers are directly and explicitly stated in the paper. "
            "A student who skimmed the paper should be able to answer these."
        ),
    },
    "medium": {
        "questions_per_paper": 10,
        "per_category": 2,
        "guidelines": (
            "Medium questions require understanding connections between concepts. "
            "Answers may need combining information from different parts of the paper. "
            "A student who read the paper carefully should be able to answer these."
        ),
    },
    "hard": {
        "questions_per_paper": 20,
        "per_category": 4,
        "guidelines": (
            "Hard questions require deep comprehension, inference, or synthesis "
            "across multiple sections. They may ask about implications, trade-offs, "
            "comparisons with related work, or subtle technical details. "
            "Only a student who studied the paper thoroughly should answer these."
        ),
    },
}


# ---------------------------------------------------------------------------
# Prompt template
# ---------------------------------------------------------------------------

PROMPT_TEMPLATE = """You are evaluating a research paper. Generate exactly {total_questions} questions at the **{difficulty}** difficulty level.

## Difficulty Guidelines
{guidelines}

## Category Distribution (generate exactly this many per category)
{category_breakdown}

## Category Descriptions
1. **core_contribution** — Main problem, key innovation, differences from prior work
2. **methodology** — Key components, algorithms, techniques, implementation details
3. **experimental_results** — Datasets, metrics, main results, baseline comparisons
4. **limitations** — Acknowledged limitations, constraints, assumptions
5. **negative_traps** — Things the paper does NOT claim, methods NOT used, results NOT achieved

For each question provide:
- question text
- comprehensive answer based on the paper
- category (one of: core_contribution, methodology, experimental_results, limitations, negative_traps)

Return ONLY a JSON object:
{{
  "questions": [
    {{
      "id": 1,
      "category": "core_contribution",
      "question": "...",
      "answer": "..."
    }},
    ...
  ]
}}

Paper content:
{paper_text}
"""


# ---------------------------------------------------------------------------
# Reused helpers (from generate_all_questions.py)
# ---------------------------------------------------------------------------

def extract_pdf_text(pdf_path: str) -> str:
    """Extract text from PDF, excluding appendix and references."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()

    text_lower = text.lower()
    appendix_markers = [
        "\nappendix",
        "\nreferences",
        "\nsupplementary material",
        "\nsupplementary",
        "\nappendices",
    ]
    earliest_pos = len(text)
    for marker in appendix_markers:
        pos = text_lower.find(marker)
        if pos != -1 and pos < earliest_pos:
            earliest_pos = pos

    if earliest_pos < len(text):
        text = text[:earliest_pos]
        print(f"   Excluded content after position {earliest_pos} (appendix/references)")

    return text


def find_pdfs(folder: str) -> List[Path]:
    """Find all PDFs in folder."""
    return sorted(Path(folder).glob("*.pdf"))


def parse_llm_json(content: str) -> Dict:
    """Parse JSON from LLM response, handling markdown code blocks and extra text."""
    # Strip markdown code fences first
    if "```json" in content:
        content = content.split("```json")[1].split("```")[0].strip()
    elif "```" in content:
        content = content.split("```")[1].split("```")[0].strip()

    # Try direct parse
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        pass

    # Extract the outermost JSON object using brace matching
    start = content.find('{')
    if start == -1:
        raise ValueError(f"No JSON object found in response: {content[:200]}")

    depth = 0
    for i in range(start, len(content)):
        if content[i] == '{':
            depth += 1
        elif content[i] == '}':
            depth -= 1
            if depth == 0:
                return json.loads(content[start:i + 1])

    raise ValueError(f"Unbalanced braces in response: {content[:200]}")


# ---------------------------------------------------------------------------
# Core logic
# ---------------------------------------------------------------------------

def load_existing(difficulty: str) -> Dict:
    """Load existing questions file for a difficulty, or return empty structure."""
    path = Path(f"evaluation/questions/{difficulty}.json")
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return {"papers": {}, "metadata": {}}


def save_questions(difficulty: str, data: Dict) -> None:
    """Save questions file for a difficulty."""
    out_dir = Path("evaluation/questions")
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{difficulty}.json"
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def build_prompt(difficulty: str, paper_text: str) -> str:
    """Build the LLM prompt for a given difficulty."""
    cfg = DIFFICULTY_CONFIGS[difficulty]
    category_lines = "\n".join(
        f"- **{cat}**: {cfg['per_category']} question(s)"
        for cat in CATEGORIES
    )
    return PROMPT_TEMPLATE.format(
        total_questions=cfg["questions_per_paper"],
        difficulty=difficulty,
        guidelines=cfg["guidelines"],
        category_breakdown=category_lines,
        paper_text=paper_text,
    )


def generate_for_difficulty(
    difficulty: str,
    pdfs: List[Path],
    llm: GEMINI,
    paper_texts: Dict[str, str],
) -> Dict:
    """Generate questions for one difficulty level, skipping existing papers."""
    cfg = DIFFICULTY_CONFIGS[difficulty]
    data = load_existing(difficulty)

    papers_to_process = []
    for pdf_path in pdfs:
        name = pdf_path.stem
        existing = data["papers"].get(name)
        if existing and len(existing.get("questions", [])) >= cfg["questions_per_paper"]:
            print(f"  [SKIP] {name} — already has {len(existing['questions'])} questions")
        else:
            papers_to_process.append(pdf_path)

    if not papers_to_process:
        print(f"  All papers already have {difficulty} questions. Nothing to do.")
        return data

    for i, pdf_path in enumerate(papers_to_process, 1):
        name = pdf_path.stem
        print(f"  [{i}/{len(papers_to_process)}] Generating {difficulty} questions for {name}...")

        max_retries = 3
        for attempt in range(1, max_retries + 1):
            try:
                text = paper_texts[name]
                prompt = build_prompt(difficulty, text)
                response = llm(prompt=prompt)
                qa_data = parse_llm_json(response)

                # Tag each question with difficulty
                for q in qa_data["questions"]:
                    q["difficulty"] = difficulty

                data["papers"][name] = {
                    "pdf_path": str(pdf_path),
                    "questions": qa_data["questions"],
                    "num_questions": len(qa_data["questions"]),
                }
                print(f"    Generated {len(qa_data['questions'])} questions")

                # Save after each paper so progress isn't lost
                save_questions(difficulty, data)
                break  # success

            except Exception as e:
                if attempt < max_retries:
                    print(f"    Attempt {attempt} failed: {e}. Retrying...")
                    time.sleep(2)
                else:
                    print(f"    Failed after {max_retries} attempts: {e}")
                    data["papers"][name] = {
                        "pdf_path": str(pdf_path),
                        "error": str(e),
                        "questions": [],
                    }

        if i < len(papers_to_process):
            time.sleep(2)

    # Update metadata
    total_q = sum(
        p.get("num_questions", 0) for p in data["papers"].values()
    )
    data["metadata"] = {
        "difficulty": difficulty,
        "questions_per_paper": cfg["questions_per_paper"],
        "total_papers": len(data["papers"]),
        "total_questions": total_q,
        "category_distribution": {cat: cfg["per_category"] for cat in CATEGORIES},
    }
    save_questions(difficulty, data)
    return data


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) != 2:
        print("Usage: python evaluation/generate_questions_by_difficulty.py <pdf_directory>")
        sys.exit(1)

    folder = sys.argv[1]
    if not os.path.isdir(folder):
        print(f"Error: Folder not found: {folder}")
        sys.exit(1)

    pdfs = find_pdfs(folder)
    if not pdfs:
        print(f"No PDFs found in: {folder}")
        sys.exit(1)

    print(f"{'=' * 60}")
    print("GENERATING QUESTIONS BY DIFFICULTY")
    print(f"{'=' * 60}")
    print(f"\nFound {len(pdfs)} PDF(s)")
    print(f"Output directory: evaluation/questions/\n")

    # Extract text once for all papers
    paper_texts: Dict[str, str] = {}
    for pdf_path in pdfs:
        name = pdf_path.stem
        print(f"Extracting text: {name}")
        paper_texts[name] = extract_pdf_text(str(pdf_path))
        print(f"  {len(paper_texts[name])} characters")

    llm = GEMINI(config_path=Path("config.yml"), silent=True)

    start_time = time.time()

    for difficulty in ["easy", "medium", "hard"]:
        cfg = DIFFICULTY_CONFIGS[difficulty]
        print(f"\n{'─' * 60}")
        print(f"  {difficulty.upper()} — {cfg['questions_per_paper']} questions/paper, {cfg['per_category']} per category")
        print(f"{'─' * 60}")
        generate_for_difficulty(difficulty, pdfs, llm, paper_texts)

    elapsed = time.time() - start_time
    print(f"\n{'=' * 60}")
    print("COMPLETE")
    print(f"{'=' * 60}")
    print(f"Time: {elapsed:.1f}s ({elapsed / 60:.1f} min)")

    for difficulty in ["easy", "medium", "hard"]:
        path = Path(f"evaluation/questions/{difficulty}.json")
        if path.exists():
            with open(path) as f:
                d = json.load(f)
            n_papers = len(d.get("papers", {}))
            n_q = d.get("metadata", {}).get("total_questions", 0)
            print(f"  {difficulty}.json — {n_papers} papers, {n_q} questions")


if __name__ == "__main__":
    main()
