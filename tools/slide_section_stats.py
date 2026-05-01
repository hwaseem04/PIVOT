"""
Statistics on slide_section values across all metadata.json files
under data_reference/style_db_refined_final/<paper_name>/metadata.json
"""
import json
import glob
from collections import Counter

meta_files = sorted(glob.glob("data_reference/style_db_refined_final/*/metadata.json"))
print(f"Total metadata.json files found: {len(meta_files)}\n")

global_section_counter = Counter()   # total slides per section (across all papers)
per_paper_section_counter = Counter() # how many papers have at least one slide of each section
total_slides = 0
total_duration = 0.0
per_paper_stats = []

for f in meta_files:
    with open(f) as fh:
        data = json.load(fh)

    paper = data.get("video_id", f)
    slides = data.get("slides", [])
    duration = data.get("duration", 0.0)
    total_slides += len(slides)
    total_duration += duration

    paper_sections = Counter()
    for slide in slides:
        sec = slide.get("slide_section", "unknown")
        paper_sections[sec] += 1
        global_section_counter[sec] += 1

    # Track which sections appear in this paper
    for sec in paper_sections:
        per_paper_section_counter[sec] += 1

    per_paper_stats.append({
        "paper": paper,
        "total_slides": len(slides),
        "sections": dict(paper_sections),
    })

# --- Print results ---
print("=" * 60)
print("Global slide_section distribution (across all papers)")
print("=" * 60)
print(f"  Total slides: {total_slides}")
print(f"  Total papers: {len(meta_files)}")
print(f"  Total duration: {total_duration:.1f}s ({total_duration/60:.1f}min)\n")

for section, count in global_section_counter.most_common():
    pct = count / total_slides * 100
    print(f"  {section:25s}: {count:4d} slides  ({pct:5.1f}%)")

print(f"\n{'=' * 60}")
print("Per-paper presence (how many papers have >= 1 slide of each section)")
print("=" * 60)
for section, count in per_paper_section_counter.most_common():
    pct = count / len(meta_files) * 100
    print(f"  {section:25s}: {count:4d} / {len(meta_files)} papers  ({pct:5.1f}%)")

# Average slides per section per paper
print(f"\n{'=' * 60}")
print("Average slides per section (per paper, when section is present)")
print("=" * 60)
for section, _ in global_section_counter.most_common():
    papers_with = per_paper_section_counter[section]
    avg = global_section_counter[section] / papers_with if papers_with > 0 else 0
    print(f"  {section:25s}: {avg:.1f} slides/paper")

# Show per-paper breakdown
print(f"\n{'=' * 60}")
print("Per-paper breakdown")
print("=" * 60)
for ps in per_paper_stats:
    print(f"\n  {ps['paper']} ({ps['total_slides']} slides)")
    for sec, cnt in sorted(ps["sections"].items(), key=lambda x: -x[1]):
        print(f"    {sec:23s}: {cnt}")
