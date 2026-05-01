"""
style_db_migrate.py — One-off migration: convert style DB metadata to LayoutSpec v1.

For each slide in the style DB, this script uses an LLM to read the existing
`layout_type` + `layout_description` fields and produce a structured LayoutSpec v1 JSON.

Results are written to `metadata_v2.json` alongside each original `metadata.json`.
Original files are never modified (non-destructive).

Usage:
    python tools/style_db_migrate.py
    python tools/style_db_migrate.py --dry_run         # parse but don't write
    python tools/style_db_migrate.py --force_redo      # re-convert already-converted slides
    python tools/style_db_migrate.py --db_path data_reference/style_db_refined_final/db_summary.json
"""

import json
import argparse
import sys
import time
import logging
from pathlib import Path

# ── Bootstrap path so we can import project modules ──────────────────────────
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from utils.textwork import _load_json_dict

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger("style_db_migrate")

# ── LayoutSpec schema injected into every conversion prompt ──────────────────
LAYOUT_SPEC_SCHEMA = """
## LayoutSpec v1 Schema

```json
{
  "version": 1,
  "layout_type": "<string — short human-readable label, same as input layout_type>",
  "layout_tags": ["<list of keyword tags, e.g. 'two_col', 'figure_left', 'method', 'results'>"],
  "layout_signature": "<string encoding element composition, e.g. 'T|F-B' or 'META|T|ST|META|QR'>",
  "background_color": "#FFFFFF",
  "elements": [
    {
      "id": "<unique string id, e.g. 'title', 'figure', 'bullets', 'subtitle', 'label_1'>",
      "type": "<one of: T ST B P EQ L META F D CH TAB QR>",
      "content_ref": "<dot-path into the content payload, e.g. 'elements.title'>",
      "box": {"x": 0.05, "y": 0.05, "w": 0.90, "h": 0.10},
      "style": {"font_size": 40, "bold": true, "align": "left"},
      "constraints": {"keep_aspect": true}
    }
  ],
  "global_constraints": {
    "no_overlap": true,
    "no_overflow": true,
    "min_font_size": 14
  }
}
```

## Element Type Reference

| Type | Description               | content_ref examples         |
|------|---------------------------|------------------------------|
| T    | Primary title             | elements.title               |
| ST   | Subtitle                  | elements.subtitle            |
| B    | Bullet list               | elements.bullets             |
| P    | Body paragraph            | elements.body                |
| EQ   | LaTeX equation            | elements.equation            |
| L    | Sub-figure label          | elements.label_1             |
| META | Authors/logos/affiliations| elements.meta                |
| F    | Paper figure/image        | elements.figure              |
| D    | Architecture/flow diagram | elements.figure              |
| CH   | Chart (bar/line/etc.)     | elements.figure              |
| TAB  | Table                     | elements.figure              |
| QR   | QR code                   | elements.qr_url              |

## Layout Signature Encoding
- `|` = vertical stack (rows top to bottom)
- `-` = horizontal group (elements side by side in one row)
- Examples:
  - `T|F-B`         = title row, then figure + bullets side by side
  - `F`             = single full-screen figure
  - `T|TAB-CH`      = title, then table + chart side by side
  - `META|T|ST`     = logo row, then title, then subtitle
  - `T|L-L-L|F-F-F` = title, row of labels, row of three figures

## Box Coordinates
- All values normalized [0.0, 1.0] where (0,0) is top-left
- x, y = top-left corner of element
- w, h = width and height
- Typical title box: {"x": 0.05, "y": 0.03, "w": 0.90, "h": 0.10}
- Keep at least 0.03 margin from all canvas edges
- Boxes must NOT overlap; total area should fill the slide reasonably
"""

CONVERSION_PROMPT_TEMPLATE = """
You are a slide layout expert. Convert the following slide layout description to a LayoutSpec v1 JSON.

## Input

layout_type: {layout_type}

layout_description:
{layout_description}

## Task

Produce a LayoutSpec v1 JSON that accurately captures the spatial arrangement described above.

Guidelines:
- Infer element types from the description (text → T or B or P, figures/diagrams/visuals → F or D or CH, tables → TAB, logos → META, equations → EQ, labels → L)
- Estimate normalized box coordinates (0.0–1.0) based on the description's spatial cues (e.g. "top-left", "centered", "right half", "full-screen", "three columns")
- Assign `content_ref` values using the standard dot-paths in the schema
- Set `layout_tags` to keywords that describe structure (e.g. 'two_col', 'full_fig', 'results', 'method', 'title_slide', 'comparison')
- Set `layout_signature` using the `|` and `-` encoding rules
- Include `style` for text elements with a reasonable `font_size` and `bold` flag

{schema}

## Output

Return ONLY a valid JSON object matching LayoutSpec v1 schema above. No markdown fences, no explanation.
"""


def _call_llm_text_only(prompt: str, llm_client) -> str:
    """Call the LLM with a text-only prompt. Returns the response string.

    BaseLLM.__call__ returns rsp_text (str) directly — not a tuple.
    """
    return llm_client(prompt=prompt)


def _convert_slide(slide: dict, llm_client) -> dict:
    """Convert a single slide's layout_structure to a LayoutSpec v1 dict.

    Returns a LayoutSpec v1 dict, or a placeholder if conversion fails.
    """
    layout_structure = slide.get("layout_structure", {})
    layout_type = layout_structure.get("layout_type", "")
    layout_description = layout_structure.get("layout_description", "")

    placeholder = {
        "version": 1,
        "layout_type": layout_type or "unknown",
        "layout_tags": [],
        "layout_signature": "",
        "background_color": "#FFFFFF",
        "elements": [],
        "global_constraints": {"no_overlap": True, "no_overflow": True, "min_font_size": 14},
    }

    if not layout_description and not layout_type:
        logger.warning("  Slide has no layout info. Using placeholder.")
        return placeholder

    prompt = CONVERSION_PROMPT_TEMPLATE.format(
        layout_type=layout_type or "(unknown)",
        layout_description=layout_description or "(no description available)",
        schema=LAYOUT_SPEC_SCHEMA,
    )

    max_retries = 3
    for attempt in range(max_retries):
        try:
            raw = _call_llm_text_only(prompt, llm_client)
            logger.debug(f"  Attempt {attempt+1} raw response (first 300 chars): {str(raw)[:300]}")
            # Strip Python triple-quote wrappers the LLM sometimes adds
            raw = raw.strip().strip('"""').strip("'''").strip()
            parsed = _load_json_dict(raw)
            if parsed and isinstance(parsed, dict):
                # Normalise version: accept int 1 or string "1"
                if str(parsed.get("version", "")) == "1":
                    parsed["version"] = 1  # ensure it's always int
                    # Basic validation: must have elements list
                    if "elements" in parsed and isinstance(parsed["elements"], list):
                        return parsed
                    else:
                        logger.warning(f"  Attempt {attempt+1}: parsed JSON missing 'elements'. Retrying.")
                        logger.warning(f"  Keys found: {list(parsed.keys())}")
                else:
                    logger.warning(
                        f"  Attempt {attempt+1}: version field is "
                        f"'{parsed.get('version')}' (expected 1). Keys: {list(parsed.keys())}. Retrying."
                    )
            else:
                logger.warning(
                    f"  Attempt {attempt+1}: could not parse JSON. "
                    f"Raw (first 200): {str(raw)[:200]}. Retrying."
                )
        except Exception as e:
            logger.warning(f"  Attempt {attempt+1}: LLM call failed: {e}. Retrying.")
        time.sleep(1.5)

    logger.error(f"  Conversion failed after {max_retries} attempts. Using placeholder.")
    return placeholder


def migrate_metadata(
    meta_path: Path,
    llm_client,
    dry_run: bool = False,
    force_redo: bool = False,
) -> dict:
    """Migrate a single metadata.json file → metadata_v2.json.

    Returns a summary dict with counts.
    """
    v2_path = meta_path.parent / "metadata_v2.json"

    with open(meta_path, "r", encoding="utf-8") as f:
        meta = json.load(f)

    # Load existing v2 if present
    if v2_path.exists() and not force_redo:
        with open(v2_path, "r", encoding="utf-8") as f:
            meta_v2 = json.load(f)
    else:
        meta_v2 = json.loads(json.dumps(meta))  # deep copy

    slides = meta_v2.get("slides", [])
    converted = 0
    skipped = 0
    failed = 0

    for i, slide in enumerate(slides):
        layout_structure = slide.get("layout_structure", {})
        already_done = "layout_spec" in layout_structure and isinstance(
            layout_structure["layout_spec"], dict
        ) and layout_structure["layout_spec"].get("version") == 1

        if already_done and not force_redo:
            skipped += 1
            continue

        slide_id = slide.get("slide_id", i)
        section = slide.get("slide_section", "?")
        layout_type = layout_structure.get("layout_type", "(none)")
        logger.info(f"  Converting slide {slide_id} [{section}] '{layout_type}'...")

        if not dry_run:
            spec = _convert_slide(slide, llm_client)
            slide["layout_structure"]["layout_spec"] = spec
            converted += 1
        else:
            logger.info("  [DRY RUN] Would convert this slide.")
            converted += 1

    if not dry_run:
        with open(v2_path, "w", encoding="utf-8") as f:
            json.dump(meta_v2, f, indent=2, ensure_ascii=False)
        logger.info(f"  Saved → {v2_path}")

    return {"converted": converted, "skipped": skipped, "failed": failed}


def main():
    parser = argparse.ArgumentParser(description="Migrate style DB metadata to LayoutSpec v1.")
    parser.add_argument(
        "--db_path",
        default="data_reference/style_db_refined_final/db_summary.json",
        help="Path to db_summary.json",
    )
    parser.add_argument("--dry_run", action="store_true", help="Parse but do not write files.")
    parser.add_argument(
        "--force_redo",
        action="store_true",
        help="Re-convert slides that already have layout_spec.",
    )
    parser.add_argument(
        "--config",
        default="config.yml",
        help="Path to LLM config YAML (default: config.yml)",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable DEBUG logging to see raw LLM responses.",
    )
    args = parser.parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    db_path = Path(args.db_path)
    if not db_path.exists():
        logger.error(f"db_summary.json not found at {db_path}")
        sys.exit(1)

    # Initialise LLM client using project GEMINI wrapper (text-only mode)
    try:
        from llms import GEMINI
        llm_client = GEMINI(config_path=Path(args.config))
        logger.info("Initialized GEMINI LLM client.")
    except Exception as e:
        logger.error(f"Failed to initialize LLM client: {e}")
        sys.exit(1)

    with open(db_path, "r") as f:
        db_summary = json.load(f)

    total_converted = 0
    total_skipped = 0
    total_failed = 0

    for item in db_summary:
        paper_title = item.get("video_id", "?")
        meta_path = Path(item.get("path", ""))

        if not meta_path.exists():
            logger.warning(f"[{paper_title}] metadata.json not found at {meta_path}. Skipping.")
            continue

        logger.info(f"\n[{paper_title}] Migrating {meta_path} ...")
        summary = migrate_metadata(meta_path, llm_client, dry_run=args.dry_run, force_redo=args.force_redo)
        total_converted += summary["converted"]
        total_skipped += summary["skipped"]
        total_failed += summary["failed"]

    logger.info(
        f"\nMigration complete. "
        f"Converted: {total_converted}, Skipped (already done): {total_skipped}, Failed: {total_failed}"
    )


if __name__ == "__main__":
    main()
