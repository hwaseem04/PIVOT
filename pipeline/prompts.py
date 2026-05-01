system_message = "You are an expert in reading academic papers and creating video summaries based on them. "

high_level_planning_prompt = """Given a paper, please design a video summary. 
The number of scenes should be based on the RECOMMENDATION in the style context below. 

**IMPORTANT**:  You MUST increase or decrease the scene count if the paper contains significantly more (or fewer) major contributions, extensive results, or complex technical analysis that merit individual focus. Ensure every major/interesting contribution and result is covered.

{style_context}

Available Video Assets:
{video_assets_context}

Requirements: 
1. Each scene must include strong relationship between last and next scene, but there must be no overlap of content.
2. STRICTLY No overlapping content between scenes.
3. Collectively present all key findings in a coherent narrative.
4. Maintain high technical accuracy and professionalism.
5. Deliver only core content; omit acknowledgements and references.
6. Do NOT create a title/introduction scene. Scene 0 (title page with paper title, authors, logos) is auto-generated separately. Start your scenes from the paper's technical content.
7. If a video asset from `Available Video Assets` is highly relevant to a scene's content, assign its filename to `asset_video` in the JSON. Otherwise, set it to `null`. Do not invent video filenames.

You MUST output the scenes in the following STRICT JSON format (list of objects):
```json
[
  {{
    "scene_id": 1,
    "title": "Brief title",
    "summary": "content covered in this scene",
    "paper_section": "Introduction/Method/etc",
    "narrative_role": "one of [introduction/experiments/method/results]",
    "asset_video": "clip1.mp4",
    "duration_stat": {{
      "min": 5.0,
      "max": 15.0,
      "avg": 8.0
    }}
  }},
  ...
]
```
Do NOT just acknowledge this request. Generate the actual scene list NOW. Ensure strictly valid JSON.
Map the paper_section to one of the 4 sections in narrative_role (Introduction, Method, Experiments, Results)."""

### ─────────────────────────────────────────────────
### Stage 1: Content Extraction
### ─────────────────────────────────────────────────

content_extraction_prompt = """
You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{scene_json}

{memory_context}

Read the paper carefully and extract ALL relevant content from the section(s) referenced in this scene.

## OUTPUT FORMAT — Return ONLY valid JSON:

{{
  "extracted_content": "A comprehensive summary of the key information from this section. Include main claims, methods, results, or insights. This should contain enough detail for someone to write presentation bullets from it.",
  "key_figures": [
    {{
      "ref": "Figure X",
      "caption": "The actual caption from the paper",
      "relevance": "Why this figure matters for this scene"
    }}
  ],
  "key_tables": [
    {{
      "ref": "Table X",
      "caption": "The actual caption from the paper",
      "relevance": "Why this table matters for this scene"
    }}
  ],
  "key_equations": [
    {{
      "ref": "Equation X or description",
      "content": "The equation in text form",
      "relevance": "Why this equation matters for this scene"
    }}
  ],
  "section_refs": ["Section 3.1", "Section 3.2"]
}}

## STRICT RULES:
1. **Only reference figures/tables that actually appear in the paper section.** Do NOT invent or guess figure/table numbers.
2. **key_figures** must list figures by their exact label in the paper (e.g., "Figure 1", "Fig. 2").
3. If no figures/tables/equations are relevant, use empty lists `[]`.
4. **extracted_content** must be detailed enough to create 2-4 meaningful bullet points from it.
5. **Memory Context**: The `Previous Scenes Memory` (if provided) shows what was ALREADY covered. You MUST NOT repeat its text content, claims, figures, tables, or equations. CRITICAL: Even if you MUST reference the same figure/table, the text content (`extracted_content`) and `relevance` MUST still be completely DIFFERENT.
6. Output ONLY valid JSON, no markdown fences, no explanation.
7. **ASCII quotes ONLY**: Every string in your JSON MUST use standard ASCII double-quote characters ("). NEVER use Unicode typographic or curly quotes (\u201c \u201d \u2018 \u2019). When copying text from the paper that contains curly quotes, replace them with straight ASCII double-quotes.
"""

### ─────────────────────────────────────────────────
### Stage 2: Style Planning (Layout Only)
### ─────────────────────────────────────────────────

import json as _json

# Element type reference table injected into every style planning prompt
_ELEMENT_TYPES_TABLE = """
## LayoutSpec v1 — Element Types

| Type | Description               | content_ref (MUST use exactly) |
|------|---------------------------|--------------------------------|
| T    | Primary title             | elements.title                 |
| ST   | Subtitle                  | elements.subtitle              |
| B    | Bullet list               | elements.bullets               |
| P    | Body paragraph            | elements.body                  |
| EQ   | LaTeX equation            | elements.equations             |
| L    | Sub-figure label          | elements.label_1 etc.          |
| META | Authors / logos row       | elements.meta                  |
| F    | Paper figure / image      | elements.figure (1st), elements.figure_2 (2nd), elements.figure_3 (3rd) |
| D    | Architecture / diagram    | elements.figure (1st), elements.figure_2 (2nd), elements.figure_3 (3rd) |
| CH   | Chart (bar/line/etc.)     | elements.figure (1st), elements.figure_2 (2nd), elements.figure_3 (3rd) |
| TAB  | Table image               | elements.figure (1st), elements.figure_2 (2nd), elements.figure_3 (3rd) |
| QR   | QR code                   | elements.qr_url                |

**CRITICAL**:
- The FIRST F / D / CH / TAB element uses `"content_ref": "elements.figure"`.
- The SECOND uses `"content_ref": "elements.figure_2"`, the THIRD uses `"content_ref": "elements.figure_3"`, and so on.
- Only use multiple figure slots if the content actually has multiple distinct key_figures that each merit their own region.
- Never invent custom keys like `"elements.table_1"` or `"elements.chart_2"`.
- EQ MUST use `"elements.equations"` (plural).

## Layout Signature Encoding
- `|` separates rows (top to bottom)
- `-` separates elements within a row (left to right)
- Examples: `T|F-B`, `F`, `T|TAB-CH`, `T|L-L-L|F-F-F`, `META|T|ST|META|QR`
"""


def style_planning_prompt(content_summary: str, scene_context: str, style_context: dict) -> str:
    """Build the style planning prompt, injecting LayoutSpec v1 examples.

    Args:
        content_summary: JSON string of the extracted content.
        scene_context: JSON string of the high-level scene plan.
        style_context: dict from retrieve_scene_style() with keys:
            layout_specs        — list of LayoutSpec v1 dicts (preferred)
            layout_descriptions — list of fallback verbose strings
            durations           — {min, max, avg} duration stats dict
    """
    # ── Build reference examples section ────────────────────────────────────
    layout_specs = style_context.get("layout_specs", [])
    layout_descriptions = style_context.get("layout_descriptions", [])
    durations = style_context.get("durations", {})

    reference_section = ""
    if layout_specs:
        reference_section += "## Reference Layout Examples (LayoutSpec v1 from similar papers)\n\n"
        for i, spec in enumerate(layout_specs):
            reference_section += f"### Example {i+1}: {spec.get('layout_type', '')} (signature: {spec.get('layout_signature', '')})\n"
            reference_section += "```json\n" + _json.dumps(spec, indent=2) + "\n```\n\n"

    if layout_descriptions:
        reference_section += "## Additional Reference Descriptions (verbose, for inspiration only)\n\n"
        for i, desc in enumerate(layout_descriptions):
            reference_section += f"- Reference {i+1}: {desc}\n"
        reference_section += "\n"

    if durations:
        reference_section += (
            f"## Duration Statistics for This Section\n"
            f"min={durations.get('min', '?')}s, max={durations.get('max', '?')}s, "
            f"avg={durations.get('avg', '?')}s\n\n"
        )

    if not reference_section:
        reference_section = "(No reference layouts available — design from scratch.)\n"

    # ── Build full prompt ────────────────────────────────────────────────────
    return f"""You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{content_summary}

Scene context from high-level plan:
{scene_context}

{reference_section}
{_ELEMENT_TYPES_TABLE}

Your job is to decide the **visual layout** for this slide as a LayoutSpec v1 JSON.
Do NOT decide builds or animations — those will be planned later.

## GRID COORDINATE SYSTEM

A reference grid image is attached. Use it to position elements precisely.

The canvas is divided into a **20×20 grid** (each cell = 5% of the slide):
- **Columns A–U** (left → right): A=0%, B=5%, C=10%, D=15%, E=20%, F=25%, G=30%, H=35%,
  I=40%, J=45%, K=50%, L=55%, M=60%, N=65%, O=70%, P=75%, Q=80%, R=85%, S=90%, T=95%, U=100%
- **Rows 00–20** (top → bottom): 00=0%, 01=5%, 02=10%, 03=15%, 04=20%, 05=25%, 06=30%,
  07=35%, 08=40%, 09=45%, 10=50%, 11=55%, 12=60%, 13=65%, 14=70%, 15=75%, 16=80%,
  17=85%, 18=90%, 19=95%, 20=100%

**Specify each element's box with two grid intersection IDs:**
`"box": {{"tl": "B01", "br": "U03"}}` — top-left corner ID and bottom-right corner ID.

Grid ID = 1 letter (column) + 2 digits (row). Examples:
- `"A00"` = top-left of canvas, `"U20"` = bottom-right
- `"B01"` = (x=0.05, y=0.05) — first safe inner column and row
- `"K10"` = (x=0.50, y=0.50) — center

**Typical layout positions (use as reference):**

| Element | tl | br | Description |
|---------|----|----|-------------|
| Full-width title | B01 | U03 | x=0.05, y=0.05, w=0.95, h=0.10 |
| Subtitle below title | B03 | U04 | x=0.05, y=0.15, h=0.05 |
| Left figure (2-col) | B04 | K18 | x=0.05, y=0.20, w=0.45, h=0.70 |
| Right bullets (2-col) | L04 | T18 | x=0.55, y=0.20, w=0.40, h=0.70 |
| Wide table/chart (above bullets) | B04 | T13 | x=0.05, y=0.20, w=0.90, h=0.45 |
| Bullets below wide table | B13 | T19 | x=0.05, y=0.65, w=0.90, h=0.30 |
| Wide figure (solo, no bullets) | B04 | T19 | x=0.05, y=0.20, w=0.90, h=0.75 |
| Wide equation row | B03 | U06 | x=0.05, y=0.15, w=0.95, h=0.15 |
| Full-body content | B04 | U19 | x=0.05, y=0.20, w=0.95, h=0.75 |

## INSTRUCTIONS

1. Study the reference layout examples above. Take inspiration from their structure and signatures.
2. Choose element types that best match the content (figures → F or D, tables → TAB, bullets → B, etc.).
3. **Position elements using the grid** — choose tl/br IDs from the image so elements do NOT share any grid cells. Keep ≥1 cell (5%) margin from the canvas edge (start at col B / row 01 minimum).
4. **Figure/table sizing — MINIMUM BOX REQUIREMENTS (strictly enforced):**
   - Every figure/table element (type F, D, CH, TAB) MUST span at least **10 grid cells wide AND 10 grid cells tall** (i.e. br_col − tl_col ≥ 10 AND br_row − tl_row ≥ 10). Smaller boxes produce unreadable thumbnails.
   - **Wide tables and charts (TAB, CH)**: minimum width is 12 cells (60% of slide). Place them at the **TOP** of the body (starting at row 04) so the full width is visible. Example: `{{"tl":"B04","br":"T13"}}`.
   - **Figure + bullets layout**: figure gets the LEFT ~11 columns (tl=B04, br=K18); bullets get the RIGHT ~8 columns (tl=L04, br=T18). NEVER give the figure fewer than 8 cells wide.
   - **Figure alone (no bullets)**: figure fills most of the body — use at least `{{"tl":"B04","br":"T19"}}`.
   - **NEVER** place a figure in a small corner box (w < 8 cells OR h < 8 cells is forbidden).
5. Generate a descriptive `layout_signature` using `|` (rows) and `-` (side-by-side) notation.
6. Set `layout_tags` to descriptive keywords (e.g. "two_col", "figure_left", "method", "results").

## OUTPUT FORMAT — Return ONLY valid LayoutSpec v1 JSON:

{{
  "version": 1,
  "layout_type": "two-column layout: figure left, bullets right",
  "layout_tags": ["two_col", "figure_left", "method"],
  "layout_signature": "T|F-B",
  "background_color": "#FFFFFF",
  "elements": [
    {{
      "id": "title",
      "type": "T",
      "content_ref": "elements.title",
      "box": {{"tl": "B01", "br": "U03"}},
      "style": {{"font_size": 40, "bold": true, "align": "left"}}
    }},
    {{
      "id": "figure",
      "type": "F",
      "content_ref": "elements.figure",
      "box": {{"tl": "B04", "br": "K19"}},
      "constraints": {{"keep_aspect": true}}
    }},
    {{
      "id": "bullets",
      "type": "B",
      "content_ref": "elements.bullets",
      "box": {{"tl": "L04", "br": "T19"}},
      "style": {{"font_size": 24, "min_font_size": 16}}
    }}
  ],
  "global_constraints": {{
    "no_overlap": true,
    "no_overflow": true,
    "min_font_size": 14
  }}
}}

## STRICT RULES:
1. **version** must be exactly `1`.
2. **Element ids**: use descriptive ids matching the target names used in builds (e.g. `"title"`, `"figure"`, `"bullets"`, `"video"`).
3. **Coordinates**: use grid IDs `{{"tl": "X##", "br": "X##"}}`. tl_col < br_col AND tl_row < br_row. No two elements may share overlapping grid cells. No element may start before col B or row 01.
4. **has_figure** / **has_video**: do NOT include — these are inferred from element types.
5. **No build info**: do NOT include build_skeleton, expected_build_steps, or animations.
6. **Figure only if content has one**: include an `F`/`D`/`TAB`/`CH` element only if `content_summary` references a relevant figure or table.
7. **Video element**: include a `"video"` element with type `F` only if `scene_context` assigns an `asset_video`.
8. Output ONLY valid JSON. No markdown fences. No explanation.
9. **ASCII quotes ONLY**: Every string in your JSON MUST use standard ASCII double-quote characters ("). NEVER use Unicode typographic or curly quotes (\u201c \u201d \u2018 \u2019). Replace any curly quotes from paper text with straight ASCII double-quotes.
"""

### ─────────────────────────────────────────────────
### Stage 3: Low-Level Planning (Content Drafting)
### ─────────────────────────────────────────────────

low_level_planning_prompt = """
You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{content_summary}

The layout has been decided:
{style_plan}

Scene context:
{scene_context}

{memory_context}

{canvas_constraints}

Your job is to **draft the actual content** (title, bullets, audio, figure choice, equations, and duration) that fits into this layout. You do NOT decide the layout — that is already set. You also do NOT decide builds or animations — those will be planned later based on your drafted content.

## OUTPUT FORMAT — Return ONLY valid JSON:

{{
  "title": "A clear, concise slide title (≤ 8 words)",
  "subtitle": "Optional one-line subtitle — ONLY include if the style plan has an ST element",
  "audio_content": "Full narration transcript for this entire scene. Natural, conversational. Covers all key points.",
  "duration_sec": 8.5,
  "bullets": [
    "Short punchy bullet (≤ 10 words)",
    "Another short bullet"
  ],
  "equations": [
    "Eq. 3: \\mathrm{{GELU}}(x) \\approx 0.125x^2 + 0.5x + 0.25",
    "Eq. 4: h_l = g_l(b_l + h_{{l-1}}) + h_{{l-1}}"
  ],
  "figure": {{
    "type": "paper_figure",
    "ref": "Figure X",
    "caption": "Brief caption describing the figure"
  }},
  "figure_2": {{
    "type": "paper_figure",
    "ref": "Figure Y",
    "caption": "Brief caption for second figure — ONLY include when layout has a 2nd F element"
  }},
  "figure_3": {{
    "type": "paper_figure",
    "ref": "Figure Z",
    "caption": "Brief caption for third figure — ONLY include when layout has a 3rd F element"
  }},
  "video": {{
    "type": "asset_video",
    "path": "clip1.mp4",
    "caption": "Brief caption describing the video contents"
  }},
  "source": ["Figure 1", "Section 3.1"],
  "prompt": "Visual description of the scene for generation"
}}

## STRICT RULES:
1. **Number of bullets**: Follow the Canvas Constraints — NEVER exceed the stated maximum. Default to 2–3 bullets. More bullets = smaller text = harder to read.
2. **Bullet brevity**: Each bullet MUST be ≤ 10 words. No sub-clauses. No semicolons joining two ideas. Split long ideas into separate bullets or drop them entirely.
3. **Subtitle**: Include `subtitle` ONLY if the style plan has an ST (subtitle) element. If no ST element, omit `subtitle` entirely.
4. **Figure/Video assignment**:
   - Assign `figure` for the FIRST key figure — ONLY if the style plan has ≥1 F/D/CH/TAB element.
   - If the style plan has a SECOND F/D/CH/TAB element (content_ref `elements.figure_2`), assign the second key figure to `figure_2`.
   - If the style plan has a THIRD F/D/CH/TAB element (content_ref `elements.figure_3`), assign the third key figure to `figure_3`.
   - Match the number of figures to the number of F/D/CH/TAB elements in the style plan — do NOT add more figures than there are figure regions.
   - Assign `video` ONLY if `scene_context` has an `asset_video`.
   - Omit a figure/video block completely if not applicable.
5. **Equations**: Include `equations` ONLY if the style plan has an EQ element. Write each equation as a **matplotlib-compatible LaTeX math string** — use backslash commands: \\alpha, \\beta, \\gamma, \\sigma, \\mathrm{{GELU}}, \\mathrm{{softmax}}, subscripts _{{...}}, superscripts ^{{...}}, \\approx, \\cdot, \\sum, \\prod, \\frac{{a}}{{b}}, etc. Format each entry as "Eq. N: <latex_string>". Example: "Eq. 6: h_l = g_l(b_l + h_{{l-1}}) + h_{{l-1}}", "Eq. 7: g_l(z) = \\alpha \\cdot W_u \\cdot \\mathrm{{GELU}}(W_d \\cdot z)". Omit if no EQ element.
6. **audio_content**: Natural narration covering ALL bullets and equations. Write this FIRST.
7. **duration_sec**: CALCULATE as `word_count(audio_content) / 2.5`. Do NOT guess.
8. Output ONLY valid JSON, no markdown fences, no explanation.
9. **ASCII quotes ONLY**: Every string in your JSON MUST use standard ASCII double-quote characters ("). NEVER use Unicode typographic or curly quotes (\u201c \u201d \u2018 \u2019). Replace any curly quotes from paper text with straight ASCII double-quotes.
"""

### ─────────────────────────────────────────────────
### Stage 4: Style Refinement (Assign Content → Builds)
### ─────────────────────────────────────────────────

style_refinement_prompt = """
You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{content_draft}

Layout information:
{layout_info}

Your job is to:
1. **Decide the build plan** — how many build steps, and what gets revealed in each step.
2. **Assign the drafted bullets to specific build steps** in the best storytelling order.
3. **Split the audio into per-build segments** so each build has matching narration.

## OUTPUT FORMAT — Return ONLY valid JSON:

{{
  "style": "Slides",
  "expected_build_steps": 3,
  "elements": {{
    "title": "The slide title from the draft",
    "subtitle": "Optional subtitle from draft — omit key entirely if not in draft",
    "figure": {{
      "type": "paper_figure",
      "ref": "Figure X",
      "caption": "Caption from draft"
    }},
    "figure_2": {{
      "type": "paper_figure",
      "ref": "Figure Y",
      "caption": "Caption for second figure — omit key entirely if not in draft"
    }},
    "figure_3": {{
      "type": "paper_figure",
      "ref": "Figure Z",
      "caption": "Caption for third figure — omit key entirely if not in draft"
    }},
    "equations": [
      "Eq. 3: \\mathrm{{GELU}}(x) \\approx 0.125x^2 + 0.5x + 0.25",
      "Eq. 7: g_l(z) = \\alpha \\cdot W_u \\cdot \\mathrm{{GELU}}(W_d \\cdot z)"
    ],
    "bullets": [
      "First bullet",
      "Second bullet"
    ]
  }},
  "builds": [
    {{
      "step_index": 0,
      "time_offset_sec": 0.0,
      "actions": [
        {{"type": "show", "target": "title"}},
        {{"type": "show", "target": "figure"}},
        {{"type": "show", "target": "figure_2"}},
        {{"type": "show", "target": "equation"}}
      ],
      "audio_segment": "Opening narration for this build step.",
      "visual_emphasis": []
    }},
    {{
      "step_index": 1,
      "time_offset_sec": 3.0,
      "actions": [
        {{"type": "fade_in", "target": "bullets[0]"}}
      ],
      "audio_segment": "Narration for the first bullet point.",
      "visual_emphasis": []
    }},
    {{
      "step_index": 2,
      "time_offset_sec": 6.0,
      "actions": [
        {{"type": "fade_in", "target": "bullets[1]"}}
      ],
      "audio_segment": "Narration for the second bullet point.",
      "visual_emphasis": []
    }}
  ]
}}

## STRICT RULES:
1. **Build count**: `expected_build_steps` = 1 + number_of_bullets. Build 0 shows title (and figure/equation/video if present), then one build per bullet.
2. **One bullet per build**: After build 0, each build reveals exactly ONE bullet. `bullets[0]` in build 1, `bullets[1]` in build 2, etc.
3. **Build 0**: Always shows `title` (and `figure`/`video`/`equation` if present). Never shows bullets in build 0.
4. **Audio segments**: Split the `audio_content` from the draft into segments. Each build's `audio_segment` must be non-empty and correspond to what that build reveals.
5. **Bullet ordering**: Assign bullets to builds in the order that creates the best storytelling flow for the audience.
6. **time_offset_sec**: Space evenly across the total time. For N builds over T seconds: offsets at 0, T/N, 2T/N, etc.
7. **visual_emphasis**: Always set to empty list `[]`.
8. **Action targets**: Only use targets that exist in `elements`: `title`, `figure`, `figure_2`, `figure_3`, `video`, `equation`, `bullets[0]`, `bullets[1]`, etc. IMPORTANT: the equation action target is always the string `"equation"` — NEVER `"equations"`, `"equations[0]"`, or any indexed form. The renderer renders all equations in the region at once. For multiple figures use `figure` for the first, `figure_2` for the second, `figure_3` for the third in Build 0 actions.
9. **elements**: Copy the drafted title, subtitle, figure, figure_2, figure_3, video, equations, and bullets exactly — do not modify text. Omit a key entirely if not present in the draft (e.g. no `equations` key if draft has none, no `figure_2` key if draft has none, no `subtitle` key if draft has none).
10. Output ONLY valid JSON, no markdown fences, no explanation.
11. **ASCII quotes ONLY**: Every string in your JSON MUST use standard ASCII double-quote characters ("). NEVER use Unicode typographic or curly quotes (\u201c \u201d \u2018 \u2019). Replace any curly quotes from paper text with straight ASCII double-quotes.
12. **LaTeX equations**: When writing equation strings in JSON, always use double backslashes for LaTeX commands so they survive JSON serialization. For example: `"\\\\frac{{a}}{{b}}"`, `"\\\\approx"`, `"\\\\right)"`, `"\\\\alpha"`. A single backslash in a JSON string (e.g. `"\\frac"`) is a JSON escape sequence — use `"\\\\frac"` to produce a literal backslash that LaTeX needs.
"""

### ─────────────────────────────────────────────────
### Title Page Prompts
### ─────────────────────────────────────────────────

title_extraction_prompt = """You are an expert at reading academic papers.

Look at the FIRST PAGE of this paper and extract the following metadata:

## OUTPUT FORMAT — Return ONLY valid JSON:

{{
  "paper_title": "The full paper title exactly as written",
  "authors": [
    {{"name": "First Author", "affiliation_id": 1}},
    {{"name": "Second Author", "affiliation_id": 2}}
  ],
  "affiliations": [
    {{"id": 1, "name": "University or Organization Name", "email_domain": "example.edu"}},
    {{"id": 2, "name": "Company Name", "email_domain": "company.com"}}
  ],
  "venue": "Conference or Journal Name and Year (e.g. CVPR 2025)"
}}

## STRICT RULES:
1. Extract the paper title EXACTLY as it appears — do not paraphrase.
2. List ALL authors in order. Use their full names as written.
3. Each author must have an affiliation_id matching one entry in the affiliations list.
4. For affiliations, extract the email domain from author emails if available (e.g. user@nvidia.com → nvidia.com).
5. If no email is visible, leave email_domain as an empty string.
6. For venue, look for conference/journal name (e.g. "CVPR 2025", "NeurIPS 2024", "ICLR 2025"). If not found, use empty string.
7. Output ONLY valid JSON, no markdown fences, no explanation.
"""

### ─────────────────────────────────────────────────
### Asset Analyser Prompts
### ─────────────────────────────────────────────────

asset_analyser_image_prompt = """You are an expert at identifying visual branding elements.

I have provided {num_images} images. One of these images is the primary conference or journal logo for a paper (e.g., CVPR, ICCV, Nature). The others are affiliation logos (e.g., University logos, Company logos like Google or Meta).

Identify which image corresponds to which category.

## OUTPUT FORMAT — Return ONLY valid JSON:
{{
  "conference_logo": "image_0",
  "affiliation_logos": ["image_1", "image_2"]
}}

## STRICT RULES:
1. ONLY exactly one image can be the `conference_logo`. The rest go into `affiliation_logos` list.
2. If an image is completely irrelevant or noise, omit it from the JSON.
3. VISUAL CONTENT OVER FILENAMES: Even if a file is named "figure1.png", if it VISUALLY looks like a logo (a logo for a university, a logo for a lab, or a logo for a conference/journal like CVPR), you SHOULD categorize it as a logo.
4. FIGURES ARE NOT LOGOS. If an image looks like a technical diagram, a results plot, or a screenshot from the paper, it is NOT a logo. Skip it.
5. Use the literal exact string "image_0" to refer to the first image, "image_1" for the second, etc.
6. Output ONLY valid JSON, no markdown fences, no explanation.
"""

asset_analyser_video_prompt = """You are an expert at analyzing research paper supplementary videos.

Please watch this video clip named '{filename}'.

What is the visual content of this clip, and what paper section does it most likely belong to?

## OUTPUT FORMAT — Return ONLY valid JSON:
{{
  "description": "A 1-2 sentence description of what the video visually demonstrates (e.g., a software demo tracking a red car, a 3D point cloud visualization, an architecture animation).",
  "relevance": "one of [Introduction, Method, Experiments, Results]"
}}

## STRICT RULES:
1. Keep the description purely factual based on visuals.
2. Select the most appropriate section from the `relevance` choices. If it's a quantitative tracking demo, choose Results. If it's explaining how a component works, choose Method.
3. Output ONLY valid JSON, no markdown fences, no explanation.
"""

title_style_prompt = """You are an expert presentation designer for academic video summaries.

You are designing the TITLE PAGE layout for a paper presentation video.

Paper metadata:
{metadata_json}

Available logos:
{available_logos}

Design a visually clean, professional title page layout. Use the reference style of academic presentation title slides:
- Conference logo in a top corner
- Affiliation logos grouped together (top row or below authors)
- Paper title large and centered
- Authors centered below title
- Affiliation text small, centered
- Venue name at bottom

IMPORTANT: Vary the placement naturally — do NOT always put logos in the same position. Sometimes conference logo goes top-left, sometimes top-right. Sometimes affiliation logos go in the top row, sometimes below authors. Be creative but professional.

## OUTPUT FORMAT — Return ONLY valid JSON:

{{
  "layout_template": "title_page",
  "background_color": "#FFFFFF",
  "layout_regions": {{
    "conference_logo": {{"x": 0.0, "y": 0.0, "w": 0.15, "h": 0.12}},
    "affiliation_logos": {{"x": 0.5, "y": 0.0, "w": 0.45, "h": 0.12}},
    "title": {{"x": 0.05, "y": 0.25, "w": 0.9, "h": 0.25}},
    "authors": {{"x": 0.1, "y": 0.55, "w": 0.8, "h": 0.12}},
    "affiliations": {{"x": 0.1, "y": 0.7, "w": 0.8, "h": 0.08}},
    "venue": {{"x": 0.3, "y": 0.82, "w": 0.4, "h": 0.06}}
  }},
  "style_rationale": "Brief explanation of why this positioning works."
}}

## STRICT RULES:
1. All x/y/w/h values must be normalized (0.0 to 1.0). Regions must not overlap.
2. If no conference logo is available, omit the conference_logo region.
3. If no affiliation logos are available, omit the affiliation_logos region.
4. The title region should be generous — wide enough for long titles to wrap.
5. Keep at least 5% margin from all edges.
6. Output ONLY valid JSON, no markdown fences, no explanation.
"""



### Old prompts

math_prompt = "You are an expert in reading academic papers and creating video summaries based on them. "

high_plan_format_prompt = " The next paragraph of TEXT will provide descriptions for multiple scenes. I need you to fill the \"***\" section of the dict LIST with the TEXT. Please output the LIST only. LIST:[{ \"SCENE1\": \"******\", \"DESCRIPTION\": \"******\", \"TIME_ALLOCATION\": \"******\"},{ \"SCENE2\": \"******\", \"DESCRIPTION\": \"******\", \"TIME_ALLOCATION\": \"******\"}...] TEXT:"

high_level_evaluate_prompt = "Below are the video-summary scenes I designed based on the corresponding paper. Please check it with answering questions: Do these scenes cover all the key points the original paper intends to convey? Do these scenes avoid overlapping content and redundancy? Do these scenes form a coherent and correct story? Please answer “YES/NO.” If you answer “NO” (i.e., issues exist), provide suggestions for improvement. Current plan:"

high_level_replanning_prompt = "The above are the scenes you previously designed. Please modify the scenes accordingly based on the following feedback while keeping the format unchanged:"

low_level_evaluate_prompt = "This is the video summary plan we created for the scene of the part of the paper. Please respond to each of the following questions with either \"YES\" or \"NO\" to determine whether the current plan meets the requirements (if \"NO\", provide the correct answer)."

low_level_replanning_prompt = "The above is the scene style selection plan you designed earlier, but it seems that the following issues have arisen. Please make the corresponding modifications and ensure that the updated version maintains the exact same format as the previous version.:"

low_plan_format_prompt="Fill in the dictionary (***** means blank ) with the given above text. For \"style,\" the blank can only be filled with one of the following options: (Slides, Professional, Talking Heads, Captioning, or General Video). If there is no suitable match, write \"PASS\":{ \"audio_content\": \"******\", \"style\": \"******\", \"source\": \"******\", \" prompt\": \"******\"} Only output this dictionary, no extra content is needed! For example: { \"audio_content\": \"This is the picture from the original paper, which means a lot.\",\"style\": \"Slides\",\"source\": \"Fig.1\",\"prompt\": \"Previous palaeomagnetic investigations using samples from Apollo and Chang'e-5 missions have revealed the Moon's magnetic history. However, these studies were limited to the nearside, leaving the farside largely unexplored.\". \n Make sure that the content replacing \"******\" are strings and does not contain double quotes inside.}"

low_level_evaluate_prompt_list = ["\n Is the video style exactly one of those choices: [Slides, Professional, Talking Heads, Captioning, or General Video] ? \n Do you think the choice of this style is reasonable?", "\n Does the \" audio_ content\" part appear to meet the required time_cost? Avoid overly lengthy text. The time_cost is fixed and cannot be changed. \n Do you think the audio_content is reasonable?","  Only If the video \" style \" is \" slides \", answer: Does the \" source \" part explicitly provide a specific source element (exact table/picture/equation)in the original paper? \n Is the professionalism of the current plan acceptable? \n Only if the video \"style \"  is \" professional \", does the original plan provide a clear mathematical expression or molecular formula so that I can know the content without reading original paper? \n","The \"prompt\" part should be a description of the scenes for the video to be generated. Does the existing \"prompt\" work as a prompt for a generation model (if the style is a General video, Captioning) or as a note to show (if the style is Slides or Professional)?\n"] 

load_table_prompt="Can you return the content of the specific table of the original paper in table fomular? No extra TEXT in output."

pro_classify_prompt = "Is this scene related to mathematical content? If yes, output \"math\". Is this scene related to molecular visualization content? If yes, output \"mol\""

pro_format_prompt = "The code I require does not need to be complete; it only needs to exist as an animation function. Please check if the following code meets my requirements: It should not contain any import statements. It should be simple and within 100 lines! It should start with 'def animate(self):\n    '. It should end with 'self.wait(X)' (where X is a number). Conforms to indentation rules! If it does not meet the requirements, rewrite it in the format I requested. Output the code Only!"

pro_gen_prompt = "Why can't the following code run? Please modify the code and make it generate the correct video. Your result must be understandable by the Python compiler! Conforms to indentation rules. Make it SIMPLE and meaningful! Make sure the code Only output the code!"

pro_vis_eval = "This is the video we created to introduce the above content, and I would like you to answer the following questions with (\"YES\" or \"NO\") to determine if the current video meets the requirements while maintaining structural integrity. If the answer is \"NO,\" please provide a reason:Is there visual content (animation) in the bottom left corner of the video? Is the animation in the video reasonable and mathematically strong? Do the visual content and text avoid meanlingless overlap in the video?"

pro_vis_rege = "The code you write has the following issues, please output the updated code ONLY:"

gen_vis_eval = "This is the video we created to introduce the above content, and I would like you to answer the following questions with (\"YES\" or \"NO\") to determine if the current video meets the requirements while maintaining structural integrity. If the answer is \"NO,\" please provide a reason:  Does it convey serious subject matter? Is the image filled with vivid scenes rather than meaningless numbers, letters, and symbols? Is the image strongly relevant to the following description?"

slides_vis_eval = "This is the video we created to introduce the above content, and I would like you to answer the following questions with (\"YES\" or \"NO\") . Is the following text works well as a caption beneath an image in a PowerPoint slide?  Is the following text explaining the image? Following text:"
