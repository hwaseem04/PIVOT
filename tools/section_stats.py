"""
Statistics on which sections are present in each paper JSON
under data_reference/categorised_section_summary_extraction_gemini/
"""
import json
import glob
from collections import Counter

TARGET_SECTIONS = {"introduction", "related work", "method", "experiments", "results"}

json_dir = "data_reference/categorised_section_summary_extraction_gemini"
files = sorted(glob.glob(f"{json_dir}/*.json"))

print(f"Total JSON files found: {len(files)}\n")

section_counter = Counter()  # how many papers have each section
extra_sections = Counter()   # sections outside the 5 target ones
missing_report = []          # papers missing one or more target sections

for f in files:
    with open(f) as fh:
        data = json.load(fh)

    paper = data.get("paper_name", f)
    sections = data.get("sections", {})
    section_keys = set(sections.keys())

    for s in section_keys:
        section_counter[s] += 1

    # Check which target sections are missing
    missing = TARGET_SECTIONS - section_keys
    if missing:
        missing_report.append((paper, missing))

    # Check for extra sections beyond the 5 targets
    extras = section_keys - TARGET_SECTIONS
    for e in extras:
        extra_sections[e] += 1

# --- Print results ---
print("=" * 60)
print("Section presence across all papers")
print("=" * 60)
for section, count in section_counter.most_common():
    pct = count / len(files) * 100
    marker = " <-- TARGET" if section in TARGET_SECTIONS else ""
    print(f"  {section:25s}: {count:4d} / {len(files)}  ({pct:5.1f}%){marker}")

print(f"\n{'=' * 60}")
print("Target section coverage")
print("=" * 60)
for s in sorted(TARGET_SECTIONS):
    count = section_counter.get(s, 0)
    pct = count / len(files) * 100
    print(f"  {s:25s}: {count:4d} / {len(files)}  ({pct:5.1f}%)")

print(f"\n{'=' * 60}")
print(f"Papers missing target sections: {len(missing_report)} / {len(files)}")
print("=" * 60)
for paper, missing in missing_report:
    print(f"  {paper}")
    print(f"    Missing: {', '.join(sorted(missing))}")

print(f"\n{'=' * 60}")
print("Extra (non-target) sections")
print("=" * 60)
for section, count in extra_sections.most_common():
    print(f"  {section:25s}: {count:4d}")
