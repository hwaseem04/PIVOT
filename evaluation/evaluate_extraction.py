"""
Evaluate extraction quality using a student LLM.

The student LLM attempts to answer ground truth questions using ONLY
the extracted information (figures, audio transcript, bullets).

Questions are loaded per difficulty level from evaluation/questions/{easy,medium,hard}.json.
Results are saved per difficulty under evaluation/results/{paper}/{difficulty}/.
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional

sys.path.append(str(Path(__file__).parent.parent))
from llms.gemini import GEMINI


DIFFICULTIES = ["easy", "medium", "hard"]

STUDENT_PROMPT = """You are a student who has watched a video presentation of a research paper. You have access to:
- The audio transcript from the video
- Visual bullet points shown in the video
- Extracted figures and images (attached)
- Figure descriptions and context
- Scene summaries

Your task: Answer the following question using ONLY the information provided below. Do not use any external knowledge.

**STRICT RULES:**
- If you cannot answer based on the given information, respond with: "INSUFFICIENT_INFORMATION"
- Do not speculate or infer beyond what is explicitly stated
- Be concise but complete in your answer

---

**Audio Transcript:**
{transcript}

**Bullet Points:**
{bullets}

**Figure Descriptions:**
{figures}

**Key Tables:**
{tables}

**Additional Context (Scene summaries and details):**
{context}

---

**Question:** {question}

**Your Answer:**
"""

def _match_paper_key(folder_name: str, paper_keys: list) -> Optional[str]:
    """Match an output folder name to a paper key in the questions JSON.

    Naming convention: folder_name.split('_')[0] gives the paper key.
    e.g. 'federated_veo' -> 'federated', 'ego3d_bytedance' -> 'ego3d'
    """
    # Exact match first
    if folder_name in paper_keys:
        return folder_name

    # Extract paper name as first segment before '_'
    paper_name = folder_name.split('_')[0]
    if paper_name in paper_keys:
        return paper_name

    return None


def load_questions_by_difficulty(folder_name: str) -> Dict[str, List[Dict]]:
    """Load questions from evaluation/questions/{difficulty}.json files.

    Uses naming convention to match folder_name (e.g. 'federated_veo') to
    the paper key in the questions JSON (e.g. 'federated').

    Returns {"easy": [...], "medium": [...], "hard": [...]}.
    """
    questions_by_diff: Dict[str, List[Dict]] = {}
    matched_key = None

    for difficulty in DIFFICULTIES:
        path = Path(f"evaluation/questions/{difficulty}.json")
        if not path.exists():
            continue
        with open(path) as f:
            data = json.load(f)

        papers = data.get("papers", {})
        key = _match_paper_key(folder_name, list(papers.keys()))
        if key:
            matched_key = key
            paper_data = papers[key]
            if paper_data.get("questions"):
                questions_by_diff[difficulty] = paper_data["questions"]

    if matched_key:
        print(f"   Matched '{folder_name}' -> paper '{matched_key}' in questions JSON")

    # Fallback to old consolidated file
    if not questions_by_diff:
        consolidated_path = Path("evaluation/all_questions_test.json")
        if consolidated_path.exists():
            with open(consolidated_path) as f:
                all_data = json.load(f)
            key = _match_paper_key(folder_name, list(all_data.get("papers", {}).keys()))
            if key:
                paper_data = all_data["papers"][key]
                if paper_data.get("questions"):
                    for q in paper_data["questions"]:
                        diff = q.get("difficulty", "medium")
                        questions_by_diff.setdefault(diff, []).append(q)

    if not questions_by_diff:
        raise FileNotFoundError(
            f"No questions found matching '{folder_name}'.\n"
            f"Run: python evaluation/generate_questions_by_difficulty.py <pdf_dir>"
        )

    return questions_by_diff


def load_extracted_info(output_dir: Path) -> Dict:
    """Load extracted information from a pipeline output directory.

    Args:
        output_dir: Direct path to the output folder (e.g. style_agent_output/federated_veo)

    Reads both file_*.json and content_*.json for each scene.
    """
    output_dir = Path(output_dir)
    logs_dir = output_dir / "logs"

    if not logs_dir.exists():
        raise FileNotFoundError(
            f"Pipeline output not found: {output_dir}\n"
            f"Expected logs/ directory inside {output_dir}"
        )

    # Collect all information
    all_transcripts = []
    all_audio_segments = []
    all_bullets = []
    all_summaries = []
    all_extracted_content = []
    all_tables = []
    figure_info = {}

    file_jsons = sorted(logs_dir.glob("file_*.json"), key=lambda x: int(x.stem.split('_')[1]))

    for file_json in file_jsons:
        idx = int(file_json.stem.split('_')[1])
        content_json = logs_dir / f"content_{idx}.json"

        # 1. Process file_i.json
        with open(file_json, 'r') as f:
            file_data = json.load(f)

            if 'summary' in file_data and file_data['summary']:
                all_summaries.append(f"[Scene {idx}] {file_data['summary']}")

            if 'extracted_content' in file_data and file_data['extracted_content']:
                all_extracted_content.append(f"[Scene {idx} - Narrative] {file_data['extracted_content']}")

            if 'audio_content' in file_data and file_data['audio_content']:
                all_transcripts.append(f"[Scene {idx}] {file_data['audio_content']}")

            if 'builds' in file_data and isinstance(file_data['builds'], list):
                for build in file_data['builds']:
                    if isinstance(build, dict) and 'audio_segment' in build and build['audio_segment']:
                        all_audio_segments.append(build['audio_segment'])

            if 'elements' in file_data:
                elements = file_data['elements']

                if 'bullets' in elements:
                    bullets = elements['bullets']
                    if isinstance(bullets, list):
                        for b in bullets:
                            all_bullets.append(f"[Scene {idx}] {b}")

                if 'figure' in elements:
                    fig = elements['figure']
                    if isinstance(fig, dict) and 'ref' in fig:
                        fig_ref = fig.get('ref', 'Unknown')
                        if fig_ref not in figure_info:
                            figure_info[fig_ref] = {
                                'caption': fig.get('caption', ''),
                                'relevance': fig.get('relevance', ''),
                                'context': []
                            }
                        if 'extracted_content' in file_data:
                             figure_info[fig_ref]['context'].append(file_data['extracted_content'])

        # 2. Process content_i.json (if exists)
        if content_json.exists():
            with open(content_json, 'r') as f:
                content_data = json.load(f)

                if 'extracted_content' in content_data and content_data['extracted_content']:
                     if 'extracted_content' in file_data and content_data['extracted_content'] != file_data['extracted_content']:
                         all_extracted_content.append(f"[Scene {idx} - Raw] {content_data['extracted_content']}")
                     elif 'extracted_content' not in file_data:
                         all_extracted_content.append(f"[Scene {idx} - Raw] {content_data['extracted_content']}")

                if 'key_tables' in content_data and isinstance(content_data['key_tables'], list):
                    for table in content_data['key_tables']:
                        all_tables.append(table)

    full_transcript = "\n\n".join(all_transcripts)

    figure_descriptions = []
    for fig_ref, info in figure_info.items():
        desc = f"Figure/Table Ref: {fig_ref}\nCaption: {info['caption']}"
        unique_contexts = list(set(info['context']))
        if unique_contexts:
            combined_context = "\n".join(unique_contexts)
            desc += f"\nContext/Discussion: {combined_context[:800]}..."
        figure_descriptions.append(desc)

    table_descriptions = []
    for table in all_tables:
        t_desc = f"Table: {table.get('ref', 'Unknown')}\nCaption: {table.get('caption', '')}\nRelevance: {table.get('relevance', '')}"
        table_descriptions.append(t_desc)

    all_images = []
    extracted_images = sorted(output_dir.glob("extracted_*.png"), key=lambda x: int(x.stem.split('_')[1]))
    for img_path in extracted_images:
        all_images.append(str(img_path))

    return {
        'transcript': full_transcript,
        'bullets': all_bullets,
        'figures': figure_descriptions,
        'tables': table_descriptions,
        'summaries': all_summaries,
        'extracted_content': all_extracted_content,
        'images': all_images
    }


def format_extracted_info(info: Dict) -> Dict[str, str]:
    """Format extracted info for the prompt."""
    context_parts = []
    if info.get('summaries'):
        context_parts.append("Scene Summaries:\n" + "\n".join([f"- {s}" for s in info['summaries']]))
    if info.get('extracted_content'):
        content = "\n".join(info['extracted_content'])
        if len(content) > 15000:
             content = content[:15000] + "... (truncated)"
        context_parts.append("Detailed Content:\n" + content)

    return {
        'transcript': info['transcript'] or "No transcript available",
        'bullets': "\n".join([f"• {b}" for b in info['bullets']]) or "No bullets available",
        'figures': "\n\n".join(info['figures']) or "No figures available",
        'tables': "\n\n".join(info['tables']) or "No tables available",
        'context': "\n\n".join(context_parts) if context_parts else "No additional context"
    }


def ask_student(question: str, extracted_info: Dict, llm: GEMINI) -> str:
    """Ask student LLM to answer the question."""
    formatted_info = format_extracted_info(extracted_info)

    prompt = STUDENT_PROMPT.format(
        question=question,
        **formatted_info
    )

    img_path_lst = []
    if 'images' in extracted_info:
        try:
            from PIL import Image
            for p in extracted_info['images']:
                try:
                    img = Image.open(p)
                    img_path_lst.append(img)
                except Exception as e:
                    print(f"Warning: Could not open image {p}: {e}")
        except ImportError:
            print("Warning: PIL not installed, cannot load images.")

    _, response = llm.query(prompt=prompt, img_path_lst=img_path_lst)

    return response.strip()


def evaluate_all_questions(qa_data: Dict, extracted_info: Dict, llm: GEMINI) -> List[Dict]:
    """Evaluate all questions with the student LLM."""
    results = []

    for i, q_data in enumerate(qa_data['questions'], 1):
        print(f"  Question {i}/{len(qa_data['questions'])}: {q_data['category']}")

        student_answer = ask_student(q_data['question'], extracted_info, llm)

        results.append({
            'id': q_data['id'],
            'category': q_data['category'],
            'difficulty': q_data.get('difficulty', 'unknown'),
            'question': q_data['question'],
            'ground_truth_answer': q_data['answer'],
            'student_answer': student_answer,
            'answered': student_answer != "INSUFFICIENT_INFORMATION"
        })

    return results


def save_student_answers(run_name: str, difficulty: str, results: List[Dict]) -> Path:
    """Save student answers for a specific difficulty level."""
    out_dir = Path("evaluation/results") / run_name / difficulty
    out_dir.mkdir(parents=True, exist_ok=True)

    output_path = out_dir / "student_answers.json"
    with open(output_path, 'w') as f:
        json.dump({'answers': results}, f, indent=2)

    print(f"  Saved to: {output_path}")
    return output_path


def main():
    if len(sys.argv) != 2:
        print("Usage: python evaluate_extraction.py <output_dir>")
        print("\nExamples:")
        print("  python evaluation/evaluate_extraction.py style_agent_output/federated")
        print("  python evaluation/evaluate_extraction.py style_agent_output/federated_veo")
        sys.exit(1)

    output_dir = Path(sys.argv[1].rstrip('/'))
    run_name = output_dir.name  # e.g. "federated_veo"

    if not output_dir.exists():
        print(f"Error: Directory not found: {output_dir}")
        sys.exit(1)

    print(f"Evaluating: {run_name}")
    print(f"Output dir: {output_dir}")
    print("=" * 60)

    # Load questions by difficulty (matches run_name to paper key via naming convention)
    print("1. Loading questions by difficulty...")
    questions_by_diff = load_questions_by_difficulty(run_name)
    for diff, qs in questions_by_diff.items():
        print(f"   {diff}: {len(qs)} questions")

    # Load extracted information directly from the output directory
    print("\n2. Loading extracted information...")
    extracted_info = load_extracted_info(output_dir)
    print(f"   Transcript: {len(extracted_info['transcript'])} chars")
    print(f"   Bullets: {len(extracted_info['bullets'])} items")
    print(f"   Figures: {len(extracted_info['figures'])} items")
    print(f"   Tables: {len(extracted_info['tables'])} items")
    print(f"   Scene summaries: {len(extracted_info.get('summaries', []))} items")
    print(f"   Extracted content sections: {len(extracted_info.get('extracted_content', []))} items")

    # Save extracted context for verification
    results_dir = Path("evaluation/results") / run_name
    results_dir.mkdir(parents=True, exist_ok=True)
    extracted_context_path = results_dir / "extracted_context.json"
    with open(extracted_context_path, 'w') as f:
        json.dump(extracted_info, f, indent=2)
    print(f"   Extracted context saved to: {extracted_context_path}")

    # Initialize LLM
    llm = GEMINI(config_path=Path("config.yml"), silent=True)

    # Evaluate per difficulty
    print("\n3. Student LLM answering questions per difficulty...")
    for difficulty in DIFFICULTIES:
        if difficulty not in questions_by_diff:
            print(f"\n  [{difficulty.upper()}] No questions found, skipping.")
            continue

        questions = questions_by_diff[difficulty]
        print(f"\n  [{difficulty.upper()}] Answering {len(questions)} questions...")

        qa_data = {'questions': questions}
        results = evaluate_all_questions(qa_data, extracted_info, llm)

        save_student_answers(run_name, difficulty, results)

        # Print summary for this difficulty
        answered = sum(1 for r in results if r['answered'])
        print(f"  Answered: {answered}/{len(results)} ({answered/len(results)*100:.1f}%)")

    # Overall summary
    print("\n" + "=" * 60)
    print("Summary by difficulty:")
    for difficulty in DIFFICULTIES:
        ans_path = Path("evaluation/results") / run_name / difficulty / "student_answers.json"
        if ans_path.exists():
            with open(ans_path) as f:
                data = json.load(f)
            answers = data['answers']
            answered = sum(1 for a in answers if a['answered'])
            total = len(answers)
            print(f"  {difficulty}: {answered}/{total} answered ({answered/total*100:.1f}%)")

    print(f"\nNext step: python evaluation/judge.py {output_dir}")


if __name__ == "__main__":
    main()
