"""
Evaluation metrics and utilities.
"""

from typing import Dict, List


def calculate_answer_rate(results: List[Dict]) -> float:
    """Calculate percentage of questions that were answered."""
    answered = sum(1 for r in results if r.get('answered', True))
    return (answered / len(results)) * 100 if results else 0.0


def calculate_category_scores(results: List[Dict]) -> Dict[str, float]:
    """Calculate average scores by category."""
    categories = {}

    for r in results:
        cat = r['category']
        if cat not in categories:
            categories[cat] = []

        if 'judgment' in r:
            categories[cat].append(r['judgment']['overall_score'])

    return {
        cat: sum(scores) / len(scores) if scores else 0.0
        for cat, scores in categories.items()
    }


def calculate_difficulty_scores(results: List[Dict]) -> Dict[str, float]:
    """Calculate average scores by difficulty."""
    difficulties = {}

    for r in results:
        diff = r.get('difficulty', 'unknown')
        if diff not in difficulties:
            difficulties[diff] = []

        if 'judgment' in r:
            difficulties[diff].append(r['judgment']['overall_score'])

    return {
        diff: sum(scores) / len(scores) if scores else 0.0
        for diff, scores in difficulties.items()
    }


def identify_weak_categories(results: List[Dict], threshold: float = 5.0) -> List[str]:
    """Identify categories with average scores below threshold."""
    category_scores = calculate_category_scores(results)
    return [cat for cat, score in category_scores.items() if score < threshold]


def calculate_information_gaps(results: List[Dict]) -> Dict[str, int]:
    """Identify which categories have the most information gaps."""
    gaps = {}

    for r in results:
        cat = r['category']
        if cat not in gaps:
            gaps[cat] = 0

        if r.get('judgment', {}).get('info_missing', False):
            gaps[cat] += 1

    return gaps


def generate_summary_stats(results: List[Dict]) -> Dict:
    """Generate comprehensive summary statistics."""
    total = len(results)

    # Overall metrics
    judgments = [r['judgment'] for r in results if 'judgment' in r]

    stats = {
        'total_questions': total,
        'avg_accuracy': sum(j['accuracy'] for j in judgments) / len(judgments) if judgments else 0,
        'avg_completeness': sum(j['completeness'] for j in judgments) / len(judgments) if judgments else 0,
        'avg_relevance': sum(j['relevance'] for j in judgments) / len(judgments) if judgments else 0,
        'avg_overall': sum(j['overall_score'] for j in judgments) / len(judgments) if judgments else 0,
        'answer_rate': calculate_answer_rate(results),
        'category_scores': calculate_category_scores(results),
        'difficulty_scores': calculate_difficulty_scores(results),
        'weak_categories': identify_weak_categories(results),
        'information_gaps': calculate_information_gaps(results)
    }

    return stats
