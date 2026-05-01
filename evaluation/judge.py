"""
LLM-as-judge evaluation.

Compares student answers against ground truth and assigns scores.
Processes each difficulty level separately, then produces an overall report.

Results per difficulty: evaluation/results/{paper}/{difficulty}/
Aggregated report:     evaluation/results/{paper}/overall_report.json
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Optional

sys.path.append(str(Path(__file__).parent.parent))
from llms.gemini import GEMINI


DIFFICULTIES = ["easy", "medium", "hard"]

JUDGE_PROMPT = """You are an expert judge evaluating whether a student's answer correctly captures the key information from a reference answer.

**Ground Truth Answer:**
{ground_truth}

**Student's Answer:**
{student_answer}

**Question Type:** {category}

Evaluate the student's answer on these criteria:

1. **Accuracy (0-10)**: Does the answer contain correct information?
2. **Completeness (0-10)**: Does it cover the key points from the ground truth?
3. **Relevance (0-10)**: Is the answer focused on the question?

**Special Cases:**
- If student answered "INSUFFICIENT_INFORMATION", score 0 on all criteria but note it as "info_missing"
- For negative trap questions, correctness means properly NOT claiming something

Return ONLY a JSON object:
{{
  "accuracy": <0-10>,
  "completeness": <0-10>,
  "relevance": <0-10>,
  "overall_score": <0-10>,
  "reasoning": "<brief explanation>",
  "info_missing": <true/false>
}}
"""


def load_student_answers(paper_name: str, difficulty: str) -> Optional[Dict]:
    """Load student answers for a specific difficulty."""
    answers_path = Path("evaluation/results") / paper_name / difficulty / "student_answers.json"
    if not answers_path.exists():
        return None
    with open(answers_path) as f:
        return json.load(f)


def judge_answer(ground_truth: str, student_answer: str, category: str, llm: GEMINI) -> Dict:
    """Judge a single answer."""
    prompt = JUDGE_PROMPT.format(
        ground_truth=ground_truth,
        student_answer=student_answer,
        category=category
    )

    response = llm(prompt=prompt)
    content = response.strip()

    # Extract JSON
    if "```json" in content:
        content = content.split("```json")[1].split("```")[0].strip()
    elif "```" in content:
        content = content.split("```")[1].split("```")[0].strip()

    # Robust extraction: find first { and last }
    start = content.find('{')
    end = content.rfind('}') + 1
    if start != -1 and end != -1:
        content = content[start:end]

    try:
        return json.loads(content)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        print(f"Raw content: {content}")
        return {
            "accuracy": 0,
            "completeness": 0,
            "relevance": 0,
            "overall_score": 0,
            "reasoning": f"JSON parsing failed: {e}",
            "info_missing": False
        }


def evaluate_all_answers(student_data: Dict, llm: GEMINI) -> List[Dict]:
    """Evaluate all student answers."""
    results = []

    for i, answer_data in enumerate(student_data['answers'], 1):
        print(f"    Judging {i}/{len(student_data['answers'])}: {answer_data['category']}")

        judgment = judge_answer(
            ground_truth=answer_data['ground_truth_answer'],
            student_answer=answer_data['student_answer'],
            category=answer_data['category'],
            llm=llm
        )

        results.append({
            **answer_data,
            'judgment': judgment
        })

    return results


def calculate_metrics(results: List[Dict]) -> Dict:
    """Calculate metrics for a set of results."""
    total = len(results)
    if total == 0:
        return {}

    avg_accuracy = sum(r['judgment']['accuracy'] for r in results) / total
    avg_completeness = sum(r['judgment']['completeness'] for r in results) / total
    avg_relevance = sum(r['judgment']['relevance'] for r in results) / total
    avg_overall = sum(r['judgment']['overall_score'] for r in results) / total

    info_missing_count = sum(1 for r in results if r['judgment'].get('info_missing', False))
    info_missing_rate = info_missing_count / total * 100

    # By category
    category_metrics = {}
    for r in results:
        cat = r['category']
        if cat not in category_metrics:
            category_metrics[cat] = {'scores': [], 'count': 0}
        category_metrics[cat]['scores'].append(r['judgment']['overall_score'])
        category_metrics[cat]['count'] += 1

    for cat in category_metrics:
        scores = category_metrics[cat]['scores']
        category_metrics[cat]['avg_score'] = sum(scores) / len(scores)

    return {
        'overall': {
            'accuracy': round(avg_accuracy, 2),
            'completeness': round(avg_completeness, 2),
            'relevance': round(avg_relevance, 2),
            'overall_score': round(avg_overall, 2)
        },
        'info_missing_rate': round(info_missing_rate, 2),
        'info_missing_count': info_missing_count,
        'total_questions': total,
        'by_category': {cat: round(data['avg_score'], 2) for cat, data in category_metrics.items()},
    }


def save_difficulty_report(paper_name: str, difficulty: str, results: List[Dict], metrics: Dict):
    """Save detailed results and report for one difficulty level."""
    output_dir = Path("evaluation/results") / paper_name / difficulty
    output_dir.mkdir(parents=True, exist_ok=True)

    detailed_path = output_dir / "detailed_results.json"
    with open(detailed_path, 'w') as f:
        json.dump({'results': results}, f, indent=2)

    report_path = output_dir / "evaluation_report.json"
    with open(report_path, 'w') as f:
        json.dump(metrics, f, indent=2)

    print(f"    Saved: {report_path}")


def aggregate_overall_report(paper_name: str) -> Dict:
    """Aggregate per-difficulty reports into overall_report.json."""
    all_results = []
    by_difficulty = {}

    for difficulty in DIFFICULTIES:
        report_path = Path("evaluation/results") / paper_name / difficulty / "evaluation_report.json"
        detailed_path = Path("evaluation/results") / paper_name / difficulty / "detailed_results.json"

        if not report_path.exists():
            continue

        with open(report_path) as f:
            metrics = json.load(f)
        by_difficulty[difficulty] = metrics

        if detailed_path.exists():
            with open(detailed_path) as f:
                data = json.load(f)
            all_results.extend(data.get('results', []))

    if not by_difficulty:
        return {}

    # Compute aggregated overall metrics across all difficulties
    total = len(all_results)
    if total == 0:
        return {"by_difficulty": by_difficulty}

    judgments = [r['judgment'] for r in all_results if 'judgment' in r]
    n = len(judgments)

    # By category (across all difficulties)
    category_scores = {}
    for r in all_results:
        cat = r['category']
        category_scores.setdefault(cat, []).append(r['judgment']['overall_score'])

    info_missing_count = sum(1 for r in all_results if r.get('judgment', {}).get('info_missing', False))

    overall_report = {
        'by_difficulty': by_difficulty,
        'overall': {
            'accuracy': round(sum(j['accuracy'] for j in judgments) / n, 2),
            'completeness': round(sum(j['completeness'] for j in judgments) / n, 2),
            'relevance': round(sum(j['relevance'] for j in judgments) / n, 2),
            'overall_score': round(sum(j['overall_score'] for j in judgments) / n, 2),
        },
        'total_questions': total,
        'info_missing_rate': round(info_missing_count / total * 100, 2),
        'info_missing_count': info_missing_count,
        'by_category': {
            cat: round(sum(scores) / len(scores), 2)
            for cat, scores in category_scores.items()
        },
    }

    output_path = Path("evaluation/results") / paper_name / "overall_report.json"
    with open(output_path, 'w') as f:
        json.dump(overall_report, f, indent=2)

    return overall_report


def print_report(overall_report: Dict):
    """Pretty print the overall evaluation report."""
    print("\n" + "=" * 60)
    print("EVALUATION REPORT")
    print("=" * 60)

    # Per difficulty
    print("\nBy Difficulty Level:")
    for diff, metrics in overall_report.get('by_difficulty', {}).items():
        ov = metrics.get('overall', {})
        score = ov.get('overall_score', 0)
        missing = metrics.get('info_missing_rate', 0)
        n = metrics.get('total_questions', 0)
        print(f"  {diff.upper()} ({n} questions): score={score}, info_missing={missing:.1f}%")

    # Overall
    ov = overall_report.get('overall', {})
    print(f"\nOverall Scores (0-10):")
    for metric, score in ov.items():
        print(f"  {metric.replace('_', ' ').title()}: {score}")

    print(f"\nInformation Coverage:")
    total = overall_report.get('total_questions', 0)
    missing_rate = overall_report.get('info_missing_rate', 0)
    missing_count = overall_report.get('info_missing_count', 0)
    print(f"  Questions with sufficient info: {100 - missing_rate:.1f}%")
    print(f"  Questions with insufficient info: {missing_rate:.1f}% ({missing_count}/{total})")

    print("\nBy Category:")
    for cat, score in overall_report.get('by_category', {}).items():
        print(f"  {cat}: {score}")

    print("\n" + "=" * 60)


def main():
    if len(sys.argv) != 2:
        print("Usage: python judge.py <output_dir>")
        print("\nExamples:")
        print("  python evaluation/judge.py style_agent_output/federated")
        print("  python evaluation/judge.py style_agent_output/federated_veo")
        sys.exit(1)

    output_dir = Path(sys.argv[1].rstrip('/'))
    run_name = output_dir.name  # e.g. "federated_veo"

    print(f"LLM-as-judge evaluation for: {run_name}")
    print("=" * 60)

    llm = GEMINI(config_path=Path("config.yml"), silent=True)

    for difficulty in DIFFICULTIES:
        student_data = load_student_answers(run_name, difficulty)
        if not student_data:
            print(f"\n  [{difficulty.upper()}] No student answers found, skipping.")
            continue

        n = len(student_data['answers'])
        print(f"\n  [{difficulty.upper()}] Judging {n} answers...")

        results = evaluate_all_answers(student_data, llm)
        metrics = calculate_metrics(results)
        save_difficulty_report(run_name, difficulty, results, metrics)

    # Aggregate
    print("\nAggregating overall report...")
    overall_report = aggregate_overall_report(run_name)

    if overall_report:
        print_report(overall_report)
        print(f"\nOverall report: evaluation/results/{run_name}/overall_report.json")
    else:
        print("No results to aggregate.")


if __name__ == "__main__":
    main()
