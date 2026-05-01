"""
Batch evaluation script for multiple output directories.

Runs the full pipeline (student evaluation + judge) for each output folder
in style_agent_output/, then generates an aggregate batch report.

Usage:
  python evaluation/batch_evaluate.py style_agent_output/
  python evaluation/batch_evaluate.py style_agent_output/federated_veo style_agent_output/ego3d_veo
"""

import json
import os
import sys
import subprocess
from pathlib import Path
from typing import List, Dict, Optional


DIFFICULTIES = ["easy", "medium", "hard"]


def find_output_dirs(parent_dir: str) -> List[Path]:
    """Find all output subdirectories (those with a logs/ folder inside)."""
    parent = Path(parent_dir)
    dirs = []
    for d in sorted(parent.iterdir()):
        if d.is_dir() and (d / "logs").exists():
            dirs.append(d)
    return dirs


def run_evaluation_pipeline(output_dir: Path) -> Optional[Dict]:
    """Run full evaluation pipeline for a single output directory."""
    run_name = output_dir.name

    print(f"\n{'='*60}")
    print(f"Evaluating: {run_name}")
    print(f"{'='*60}")

    steps = [
        ("evaluate_extraction.py", "Student evaluation"),
        ("judge.py", "Judge evaluation")
    ]

    for script, description in steps:
        print(f"\n{description}...")
        cmd = ["python", f"evaluation/{script}", str(output_dir)]
        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            print(f"Failed: {description}")
            print(result.stderr)
            return None

    # Load overall report
    report_path = Path("evaluation/results") / run_name / "overall_report.json"
    if report_path.exists():
        with open(report_path) as f:
            return json.load(f)

    return None


def generate_batch_report(results: Dict[str, Optional[Dict]]) -> Dict:
    """Generate batch evaluation report with per-difficulty breakdowns."""
    valid_results = {k: v for k, v in results.items() if v is not None}

    batch_report = {
        'total_runs': len(results),
        'successful_runs': len(valid_results),
        'runs': {},
        'aggregate_by_difficulty': {},
        'aggregate_overall': {},
    }

    # Per-run results
    for run_name, report in valid_results.items():
        batch_report['runs'][run_name] = {
            'overall_score': report.get('overall', {}).get('overall_score', 0),
            'info_missing_rate': report.get('info_missing_rate', 0),
            'by_difficulty': {
                diff: metrics.get('overall', {}).get('overall_score', 0)
                for diff, metrics in report.get('by_difficulty', {}).items()
            },
            'by_category': report.get('by_category', {}),
        }

    if not valid_results:
        return batch_report

    # Aggregate per difficulty across all runs
    for diff in DIFFICULTIES:
        diff_scores = []
        diff_accuracy = []
        diff_completeness = []
        diff_relevance = []
        diff_missing = []

        for report in valid_results.values():
            diff_metrics = report.get('by_difficulty', {}).get(diff)
            if not diff_metrics:
                continue
            ov = diff_metrics.get('overall', {})
            diff_scores.append(ov.get('overall_score', 0))
            diff_accuracy.append(ov.get('accuracy', 0))
            diff_completeness.append(ov.get('completeness', 0))
            diff_relevance.append(ov.get('relevance', 0))
            diff_missing.append(diff_metrics.get('info_missing_rate', 0))

        if diff_scores:
            n = len(diff_scores)
            batch_report['aggregate_by_difficulty'][diff] = {
                'avg_overall_score': round(sum(diff_scores) / n, 2),
                'avg_accuracy': round(sum(diff_accuracy) / n, 2),
                'avg_completeness': round(sum(diff_completeness) / n, 2),
                'avg_relevance': round(sum(diff_relevance) / n, 2),
                'avg_info_missing_rate': round(sum(diff_missing) / n, 2),
                'num_runs': n,
            }

    # Aggregate overall across all runs
    all_scores = [r.get('overall', {}).get('overall_score', 0) for r in valid_results.values()]
    all_accuracy = [r.get('overall', {}).get('accuracy', 0) for r in valid_results.values()]
    all_completeness = [r.get('overall', {}).get('completeness', 0) for r in valid_results.values()]
    all_relevance = [r.get('overall', {}).get('relevance', 0) for r in valid_results.values()]
    all_missing = [r.get('info_missing_rate', 0) for r in valid_results.values()]

    n = len(valid_results)
    batch_report['aggregate_overall'] = {
        'avg_overall_score': round(sum(all_scores) / n, 2),
        'avg_accuracy': round(sum(all_accuracy) / n, 2),
        'avg_completeness': round(sum(all_completeness) / n, 2),
        'avg_relevance': round(sum(all_relevance) / n, 2),
        'avg_info_missing_rate': round(sum(all_missing) / n, 2),
    }

    # Category averages across all runs
    all_categories = set()
    for report in valid_results.values():
        all_categories.update(report.get('by_category', {}).keys())

    category_avg = {}
    for cat in all_categories:
        scores = [r.get('by_category', {}).get(cat) for r in valid_results.values()]
        scores = [s for s in scores if s is not None]
        if scores:
            category_avg[cat] = round(sum(scores) / len(scores), 2)

    batch_report['aggregate_overall']['category_averages'] = category_avg

    return batch_report


def save_batch_report(report: Dict) -> str:
    """Save batch evaluation report."""
    output_path = "evaluation/results/batch_report.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(report, f, indent=2)

    print(f"\nBatch report saved to: {output_path}")
    return output_path


def print_batch_summary(report: Dict):
    """Print batch evaluation summary."""
    print(f"\n{'='*60}")
    print("BATCH EVALUATION SUMMARY")
    print(f"{'='*60}")

    print(f"\nTotal runs: {report['total_runs']}")
    print(f"Successful: {report['successful_runs']}")

    agg = report.get('aggregate_overall', {})
    if agg:
        print(f"\nAggregate Metrics:")
        print(f"  Overall Score:     {agg.get('avg_overall_score', 0):.2f}/10")
        print(f"  Accuracy:          {agg.get('avg_accuracy', 0):.2f}/10")
        print(f"  Completeness:      {agg.get('avg_completeness', 0):.2f}/10")
        print(f"  Relevance:         {agg.get('avg_relevance', 0):.2f}/10")
        print(f"  Info Missing:      {agg.get('avg_info_missing_rate', 0):.1f}%")

    by_diff = report.get('aggregate_by_difficulty', {})
    if by_diff:
        print(f"\nBy Difficulty (avg across runs):")
        for diff in DIFFICULTIES:
            if diff in by_diff:
                d = by_diff[diff]
                print(f"  {diff.upper():8} score={d['avg_overall_score']:.2f}  "
                      f"missing={d['avg_info_missing_rate']:.1f}%  "
                      f"({d['num_runs']} runs)")

    cat_avg = agg.get('category_averages', {})
    if cat_avg:
        print(f"\nAverage by Category:")
        for cat, score in cat_avg.items():
            bar_length = int(score)
            bar = '#' * bar_length + '.' * (10 - bar_length)
            print(f"  {cat:25} {bar} {score:.2f}")

    print(f"\nPer-Run Results:")
    for run_name, metrics in report.get('runs', {}).items():
        diff_str = ", ".join(
            f"{d}={s:.1f}" for d, s in metrics.get('by_difficulty', {}).items()
        )
        print(f"  {run_name}: overall={metrics['overall_score']:.2f} [{diff_str}]")

    print(f"\n{'='*60}")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python evaluation/batch_evaluate.py style_agent_output/")
        print("  python evaluation/batch_evaluate.py style_agent_output/federated_veo style_agent_output/ego3d_veo")
        sys.exit(1)

    # Determine output directories to evaluate
    output_dirs = []
    for arg in sys.argv[1:]:
        p = Path(arg.rstrip('/'))
        if not p.exists():
            print(f"Warning: {p} not found, skipping.")
            continue

        # If it has a logs/ subdir, it's a single output dir
        if (p / "logs").exists():
            output_dirs.append(p)
        else:
            # It's a parent dir — find all output subdirs
            found = find_output_dirs(str(p))
            output_dirs.extend(found)

    if not output_dirs:
        print("No valid output directories found.")
        sys.exit(1)

    print(f"Found {len(output_dirs)} output dir(s) to evaluate:")
    for d in output_dirs:
        print(f"  - {d}")

    # Run evaluation for each output dir
    results = {}
    for output_dir in output_dirs:
        run_name = output_dir.name
        try:
            result = run_evaluation_pipeline(output_dir)
            results[run_name] = result
        except Exception as e:
            print(f"Error evaluating {run_name}: {e}")
            results[run_name] = None

    # Generate and save batch report
    print("\nGenerating batch report...")
    batch_report = generate_batch_report(results)
    save_batch_report(batch_report)
    print_batch_summary(batch_report)

    print("\nBatch evaluation complete!")


if __name__ == "__main__":
    main()
