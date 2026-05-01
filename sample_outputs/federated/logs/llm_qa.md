_Note: These user-assistant interactions are independent and the system message is always attached in each turn for GPT._

**System message for GPT**

You are an expert in reading academic papers and creating video summaries based on them. 

_Note: These user-assistant interactions are independent and the system message is always attached in each turn for GPT._

**System message for GPT**

You are an expert in reading academic papers and creating video summaries based on them. 

_Note: These user-assistant interactions are independent and the system message is always attached in each turn for GPT._

**System message for GPT**

You are an expert in reading academic papers and creating video summaries based on them. 

**Question**

Given a paper, please design a video summary. 
The number of scenes should be based on the RECOMMENDATION in the style context below. 

**IMPORTANT**:  You MUST increase or decrease the scene count if the paper contains significantly more (or fewer) major contributions, extensive results, or complex technical analysis that merit individual focus. Ensure every major/interesting contribution and result is covered.



Available Video Assets:


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
  {
    "scene_id": 1,
    "title": "Brief title",
    "summary": "content covered in this scene",
    "paper_section": "Introduction/Method/etc",
    "narrative_role": "one of [introduction/experiments/method/results]",
    "asset_video": "clip1.mp4",
    "duration_stat": {
      "min": 5.0,
      "max": 15.0,
      "avg": 8.0
    }
  },
  ...
]
```
Do NOT just acknowledge this request. Generate the actual scene list NOW. Ensure strictly valid JSON.
Map the paper_section to one of the 4 sections in narrative_role (Introduction, Method, Experiments, Results).

**Answer (from GEMINI)**

"""```json
[
  {
    "scene_id": 1,
    "title": "Challenges in Foundation Model Adaptation",
    "summary": "Adapting Foundation Models (FMs) for downstream tasks faces two major hurdles: data owners cannot share sensitive data due to privacy regulations, and service providers cannot share proprietary FMs due to intellectual property restrictions.",
    "paper_section": "Introduction",
    "narrative_role": "introduction",
    "asset_video": null,
    "duration_stat": {
      "min": 8.0,
      "max": 12.0,
      "avg": 10.0
    }
  },
  {
    "scene_id": 2,
    "title": "The BlindFed Framework",
    "summary": "BlindFed is a novel framework for double-blind federated adaptation. It allows collaborative training where data owners never access the FM, and the Learning Service Provider never sees the sensitive task data, utilizing Fully Homomorphic Encryption (FHE).",
    "paper_section": "Proposed BlindFed Framework",
    "narrative_role": "method",
    "asset_video": null,
    "duration_stat": {
      "min": 10.0,
      "max": 15.0,
      "avg": 12.0
    }
  },
  {
    "scene_id": 3,
    "title": "FHE-friendly Architecture Redesign",
    "summary": "To support encrypted inference, BlindFed replaces non-linear FM operations like Softmax, GELU, and LayerNorm with low-degree polynomial approximations and integrates lightweight parallel adapters for efficient client-side training.",
    "paper_section": "FHE-friendly Architecture Redesign",
    "narrative_role": "method",
    "asset_video": null,
    "duration_stat": {
      "min": 12.0,
      "max": 18.0,
      "avg": 15.0
    }
  },
  {
    "scene_id": 4,
    "title": "Two-stage Split Learning Approach",
    "summary": "The framework employs a two-stage process: first, offline knowledge distillation on auxiliary data to pre-train FHE-friendly blocks; second, online encrypted inference where clients train local adapters without backpropagating through the main FM.",
    "paper_section": "Two-stage Split Learning",
    "narrative_role": "method",
    "asset_video": null,
    "duration_stat": {
      "min": 12.0,
      "max": 18.0,
      "avg": 15.0
    }
  },
  {
    "scene_id": 5,
    "title": "Privacy-Boosting Mechanisms",
    "summary": "To mitigate model extraction attacks, BlindFed introduces sample-level permutations and stochastic block sampling (SBS). These ensure that clients only see a subset of permuted intermediate representations, preventing them from reconstructing the FM parameters.",
    "paper_section": "Model Privacy Boosting",
    "narrative_role": "method",
    "asset_video": null,
    "duration_stat": {
      "min": 10.0,
      "max": 15.0,
      "avg": 13.0
    }
  },
  {
    "scene_id": 6,
    "title": "Experimental Results and Accuracy",
    "summary": "Evaluated on CIFAR and SVHN datasets, BlindFed achieves accuracy levels comparable to LoRA and significantly outperforms linear probing, demonstrating that double-blind privacy can be maintained without sacrificing model performance.",
    "paper_section": "Results",
    "narrative_role": "results",
    "asset_video": null,
    "duration_stat": {
      "min": 10.0,
      "max": 15.0,
      "avg": 12.0
    }
  },
  {
    "scene_id": 7,
    "title": "Efficiency and Scalability Analysis",
    "summary": "While BlindFed incurs high communication costs and server-side computational complexity due to FHE, it maintains a low memory footprint for clients and demonstrates robust scalability across varying numbers of participants in federated settings.",
    "paper_section": "Results",
    "narrative_role": "results",
    "asset_video": null,
    "duration_stat": {
      "min": 8.0,
      "max": 14.0,
      "avg": 11.0
    }
  }
]
```"""

Token usage so far: 10336 prompt tokens, 1067 completion tokens

Cost so far: $0.13537

**Question**

You are an expert at reading academic papers.

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


**Answer (from GEMINI)**

"""{
  "paper_title": "A Framework for Double-Blind Federated Adaptation of Foundation Models",
  "authors": [
    {
      "name": "Nurbek Tastan",
      "affiliation_id": 1
    },
    {
      "name": "Karthik Nandakumar",
      "affiliation_id": 2
    }
  ],
  "affiliations": [
    {
      "id": 1,
      "name": "Mohamed bin Zayed University of Artificial Intelligence (MBZUAI), UAE",
      "email_domain": "mbzuai.ac.ae"
    },
    {
      "id": 2,
      "name": "Michigan State University (MSU), USA",
      "email_domain": "msu.edu"
    }
  ],
  "venue": ""
}"""

Token usage so far: 20579 prompt tokens, 1262 completion tokens

Cost so far: $0.24365

**Question**

You are an expert presentation designer for academic video summaries.

You are designing the TITLE PAGE layout for a paper presentation video.

Paper metadata:
{
  "paper_title": "A Framework for Double-Blind Federated Adaptation of Foundation Models",
  "authors": [
    {
      "name": "Nurbek Tastan",
      "affiliation_id": 1
    },
    {
      "name": "Karthik Nandakumar",
      "affiliation_id": 2
    }
  ],
  "affiliations": [
    {
      "id": 1,
      "name": "Mohamed bin Zayed University of Artificial Intelligence (MBZUAI), UAE",
      "email_domain": "mbzuai.ac.ae"
    },
    {
      "id": 2,
      "name": "Michigan State University (MSU), USA",
      "email_domain": "msu.edu"
    }
  ],
  "venue": ""
}

Available logos:
No logos available.

Design a visually clean, professional title page layout. Use the reference style of academic presentation title slides:
- Conference logo in a top corner
- Affiliation logos grouped together (top row or below authors)
- Paper title large and centered
- Authors centered below title
- Affiliation text small, centered
- Venue name at bottom

IMPORTANT: Vary the placement naturally — do NOT always put logos in the same position. Sometimes conference logo goes top-left, sometimes top-right. Sometimes affiliation logos go in the top row, sometimes below authors. Be creative but professional.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "layout_template": "title_page",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "conference_logo": {"x": 0.0, "y": 0.0, "w": 0.15, "h": 0.12},
    "affiliation_logos": {"x": 0.5, "y": 0.0, "w": 0.45, "h": 0.12},
    "title": {"x": 0.05, "y": 0.25, "w": 0.9, "h": 0.25},
    "authors": {"x": 0.1, "y": 0.55, "w": 0.8, "h": 0.12},
    "affiliations": {"x": 0.1, "y": 0.7, "w": 0.8, "h": 0.08},
    "venue": {"x": 0.3, "y": 0.82, "w": 0.4, "h": 0.06}
  },
  "style_rationale": "Brief explanation of why this positioning works."
}

## STRICT RULES:
1. All x/y/w/h values must be normalized (0.0 to 1.0). Regions must not overlap.
2. If no conference logo is available, omit the conference_logo region.
3. If no affiliation logos are available, omit the affiliation_logos region.
4. The title region should be generous — wide enough for long titles to wrap.
5. Keep at least 5% margin from all edges.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "layout_template": "title_page",
  "background_color": "#F8F9FA",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.2,
      "w": 0.9,
      "h": 0.3
    },
    "authors": {
      "x": 0.1,
      "y": 0.55,
      "w": 0.8,
      "h": 0.1
    },
    "affiliations": {
      "x": 0.1,
      "y": 0.68,
      "w": 0.8,
      "h": 0.15
    }
  },
  "style_rationale": "Since no logos or venue information were provided, this layout focuses on a clean, centered typographic hierarchy. The title is given ample space to wrap naturally, while the authors and affiliations are positioned in the lower half to create a balanced, professional academic aesthetic."
}"""

Token usage so far: 31233 prompt tokens, 1510 completion tokens

Cost so far: $0.35763

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 1,
  "title": "Challenges in Foundation Model Adaptation",
  "summary": "Adapting Foundation Models (FMs) for downstream tasks faces two major hurdles: data owners cannot share sensitive data due to privacy regulations, and service providers cannot share proprietary FMs due to intellectual property restrictions.",
  "paper_section": "Introduction",
  "narrative_role": "introduction",
  "asset_video": null,
  "duration_stat": {
    "min": 8.0,
    "max": 12.0,
    "avg": 10.0
  }
}



Read the paper carefully and extract ALL relevant content from the section(s) referenced in this scene.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "extracted_content": "A comprehensive summary of the key information from this section. Include main claims, methods, results, or insights. This should contain enough detail for someone to write presentation bullets from it.",
  "key_figures": [
    {
      "ref": "Figure X",
      "caption": "The actual caption from the paper",
      "relevance": "Why this figure matters for this scene"
    }
  ],
  "key_tables": [
    {
      "ref": "Table X",
      "caption": "The actual caption from the paper",
      "relevance": "Why this table matters for this scene"
    }
  ],
  "key_equations": [
    {
      "ref": "Equation X or description",
      "content": "The equation in text form",
      "relevance": "Why this equation matters for this scene"
    }
  ],
  "section_refs": ["Section 3.1", "Section 3.2"]
}

## STRICT RULES:
1. **Only reference figures/tables that actually appear in the paper section.** Do NOT invent or guess figure/table numbers.
2. **key_figures** must list figures by their exact label in the paper (e.g., "Figure 1", "Fig. 2").
3. If no figures/tables/equations are relevant, use empty lists `[]`.
4. **extracted_content** must be detailed enough to create 2-4 meaningful bullet points from it.
5. **Memory Context**: The `Previous Scenes Memory` (if provided) shows what was ALREADY covered. You MUST NOT repeat its text content, claims, figures, tables, or equations. CRITICAL: Even if you MUST reference the same figure/table, the text content (`extracted_content`) and `relevance` MUST still be completely DIFFERENT.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "extracted_content": "Foundation models (FMs) like GPT, CLIP, and ViT demonstrate exceptional zero-shot performance but often require task-specific adaptation for challenging out-of-domain tasks such as medical or satellite imagery. This adaptation process faces two primary hurdles: first, data owners (clients) are restricted by privacy regulations from sharing sensitive datasets with the Learning Service Provider (LSP) or other clients. Second, the LSP must protect the intellectual property of its proprietary FM, preventing it from being shared with clients. These conflicting requirements necessitate a 'double-blind' privacy approach where the LSP never sees the task data and clients never access the FM. Furthermore, traditional adaptation techniques like full fine-tuning or standard adapters (e.g., LoRA) are often impractical because they require computationally expensive backpropagation through the massive FM backbone, which is infeasible when the model is kept private by the server.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Conceptual illustration of BlindFed framework for double-blind federated adaptation of a foundation model.",
      "relevance": "This figure visually defines the 'double-blind' challenge by showing the separation between the LSP (Server) holding the FM and the Data Owners (Clients) holding private datasets D1 through DN."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Section 1",
    "Section 3"
  ]
}"""

Token usage so far: 41748 prompt tokens, 1838 completion tokens

Cost so far: $0.47262

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "Foundation models (FMs) like GPT, CLIP, and ViT demonstrate exceptional zero-shot performance but often require task-specific adaptation for challenging out-of-domain tasks such as medical or satellite imagery. This adaptation process faces two primary hurdles: first, data owners (clients) are restricted by privacy regulations from sharing sensitive datasets with the Learning Service Provider (LSP) or other clients. Second, the LSP must protect the intellectual property of its proprietary FM, preventing it from being shared with clients. These conflicting requirements necessitate a 'double-blind' privacy approach where the LSP never sees the task data and clients never access the FM. Furthermore, traditional adaptation techniques like full fine-tuning or standard adapters (e.g., LoRA) are often impractical because they require computationally expensive backpropagation through the massive FM backbone, which is infeasible when the model is kept private by the server.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Conceptual illustration of BlindFed framework for double-blind federated adaptation of a foundation model.",
      "relevance": "This figure visually defines the 'double-blind' challenge by showing the separation between the LSP (Server) holding the FM and the Data Owners (Clients) holding private datasets D1 through DN."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Section 1",
    "Section 3"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 1,
  "title": "Challenges in Foundation Model Adaptation",
  "summary": "Adapting Foundation Models (FMs) for downstream tasks faces two major hurdles: data owners cannot share sensitive data due to privacy regulations, and service providers cannot share proprietary FMs due to intellectual property restrictions.",
  "paper_section": "Introduction",
  "narrative_role": "introduction",
  "asset_video": null,
  "duration_stat": {
    "min": 8.0,
    "max": 12.0,
    "avg": 10.0
  }
}

Reference style advice:
Reference Layouts for 'introduction' section from similar papers:
- Example 1: The slide uses a simple single-column layout on a plain white background. The title is located at the top left and is distinctive for its multi-colored text: 'Open-world' is orange, 'part' is blue, 'segmentation in' is black, and '3D' is purple. Below the title, the content is structured as a short list introduced by the word 'But:'. There are two bullet points describing challenges: the first states 'No large-scale data' followed by a red 'X' mark, and the second states 'Collecting human annotations for 3D is difficult' followed by a worried face emoji. The text density is very light, leaving significant white space in the center and bottom. A circular video inset of the presenter is positioned in the bottom right corner of the frame.
- Example 2: The slide is organized with a large, bold title 'Background' at the top left, followed by a subtitle 'The capability gap from single-image to multi-image reasoning' and a numbered list of four reasoning capabilities. The main body is divided into two horizontal sections, each labeled vertically on the far left. The top section, labeled 'OK-VQA', features a five-column grid. Each column has a colored header box (green, blue, yellow, red, and teal) containing a category name, followed by a single image and a corresponding question-and-answer pair. The bottom section, labeled 'Mantis-Eval', is divided into two parts by a vertical dashed line. The left part displays two images of dice with a question below them, while the right part shows three images of people with a question below. The overall background is white, and small bibliographic citations are placed at the bottom left corner. The text density is moderate, balancing descriptive text with multiple illustrative images.
- Example 3: The slide uses a minimalist single-column layout on a plain white background. The main title is located at the top left, featuring a multi-colored font style where 'Open-world' is orange, 'part' is blue, and '3D' is purple. Below the title, a sub-header 'But:' introduces a list of challenges. There are two bullet points: the first states 'No large-scale data' followed by a red 'X' icon, and the second states 'Collecting human annotations for 3D is difficult' followed by a worried face emoji. The text is left-aligned, leaving a large amount of empty white space in the center and bottom of the slide. A circular video inset of the presenter is positioned in the bottom right corner. The text density is light, focusing on high-level motivation and problem statements.
- Example 4: The slide is organized into two main vertical sections. On the left, a dark-colored sidebar serves as a navigation menu or table of contents, featuring a multi-level hierarchical list of topics in various colors (green, blue, orange, and white) starting with 'Introduction'. The right section, which occupies the majority of the slide, displays a page from a research paper on a white background. This page begins with a comparison figure (Figure 1) that uses a grid of icons (green checkmarks and red crosses) to contrast 'Autoregression', 'Diffusion', and 'Block Diffusion (Ours)' across four performance metrics. Below the figure, there are several paragraphs of dense academic text, including a bulleted list of four key contributions. Specific phrases within the text are highlighted with a green background. The bottom of the right section introduces 'Section 2: BACKGROUND' with mathematical notation for discrete random variables. A small, green pixel-art frog icon is positioned in the bottom right corner.
- Example 5: The slide is structured with a large, bold serif title 'Motivation' at the top-left, followed by a secondary question-style heading. The central content is organized into three vertical columns, each presenting a different example of model behavior. Each column contains a row of images at the top, followed by two sets of question-and-answer pairs. These Q&A pairs are housed in light gray rectangular blocks to distinguish them. The questions ask the model to compare or count elements across the images, while the answers (marked with small icons like a flamingo, cat, or globe) show how the model's reasoning changes when the order of the images in the prompt is swapped. Key words in the answers are highlighted in green or red to emphasize consistency or errors. At the bottom of the slide, a large bold summary statement explains the concept of 'Position bias' across the full width of the page. The overall text density is moderate, balanced by the visual examples.

Duration statistics for this section (from references): min=1.0s, max=139.0s, avg=31.8s.

Your job is to decide the **visual layout** for this slide. Do NOT decide builds or animations — those will be planned later.

## CHOOSE THE BEST LAYOUT

Pick the layout template that best suits the content. Common templates include (but you are NOT limited to these):
- `two_col_fig_left` — Figure on left, bullets on right. Best for: method diagrams, architecture figures, or tall/vertical figures.
- `two_col_fig_right` — Bullets on left, figure on right. Best for: motivation slides with illustrative or tall/vertical figures.
- `full_fig_with_callouts` — Large figure with small bullet callouts below. Best for: results, data visualizations, or wide/horizontal figures.
- `one_col_bullets` — Full-width bullets, no figure. Best for: text-heavy overview or summary slides.
- `video_with_caption` — Large video region with small bullet callouts below. Best for: when an `asset_video` is provided.

If none of these fit, invent a descriptive template name and define its regions.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "video": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "bullets": {"x": 0.55, "y": 0.25, "w": 0.4, "h": 0.6}
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "Two-column layout with figure on left is ideal for showing the architecture diagram alongside explanatory bullets."
}

## STRICT RULES:
1. **Region keys**: Only use `title`, `bullets`, `figure`, `video` as region keys. Do NOT invent keys like `callout_1`, `table`, etc.
2. **Coordinates**: All x/y/w/h values must be normalized (0.0 to 1.0). Regions must not overlap.
3. **has_figure**: Set to `true` only if the content summary has relevant figures. If no figure is available, omit `figure` from regions.
4. **has_video**: Set to `true` only if `scene_context` specifically assigns an `asset_video`. If true, include the `video` region. Do not include both `figure` and `video` unless space permits.
5. **No builds**: Do NOT include `build_skeleton`, `expected_build_steps`, or any animation information.
6. Output ONLY valid JSON, no markdown fences, no explanation.

IMPORTANT FIGURE ASPECT RATIO RULE:
If the extracted figure is nearly square, its placement is flexible. However, if the figure has a much larger dimension horizontally (like a wide rectangle), choose a layout with a wide figure region (e.g., `full_fig_with_callouts` or placing it spanning top/bottom) so it is not shrunk awkwardly. If it is very tall/vertical, choose a side-by-side template (e.g., `two_col_fig_left`) where it has vertical space. Ensure your chosen template and `layout_regions` coordinates are decided accordingly to preserve the figure's aspect ratio without shrinking it.


**Answer (from GEMINI)**

"""{
  "layout_template": "two_col_fig_right",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "bullets": {
      "x": 0.05,
      "y": 0.2,
      "w": 0.4,
      "h": 0.7
    },
    "figure": {
      "x": 0.5,
      "y": 0.2,
      "w": 0.45,
      "h": 0.7
    }
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "A two-column layout with bullets on the left and the figure on the right is a classic motivation slide structure. It allows for a clear textual explanation of the two conflicting privacy hurdles while using Figure 1 to visually anchor the 'double-blind' concept. The white background and clean alignment reflect the minimalist academic style seen in the reference examples."
}"""

Token usage so far: 54003 prompt tokens, 2122 completion tokens

Cost so far: $0.60369

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "Foundation models (FMs) like GPT, CLIP, and ViT demonstrate exceptional zero-shot performance but often require task-specific adaptation for challenging out-of-domain tasks such as medical or satellite imagery. This adaptation process faces two primary hurdles: first, data owners (clients) are restricted by privacy regulations from sharing sensitive datasets with the Learning Service Provider (LSP) or other clients. Second, the LSP must protect the intellectual property of its proprietary FM, preventing it from being shared with clients. These conflicting requirements necessitate a 'double-blind' privacy approach where the LSP never sees the task data and clients never access the FM. Furthermore, traditional adaptation techniques like full fine-tuning or standard adapters (e.g., LoRA) are often impractical because they require computationally expensive backpropagation through the massive FM backbone, which is infeasible when the model is kept private by the server.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Conceptual illustration of BlindFed framework for double-blind federated adaptation of a foundation model.",
      "relevance": "This figure visually defines the 'double-blind' challenge by showing the separation between the LSP (Server) holding the FM and the Data Owners (Clients) holding private datasets D1 through DN."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Section 1",
    "Section 3"
  ]
}

The layout has been decided:
{
  "layout_template": "two_col_fig_right",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "bullets": {
      "x": 0.05,
      "y": 0.2,
      "w": 0.4,
      "h": 0.7
    },
    "figure": {
      "x": 0.5,
      "y": 0.2,
      "w": 0.45,
      "h": 0.7
    }
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "A two-column layout with bullets on the left and the figure on the right is a classic motivation slide structure. It allows for a clear textual explanation of the two conflicting privacy hurdles while using Figure 1 to visually anchor the 'double-blind' concept. The white background and clean alignment reflect the minimalist academic style seen in the reference examples."
}

Scene context:
{
  "scene_id": 1,
  "title": "Challenges in Foundation Model Adaptation",
  "summary": "Adapting Foundation Models (FMs) for downstream tasks faces two major hurdles: data owners cannot share sensitive data due to privacy regulations, and service providers cannot share proprietary FMs due to intellectual property restrictions.",
  "paper_section": "Introduction",
  "narrative_role": "introduction",
  "asset_video": null,
  "duration_stat": {
    "min": 8.0,
    "max": 12.0,
    "avg": 10.0
  }
}



Your job is to **draft the actual content** (title, bullets, audio, figure choice, and duration) that fits into this layout. You do NOT decide the layout — that is already set. You also do NOT decide builds or animations — those will be planned later based on your drafted content.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "title": "A clear, concise slide title",
  "audio_content": "Full narration transcript for this entire scene. Should be natural, conversational, and cover all key points. The duration should be based on the length of this transcript.",
  "duration_sec": 8.5,
  "bullets": [
    "First concise bullet point",
    "Second concise bullet point",
    "Third concise bullet point"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure X",
    "caption": "Brief caption describing the figure"
  },
  "video": {
    "type": "asset_video",
    "path": "clip1.mp4",
    "caption": "Brief caption describing the video contents"
  },
  "source": ["Figure 1", "Section 3.1"],
  "prompt": "Visual description of the scene for generation"
}

## STRICT RULES:
1. **Number of bullets**: Write 2-4 concise, impactful bullets that cover the key points from the extracted content.
2. **Figure/Video assignment**: 
   - Assign `figure` ONLY if the content summary's `key_figures` has relevant images. 
   - Assign `video` ONLY if the `scene_context` assigns an `asset_video`.
   - If the style plan omits `has_figure` or `has_video`, omit the respective block completely.
3. **Bullet text**: Each bullet should be concise (under 15 words preferred), impactful, and directly derived from `extracted_content`. Not a copy — a focused summary.
4. **audio_content**: Natural narration covering all bullet points AND the video clip action if a video is present. 
5. **duration_sec**: First, draft the `audio_content`. Then, CALCULATE the duration: `duration_sec = word_count_of_audio / 2.5`. Do NOT guess. If the stats say 8s but you wrote 40 words, `duration_sec` MUST be 16.0.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "title": "Adapting Foundation Models: The Privacy Paradox",
  "audio_content": "Adapting foundation models for specialized tasks creates a privacy paradox. Data owners cannot share sensitive data, while providers must protect proprietary models. This 'double-blind' challenge makes traditional adaptation techniques practically infeasible.",
  "duration_sec": 12.8,
  "bullets": [
    "FMs require task-specific adaptation for specialized domains",
    "Data owners must protect sensitive datasets from exposure",
    "Service providers must safeguard proprietary model weights",
    "Traditional fine-tuning is infeasible under 'double-blind' constraints"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 1",
    "caption": "Conceptual illustration of the double-blind adaptation challenge."
  },
  "source": [
    "Figure 1",
    "Section 1"
  ],
  "prompt": "A slide showing the challenges of foundation model adaptation. On the left, bullet points describe the conflict between data privacy and model intellectual property. On the right, a conceptual diagram shows a server with a foundation model separated from multiple clients with private datasets."
}"""

Token usage so far: 65239 prompt tokens, 2389 completion tokens

Cost so far: $0.72406

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "Adapting Foundation Models: The Privacy Paradox",
  "audio_content": "Adapting foundation models for specialized tasks creates a privacy paradox. Data owners cannot share sensitive data, while providers must protect proprietary models. This 'double-blind' challenge makes traditional adaptation techniques practically infeasible.",
  "duration_sec": 12.8,
  "bullets": [
    "FMs require task-specific adaptation for specialized domains",
    "Data owners must protect sensitive datasets from exposure",
    "Service providers must safeguard proprietary model weights",
    "Traditional fine-tuning is infeasible under 'double-blind' constraints"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 1",
    "caption": "Conceptual illustration of the double-blind adaptation challenge."
  },
  "source": [
    "Figure 1",
    "Section 1"
  ],
  "prompt": "A slide showing the challenges of foundation model adaptation. On the left, bullet points describe the conflict between data privacy and model intellectual property. On the right, a conceptual diagram shows a server with a foundation model separated from multiple clients with private datasets."
}

Layout information:
{
  "layout_template": "two_col_fig_right",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "bullets": {
      "x": 0.05,
      "y": 0.2,
      "w": 0.4,
      "h": 0.7
    },
    "figure": {
      "x": 0.5,
      "y": 0.2,
      "w": 0.45,
      "h": 0.7
    }
  },
  "has_figure": true,
  "total_time_sec": 12.8
}

Your job is to:
1. **Decide the build plan** — how many build steps, and what gets revealed in each step.
2. **Assign the drafted bullets to specific build steps** in the best storytelling order.
3. **Split the audio into per-build segments** so each build has matching narration.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "style": "Slides",
  "expected_build_steps": 3,
  "elements": {
    "title": "The slide title from the draft",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure X",
      "caption": "Caption from draft"
    },
    "bullets": [
      "First bullet",
      "Second bullet"
    ]
  },
  "builds": [
    {
      "step_index": 0,
      "time_offset_sec": 0.0,
      "actions": [
        {"type": "show", "target": "title"},
        {"type": "show", "target": "figure"}
      ],
      "audio_segment": "Opening narration for this build step.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 3.0,
      "actions": [
        {"type": "fade_in", "target": "bullets[0]"}
      ],
      "audio_segment": "Narration for the first bullet point.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 6.0,
      "actions": [
        {"type": "fade_in", "target": "bullets[1]"}
      ],
      "audio_segment": "Narration for the second bullet point.",
      "visual_emphasis": []
    }
  ]
}

## STRICT RULES:
1. **Build count**: `expected_build_steps` = 1 + number_of_bullets. Build 0 shows title (and figure/video if present), then one build per bullet.
2. **One bullet per build**: After build 0, each build reveals exactly ONE bullet. `bullets[0]` in build 1, `bullets[1]` in build 2, etc.
3. **Build 0**: Always shows `title` (and `figure`/`video` if present). Never shows bullets in build 0.
4. **Audio segments**: Split the `audio_content` from the draft into segments. Each build's `audio_segment` must be non-empty and correspond to what that build reveals.
5. **Bullet ordering**: Assign bullets to builds in the order that creates the best storytelling flow for the audience.
6. **time_offset_sec**: Space evenly across the total time. For N builds over T seconds: offsets at 0, T/N, 2T/N, etc.
7. **visual_emphasis**: Always set to empty list `[]`.
8. **Action targets**: Only use targets that exist in `elements`: `title`, `figure`, `video`, `bullets[0]`, `bullets[1]`, etc.
9. **elements**: Copy the drafted title, figure, video, and bullets exactly — do not modify the text content.
10. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""```json
{
  "style": "Slides",
  "expected_build_steps": 5,
  "elements": {
    "title": "Adapting Foundation Models: The Privacy Paradox",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 1",
      "caption": "Conceptual illustration of the double-blind adaptation challenge."
    },
    "bullets": [
      "FMs require task-specific adaptation for specialized domains",
      "Data owners must protect sensitive datasets from exposure",
      "Service providers must safeguard proprietary model weights",
      "Traditional fine-tuning is infeasible under 'double-blind' constraints"
    ]
  },
  "builds": [
    {
      "step_index": 0,
      "time_offset_sec": 0.0,
      "actions": [
        {
          "type": "show",
          "target": "title"
        },
        {
          "type": "show",
          "target": "figure"
        }
      ],
      "audio_segment": "Adapting foundation models for specialized tasks",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 2.56,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[0]"
        }
      ],
      "audio_segment": "creates a privacy paradox.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 5.12,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[1]"
        }
      ],
      "audio_segment": "Data owners cannot share sensitive data,",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 7.68,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[2]"
        }
      ],
      "audio_segment": "while providers must protect proprietary models.",
      "visual_emphasis": []
    },
    {
      "step_index": 4,
      "time_offset_sec": 10.24,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[3]"
        }
      ],
      "audio_segment": "This 'double-blind' challenge makes traditional adaptation techniques practically infeasible.",
      "visual_emphasis": []
    }
  ]
}
```"""

Token usage so far: 76393 prompt tokens, 3030 completion tokens

Cost so far: $0.85483

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 2,
  "title": "The BlindFed Framework",
  "summary": "BlindFed is a novel framework for double-blind federated adaptation. It allows collaborative training where data owners never access the FM, and the Learning Service Provider never sees the sensitive task data, utilizing Fully Homomorphic Encryption (FHE).",
  "paper_section": "Proposed BlindFed Framework",
  "narrative_role": "method",
  "asset_video": null,
  "duration_stat": {
    "min": 10.0,
    "max": 15.0,
    "avg": 12.0
  }
}

## Previous Scenes Memory
The following content was extracted for the immediately preceding scenes. **This is provided as a memory of what the audience has JUST seen.**
You MUST NOT repeat the claims, figures, tables, or equations from these previous scenes in your current extraction, to ensure the presentation maintains forward momentum without redundant slides.
If you must reference the exactly same figure/table, the 'relevance' MUST be clearly unique to avoid narrative duplication.

{
  "extracted_content": "Foundation models (FMs) like GPT, CLIP, and ViT demonstrate exceptional zero-shot performance but often require task-specific adaptation for challenging out-of-domain tasks such as medical or satellite imagery. This adaptation process faces two primary hurdles: first, data owners (clients) are restricted by privacy regulations from sharing sensitive datasets with the Learning Service Provider (LSP) or other clients. Second, the LSP must protect the intellectual property of its proprietary FM, preventing it from being shared with clients. These conflicting requirements necessitate a 'double-blind' privacy approach where the LSP never sees the task data and clients never access the FM. Furthermore, traditional adaptation techniques like full fine-tuning or standard adapters (e.g., LoRA) are often impractical because they require computationally expensive backpropagation through the massive FM backbone, which is infeasible when the model is kept private by the server.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Conceptual illustration of BlindFed framework for double-blind federated adaptation of a foundation model.",
      "relevance": "This figure visually defines the 'double-blind' challenge by showing the separation between the LSP (Server) holding the FM and the Data Owners (Clients) holding private datasets D1 through DN."
    }
  ],
  "key_tables": [],
  "key_equations": []
}


Read the paper carefully and extract ALL relevant content from the section(s) referenced in this scene.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "extracted_content": "A comprehensive summary of the key information from this section. Include main claims, methods, results, or insights. This should contain enough detail for someone to write presentation bullets from it.",
  "key_figures": [
    {
      "ref": "Figure X",
      "caption": "The actual caption from the paper",
      "relevance": "Why this figure matters for this scene"
    }
  ],
  "key_tables": [
    {
      "ref": "Table X",
      "caption": "The actual caption from the paper",
      "relevance": "Why this table matters for this scene"
    }
  ],
  "key_equations": [
    {
      "ref": "Equation X or description",
      "content": "The equation in text form",
      "relevance": "Why this equation matters for this scene"
    }
  ],
  "section_refs": ["Section 3.1", "Section 3.2"]
}

## STRICT RULES:
1. **Only reference figures/tables that actually appear in the paper section.** Do NOT invent or guess figure/table numbers.
2. **key_figures** must list figures by their exact label in the paper (e.g., "Figure 1", "Fig. 2").
3. If no figures/tables/equations are relevant, use empty lists `[]`.
4. **extracted_content** must be detailed enough to create 2-4 meaningful bullet points from it.
5. **Memory Context**: The `Previous Scenes Memory` (if provided) shows what was ALREADY covered. You MUST NOT repeat its text content, claims, figures, tables, or equations. CRITICAL: Even if you MUST reference the same figure/table, the text content (`extracted_content`) and `relevance` MUST still be completely DIFFERENT.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "extracted_content": "BlindFed addresses the double-blind adaptation challenge through three core innovations. First, the original FM is redesigned into an FHE-friendly architecture by replacing non-linear operations (GELU, Softmax, LayerNorm) with low-degree polynomial approximations, such as a quadratic function for GELU. Second, a two-stage split learning approach is used: an offline stage where the server distills knowledge from the original FM into the FHE-friendly version using auxiliary data, and an online stage where clients perform encrypted inference block-by-block. This allows clients to train local parallel adapters and classification heads in plaintext without backpropagating through the FM backbone. Third, the framework incorporates privacy-boosting schemes like sample-level permutation and Stochastic Block Sampling (SBS) to mitigate model extraction attacks by randomizing sample order and hiding a subset of block outputs during training.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "Overview of the proposed BlindFed framework for double-blind federated adaptation.",
      "relevance": "Provides a high-level workflow of the three main components: architecture redesign, offline distillation, and online adaptation."
    },
    {
      "ref": "Figure 3",
      "caption": "FHE-friendly architecture redesign.",
      "relevance": "Illustrates the specific polynomial replacements for non-linear operations (e.g., Quad for GELU) and the placement of the parallel adapter."
    },
    {
      "ref": "Figure 5",
      "caption": "Stochastic block sampling strategy.",
      "relevance": "Visualizes the probabilistic approach used to hide intermediate block outputs from clients to boost model privacy."
    }
  ],
  "key_tables": [],
  "key_equations": [
    {
      "ref": "Equation 4",
      "content": "GELU(x) ≈ Quad(x) = 0.125x^2 + 0.25x + 0.5",
      "relevance": "Shows the specific quadratic approximation used to make the GELU activation function compatible with FHE."
    },
    {
      "ref": "Equation 7",
      "content": "g_l(z) = α W^u_l GELU(W^d_l z)",
      "relevance": "Defines the low-rank parallel adapter function used for local client-side training."
    }
  ],
  "section_refs": ["Section 4", "Section 4.1", "Section 4.2", "Section 4.3"]
}"""

Token usage so far: 87314 prompt tokens, 3613 completion tokens

Cost so far: $0.98153

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "BlindFed addresses the double-blind adaptation challenge through three core innovations. First, the original FM is redesigned into an FHE-friendly architecture by replacing non-linear operations (GELU, Softmax, LayerNorm) with low-degree polynomial approximations, such as a quadratic function for GELU. Second, a two-stage split learning approach is used: an offline stage where the server distills knowledge from the original FM into the FHE-friendly version using auxiliary data, and an online stage where clients perform encrypted inference block-by-block. This allows clients to train local parallel adapters and classification heads in plaintext without backpropagating through the FM backbone. Third, the framework incorporates privacy-boosting schemes like sample-level permutation and Stochastic Block Sampling (SBS) to mitigate model extraction attacks by randomizing sample order and hiding a subset of block outputs during training.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "Overview of the proposed BlindFed framework for double-blind federated adaptation.",
      "relevance": "Provides a high-level workflow of the three main components: architecture redesign, offline distillation, and online adaptation."
    },
    {
      "ref": "Figure 3",
      "caption": "FHE-friendly architecture redesign.",
      "relevance": "Illustrates the specific polynomial replacements for non-linear operations (e.g., Quad for GELU) and the placement of the parallel adapter."
    },
    {
      "ref": "Figure 5",
      "caption": "Stochastic block sampling strategy.",
      "relevance": "Visualizes the probabilistic approach used to hide intermediate block outputs from clients to boost model privacy."
    }
  ],
  "key_tables": [],
  "key_equations": [
    {
      "ref": "Equation 4",
      "content": "GELU(x) \u2248 Quad(x) = 0.125x^2 + 0.25x + 0.5",
      "relevance": "Shows the specific quadratic approximation used to make the GELU activation function compatible with FHE."
    },
    {
      "ref": "Equation 7",
      "content": "g_l(z) = \u03b1 W^u_l GELU(W^d_l z)",
      "relevance": "Defines the low-rank parallel adapter function used for local client-side training."
    }
  ],
  "section_refs": [
    "Section 4",
    "Section 4.1",
    "Section 4.2",
    "Section 4.3"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 2,
  "title": "The BlindFed Framework",
  "summary": "BlindFed is a novel framework for double-blind federated adaptation. It allows collaborative training where data owners never access the FM, and the Learning Service Provider never sees the sensitive task data, utilizing Fully Homomorphic Encryption (FHE).",
  "paper_section": "Proposed BlindFed Framework",
  "narrative_role": "method",
  "asset_video": null,
  "duration_stat": {
    "min": 10.0,
    "max": 15.0,
    "avg": 12.0
  }
}

Reference style advice:
Reference Layouts for 'method' section from similar papers:
- Example 1: The slide follows a clean, single-column layout on a white background. The title 'Prototype Evolution' is prominently displayed in the top-left corner in a large, bold, dark red font. In the top-right corner, there is a logo for 'NEURAL INFORMATION PROCESSING SYSTEMS' featuring a purple abstract neural network icon. The main body of the slide starts with an introductory paragraph. Below this, the content is structured into two main hierarchical sections: 'Textual Prototype Evolution' and 'Visual Prototype Evolution'. Each section is introduced by a bolded heading with a square bullet point and contains two sub-bullets marked with small circles. The text is left-aligned, and the hierarchical structure uses indentation to organize the information. A small page number '4' is visible in the bottom-right corner. The slide has a moderate text density with significant white space, making it easy to read.
- Example 2: The slide follows a clean, single-column layout on a plain white background. The title, 'Prototype Evolution', is prominently displayed in the top-left corner in a large, bold, dark red font. In the top-right corner, there is a decorative purple logo for 'NEURAL INFORMATION PROCESSING SYSTEMS'. The main body of the slide begins with an introductory paragraph explaining the 'DPE method'. This is followed by two main sections, each marked with a square bullet and a bolded sub-heading: 'Textual Prototype Evolution' and 'Visual Prototype Evolution'. Each of these sections contains two sub-bullets (circles) that provide technical details about the approach. The text is left-aligned throughout, creating a clear hierarchical structure. A small page number '4' is visible in the bottom-right corner. The overall text density is moderate, focusing on explaining the methodology.
- Example 3: The slide follows a top-to-bottom flow. At the top-left is a large, bold serif title. Below it, the content is organized into two text blocks. The first block contains a sub-heading about causal masks followed by two bullet points. The second block introduces a comparison of three variants with three corresponding bullet points (Causal Mask, Isolated Mask, and Bidirectional Mask). The bottom third of the slide features three side-by-side diagrams that visually represent these masking strategies. Each diagram is a 4x4 attention matrix with blue-labeled axes (I1, T1, I2, T2). The matrices use orange squares to show allowed interactions and light grey squares for masked ones. The overall design is clean with a white background, using a color palette of dark blue for text, light blue for labels, and orange for highlights. Text density is moderate and well-structured.
- Example 4: The slide follows a clean, single-column layout on a white background. A large, bold title is positioned at the top-left. Immediately below the title is a single line of introductory text. The middle section of the slide is dominated by a centered block of mathematical equations that define the 'SoFt Attention' (SoFA) method. Below these equations, two small, side-by-side grid diagrams illustrate the 'W_causal' and 'W_bidirect' attention masks using orange and blue colored squares. The bottom third of the slide contains explanatory text regarding the parameter sigma, organized with an introductory sentence followed by two bullet points. The text density is moderate, and the visual hierarchy clearly leads from the problem statement to the mathematical solution and then to its practical implications.
- Example 5: The slide features a large, complex architectural diagram centered between a top title and a bottom summary text. The title 'DPE Overview' is positioned in a large, bold, dark red font at the top-left, while the 'NEURAL INFORMATION PROCESSING SYSTEMS' logo with its purple dot pattern is at the top-right. The central diagram flows from left to right, starting with input sources on the left: 'Text Descriptions', 'High-Confidence Samples' (images of dogs, cats, and cars), and 'Augmented Test Images'. These inputs pass through frozen encoders, indicated by snowflake icons. The middle section illustrates 'Textual Prototypes' and 'Visual Prototypes' undergoing a 'Prototype Evolving' process with an 'L_align' loss. To the right of the main flow, two separate panels show the 'Textual Prototype Evolution' and 'Visual Prototype Evolution' over time, marked by clock icons. The final stage of the main diagram shows 'Predictions of All Views', 'Confidence Selection', and an 'Average' step leading to final class scores and an 'L_aug' loss. A two-line summary paragraph at the bottom explains the method's use of prototypes and CLIP. The slide has a white background with a page number '3' in the bottom-right corner.

Duration statistics for this section (from references): min=1.0s, max=83.2s, avg=19.5s.

Your job is to decide the **visual layout** for this slide. Do NOT decide builds or animations — those will be planned later.

## CHOOSE THE BEST LAYOUT

Pick the layout template that best suits the content. Common templates include (but you are NOT limited to these):
- `two_col_fig_left` — Figure on left, bullets on right. Best for: method diagrams, architecture figures, or tall/vertical figures.
- `two_col_fig_right` — Bullets on left, figure on right. Best for: motivation slides with illustrative or tall/vertical figures.
- `full_fig_with_callouts` — Large figure with small bullet callouts below. Best for: results, data visualizations, or wide/horizontal figures.
- `one_col_bullets` — Full-width bullets, no figure. Best for: text-heavy overview or summary slides.
- `video_with_caption` — Large video region with small bullet callouts below. Best for: when an `asset_video` is provided.

If none of these fit, invent a descriptive template name and define its regions.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "video": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "bullets": {"x": 0.55, "y": 0.25, "w": 0.4, "h": 0.6}
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "Two-column layout with figure on left is ideal for showing the architecture diagram alongside explanatory bullets."
}

## STRICT RULES:
1. **Region keys**: Only use `title`, `bullets`, `figure`, `video` as region keys. Do NOT invent keys like `callout_1`, `table`, etc.
2. **Coordinates**: All x/y/w/h values must be normalized (0.0 to 1.0). Regions must not overlap.
3. **has_figure**: Set to `true` only if the content summary has relevant figures. If no figure is available, omit `figure` from regions.
4. **has_video**: Set to `true` only if `scene_context` specifically assigns an `asset_video`. If true, include the `video` region. Do not include both `figure` and `video` unless space permits.
5. **No builds**: Do NOT include `build_skeleton`, `expected_build_steps`, or any animation information.
6. Output ONLY valid JSON, no markdown fences, no explanation.

IMPORTANT FIGURE ASPECT RATIO RULE:
If the extracted figure is nearly square, its placement is flexible. However, if the figure has a much larger dimension horizontally (like a wide rectangle), choose a layout with a wide figure region (e.g., `full_fig_with_callouts` or placing it spanning top/bottom) so it is not shrunk awkwardly. If it is very tall/vertical, choose a side-by-side template (e.g., `two_col_fig_left`) where it has vertical space. Ensure your chosen template and `layout_regions` coordinates are decided accordingly to preserve the figure's aspect ratio without shrinking it.


**Answer (from GEMINI)**

"""{
  "layout_template": "full_fig_with_callouts",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.15, "w": 0.9, "h": 0.45},
    "bullets": {"x": 0.05, "y": 0.62, "w": 0.9, "h": 0.33}
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "Figure 2 is a wide horizontal overview of the entire framework, illustrating the flow from server to client. A full-width figure placement preserves its aspect ratio and provides a clear visual anchor for the three core innovations (redesign, split learning, and privacy boosting) which are detailed in the bullets below."
}"""

Token usage so far: 99883 prompt tokens, 3860 completion tokens

Cost so far: $1.11463

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "BlindFed addresses the double-blind adaptation challenge through three core innovations. First, the original FM is redesigned into an FHE-friendly architecture by replacing non-linear operations (GELU, Softmax, LayerNorm) with low-degree polynomial approximations, such as a quadratic function for GELU. Second, a two-stage split learning approach is used: an offline stage where the server distills knowledge from the original FM into the FHE-friendly version using auxiliary data, and an online stage where clients perform encrypted inference block-by-block. This allows clients to train local parallel adapters and classification heads in plaintext without backpropagating through the FM backbone. Third, the framework incorporates privacy-boosting schemes like sample-level permutation and Stochastic Block Sampling (SBS) to mitigate model extraction attacks by randomizing sample order and hiding a subset of block outputs during training.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "Overview of the proposed BlindFed framework for double-blind federated adaptation.",
      "relevance": "Provides a high-level workflow of the three main components: architecture redesign, offline distillation, and online adaptation."
    },
    {
      "ref": "Figure 3",
      "caption": "FHE-friendly architecture redesign.",
      "relevance": "Illustrates the specific polynomial replacements for non-linear operations (e.g., Quad for GELU) and the placement of the parallel adapter."
    },
    {
      "ref": "Figure 5",
      "caption": "Stochastic block sampling strategy.",
      "relevance": "Visualizes the probabilistic approach used to hide intermediate block outputs from clients to boost model privacy."
    }
  ],
  "key_tables": [],
  "key_equations": [
    {
      "ref": "Equation 4",
      "content": "GELU(x) \u2248 Quad(x) = 0.125x^2 + 0.25x + 0.5",
      "relevance": "Shows the specific quadratic approximation used to make the GELU activation function compatible with FHE."
    },
    {
      "ref": "Equation 7",
      "content": "g_l(z) = \u03b1 W^u_l GELU(W^d_l z)",
      "relevance": "Defines the low-rank parallel adapter function used for local client-side training."
    }
  ],
  "section_refs": [
    "Section 4",
    "Section 4.1",
    "Section 4.2",
    "Section 4.3"
  ]
}

The layout has been decided:
{
  "layout_template": "full_fig_with_callouts",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "figure": {
      "x": 0.05,
      "y": 0.15,
      "w": 0.9,
      "h": 0.45
    },
    "bullets": {
      "x": 0.05,
      "y": 0.62,
      "w": 0.9,
      "h": 0.33
    }
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "Figure 2 is a wide horizontal overview of the entire framework, illustrating the flow from server to client. A full-width figure placement preserves its aspect ratio and provides a clear visual anchor for the three core innovations (redesign, split learning, and privacy boosting) which are detailed in the bullets below."
}

Scene context:
{
  "scene_id": 2,
  "title": "The BlindFed Framework",
  "summary": "BlindFed is a novel framework for double-blind federated adaptation. It allows collaborative training where data owners never access the FM, and the Learning Service Provider never sees the sensitive task data, utilizing Fully Homomorphic Encryption (FHE).",
  "paper_section": "Proposed BlindFed Framework",
  "narrative_role": "method",
  "asset_video": null,
  "duration_stat": {
    "min": 10.0,
    "max": 15.0,
    "avg": 12.0
  }
}

## Previous Content
The following content was drafted for the immediately preceding scenes.
You MUST NOT repeat the exact text content or claims from these previous scenes in your current draft.

{
  "bullets": [
    "FMs require task-specific adaptation for specialized domains",
    "Data owners must protect sensitive datasets from exposure",
    "Service providers must safeguard proprietary model weights",
    "Traditional fine-tuning is infeasible under 'double-blind' constraints"
  ],
  "audio_content": "Adapting foundation models for specialized tasks creates a privacy paradox. Data owners cannot share sensitive data, while providers must protect proprietary models. This 'double-blind' challenge makes traditional adaptation techniques practically infeasible."
}


Your job is to **draft the actual content** (title, bullets, audio, figure choice, and duration) that fits into this layout. You do NOT decide the layout — that is already set. You also do NOT decide builds or animations — those will be planned later based on your drafted content.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "title": "A clear, concise slide title",
  "audio_content": "Full narration transcript for this entire scene. Should be natural, conversational, and cover all key points. The duration should be based on the length of this transcript.",
  "duration_sec": 8.5,
  "bullets": [
    "First concise bullet point",
    "Second concise bullet point",
    "Third concise bullet point"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure X",
    "caption": "Brief caption describing the figure"
  },
  "video": {
    "type": "asset_video",
    "path": "clip1.mp4",
    "caption": "Brief caption describing the video contents"
  },
  "source": ["Figure 1", "Section 3.1"],
  "prompt": "Visual description of the scene for generation"
}

## STRICT RULES:
1. **Number of bullets**: Write 2-4 concise, impactful bullets that cover the key points from the extracted content.
2. **Figure/Video assignment**: 
   - Assign `figure` ONLY if the content summary's `key_figures` has relevant images. 
   - Assign `video` ONLY if the `scene_context` assigns an `asset_video`.
   - If the style plan omits `has_figure` or `has_video`, omit the respective block completely.
3. **Bullet text**: Each bullet should be concise (under 15 words preferred), impactful, and directly derived from `extracted_content`. Not a copy — a focused summary.
4. **audio_content**: Natural narration covering all bullet points AND the video clip action if a video is present. 
5. **duration_sec**: First, draft the `audio_content`. Then, CALCULATE the duration: `duration_sec = word_count_of_audio / 2.5`. Do NOT guess. If the stats say 8s but you wrote 40 words, `duration_sec` MUST be 16.0.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "title": "The BlindFed Framework",
  "audio_content": "BlindFed redesigns models with FHE-friendly polynomial approximations, enabling encrypted inference. It uses two-stage split learning to train local adapters without backpropagation through the backbone. Finally, privacy-boosting schemes like stochastic block sampling protect the model from extraction attacks while maintaining adaptation performance.",
  "duration_sec": 16.4,
  "bullets": [
    "Redesigns models with FHE-friendly polynomial approximations for non-linear layers",
    "Uses two-stage split learning to train adapters via encrypted inference",
    "Mitigates model extraction attacks through Stochastic Block Sampling (SBS)"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 2",
    "caption": "Overview of the BlindFed framework: architecture redesign, offline distillation, and online adaptation."
  },
  "source": [
    "Section 4",
    "Figure 2",
    "Section 4.3.2"
  ],
  "prompt": "A wide horizontal diagram showing the three-stage workflow of BlindFed: starting with the original FM, moving to FHE-friendly redesign, then offline distillation on the server, and finally online adaptation with encrypted communication between server and client."
}"""

Token usage so far: 111556 prompt tokens, 4151 completion tokens

Cost so far: $1.24009

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "The BlindFed Framework",
  "audio_content": "BlindFed redesigns models with FHE-friendly polynomial approximations, enabling encrypted inference. It uses two-stage split learning to train local adapters without backpropagation through the backbone. Finally, privacy-boosting schemes like stochastic block sampling protect the model from extraction attacks while maintaining adaptation performance.",
  "duration_sec": 16.4,
  "bullets": [
    "Redesigns models with FHE-friendly polynomial approximations for non-linear layers",
    "Uses two-stage split learning to train adapters via encrypted inference",
    "Mitigates model extraction attacks through Stochastic Block Sampling (SBS)"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 2",
    "caption": "Overview of the BlindFed framework: architecture redesign, offline distillation, and online adaptation."
  },
  "source": [
    "Section 4",
    "Figure 2",
    "Section 4.3.2"
  ],
  "prompt": "A wide horizontal diagram showing the three-stage workflow of BlindFed: starting with the original FM, moving to FHE-friendly redesign, then offline distillation on the server, and finally online adaptation with encrypted communication between server and client."
}

Layout information:
{
  "layout_template": "full_fig_with_callouts",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "figure": {
      "x": 0.05,
      "y": 0.15,
      "w": 0.9,
      "h": 0.45
    },
    "bullets": {
      "x": 0.05,
      "y": 0.62,
      "w": 0.9,
      "h": 0.33
    }
  },
  "has_figure": true,
  "total_time_sec": 16.4
}

Your job is to:
1. **Decide the build plan** — how many build steps, and what gets revealed in each step.
2. **Assign the drafted bullets to specific build steps** in the best storytelling order.
3. **Split the audio into per-build segments** so each build has matching narration.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "style": "Slides",
  "expected_build_steps": 3,
  "elements": {
    "title": "The slide title from the draft",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure X",
      "caption": "Caption from draft"
    },
    "bullets": [
      "First bullet",
      "Second bullet"
    ]
  },
  "builds": [
    {
      "step_index": 0,
      "time_offset_sec": 0.0,
      "actions": [
        {"type": "show", "target": "title"},
        {"type": "show", "target": "figure"}
      ],
      "audio_segment": "Opening narration for this build step.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 3.0,
      "actions": [
        {"type": "fade_in", "target": "bullets[0]"}
      ],
      "audio_segment": "Narration for the first bullet point.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 6.0,
      "actions": [
        {"type": "fade_in", "target": "bullets[1]"}
      ],
      "audio_segment": "Narration for the second bullet point.",
      "visual_emphasis": []
    }
  ]
}

## STRICT RULES:
1. **Build count**: `expected_build_steps` = 1 + number_of_bullets. Build 0 shows title (and figure/video if present), then one build per bullet.
2. **One bullet per build**: After build 0, each build reveals exactly ONE bullet. `bullets[0]` in build 1, `bullets[1]` in build 2, etc.
3. **Build 0**: Always shows `title` (and `figure`/`video` if present). Never shows bullets in build 0.
4. **Audio segments**: Split the `audio_content` from the draft into segments. Each build's `audio_segment` must be non-empty and correspond to what that build reveals.
5. **Bullet ordering**: Assign bullets to builds in the order that creates the best storytelling flow for the audience.
6. **time_offset_sec**: Space evenly across the total time. For N builds over T seconds: offsets at 0, T/N, 2T/N, etc.
7. **visual_emphasis**: Always set to empty list `[]`.
8. **Action targets**: Only use targets that exist in `elements`: `title`, `figure`, `video`, `bullets[0]`, `bullets[1]`, etc.
9. **elements**: Copy the drafted title, figure, video, and bullets exactly — do not modify the text content.
10. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "style": "Slides",
  "expected_build_steps": 4,
  "elements": {
    "title": "The BlindFed Framework",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 2",
      "caption": "Overview of the BlindFed framework: architecture redesign, offline distillation, and online adaptation."
    },
    "bullets": [
      "Redesigns models with FHE-friendly polynomial approximations for non-linear layers",
      "Uses two-stage split learning to train adapters via encrypted inference",
      "Mitigates model extraction attacks through Stochastic Block Sampling (SBS)"
    ]
  },
  "builds": [
    {
      "step_index": 0,
      "time_offset_sec": 0.0,
      "actions": [
        {
          "type": "show",
          "target": "title"
        },
        {
          "type": "show",
          "target": "figure"
        }
      ],
      "audio_segment": "BlindFed redesigns models with FHE-friendly polynomial approximations,",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 4.1,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[0]"
        }
      ],
      "audio_segment": "enabling encrypted inference.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 8.2,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[1]"
        }
      ],
      "audio_segment": "It uses two-stage split learning to train local adapters without backpropagation through the backbone.",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 12.3,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[2]"
        }
      ],
      "audio_segment": "Finally, privacy-boosting schemes like stochastic block sampling protect the model from extraction attacks while maintaining adaptation performance.",
      "visual_emphasis": []
    }
  ]
}"""

Token usage so far: 122739 prompt tokens, 4717 completion tokens

Cost so far: $1.36890

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 3,
  "title": "FHE-friendly Architecture Redesign",
  "summary": "To support encrypted inference, BlindFed replaces non-linear FM operations like Softmax, GELU, and LayerNorm with low-degree polynomial approximations and integrates lightweight parallel adapters for efficient client-side training.",
  "paper_section": "FHE-friendly Architecture Redesign",
  "narrative_role": "method",
  "asset_video": null,
  "duration_stat": {
    "min": 12.0,
    "max": 18.0,
    "avg": 15.0
  }
}

## Previous Scenes Memory
The following content was extracted for the immediately preceding scenes. **This is provided as a memory of what the audience has JUST seen.**
You MUST NOT repeat the claims, figures, tables, or equations from these previous scenes in your current extraction, to ensure the presentation maintains forward momentum without redundant slides.
If you must reference the exactly same figure/table, the 'relevance' MUST be clearly unique to avoid narrative duplication.

{
  "extracted_content": "Foundation models (FMs) like GPT, CLIP, and ViT demonstrate exceptional zero-shot performance but often require task-specific adaptation for challenging out-of-domain tasks such as medical or satellite imagery. This adaptation process faces two primary hurdles: first, data owners (clients) are restricted by privacy regulations from sharing sensitive datasets with the Learning Service Provider (LSP) or other clients. Second, the LSP must protect the intellectual property of its proprietary FM, preventing it from being shared with clients. These conflicting requirements necessitate a 'double-blind' privacy approach where the LSP never sees the task data and clients never access the FM. Furthermore, traditional adaptation techniques like full fine-tuning or standard adapters (e.g., LoRA) are often impractical because they require computationally expensive backpropagation through the massive FM backbone, which is infeasible when the model is kept private by the server.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Conceptual illustration of BlindFed framework for double-blind federated adaptation of a foundation model.",
      "relevance": "This figure visually defines the 'double-blind' challenge by showing the separation between the LSP (Server) holding the FM and the Data Owners (Clients) holding private datasets D1 through DN."
    }
  ],
  "key_tables": [],
  "key_equations": []
}
{
  "extracted_content": "BlindFed addresses the double-blind adaptation challenge through three core innovations. First, the original FM is redesigned into an FHE-friendly architecture by replacing non-linear operations (GELU, Softmax, LayerNorm) with low-degree polynomial approximations, such as a quadratic function for GELU. Second, a two-stage split learning approach is used: an offline stage where the server distills knowledge from the original FM into the FHE-friendly version using auxiliary data, and an online stage where clients perform encrypted inference block-by-block. This allows clients to train local parallel adapters and classification heads in plaintext without backpropagating through the FM backbone. Third, the framework incorporates privacy-boosting schemes like sample-level permutation and Stochastic Block Sampling (SBS) to mitigate model extraction attacks by randomizing sample order and hiding a subset of block outputs during training.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "Overview of the proposed BlindFed framework for double-blind federated adaptation.",
      "relevance": "Provides a high-level workflow of the three main components: architecture redesign, offline distillation, and online adaptation."
    },
    {
      "ref": "Figure 3",
      "caption": "FHE-friendly architecture redesign.",
      "relevance": "Illustrates the specific polynomial replacements for non-linear operations (e.g., Quad for GELU) and the placement of the parallel adapter."
    },
    {
      "ref": "Figure 5",
      "caption": "Stochastic block sampling strategy.",
      "relevance": "Visualizes the probabilistic approach used to hide intermediate block outputs from clients to boost model privacy."
    }
  ],
  "key_tables": [],
  "key_equations": [
    {
      "ref": "Equation 4",
      "content": "GELU(x) \u2248 Quad(x) = 0.125x^2 + 0.25x + 0.5",
      "relevance": "Shows the specific quadratic approximation used to make the GELU activation function compatible with FHE."
    },
    {
      "ref": "Equation 7",
      "content": "g_l(z) = \u03b1 W^u_l GELU(W^d_l z)",
      "relevance": "Defines the low-rank parallel adapter function used for local client-side training."
    }
  ]
}


Read the paper carefully and extract ALL relevant content from the section(s) referenced in this scene.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "extracted_content": "A comprehensive summary of the key information from this section. Include main claims, methods, results, or insights. This should contain enough detail for someone to write presentation bullets from it.",
  "key_figures": [
    {
      "ref": "Figure X",
      "caption": "The actual caption from the paper",
      "relevance": "Why this figure matters for this scene"
    }
  ],
  "key_tables": [
    {
      "ref": "Table X",
      "caption": "The actual caption from the paper",
      "relevance": "Why this table matters for this scene"
    }
  ],
  "key_equations": [
    {
      "ref": "Equation X or description",
      "content": "The equation in text form",
      "relevance": "Why this equation matters for this scene"
    }
  ],
  "section_refs": ["Section 3.1", "Section 3.2"]
}

## STRICT RULES:
1. **Only reference figures/tables that actually appear in the paper section.** Do NOT invent or guess figure/table numbers.
2. **key_figures** must list figures by their exact label in the paper (e.g., "Figure 1", "Fig. 2").
3. If no figures/tables/equations are relevant, use empty lists `[]`.
4. **extracted_content** must be detailed enough to create 2-4 meaningful bullet points from it.
5. **Memory Context**: The `Previous Scenes Memory` (if provided) shows what was ALREADY covered. You MUST NOT repeat its text content, claims, figures, tables, or equations. CRITICAL: Even if you MUST reference the same figure/table, the text content (`extracted_content`) and `relevance` MUST still be completely DIFFERENT.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "extracted_content": "The FHE-friendly architecture redesign transforms the original Foundation Model (FM) into a sequence of blocks $\\hat{B}_{\\hat{\\psi}_\\ell}$ that only utilize polynomial operations, as required by homomorphic encryption schemes like CKKS. The redesign focuses on three primary non-linearities: Softmax, GELU, and LayerNorm. Softmax is approximated by applying a Taylor series expansion to the exponential function, while the division operations necessary for both Softmax normalization and LayerNorm are implemented via Goldschmidt’s algorithm, which replaces direct division with iterative multiplications. The final adapted model is structured as a composition $\\mathcal{M}_\\psi = (\\hat{\\mathcal{M}}_{\\hat{\\psi}} \\parallel A_\\theta) \\circ H_\\eta$, where the approximated FM backbone runs in parallel with a lightweight adapter. This parallel configuration is a critical design choice; unlike sequential adapters (e.g., LoRA), it enables the client to perform local updates on the adapter and classification head using intermediate representations received from the server, completely bypassing the need for backpropagation through the massive, encrypted FM backbone.",
  "key_figures": [
    {
      "ref": "Figure 4",
      "caption": "Illustration of the parallel adapter design.",
      "relevance": "This figure details how the parallel adapters ($g_1$ through $g_L$) are integrated with the transformer blocks, allowing for client-side training without backpropagating through the main model."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 5",
      "caption": "Softmax approximation results.",
      "relevance": "Demonstrates the trade-off between the polynomial degree ($d$) used in the Taylor approximation and the resulting model accuracy and computational latency."
    }
  ],
  "key_equations": [
    {
      "ref": "Equation 3",
      "content": "e^x = \\sum_{i=0}^{\\infty} \\frac{x^i}{i!} \\approx \\sum_{i=0}^{d} \\frac{x^i}{i!}",
      "relevance": "The Taylor series approximation used to replace the exponential function in Softmax to make it FHE-compatible."
    },
    {
      "ref": "Equation 5",
      "content": "\\frac{1}{x} = \\frac{1}{1-(1-x)} = \\prod_{i=0}^{\\infty} (1 + (1-x)^{2^i}) \\approx \\prod_{i=0}^{d} (1 + (1-x)^{2^i})",
      "relevance": "Goldschmidt’s algorithm for approximating the inverse function, which is essential for performing division in LayerNorm and Softmax under FHE."
    }
  ],
  "section_refs": [
    "Section 4.1"
  ]
}"""

Token usage so far: 134220 prompt tokens, 5371 completion tokens

Cost so far: $1.50333

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "The FHE-friendly architecture redesign transforms the original Foundation Model (FM) into a sequence of blocks $\\hat{B}_{\\hat{\\psi}_\\ell}$ that only utilize polynomial operations, as required by homomorphic encryption schemes like CKKS. The redesign focuses on three primary non-linearities: Softmax, GELU, and LayerNorm. Softmax is approximated by applying a Taylor series expansion to the exponential function, while the division operations necessary for both Softmax normalization and LayerNorm are implemented via Goldschmidt\u2019s algorithm, which replaces direct division with iterative multiplications. The final adapted model is structured as a composition $\\mathcal{M}_\\psi = (\\hat{\\mathcal{M}}_{\\hat{\\psi}} \\parallel A_\theta) \\circ H_\\eta$, where the approximated FM backbone runs in parallel with a lightweight adapter. This parallel configuration is a critical design choice; unlike sequential adapters (e.g., LoRA), it enables the client to perform local updates on the adapter and classification head using intermediate representations received from the server, completely bypassing the need for backpropagation through the massive, encrypted FM backbone.",
  "key_figures": [
    {
      "ref": "Figure 4",
      "caption": "Illustration of the parallel adapter design.",
      "relevance": "This figure details how the parallel adapters ($g_1$ through $g_L$) are integrated with the transformer blocks, allowing for client-side training without backpropagating through the main model."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 5",
      "caption": "Softmax approximation results.",
      "relevance": "Demonstrates the trade-off between the polynomial degree ($d$) used in the Taylor approximation and the resulting model accuracy and computational latency."
    }
  ],
  "key_equations": [
    {
      "ref": "Equation 3",
      "content": "e^x = \\sum_{i=0}^{\\infty} \frac{x^i}{i!} \\approx \\sum_{i=0}^{d} \frac{x^i}{i!}",
      "relevance": "The Taylor series approximation used to replace the exponential function in Softmax to make it FHE-compatible."
    },
    {
      "ref": "Equation 5",
      "content": "\frac{1}{x} = \frac{1}{1-(1-x)} = \\prod_{i=0}^{\\infty} (1 + (1-x)^{2^i}) \\approx \\prod_{i=0}^{d} (1 + (1-x)^{2^i})",
      "relevance": "Goldschmidt\u2019s algorithm for approximating the inverse function, which is essential for performing division in LayerNorm and Softmax under FHE."
    }
  ],
  "section_refs": [
    "Section 4.1"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 3,
  "title": "FHE-friendly Architecture Redesign",
  "summary": "To support encrypted inference, BlindFed replaces non-linear FM operations like Softmax, GELU, and LayerNorm with low-degree polynomial approximations and integrates lightweight parallel adapters for efficient client-side training.",
  "paper_section": "FHE-friendly Architecture Redesign",
  "narrative_role": "method",
  "asset_video": null,
  "duration_stat": {
    "min": 12.0,
    "max": 18.0,
    "avg": 15.0
  }
}

Reference style advice:
Reference Layouts for 'method' section from similar papers:
- Example 1: The slide features a large, plain-text title 'Overview' positioned at the top-left. The central portion of the slide is dominated by a complex architectural flowchart that illustrates a machine learning pipeline. This diagram flows from left to right, starting with input images (ground and satellite views) that pass through a 'Feature Extractor'. A prominent red-bordered box in the center, labeled 'T2GA', details a feature aggregation mechanism using MLPs and attention. To its right, a 'Baseline Model' box lists several internal components like a 'Keypoint Detector' and 'Pose Optimizer'. The diagram concludes on the far right with three distinct loss function boxes. Below this diagram, a 'Contributions:' section contains three bullet points that are color-coded to match specific elements in the flowchart: 'T2GA' and 'CycDA Loss' are in red, while 'Equidistant Re-projection Loss' is highlighted with a yellow background. The slide uses a clean white background with moderate text density, focusing primarily on the visual representation of the proposed method's architecture.
- Example 2: The slide follows a clean, single-column layout on a plain white background. The title, 'Prototype Evolution', is prominently displayed in the top-left corner in a large, bold, dark red font. In the top-right corner, there is a decorative purple logo for 'NEURAL INFORMATION PROCESSING SYSTEMS'. The main body of the slide begins with an introductory paragraph explaining the 'DPE method'. This is followed by two main sections, each marked with a square bullet and a bolded sub-heading: 'Textual Prototype Evolution' and 'Visual Prototype Evolution'. Each of these sections contains two sub-bullets (circles) that provide technical details about the approach. The text is left-aligned throughout, creating a clear hierarchical structure. A small page number '4' is visible in the bottom-right corner. The overall text density is moderate, focusing on explaining the methodology.
- Example 3: The slide is organized into three main vertical sections on a white background. At the top, a large bold serif title is positioned at the top-left, followed by a sub-heading that spans the width of the slide. The middle section contains a horizontal row of three image groups, each containing two to three small images. Below each image group is a light gray text box containing a specific question, where image references are color-coded (e.g., blue for image 1, orange for image 2). The bottom section begins with two full-width bold headings introducing 'Position-wise Question Answering (PQA)'. Below these headings, the content is split into two columns: the left column displays a monospaced text block formatted as an instruction-question-answer (I, Q, A) example, while the right column features two bullet points explaining the purpose and interpretation of the PQA metric. The text density is moderate, and the layout uses color accents in the text to link back to the visual examples.
- Example 4: The slide uses a two-column layout on a clean white background. A large, black title 'Training Pipeline' is located at the top-left. The left column consists of hierarchical bullet points with two levels of indentation, detailing the 'Early training' and 'Later training' phases, followed by a final note that the system is 'End-to-end trainable'. The right column contains a complex technical flowchart illustrating the data flow and loss functions. At the top of the diagram, a yellow box represents the 'Time-dependent NeRF' model, which branches into 'Surface points', 'Rendered colors', and 'Predicted signed distance'. Below these, small thumbnail images show rendered scenes and depth maps. At the bottom, a blue box for the 'Motion network' processes timesteps to produce camera poses (green boxes) and motion vectors. Red double-headed arrows labeled with mathematical loss symbols (e.g., L_rgb, L_p, L_sdf, L_flow) connect various nodes to indicate optimization objectives. The diagram uses a consistent color-coding scheme: yellow for the NeRF model, green for pose-related elements, and blue for the motion network.
- Example 5: The slide uses a minimalist design with a solid black background. A single line of white, sans-serif text is centered at the top, serving as a descriptive title or caption. Below this text, a large photographic image spans the width of the slide, showing a street-level view of a residential road lined with trees and fences under a clear sky. A prominent horizontal dashed white line is overlaid across the lower third of the image. Scattered throughout the scene, particularly concentrated along this dashed line and trailing into the distance, are glowing purple and blue light effects that represent the 'query pixels' mentioned in the title. The overall text density is light, prioritizing the visual demonstration over textual information.

Duration statistics for this section (from references): min=1.0s, max=83.2s, avg=19.5s.

Your job is to decide the **visual layout** for this slide. Do NOT decide builds or animations — those will be planned later.

## CHOOSE THE BEST LAYOUT

Pick the layout template that best suits the content. Common templates include (but you are NOT limited to these):
- `two_col_fig_left` — Figure on left, bullets on right. Best for: method diagrams, architecture figures, or tall/vertical figures.
- `two_col_fig_right` — Bullets on left, figure on right. Best for: motivation slides with illustrative or tall/vertical figures.
- `full_fig_with_callouts` — Large figure with small bullet callouts below. Best for: results, data visualizations, or wide/horizontal figures.
- `one_col_bullets` — Full-width bullets, no figure. Best for: text-heavy overview or summary slides.
- `video_with_caption` — Large video region with small bullet callouts below. Best for: when an `asset_video` is provided.

If none of these fit, invent a descriptive template name and define its regions.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "video": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "bullets": {"x": 0.55, "y": 0.25, "w": 0.4, "h": 0.6}
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "Two-column layout with figure on left is ideal for showing the architecture diagram alongside explanatory bullets."
}

## STRICT RULES:
1. **Region keys**: Only use `title`, `bullets`, `figure`, `video` as region keys. Do NOT invent keys like `callout_1`, `table`, etc.
2. **Coordinates**: All x/y/w/h values must be normalized (0.0 to 1.0). Regions must not overlap.
3. **has_figure**: Set to `true` only if the content summary has relevant figures. If no figure is available, omit `figure` from regions.
4. **has_video**: Set to `true` only if `scene_context` specifically assigns an `asset_video`. If true, include the `video` region. Do not include both `figure` and `video` unless space permits.
5. **No builds**: Do NOT include `build_skeleton`, `expected_build_steps`, or any animation information.
6. Output ONLY valid JSON, no markdown fences, no explanation.

IMPORTANT FIGURE ASPECT RATIO RULE:
If the extracted figure is nearly square, its placement is flexible. However, if the figure has a much larger dimension horizontally (like a wide rectangle), choose a layout with a wide figure region (e.g., `full_fig_with_callouts` or placing it spanning top/bottom) so it is not shrunk awkwardly. If it is very tall/vertical, choose a side-by-side template (e.g., `two_col_fig_left`) where it has vertical space. Ensure your chosen template and `layout_regions` coordinates are decided accordingly to preserve the figure's aspect ratio without shrinking it.


**Answer (from GEMINI)**

"""{
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "figure": {
      "x": 0.05,
      "y": 0.2,
      "w": 0.4,
      "h": 0.75
    },
    "bullets": {
      "x": 0.5,
      "y": 0.2,
      "w": 0.45,
      "h": 0.75
    }
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "A two-column layout is chosen to accommodate the vertical orientation of Figure 4 (the architecture diagram) on the left. This allows the right column to provide detailed bullet points explaining the polynomial approximations and parallel adapter design, including the critical mathematical equations for FHE compatibility."
}"""

Token usage so far: 146862 prompt tokens, 5642 completion tokens

Cost so far: $1.63788

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "The FHE-friendly architecture redesign transforms the original Foundation Model (FM) into a sequence of blocks $\\hat{B}_{\\hat{\\psi}_\\ell}$ that only utilize polynomial operations, as required by homomorphic encryption schemes like CKKS. The redesign focuses on three primary non-linearities: Softmax, GELU, and LayerNorm. Softmax is approximated by applying a Taylor series expansion to the exponential function, while the division operations necessary for both Softmax normalization and LayerNorm are implemented via Goldschmidt\u2019s algorithm, which replaces direct division with iterative multiplications. The final adapted model is structured as a composition $\\mathcal{M}_\\psi = (\\hat{\\mathcal{M}}_{\\hat{\\psi}} \\parallel A_\theta) \\circ H_\\eta$, where the approximated FM backbone runs in parallel with a lightweight adapter. This parallel configuration is a critical design choice; unlike sequential adapters (e.g., LoRA), it enables the client to perform local updates on the adapter and classification head using intermediate representations received from the server, completely bypassing the need for backpropagation through the massive, encrypted FM backbone.",
  "key_figures": [
    {
      "ref": "Figure 4",
      "caption": "Illustration of the parallel adapter design.",
      "relevance": "This figure details how the parallel adapters ($g_1$ through $g_L$) are integrated with the transformer blocks, allowing for client-side training without backpropagating through the main model."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 5",
      "caption": "Softmax approximation results.",
      "relevance": "Demonstrates the trade-off between the polynomial degree ($d$) used in the Taylor approximation and the resulting model accuracy and computational latency."
    }
  ],
  "key_equations": [
    {
      "ref": "Equation 3",
      "content": "e^x = \\sum_{i=0}^{\\infty} \frac{x^i}{i!} \\approx \\sum_{i=0}^{d} \frac{x^i}{i!}",
      "relevance": "The Taylor series approximation used to replace the exponential function in Softmax to make it FHE-compatible."
    },
    {
      "ref": "Equation 5",
      "content": "\frac{1}{x} = \frac{1}{1-(1-x)} = \\prod_{i=0}^{\\infty} (1 + (1-x)^{2^i}) \\approx \\prod_{i=0}^{d} (1 + (1-x)^{2^i})",
      "relevance": "Goldschmidt\u2019s algorithm for approximating the inverse function, which is essential for performing division in LayerNorm and Softmax under FHE."
    }
  ],
  "section_refs": [
    "Section 4.1"
  ]
}

The layout has been decided:
{
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "figure": {
      "x": 0.05,
      "y": 0.2,
      "w": 0.4,
      "h": 0.75
    },
    "bullets": {
      "x": 0.5,
      "y": 0.2,
      "w": 0.45,
      "h": 0.75
    }
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "A two-column layout is chosen to accommodate the vertical orientation of Figure 4 (the architecture diagram) on the left. This allows the right column to provide detailed bullet points explaining the polynomial approximations and parallel adapter design, including the critical mathematical equations for FHE compatibility."
}

Scene context:
{
  "scene_id": 3,
  "title": "FHE-friendly Architecture Redesign",
  "summary": "To support encrypted inference, BlindFed replaces non-linear FM operations like Softmax, GELU, and LayerNorm with low-degree polynomial approximations and integrates lightweight parallel adapters for efficient client-side training.",
  "paper_section": "FHE-friendly Architecture Redesign",
  "narrative_role": "method",
  "asset_video": null,
  "duration_stat": {
    "min": 12.0,
    "max": 18.0,
    "avg": 15.0
  }
}

## Previous Content
The following content was drafted for the immediately preceding scenes.
You MUST NOT repeat the exact text content or claims from these previous scenes in your current draft.

{
  "bullets": [
    "Redesigns models with FHE-friendly polynomial approximations for non-linear layers",
    "Uses two-stage split learning to train adapters via encrypted inference",
    "Mitigates model extraction attacks through Stochastic Block Sampling (SBS)"
  ],
  "audio_content": "BlindFed redesigns models with FHE-friendly polynomial approximations, enabling encrypted inference. It uses two-stage split learning to train local adapters without backpropagation through the backbone. Finally, privacy-boosting schemes like stochastic block sampling protect the model from extraction attacks while maintaining adaptation performance."
}


Your job is to **draft the actual content** (title, bullets, audio, figure choice, and duration) that fits into this layout. You do NOT decide the layout — that is already set. You also do NOT decide builds or animations — those will be planned later based on your drafted content.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "title": "A clear, concise slide title",
  "audio_content": "Full narration transcript for this entire scene. Should be natural, conversational, and cover all key points. The duration should be based on the length of this transcript.",
  "duration_sec": 8.5,
  "bullets": [
    "First concise bullet point",
    "Second concise bullet point",
    "Third concise bullet point"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure X",
    "caption": "Brief caption describing the figure"
  },
  "video": {
    "type": "asset_video",
    "path": "clip1.mp4",
    "caption": "Brief caption describing the video contents"
  },
  "source": ["Figure 1", "Section 3.1"],
  "prompt": "Visual description of the scene for generation"
}

## STRICT RULES:
1. **Number of bullets**: Write 2-4 concise, impactful bullets that cover the key points from the extracted content.
2. **Figure/Video assignment**: 
   - Assign `figure` ONLY if the content summary's `key_figures` has relevant images. 
   - Assign `video` ONLY if the `scene_context` assigns an `asset_video`.
   - If the style plan omits `has_figure` or `has_video`, omit the respective block completely.
3. **Bullet text**: Each bullet should be concise (under 15 words preferred), impactful, and directly derived from `extracted_content`. Not a copy — a focused summary.
4. **audio_content**: Natural narration covering all bullet points AND the video clip action if a video is present. 
5. **duration_sec**: First, draft the `audio_content`. Then, CALCULATE the duration: `duration_sec = word_count_of_audio / 2.5`. Do NOT guess. If the stats say 8s but you wrote 40 words, `duration_sec` MUST be 16.0.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "title": "FHE-friendly Architecture Redesign",
  "audio_content": "BlindFed replaces non-linearities like Softmax and LayerNorm with polynomial approximations using Taylor series and Goldschmidt’s algorithm. A key innovation is the parallel adapter design shown here. This structure allows clients to update the model using intermediate representations received from the server, completely bypassing the need for backpropagation through the massive, encrypted backbone.",
  "duration_sec": 18.4,
  "bullets": [
    "Approximates Softmax, GELU, and LayerNorm using low-degree polynomial operations",
    "Uses Taylor series for exponentials and Goldschmidt’s algorithm for division",
    "Parallel adapters enable local training without backpropagation through the backbone"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 4",
    "caption": "Parallel adapter integration with transformer blocks"
  },
  "source": [
    "Section 4.1",
    "Figure 4",
    "Equation 3",
    "Equation 5"
  ],
  "prompt": "A technical diagram showing a vertical stack of transformer blocks on the left, with corresponding parallel adapter modules on the right. Arrows indicate the flow of intermediate representations from the backbone to the adapters, highlighting the client-side training path."
}"""

Token usage so far: 158594 prompt tokens, 5945 completion tokens

Cost so far: $1.76429

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "FHE-friendly Architecture Redesign",
  "audio_content": "BlindFed replaces non-linearities like Softmax and LayerNorm with polynomial approximations using Taylor series and Goldschmidt\u2019s algorithm. A key innovation is the parallel adapter design shown here. This structure allows clients to update the model using intermediate representations received from the server, completely bypassing the need for backpropagation through the massive, encrypted backbone.",
  "duration_sec": 18.4,
  "bullets": [
    "Approximates Softmax, GELU, and LayerNorm using low-degree polynomial operations",
    "Uses Taylor series for exponentials and Goldschmidt\u2019s algorithm for division",
    "Parallel adapters enable local training without backpropagation through the backbone"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 4",
    "caption": "Parallel adapter integration with transformer blocks"
  },
  "source": [
    "Section 4.1",
    "Figure 4",
    "Equation 3",
    "Equation 5"
  ],
  "prompt": "A technical diagram showing a vertical stack of transformer blocks on the left, with corresponding parallel adapter modules on the right. Arrows indicate the flow of intermediate representations from the backbone to the adapters, highlighting the client-side training path."
}

Layout information:
{
  "layout_template": "two_col_fig_left",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "figure": {
      "x": 0.05,
      "y": 0.2,
      "w": 0.4,
      "h": 0.75
    },
    "bullets": {
      "x": 0.5,
      "y": 0.2,
      "w": 0.45,
      "h": 0.75
    }
  },
  "has_figure": true,
  "total_time_sec": 18.4
}

Your job is to:
1. **Decide the build plan** — how many build steps, and what gets revealed in each step.
2. **Assign the drafted bullets to specific build steps** in the best storytelling order.
3. **Split the audio into per-build segments** so each build has matching narration.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "style": "Slides",
  "expected_build_steps": 3,
  "elements": {
    "title": "The slide title from the draft",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure X",
      "caption": "Caption from draft"
    },
    "bullets": [
      "First bullet",
      "Second bullet"
    ]
  },
  "builds": [
    {
      "step_index": 0,
      "time_offset_sec": 0.0,
      "actions": [
        {"type": "show", "target": "title"},
        {"type": "show", "target": "figure"}
      ],
      "audio_segment": "Opening narration for this build step.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 3.0,
      "actions": [
        {"type": "fade_in", "target": "bullets[0]"}
      ],
      "audio_segment": "Narration for the first bullet point.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 6.0,
      "actions": [
        {"type": "fade_in", "target": "bullets[1]"}
      ],
      "audio_segment": "Narration for the second bullet point.",
      "visual_emphasis": []
    }
  ]
}

## STRICT RULES:
1. **Build count**: `expected_build_steps` = 1 + number_of_bullets. Build 0 shows title (and figure/video if present), then one build per bullet.
2. **One bullet per build**: After build 0, each build reveals exactly ONE bullet. `bullets[0]` in build 1, `bullets[1]` in build 2, etc.
3. **Build 0**: Always shows `title` (and `figure`/`video` if present). Never shows bullets in build 0.
4. **Audio segments**: Split the `audio_content` from the draft into segments. Each build's `audio_segment` must be non-empty and correspond to what that build reveals.
5. **Bullet ordering**: Assign bullets to builds in the order that creates the best storytelling flow for the audience.
6. **time_offset_sec**: Space evenly across the total time. For N builds over T seconds: offsets at 0, T/N, 2T/N, etc.
7. **visual_emphasis**: Always set to empty list `[]`.
8. **Action targets**: Only use targets that exist in `elements`: `title`, `figure`, `video`, `bullets[0]`, `bullets[1]`, etc.
9. **elements**: Copy the drafted title, figure, video, and bullets exactly — do not modify the text content.
10. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""```json
{
  "style": "Slides",
  "expected_build_steps": 4,
  "elements": {
    "title": "FHE-friendly Architecture Redesign",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 4",
      "caption": "Parallel adapter integration with transformer blocks"
    },
    "bullets": [
      "Approximates Softmax, GELU, and LayerNorm using low-degree polynomial operations",
      "Uses Taylor series for exponentials and Goldschmidt’s algorithm for division",
      "Parallel adapters enable local training without backpropagation through the backbone"
    ]
  },
  "builds": [
    {
      "step_index": 0,
      "time_offset_sec": 0.0,
      "actions": [
        {
          "type": "show",
          "target": "title"
        },
        {
          "type": "show",
          "target": "figure"
        }
      ],
      "audio_segment": "BlindFed replaces non-linearities like Softmax and LayerNorm with polynomial approximations",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 4.6,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[0]"
        }
      ],
      "audio_segment": "using Taylor series and Goldschmidt’s algorithm.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 9.2,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[1]"
        }
      ],
      "audio_segment": "A key innovation is the parallel adapter design shown here.",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 13.8,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[2]"
        }
      ],
      "audio_segment": "This structure allows clients to update the model using intermediate representations received from the server, completely bypassing the need for backpropagation through the massive, encrypted backbone.",
      "visual_emphasis": []
    }
  ]
}
```"""

Token usage so far: 169796 prompt tokens, 6525 completion tokens

Cost so far: $1.89371

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 4,
  "title": "Two-stage Split Learning Approach",
  "summary": "The framework employs a two-stage process: first, offline knowledge distillation on auxiliary data to pre-train FHE-friendly blocks; second, online encrypted inference where clients train local adapters without backpropagating through the main FM.",
  "paper_section": "Two-stage Split Learning",
  "narrative_role": "method",
  "asset_video": null,
  "duration_stat": {
    "min": 12.0,
    "max": 18.0,
    "avg": 15.0
  }
}

## Previous Scenes Memory
The following content was extracted for the immediately preceding scenes. **This is provided as a memory of what the audience has JUST seen.**
You MUST NOT repeat the claims, figures, tables, or equations from these previous scenes in your current extraction, to ensure the presentation maintains forward momentum without redundant slides.
If you must reference the exactly same figure/table, the 'relevance' MUST be clearly unique to avoid narrative duplication.

{
  "extracted_content": "BlindFed addresses the double-blind adaptation challenge through three core innovations. First, the original FM is redesigned into an FHE-friendly architecture by replacing non-linear operations (GELU, Softmax, LayerNorm) with low-degree polynomial approximations, such as a quadratic function for GELU. Second, a two-stage split learning approach is used: an offline stage where the server distills knowledge from the original FM into the FHE-friendly version using auxiliary data, and an online stage where clients perform encrypted inference block-by-block. This allows clients to train local parallel adapters and classification heads in plaintext without backpropagating through the FM backbone. Third, the framework incorporates privacy-boosting schemes like sample-level permutation and Stochastic Block Sampling (SBS) to mitigate model extraction attacks by randomizing sample order and hiding a subset of block outputs during training.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "Overview of the proposed BlindFed framework for double-blind federated adaptation.",
      "relevance": "Provides a high-level workflow of the three main components: architecture redesign, offline distillation, and online adaptation."
    },
    {
      "ref": "Figure 3",
      "caption": "FHE-friendly architecture redesign.",
      "relevance": "Illustrates the specific polynomial replacements for non-linear operations (e.g., Quad for GELU) and the placement of the parallel adapter."
    },
    {
      "ref": "Figure 5",
      "caption": "Stochastic block sampling strategy.",
      "relevance": "Visualizes the probabilistic approach used to hide intermediate block outputs from clients to boost model privacy."
    }
  ],
  "key_tables": [],
  "key_equations": [
    {
      "ref": "Equation 4",
      "content": "GELU(x) \u2248 Quad(x) = 0.125x^2 + 0.25x + 0.5",
      "relevance": "Shows the specific quadratic approximation used to make the GELU activation function compatible with FHE."
    },
    {
      "ref": "Equation 7",
      "content": "g_l(z) = \u03b1 W^u_l GELU(W^d_l z)",
      "relevance": "Defines the low-rank parallel adapter function used for local client-side training."
    }
  ]
}
{
  "extracted_content": "The FHE-friendly architecture redesign transforms the original Foundation Model (FM) into a sequence of blocks $\\hat{B}_{\\hat{\\psi}_\\ell}$ that only utilize polynomial operations, as required by homomorphic encryption schemes like CKKS. The redesign focuses on three primary non-linearities: Softmax, GELU, and LayerNorm. Softmax is approximated by applying a Taylor series expansion to the exponential function, while the division operations necessary for both Softmax normalization and LayerNorm are implemented via Goldschmidt\u2019s algorithm, which replaces direct division with iterative multiplications. The final adapted model is structured as a composition $\\mathcal{M}_\\psi = (\\hat{\\mathcal{M}}_{\\hat{\\psi}} \\parallel A_\theta) \\circ H_\\eta$, where the approximated FM backbone runs in parallel with a lightweight adapter. This parallel configuration is a critical design choice; unlike sequential adapters (e.g., LoRA), it enables the client to perform local updates on the adapter and classification head using intermediate representations received from the server, completely bypassing the need for backpropagation through the massive, encrypted FM backbone.",
  "key_figures": [
    {
      "ref": "Figure 4",
      "caption": "Illustration of the parallel adapter design.",
      "relevance": "This figure details how the parallel adapters ($g_1$ through $g_L$) are integrated with the transformer blocks, allowing for client-side training without backpropagating through the main model."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 5",
      "caption": "Softmax approximation results.",
      "relevance": "Demonstrates the trade-off between the polynomial degree ($d$) used in the Taylor approximation and the resulting model accuracy and computational latency."
    }
  ],
  "key_equations": [
    {
      "ref": "Equation 3",
      "content": "e^x = \\sum_{i=0}^{\\infty} \frac{x^i}{i!} \\approx \\sum_{i=0}^{d} \frac{x^i}{i!}",
      "relevance": "The Taylor series approximation used to replace the exponential function in Softmax to make it FHE-compatible."
    },
    {
      "ref": "Equation 5",
      "content": "\frac{1}{x} = \frac{1}{1-(1-x)} = \\prod_{i=0}^{\\infty} (1 + (1-x)^{2^i}) \\approx \\prod_{i=0}^{d} (1 + (1-x)^{2^i})",
      "relevance": "Goldschmidt\u2019s algorithm for approximating the inverse function, which is essential for performing division in LayerNorm and Softmax under FHE."
    }
  ]
}


Read the paper carefully and extract ALL relevant content from the section(s) referenced in this scene.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "extracted_content": "A comprehensive summary of the key information from this section. Include main claims, methods, results, or insights. This should contain enough detail for someone to write presentation bullets from it.",
  "key_figures": [
    {
      "ref": "Figure X",
      "caption": "The actual caption from the paper",
      "relevance": "Why this figure matters for this scene"
    }
  ],
  "key_tables": [
    {
      "ref": "Table X",
      "caption": "The actual caption from the paper",
      "relevance": "Why this table matters for this scene"
    }
  ],
  "key_equations": [
    {
      "ref": "Equation X or description",
      "content": "The equation in text form",
      "relevance": "Why this equation matters for this scene"
    }
  ],
  "section_refs": ["Section 3.1", "Section 3.2"]
}

## STRICT RULES:
1. **Only reference figures/tables that actually appear in the paper section.** Do NOT invent or guess figure/table numbers.
2. **key_figures** must list figures by their exact label in the paper (e.g., "Figure 1", "Fig. 2").
3. If no figures/tables/equations are relevant, use empty lists `[]`.
4. **extracted_content** must be detailed enough to create 2-4 meaningful bullet points from it.
5. **Memory Context**: The `Previous Scenes Memory` (if provided) shows what was ALREADY covered. You MUST NOT repeat its text content, claims, figures, tables, or equations. CRITICAL: Even if you MUST reference the same figure/table, the text content (`extracted_content`) and `relevance` MUST still be completely DIFFERENT.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "extracted_content": "The BlindFed framework utilizes a two-stage split learning strategy to bridge the gap between the original Foundation Model (FM) and its FHE-friendly counterpart. In the first stage, Offline Distillation, the server acts as a teacher to train the approximated student model using an auxiliary dataset. This process is split into two phases: first, aligning embeddings, attention matrices, and hidden states; and second, distilling the final prediction layer. In the second stage, Online Adaptation, a block-by-block interactive protocol is used to perform encrypted inference. Because FHE has limited multiplicative depth, the server processes one transformer block at a time, sending the encrypted output to the client for decryption and re-encryption before proceeding. This interaction provides clients with the plaintext intermediate representations necessary to train their local parallel adapters and classification heads. Finally, secure multi-party computation (MPC) is used for secure aggregation, allowing the server to compute the average of client updates without accessing individual local parameters.",
  "key_figures": [
    {
      "ref": "Figure 9",
      "caption": "Schematic illustration of the layer-wise knowledge distillation (Equations 17 and 18).",
      "relevance": "Visualizes the teacher-student distillation process used in the offline stage to align the FHE-friendly student model's attention matrices and hidden representations with the original FM."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 7",
      "caption": "Computational and memory overhead for encrypted inference and encryption using FHE with the Tile Tensors framework.",
      "relevance": "Quantifies the practical costs of the online adaptation stage, showing the time and memory required for encryption, decryption, and encrypted inference per transformer block."
    }
  ],
  "key_equations": [
    {
      "ref": "Equation 21",
      "content": "\\mathcal{L} = \\begin{cases} \\mathcal{L}_a + \\mathcal{L}_h & \\triangleright \\text{Stage I}, \\\\ \\mathcal{L}_p & \\triangleright \\text{Stage II}. \\end{cases}",
      "relevance": "Defines the two-stage loss objective for the distillation process, where Stage I focuses on internal layer alignment and Stage II focuses on logit-based prediction alignment."
    }
  ],
  "section_refs": [
    "Section 4.2",
    "Section 4.2.1",
    "Section 4.2.2",
    "Section 4.2.3",
    "Appendix C"
  ]
}"""

Token usage so far: 181619 prompt tokens, 7102 completion tokens

Cost so far: $2.02925

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "The BlindFed framework utilizes a two-stage split learning strategy to bridge the gap between the original Foundation Model (FM) and its FHE-friendly counterpart. In the first stage, Offline Distillation, the server acts as a teacher to train the approximated student model using an auxiliary dataset. This process is split into two phases: first, aligning embeddings, attention matrices, and hidden states; and second, distilling the final prediction layer. In the second stage, Online Adaptation, a block-by-block interactive protocol is used to perform encrypted inference. Because FHE has limited multiplicative depth, the server processes one transformer block at a time, sending the encrypted output to the client for decryption and re-encryption before proceeding. This interaction provides clients with the plaintext intermediate representations necessary to train their local parallel adapters and classification heads. Finally, secure multi-party computation (MPC) is used for secure aggregation, allowing the server to compute the average of client updates without accessing individual local parameters.",
  "key_figures": [
    {
      "ref": "Figure 9",
      "caption": "Schematic illustration of the layer-wise knowledge distillation (Equations 17 and 18).",
      "relevance": "Visualizes the teacher-student distillation process used in the offline stage to align the FHE-friendly student model's attention matrices and hidden representations with the original FM."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 7",
      "caption": "Computational and memory overhead for encrypted inference and encryption using FHE with the Tile Tensors framework.",
      "relevance": "Quantifies the practical costs of the online adaptation stage, showing the time and memory required for encryption, decryption, and encrypted inference per transformer block."
    }
  ],
  "key_equations": [
    {
      "ref": "Equation 21",
      "content": "\\mathcal{L} = \begin{cases} \\mathcal{L}_a + \\mathcal{L}_h & \triangleright \text{Stage I}, \\ \\mathcal{L}_p & \triangleright \text{Stage II}. \\end{cases}",
      "relevance": "Defines the two-stage loss objective for the distillation process, where Stage I focuses on internal layer alignment and Stage II focuses on logit-based prediction alignment."
    }
  ],
  "section_refs": [
    "Section 4.2",
    "Section 4.2.1",
    "Section 4.2.2",
    "Section 4.2.3",
    "Appendix C"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 4,
  "title": "Two-stage Split Learning Approach",
  "summary": "The framework employs a two-stage process: first, offline knowledge distillation on auxiliary data to pre-train FHE-friendly blocks; second, online encrypted inference where clients train local adapters without backpropagating through the main FM.",
  "paper_section": "Two-stage Split Learning",
  "narrative_role": "method",
  "asset_video": null,
  "duration_stat": {
    "min": 12.0,
    "max": 18.0,
    "avg": 15.0
  }
}

Reference style advice:
Reference Layouts for 'method' section from similar papers:
- Example 1: The slide follows a clean, single-column layout on a white background. At the top-left, there is a large, bold title in a dark blue serif font. Below the title, a single sentence of introductory text spans the width of the slide. The middle section is dominated by a centered block of mathematical equations defining the 'SoFt Attention (SoFA)' method. Directly beneath the equations are two small, side-by-side grid diagrams (4x4 squares) labeled as 'W_causal' and 'W_bidirect', which use blue, orange, and grey colors to represent different attention mask patterns. The bottom third of the slide contains a brief explanatory sentence about the parameter sigma, followed by two bullet points that detail the trade-offs of its value. The text density is moderate, with a clear hierarchical flow from the general concept to mathematical formulation and then to specific parameter analysis.
- Example 2: The slide follows a top-down structure starting with a large, bold serif title in the top-left corner. Below the title is a single sentence of introductory text. The middle section features two side-by-side visual elements: a detailed architectural diagram on the left showing the components of a Vision-Language Model (Vision Encoder, Projection W, and Language Model) with mathematical notations, and a 'Causal Mask' grid on the right illustrating token interactions. Underneath these diagrams, a paragraph of text introduces the concept of unidirectional information flow, which is further elaborated by two bullet points at the bottom. Small, numbered citations are placed in the bottom-left footer. The slide uses a clean white background with a professional color palette of light blue, orange, and green for the diagram components.
- Example 3: The slide uses a two-column layout with a large, black title 'Related Works' positioned at the top-left. The left column is dedicated to text, featuring hierarchical bullet points that contrast prior methods with the current work's contributions. Specific technical terms are emphasized using red and green text. A right-pointing arrow highlights a limitation of previous work. The right column contains two distinct visual blocks. The upper block shows three diagrams labeled (a), (b), and (c) under the heading 'SCNeRF (ICCV21)', illustrating camera calibration. The lower, larger block is labeled 'NoPe-NeRF (CVPR2024)' and includes a 'Key Components' section with 3D point clouds and images, a 'Training Pipeline' flowchart with color-coded arrows, and a detailed 'Legend' box on the right side. The slide has a moderate text density and a clean white background.
- Example 4: The slide features a clean, minimalist design divided into two horizontal sections. The top half is a solid teal-colored banner containing the title 'Method' in a large, white, sans-serif font, centered both horizontally and vertically within the colored block. The bottom half of the slide has a plain white background. A single sentence of black text, 'We propose three novel components to the geometry-alignment pipeline.', is positioned near the top of this white section, left-aligned. In the bottom-left corner, there is small grey text identifying 'Australia's National Science Agency'. The bottom-right corner contains two institutional logos: the Australian National University crest and text, and the CSIRO circular logo. The overall text density is very light, serving as an introductory slide for the methodology section.
- Example 5: The slide uses a minimalist design with a solid black background. A single line of white, sans-serif text is centered at the top, serving as a descriptive title or caption. Below this text, a large photographic image spans the width of the slide, showing a street-level view of a residential road lined with trees and fences under a clear sky. A prominent horizontal dashed white line is overlaid across the lower third of the image. Scattered throughout the scene, particularly concentrated along this dashed line and trailing into the distance, are glowing purple and blue light effects that represent the 'query pixels' mentioned in the title. The overall text density is light, prioritizing the visual demonstration over textual information.

Duration statistics for this section (from references): min=1.0s, max=83.2s, avg=19.5s.

Your job is to decide the **visual layout** for this slide. Do NOT decide builds or animations — those will be planned later.

## CHOOSE THE BEST LAYOUT

Pick the layout template that best suits the content. Common templates include (but you are NOT limited to these):
- `two_col_fig_left` — Figure on left, bullets on right. Best for: method diagrams, architecture figures, or tall/vertical figures.
- `two_col_fig_right` — Bullets on left, figure on right. Best for: motivation slides with illustrative or tall/vertical figures.
- `full_fig_with_callouts` — Large figure with small bullet callouts below. Best for: results, data visualizations, or wide/horizontal figures.
- `one_col_bullets` — Full-width bullets, no figure. Best for: text-heavy overview or summary slides.
- `video_with_caption` — Large video region with small bullet callouts below. Best for: when an `asset_video` is provided.

If none of these fit, invent a descriptive template name and define its regions.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "video": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "bullets": {"x": 0.55, "y": 0.25, "w": 0.4, "h": 0.6}
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "Two-column layout with figure on left is ideal for showing the architecture diagram alongside explanatory bullets."
}

## STRICT RULES:
1. **Region keys**: Only use `title`, `bullets`, `figure`, `video` as region keys. Do NOT invent keys like `callout_1`, `table`, etc.
2. **Coordinates**: All x/y/w/h values must be normalized (0.0 to 1.0). Regions must not overlap.
3. **has_figure**: Set to `true` only if the content summary has relevant figures. If no figure is available, omit `figure` from regions.
4. **has_video**: Set to `true` only if `scene_context` specifically assigns an `asset_video`. If true, include the `video` region. Do not include both `figure` and `video` unless space permits.
5. **No builds**: Do NOT include `build_skeleton`, `expected_build_steps`, or any animation information.
6. Output ONLY valid JSON, no markdown fences, no explanation.

IMPORTANT FIGURE ASPECT RATIO RULE:
If the extracted figure is nearly square, its placement is flexible. However, if the figure has a much larger dimension horizontally (like a wide rectangle), choose a layout with a wide figure region (e.g., `full_fig_with_callouts` or placing it spanning top/bottom) so it is not shrunk awkwardly. If it is very tall/vertical, choose a side-by-side template (e.g., `two_col_fig_left`) where it has vertical space. Ensure your chosen template and `layout_regions` coordinates are decided accordingly to preserve the figure's aspect ratio without shrinking it.


**Answer (from GEMINI)**

"""{
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "figure": {
      "x": 0.05,
      "y": 0.18,
      "w": 0.45,
      "h": 0.75
    },
    "bullets": {
      "x": 0.55,
      "y": 0.18,
      "w": 0.4,
      "h": 0.75
    }
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "The vertical orientation of Figure 9, which illustrates the layer-wise distillation process between teacher and student models, is best served by a two-column layout. Placing the figure on the left provides a strong visual anchor for the methodology, while the right column provides space for the two-stage explanation and the piecewise loss equation (Eq. 21)."
}"""

Token usage so far: 194024 prompt tokens, 7393 completion tokens

Cost so far: $2.16203

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "The BlindFed framework utilizes a two-stage split learning strategy to bridge the gap between the original Foundation Model (FM) and its FHE-friendly counterpart. In the first stage, Offline Distillation, the server acts as a teacher to train the approximated student model using an auxiliary dataset. This process is split into two phases: first, aligning embeddings, attention matrices, and hidden states; and second, distilling the final prediction layer. In the second stage, Online Adaptation, a block-by-block interactive protocol is used to perform encrypted inference. Because FHE has limited multiplicative depth, the server processes one transformer block at a time, sending the encrypted output to the client for decryption and re-encryption before proceeding. This interaction provides clients with the plaintext intermediate representations necessary to train their local parallel adapters and classification heads. Finally, secure multi-party computation (MPC) is used for secure aggregation, allowing the server to compute the average of client updates without accessing individual local parameters.",
  "key_figures": [
    {
      "ref": "Figure 9",
      "caption": "Schematic illustration of the layer-wise knowledge distillation (Equations 17 and 18).",
      "relevance": "Visualizes the teacher-student distillation process used in the offline stage to align the FHE-friendly student model's attention matrices and hidden representations with the original FM."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 7",
      "caption": "Computational and memory overhead for encrypted inference and encryption using FHE with the Tile Tensors framework.",
      "relevance": "Quantifies the practical costs of the online adaptation stage, showing the time and memory required for encryption, decryption, and encrypted inference per transformer block."
    }
  ],
  "key_equations": [
    {
      "ref": "Equation 21",
      "content": "\\mathcal{L} = \begin{cases} \\mathcal{L}_a + \\mathcal{L}_h & \triangleright \text{Stage I}, \\ \\mathcal{L}_p & \triangleright \text{Stage II}. \\end{cases}",
      "relevance": "Defines the two-stage loss objective for the distillation process, where Stage I focuses on internal layer alignment and Stage II focuses on logit-based prediction alignment."
    }
  ],
  "section_refs": [
    "Section 4.2",
    "Section 4.2.1",
    "Section 4.2.2",
    "Section 4.2.3",
    "Appendix C"
  ]
}

The layout has been decided:
{
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "figure": {
      "x": 0.05,
      "y": 0.18,
      "w": 0.45,
      "h": 0.75
    },
    "bullets": {
      "x": 0.55,
      "y": 0.18,
      "w": 0.4,
      "h": 0.75
    }
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "The vertical orientation of Figure 9, which illustrates the layer-wise distillation process between teacher and student models, is best served by a two-column layout. Placing the figure on the left provides a strong visual anchor for the methodology, while the right column provides space for the two-stage explanation and the piecewise loss equation (Eq. 21)."
}

Scene context:
{
  "scene_id": 4,
  "title": "Two-stage Split Learning Approach",
  "summary": "The framework employs a two-stage process: first, offline knowledge distillation on auxiliary data to pre-train FHE-friendly blocks; second, online encrypted inference where clients train local adapters without backpropagating through the main FM.",
  "paper_section": "Two-stage Split Learning",
  "narrative_role": "method",
  "asset_video": null,
  "duration_stat": {
    "min": 12.0,
    "max": 18.0,
    "avg": 15.0
  }
}

## Previous Content
The following content was drafted for the immediately preceding scenes.
You MUST NOT repeat the exact text content or claims from these previous scenes in your current draft.

{
  "bullets": [
    "Approximates Softmax, GELU, and LayerNorm using low-degree polynomial operations",
    "Uses Taylor series for exponentials and Goldschmidt\u2019s algorithm for division",
    "Parallel adapters enable local training without backpropagation through the backbone"
  ],
  "audio_content": "BlindFed replaces non-linearities like Softmax and LayerNorm with polynomial approximations using Taylor series and Goldschmidt\u2019s algorithm. A key innovation is the parallel adapter design shown here. This structure allows clients to update the model using intermediate representations received from the server, completely bypassing the need for backpropagation through the massive, encrypted backbone."
}


Your job is to **draft the actual content** (title, bullets, audio, figure choice, and duration) that fits into this layout. You do NOT decide the layout — that is already set. You also do NOT decide builds or animations — those will be planned later based on your drafted content.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "title": "A clear, concise slide title",
  "audio_content": "Full narration transcript for this entire scene. Should be natural, conversational, and cover all key points. The duration should be based on the length of this transcript.",
  "duration_sec": 8.5,
  "bullets": [
    "First concise bullet point",
    "Second concise bullet point",
    "Third concise bullet point"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure X",
    "caption": "Brief caption describing the figure"
  },
  "video": {
    "type": "asset_video",
    "path": "clip1.mp4",
    "caption": "Brief caption describing the video contents"
  },
  "source": ["Figure 1", "Section 3.1"],
  "prompt": "Visual description of the scene for generation"
}

## STRICT RULES:
1. **Number of bullets**: Write 2-4 concise, impactful bullets that cover the key points from the extracted content.
2. **Figure/Video assignment**: 
   - Assign `figure` ONLY if the content summary's `key_figures` has relevant images. 
   - Assign `video` ONLY if the `scene_context` assigns an `asset_video`.
   - If the style plan omits `has_figure` or `has_video`, omit the respective block completely.
3. **Bullet text**: Each bullet should be concise (under 15 words preferred), impactful, and directly derived from `extracted_content`. Not a copy — a focused summary.
4. **audio_content**: Natural narration covering all bullet points AND the video clip action if a video is present. 
5. **duration_sec**: First, draft the `audio_content`. Then, CALCULATE the duration: `duration_sec = word_count_of_audio / 2.5`. Do NOT guess. If the stats say 8s but you wrote 40 words, `duration_sec` MUST be 16.0.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "title": "Two-Stage Split Learning Strategy",
  "audio_content": "BlindFed uses a two-stage strategy to bridge the gap between models. First, offline distillation aligns the FHE-friendly student with the original teacher using auxiliary data. Then, online adaptation uses block-by-block encrypted inference for private local training. Finally, secure multi-party computation aggregates updates into a global model without exposing individual parameters.",
  "duration_sec": 18.4,
  "bullets": [
    "Offline distillation aligns FHE-friendly blocks with the original foundation model",
    "Online adaptation enables private local training via block-by-block encrypted inference",
    "Secure aggregation via MPC combines client updates without exposing local parameters"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 9",
    "caption": "Layer-wise knowledge distillation between teacher and student models"
  },
  "source": [
    "Section 4.2",
    "Figure 9",
    "Equation 21"
  ],
  "prompt": "A diagram showing a two-stage process: Stage 1 (Offline) shows a teacher model transferring knowledge to a student model via layer-wise distillation; Stage 2 (Online) shows a server and client interacting block-by-block with encrypted data to train local adapters."
}"""

Token usage so far: 205717 prompt tokens, 7699 completion tokens

Cost so far: $2.28814

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "Two-Stage Split Learning Strategy",
  "audio_content": "BlindFed uses a two-stage strategy to bridge the gap between models. First, offline distillation aligns the FHE-friendly student with the original teacher using auxiliary data. Then, online adaptation uses block-by-block encrypted inference for private local training. Finally, secure multi-party computation aggregates updates into a global model without exposing individual parameters.",
  "duration_sec": 18.4,
  "bullets": [
    "Offline distillation aligns FHE-friendly blocks with the original foundation model",
    "Online adaptation enables private local training via block-by-block encrypted inference",
    "Secure aggregation via MPC combines client updates without exposing local parameters"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 9",
    "caption": "Layer-wise knowledge distillation between teacher and student models"
  },
  "source": [
    "Section 4.2",
    "Figure 9",
    "Equation 21"
  ],
  "prompt": "A diagram showing a two-stage process: Stage 1 (Offline) shows a teacher model transferring knowledge to a student model via layer-wise distillation; Stage 2 (Online) shows a server and client interacting block-by-block with encrypted data to train local adapters."
}

Layout information:
{
  "layout_template": "two_col_fig_left",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "figure": {
      "x": 0.05,
      "y": 0.18,
      "w": 0.45,
      "h": 0.75
    },
    "bullets": {
      "x": 0.55,
      "y": 0.18,
      "w": 0.4,
      "h": 0.75
    }
  },
  "has_figure": true,
  "total_time_sec": 18.4
}

Your job is to:
1. **Decide the build plan** — how many build steps, and what gets revealed in each step.
2. **Assign the drafted bullets to specific build steps** in the best storytelling order.
3. **Split the audio into per-build segments** so each build has matching narration.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "style": "Slides",
  "expected_build_steps": 3,
  "elements": {
    "title": "The slide title from the draft",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure X",
      "caption": "Caption from draft"
    },
    "bullets": [
      "First bullet",
      "Second bullet"
    ]
  },
  "builds": [
    {
      "step_index": 0,
      "time_offset_sec": 0.0,
      "actions": [
        {"type": "show", "target": "title"},
        {"type": "show", "target": "figure"}
      ],
      "audio_segment": "Opening narration for this build step.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 3.0,
      "actions": [
        {"type": "fade_in", "target": "bullets[0]"}
      ],
      "audio_segment": "Narration for the first bullet point.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 6.0,
      "actions": [
        {"type": "fade_in", "target": "bullets[1]"}
      ],
      "audio_segment": "Narration for the second bullet point.",
      "visual_emphasis": []
    }
  ]
}

## STRICT RULES:
1. **Build count**: `expected_build_steps` = 1 + number_of_bullets. Build 0 shows title (and figure/video if present), then one build per bullet.
2. **One bullet per build**: After build 0, each build reveals exactly ONE bullet. `bullets[0]` in build 1, `bullets[1]` in build 2, etc.
3. **Build 0**: Always shows `title` (and `figure`/`video` if present). Never shows bullets in build 0.
4. **Audio segments**: Split the `audio_content` from the draft into segments. Each build's `audio_segment` must be non-empty and correspond to what that build reveals.
5. **Bullet ordering**: Assign bullets to builds in the order that creates the best storytelling flow for the audience.
6. **time_offset_sec**: Space evenly across the total time. For N builds over T seconds: offsets at 0, T/N, 2T/N, etc.
7. **visual_emphasis**: Always set to empty list `[]`.
8. **Action targets**: Only use targets that exist in `elements`: `title`, `figure`, `video`, `bullets[0]`, `bullets[1]`, etc.
9. **elements**: Copy the drafted title, figure, video, and bullets exactly — do not modify the text content.
10. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "style": "Slides",
  "expected_build_steps": 4,
  "elements": {
    "title": "Two-Stage Split Learning Strategy",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 9",
      "caption": "Layer-wise knowledge distillation between teacher and student models"
    },
    "bullets": [
      "Offline distillation aligns FHE-friendly blocks with the original foundation model",
      "Online adaptation enables private local training via block-by-block encrypted inference",
      "Secure aggregation via MPC combines client updates without exposing local parameters"
    ]
  },
  "builds": [
    {
      "step_index": 0,
      "time_offset_sec": 0.0,
      "actions": [
        {
          "type": "show",
          "target": "title"
        },
        {
          "type": "show",
          "target": "figure"
        }
      ],
      "audio_segment": "BlindFed uses a two-stage strategy to bridge the gap between models.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 4.6,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[0]"
        }
      ],
      "audio_segment": "First, offline distillation aligns the FHE-friendly student with the original teacher using auxiliary data.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 9.2,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[1]"
        }
      ],
      "audio_segment": "Then, online adaptation uses block-by-block encrypted inference for private local training.",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 13.8,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[2]"
        }
      ],
      "audio_segment": "Finally, secure multi-party computation aggregates updates into a global model without exposing individual parameters.",
      "visual_emphasis": []
    }
  ]
}"""

Token usage so far: 216915 prompt tokens, 8271 completion tokens

Cost so far: $2.41728

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 5,
  "title": "Privacy-Boosting Mechanisms",
  "summary": "To mitigate model extraction attacks, BlindFed introduces sample-level permutations and stochastic block sampling (SBS). These ensure that clients only see a subset of permuted intermediate representations, preventing them from reconstructing the FM parameters.",
  "paper_section": "Model Privacy Boosting",
  "narrative_role": "method",
  "asset_video": null,
  "duration_stat": {
    "min": 10.0,
    "max": 15.0,
    "avg": 13.0
  }
}

## Previous Scenes Memory
The following content was extracted for the immediately preceding scenes. **This is provided as a memory of what the audience has JUST seen.**
You MUST NOT repeat the claims, figures, tables, or equations from these previous scenes in your current extraction, to ensure the presentation maintains forward momentum without redundant slides.
If you must reference the exactly same figure/table, the 'relevance' MUST be clearly unique to avoid narrative duplication.

{
  "extracted_content": "The FHE-friendly architecture redesign transforms the original Foundation Model (FM) into a sequence of blocks $\\hat{B}_{\\hat{\\psi}_\\ell}$ that only utilize polynomial operations, as required by homomorphic encryption schemes like CKKS. The redesign focuses on three primary non-linearities: Softmax, GELU, and LayerNorm. Softmax is approximated by applying a Taylor series expansion to the exponential function, while the division operations necessary for both Softmax normalization and LayerNorm are implemented via Goldschmidt\u2019s algorithm, which replaces direct division with iterative multiplications. The final adapted model is structured as a composition $\\mathcal{M}_\\psi = (\\hat{\\mathcal{M}}_{\\hat{\\psi}} \\parallel A_\theta) \\circ H_\\eta$, where the approximated FM backbone runs in parallel with a lightweight adapter. This parallel configuration is a critical design choice; unlike sequential adapters (e.g., LoRA), it enables the client to perform local updates on the adapter and classification head using intermediate representations received from the server, completely bypassing the need for backpropagation through the massive, encrypted FM backbone.",
  "key_figures": [
    {
      "ref": "Figure 4",
      "caption": "Illustration of the parallel adapter design.",
      "relevance": "This figure details how the parallel adapters ($g_1$ through $g_L$) are integrated with the transformer blocks, allowing for client-side training without backpropagating through the main model."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 5",
      "caption": "Softmax approximation results.",
      "relevance": "Demonstrates the trade-off between the polynomial degree ($d$) used in the Taylor approximation and the resulting model accuracy and computational latency."
    }
  ],
  "key_equations": [
    {
      "ref": "Equation 3",
      "content": "e^x = \\sum_{i=0}^{\\infty} \frac{x^i}{i!} \\approx \\sum_{i=0}^{d} \frac{x^i}{i!}",
      "relevance": "The Taylor series approximation used to replace the exponential function in Softmax to make it FHE-compatible."
    },
    {
      "ref": "Equation 5",
      "content": "\frac{1}{x} = \frac{1}{1-(1-x)} = \\prod_{i=0}^{\\infty} (1 + (1-x)^{2^i}) \\approx \\prod_{i=0}^{d} (1 + (1-x)^{2^i})",
      "relevance": "Goldschmidt\u2019s algorithm for approximating the inverse function, which is essential for performing division in LayerNorm and Softmax under FHE."
    }
  ]
}
{
  "extracted_content": "The BlindFed framework utilizes a two-stage split learning strategy to bridge the gap between the original Foundation Model (FM) and its FHE-friendly counterpart. In the first stage, Offline Distillation, the server acts as a teacher to train the approximated student model using an auxiliary dataset. This process is split into two phases: first, aligning embeddings, attention matrices, and hidden states; and second, distilling the final prediction layer. In the second stage, Online Adaptation, a block-by-block interactive protocol is used to perform encrypted inference. Because FHE has limited multiplicative depth, the server processes one transformer block at a time, sending the encrypted output to the client for decryption and re-encryption before proceeding. This interaction provides clients with the plaintext intermediate representations necessary to train their local parallel adapters and classification heads. Finally, secure multi-party computation (MPC) is used for secure aggregation, allowing the server to compute the average of client updates without accessing individual local parameters.",
  "key_figures": [
    {
      "ref": "Figure 9",
      "caption": "Schematic illustration of the layer-wise knowledge distillation (Equations 17 and 18).",
      "relevance": "Visualizes the teacher-student distillation process used in the offline stage to align the FHE-friendly student model's attention matrices and hidden representations with the original FM."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 7",
      "caption": "Computational and memory overhead for encrypted inference and encryption using FHE with the Tile Tensors framework.",
      "relevance": "Quantifies the practical costs of the online adaptation stage, showing the time and memory required for encryption, decryption, and encrypted inference per transformer block."
    }
  ],
  "key_equations": [
    {
      "ref": "Equation 21",
      "content": "\\mathcal{L} = \begin{cases} \\mathcal{L}_a + \\mathcal{L}_h & \triangleright \text{Stage I}, \\ \\mathcal{L}_p & \triangleright \text{Stage II}. \\end{cases}",
      "relevance": "Defines the two-stage loss objective for the distillation process, where Stage I focuses on internal layer alignment and Stage II focuses on logit-based prediction alignment."
    }
  ]
}


Read the paper carefully and extract ALL relevant content from the section(s) referenced in this scene.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "extracted_content": "A comprehensive summary of the key information from this section. Include main claims, methods, results, or insights. This should contain enough detail for someone to write presentation bullets from it.",
  "key_figures": [
    {
      "ref": "Figure X",
      "caption": "The actual caption from the paper",
      "relevance": "Why this figure matters for this scene"
    }
  ],
  "key_tables": [
    {
      "ref": "Table X",
      "caption": "The actual caption from the paper",
      "relevance": "Why this table matters for this scene"
    }
  ],
  "key_equations": [
    {
      "ref": "Equation X or description",
      "content": "The equation in text form",
      "relevance": "Why this equation matters for this scene"
    }
  ],
  "section_refs": ["Section 3.1", "Section 3.2"]
}

## STRICT RULES:
1. **Only reference figures/tables that actually appear in the paper section.** Do NOT invent or guess figure/table numbers.
2. **key_figures** must list figures by their exact label in the paper (e.g., "Figure 1", "Fig. 2").
3. If no figures/tables/equations are relevant, use empty lists `[]`.
4. **extracted_content** must be detailed enough to create 2-4 meaningful bullet points from it.
5. **Memory Context**: The `Previous Scenes Memory` (if provided) shows what was ALREADY covered. You MUST NOT repeat its text content, claims, figures, tables, or equations. CRITICAL: Even if you MUST reference the same figure/table, the text content (`extracted_content`) and `relevance` MUST still be completely DIFFERENT.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "extracted_content": "BlindFed addresses the risk of model extraction attacks where a malicious client might use pairs of intermediate representations $(b_{\ell-1}, b_\ell)$ to learn the parameters of the transformer blocks. To counter this, the framework implements two primary privacy-boosting mechanisms. First, **Sample-level Permutation** applies a unique random permutation matrix $\Pi_\ell$ to each batch of intermediate representations at every block $\ell$. By only sharing the product of these matrices $(\Pi_{\ell-1}^{-1} \cdot \Pi_\ell)$ with the client, the server ensures that individual sample mappings remain hidden, a property formally supported by Proposition 1. Second, **Stochastic Block Sampling (SBS)** mitigates similarity-based attacks by only revealing a subset of block outputs. Based on a structured probabilistic rule, each block has a stationary probability of $1/3$ of being sampled, resulting in an expected $L/3$ blocks being revealed. This breaks the continuity of the representations, as non-consecutive blocks exhibit significantly lower feature similarity, making it computationally infeasible for clients to reconstruct the full model sequence.",
  "key_figures": [
    {
      "ref": "Figure 5",
      "caption": "Stochastic block sampling strategy.",
      "relevance": "Illustrates the Markov-chain-like transition states (0 for not sampled, 1 for sampled) used to determine which transformer block outputs are revealed to the client."
    },
    {
      "ref": "Figure 6",
      "caption": "Heatmap visualization of the similarity (L2 distance) between corresponding block outputs or hidden representations",
      "relevance": "Demonstrates that consecutive block outputs (e.g., $b_1$ and $b_2$) have high similarity, which could be exploited for model extraction if not for the proposed privacy mechanisms."
    },
    {
      "ref": "Figure 7",
      "caption": "Heatmap visualization of the similarity (L2 distance) between non-consecutive block outputs or hidden representations",
      "relevance": "Shows that non-consecutive blocks (e.g., $b_1$ and $b_3$) have negligible similarity, validating why the SBS strategy effectively thwarts similarity-based attacks."
    }
  ],
  "key_tables": [],
  "key_equations": [
    {
      "ref": "Proposition 1",
      "content": "Let A, B, and C be n \u00d7 n permutation matrices. Given only $A^{-1}B$, $B^{-1}C$, and $C^{-1}A$, it is computationally infeasible to uniquely recover the individual matrices A, B, and C without additional information.",
      "relevance": "Provides the mathematical foundation for the sample-level permutation's security, ensuring that clients cannot reverse-engineer the random permutations applied by the server."
    },
    {
      "ref": "Equation 12",
      "content": "p = 0.5(1 - p)",
      "relevance": "The equilibrium equation used to derive the stationary probability ($p=1/3$) of a block being sampled during the SBS process."
    },
    {
      "ref": "Equation 8",
      "content": "\\mathbf{H}_\\ell = g_\\ell(\\mathbf{B}_\\ell + \\mathbf{H}_{\\ell-1}) + \\mathbf{H}_{\\ell-1}",
      "relevance": "The reformulated adapter computation used when operating on batches of permuted samples to ensure consistent updates despite the random shuffling."
    }
  ],
  "section_refs": [
    "Section 4.3",
    "Section 4.3.1",
    "Section 4.3.2",
    "Appendix A",
    "Appendix B"
  ]
}"""

Token usage so far: 228687 prompt tokens, 9122 completion tokens

Cost so far: $2.56053

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "BlindFed addresses the risk of model extraction attacks where a malicious client might use pairs of intermediate representations $(b_{\\ell-1}, b_\\ell)$ to learn the parameters of the transformer blocks. To counter this, the framework implements two primary privacy-boosting mechanisms. First, **Sample-level Permutation** applies a unique random permutation matrix $\\Pi_\\ell$ to each batch of intermediate representations at every block $\\ell$. By only sharing the product of these matrices $(\\Pi_{\\ell-1}^{-1} \\cdot \\Pi_\\ell)$ with the client, the server ensures that individual sample mappings remain hidden, a property formally supported by Proposition 1. Second, **Stochastic Block Sampling (SBS)** mitigates similarity-based attacks by only revealing a subset of block outputs. Based on a structured probabilistic rule, each block has a stationary probability of $1/3$ of being sampled, resulting in an expected $L/3$ blocks being revealed. This breaks the continuity of the representations, as non-consecutive blocks exhibit significantly lower feature similarity, making it computationally infeasible for clients to reconstruct the full model sequence.",
  "key_figures": [
    {
      "ref": "Figure 5",
      "caption": "Stochastic block sampling strategy.",
      "relevance": "Illustrates the Markov-chain-like transition states (0 for not sampled, 1 for sampled) used to determine which transformer block outputs are revealed to the client."
    },
    {
      "ref": "Figure 6",
      "caption": "Heatmap visualization of the similarity (L2 distance) between corresponding block outputs or hidden representations",
      "relevance": "Demonstrates that consecutive block outputs (e.g., $b_1$ and $b_2$) have high similarity, which could be exploited for model extraction if not for the proposed privacy mechanisms."
    },
    {
      "ref": "Figure 7",
      "caption": "Heatmap visualization of the similarity (L2 distance) between non-consecutive block outputs or hidden representations",
      "relevance": "Shows that non-consecutive blocks (e.g., $b_1$ and $b_3$) have negligible similarity, validating why the SBS strategy effectively thwarts similarity-based attacks."
    }
  ],
  "key_tables": [],
  "key_equations": [
    {
      "ref": "Proposition 1",
      "content": "Let A, B, and C be n \u00d7 n permutation matrices. Given only $A^{-1}B$, $B^{-1}C$, and $C^{-1}A$, it is computationally infeasible to uniquely recover the individual matrices A, B, and C without additional information.",
      "relevance": "Provides the mathematical foundation for the sample-level permutation's security, ensuring that clients cannot reverse-engineer the random permutations applied by the server."
    },
    {
      "ref": "Equation 12",
      "content": "p = 0.5(1 - p)",
      "relevance": "The equilibrium equation used to derive the stationary probability ($p=1/3$) of a block being sampled during the SBS process."
    },
    {
      "ref": "Equation 8",
      "content": "\\mathbf{H}_\\ell = g_\\ell(\\mathbf{B}_\\ell + \\mathbf{H}_{\\ell-1}) + \\mathbf{H}_{\\ell-1}",
      "relevance": "The reformulated adapter computation used when operating on batches of permuted samples to ensure consistent updates despite the random shuffling."
    }
  ],
  "section_refs": [
    "Section 4.3",
    "Section 4.3.1",
    "Section 4.3.2",
    "Appendix A",
    "Appendix B"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 5,
  "title": "Privacy-Boosting Mechanisms",
  "summary": "To mitigate model extraction attacks, BlindFed introduces sample-level permutations and stochastic block sampling (SBS). These ensure that clients only see a subset of permuted intermediate representations, preventing them from reconstructing the FM parameters.",
  "paper_section": "Model Privacy Boosting",
  "narrative_role": "method",
  "asset_video": null,
  "duration_stat": {
    "min": 10.0,
    "max": 15.0,
    "avg": 13.0
  }
}

Reference style advice:
Reference Layouts for 'method' section from similar papers:
- Example 1: The slide features a large, plain-text title 'Overview' positioned at the top-left. The central portion of the slide is dominated by a complex architectural flowchart that illustrates a machine learning pipeline. This diagram flows from left to right, starting with input images (ground and satellite views) that pass through a 'Feature Extractor'. A prominent red-bordered box in the center, labeled 'T2GA', details a feature aggregation mechanism using MLPs and attention. To its right, a 'Baseline Model' box lists several internal components like a 'Keypoint Detector' and 'Pose Optimizer'. The diagram concludes on the far right with three distinct loss function boxes. Below this diagram, a 'Contributions:' section contains three bullet points that are color-coded to match specific elements in the flowchart: 'T2GA' and 'CycDA Loss' are in red, while 'Equidistant Re-projection Loss' is highlighted with a yellow background. The slide uses a clean white background with moderate text density, focusing primarily on the visual representation of the proposed method's architecture.
- Example 2: The slide features a large, complex architectural diagram centered between a top title and a bottom summary text. The title 'DPE Overview' is positioned in a large, bold, dark red font at the top-left, while the 'NEURAL INFORMATION PROCESSING SYSTEMS' logo with its purple dot pattern is at the top-right. The central diagram flows from left to right, starting with input sources on the left: 'Text Descriptions', 'High-Confidence Samples' (images of dogs, cats, and cars), and 'Augmented Test Images'. These inputs pass through frozen encoders, indicated by snowflake icons. The middle section illustrates 'Textual Prototypes' and 'Visual Prototypes' undergoing a 'Prototype Evolving' process with an 'L_align' loss. To the right of the main flow, two separate panels show the 'Textual Prototype Evolution' and 'Visual Prototype Evolution' over time, marked by clock icons. The final stage of the main diagram shows 'Predictions of All Views', 'Confidence Selection', and an 'Average' step leading to final class scores and an 'L_aug' loss. A two-line summary paragraph at the bottom explains the method's use of prototypes and CLIP. The slide has a white background with a page number '3' in the bottom-right corner.
- Example 3: The slide follows a top-to-bottom flow with a large, bold, dark blue title positioned at the top-left. Below the title, the content is organized into two main text blocks followed by a row of figures. The first text block introduces a hypothesis with a heading and two bullet points. The second text block introduces three specific variants with a lead-in sentence followed by three bullet points where the variant names are italicized. At the bottom of the slide, three diagrams are arranged side-by-side to visually represent the 'Causal Mask', 'Isolated Mask', and 'Bidirectional Mask'. Each diagram is a 4x4 grid with light blue labels (I1, T1, I2, T2) on the top and left axes. The grids use orange squares to indicate active attention and light gray squares for masked areas. The names of the masks are centered directly beneath each corresponding grid. The overall design is clean with a white background and moderate text density.
- Example 4: The slide features a large, bold blue title at the top-left. The main body of the slide is dominated by a complex flowchart diagram in the upper half, illustrating the 'Focus-N-Fix' method. This diagram flows from left to right, starting with inputs like 'Prompt' and 'Initial Noise', passing through 'Sample' blocks (LoRA and Pre-Trained Params), and resulting in 'Fine-Tuned' and 'Pre-Trained' clock images. It further branches into 'Reward' and 'Problematic Region' (mask) components, culminating in a 'Fine-Tuning Objective' equation and a 'Regional Constraint' visualization on the right. Solid black arrows indicate the forward path, while dashed red arrows indicate backpropagation. Below the diagram, there are two primary bullet points explaining the traditional fine-tuning objective versus the proposed regional constraint, which includes a mathematical formula. The second bullet point has a nested sub-bullet. At the bottom of the slide, a full-width blue footer bar contains a white summary sentence describing the method's use of a reward model and mask for localized correction. The background is plain white, and the text density is moderate.
- Example 5: The slide uses a two-column layout on a clean white background. A large, black title 'Training Pipeline' is located at the top-left. The left column consists of hierarchical bullet points with two levels of indentation, detailing the 'Early training' and 'Later training' phases, followed by a final note that the system is 'End-to-end trainable'. The right column contains a complex technical flowchart illustrating the data flow and loss functions. At the top of the diagram, a yellow box represents the 'Time-dependent NeRF' model, which branches into 'Surface points', 'Rendered colors', and 'Predicted signed distance'. Below these, small thumbnail images show rendered scenes and depth maps. At the bottom, a blue box for the 'Motion network' processes timesteps to produce camera poses (green boxes) and motion vectors. Red double-headed arrows labeled with mathematical loss symbols (e.g., L_rgb, L_p, L_sdf, L_flow) connect various nodes to indicate optimization objectives. The diagram uses a consistent color-coding scheme: yellow for the NeRF model, green for pose-related elements, and blue for the motion network.

Duration statistics for this section (from references): min=1.0s, max=83.2s, avg=19.5s.

Your job is to decide the **visual layout** for this slide. Do NOT decide builds or animations — those will be planned later.

## CHOOSE THE BEST LAYOUT

Pick the layout template that best suits the content. Common templates include (but you are NOT limited to these):
- `two_col_fig_left` — Figure on left, bullets on right. Best for: method diagrams, architecture figures, or tall/vertical figures.
- `two_col_fig_right` — Bullets on left, figure on right. Best for: motivation slides with illustrative or tall/vertical figures.
- `full_fig_with_callouts` — Large figure with small bullet callouts below. Best for: results, data visualizations, or wide/horizontal figures.
- `one_col_bullets` — Full-width bullets, no figure. Best for: text-heavy overview or summary slides.
- `video_with_caption` — Large video region with small bullet callouts below. Best for: when an `asset_video` is provided.

If none of these fit, invent a descriptive template name and define its regions.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "video": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "bullets": {"x": 0.55, "y": 0.25, "w": 0.4, "h": 0.6}
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "Two-column layout with figure on left is ideal for showing the architecture diagram alongside explanatory bullets."
}

## STRICT RULES:
1. **Region keys**: Only use `title`, `bullets`, `figure`, `video` as region keys. Do NOT invent keys like `callout_1`, `table`, etc.
2. **Coordinates**: All x/y/w/h values must be normalized (0.0 to 1.0). Regions must not overlap.
3. **has_figure**: Set to `true` only if the content summary has relevant figures. If no figure is available, omit `figure` from regions.
4. **has_video**: Set to `true` only if `scene_context` specifically assigns an `asset_video`. If true, include the `video` region. Do not include both `figure` and `video` unless space permits.
5. **No builds**: Do NOT include `build_skeleton`, `expected_build_steps`, or any animation information.
6. Output ONLY valid JSON, no markdown fences, no explanation.

IMPORTANT FIGURE ASPECT RATIO RULE:
If the extracted figure is nearly square, its placement is flexible. However, if the figure has a much larger dimension horizontally (like a wide rectangle), choose a layout with a wide figure region (e.g., `full_fig_with_callouts` or placing it spanning top/bottom) so it is not shrunk awkwardly. If it is very tall/vertical, choose a side-by-side template (e.g., `two_col_fig_left`) where it has vertical space. Ensure your chosen template and `layout_regions` coordinates are decided accordingly to preserve the figure's aspect ratio without shrinking it.


**Answer (from GEMINI)**

"""{
  "layout_template": "two_col_fig_right",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "bullets": {
      "x": 0.05,
      "y": 0.2,
      "w": 0.45,
      "h": 0.7
    },
    "figure": {
      "x": 0.55,
      "y": 0.2,
      "w": 0.4,
      "h": 0.7
    }
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "A two-column layout with bullets on the left and figures on the right is ideal for explaining the dual privacy mechanisms. The right column can vertically stack the SBS strategy diagram (Figure 5) and the resulting similarity heatmap (Figure 7) to visually validate the method's effectiveness."
}"""

Token usage so far: 241703 prompt tokens, 9396 completion tokens

Cost so far: $2.69891

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "BlindFed addresses the risk of model extraction attacks where a malicious client might use pairs of intermediate representations $(b_{\\ell-1}, b_\\ell)$ to learn the parameters of the transformer blocks. To counter this, the framework implements two primary privacy-boosting mechanisms. First, **Sample-level Permutation** applies a unique random permutation matrix $\\Pi_\\ell$ to each batch of intermediate representations at every block $\\ell$. By only sharing the product of these matrices $(\\Pi_{\\ell-1}^{-1} \\cdot \\Pi_\\ell)$ with the client, the server ensures that individual sample mappings remain hidden, a property formally supported by Proposition 1. Second, **Stochastic Block Sampling (SBS)** mitigates similarity-based attacks by only revealing a subset of block outputs. Based on a structured probabilistic rule, each block has a stationary probability of $1/3$ of being sampled, resulting in an expected $L/3$ blocks being revealed. This breaks the continuity of the representations, as non-consecutive blocks exhibit significantly lower feature similarity, making it computationally infeasible for clients to reconstruct the full model sequence.",
  "key_figures": [
    {
      "ref": "Figure 5",
      "caption": "Stochastic block sampling strategy.",
      "relevance": "Illustrates the Markov-chain-like transition states (0 for not sampled, 1 for sampled) used to determine which transformer block outputs are revealed to the client."
    },
    {
      "ref": "Figure 6",
      "caption": "Heatmap visualization of the similarity (L2 distance) between corresponding block outputs or hidden representations",
      "relevance": "Demonstrates that consecutive block outputs (e.g., $b_1$ and $b_2$) have high similarity, which could be exploited for model extraction if not for the proposed privacy mechanisms."
    },
    {
      "ref": "Figure 7",
      "caption": "Heatmap visualization of the similarity (L2 distance) between non-consecutive block outputs or hidden representations",
      "relevance": "Shows that non-consecutive blocks (e.g., $b_1$ and $b_3$) have negligible similarity, validating why the SBS strategy effectively thwarts similarity-based attacks."
    }
  ],
  "key_tables": [],
  "key_equations": [
    {
      "ref": "Proposition 1",
      "content": "Let A, B, and C be n \u00d7 n permutation matrices. Given only $A^{-1}B$, $B^{-1}C$, and $C^{-1}A$, it is computationally infeasible to uniquely recover the individual matrices A, B, and C without additional information.",
      "relevance": "Provides the mathematical foundation for the sample-level permutation's security, ensuring that clients cannot reverse-engineer the random permutations applied by the server."
    },
    {
      "ref": "Equation 12",
      "content": "p = 0.5(1 - p)",
      "relevance": "The equilibrium equation used to derive the stationary probability ($p=1/3$) of a block being sampled during the SBS process."
    },
    {
      "ref": "Equation 8",
      "content": "\\mathbf{H}_\\ell = g_\\ell(\\mathbf{B}_\\ell + \\mathbf{H}_{\\ell-1}) + \\mathbf{H}_{\\ell-1}",
      "relevance": "The reformulated adapter computation used when operating on batches of permuted samples to ensure consistent updates despite the random shuffling."
    }
  ],
  "section_refs": [
    "Section 4.3",
    "Section 4.3.1",
    "Section 4.3.2",
    "Appendix A",
    "Appendix B"
  ]
}

The layout has been decided:
{
  "layout_template": "two_col_fig_right",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "bullets": {
      "x": 0.05,
      "y": 0.2,
      "w": 0.45,
      "h": 0.7
    },
    "figure": {
      "x": 0.55,
      "y": 0.2,
      "w": 0.4,
      "h": 0.7
    }
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "A two-column layout with bullets on the left and figures on the right is ideal for explaining the dual privacy mechanisms. The right column can vertically stack the SBS strategy diagram (Figure 5) and the resulting similarity heatmap (Figure 7) to visually validate the method's effectiveness."
}

Scene context:
{
  "scene_id": 5,
  "title": "Privacy-Boosting Mechanisms",
  "summary": "To mitigate model extraction attacks, BlindFed introduces sample-level permutations and stochastic block sampling (SBS). These ensure that clients only see a subset of permuted intermediate representations, preventing them from reconstructing the FM parameters.",
  "paper_section": "Model Privacy Boosting",
  "narrative_role": "method",
  "asset_video": null,
  "duration_stat": {
    "min": 10.0,
    "max": 15.0,
    "avg": 13.0
  }
}

## Previous Content
The following content was drafted for the immediately preceding scenes.
You MUST NOT repeat the exact text content or claims from these previous scenes in your current draft.

{
  "bullets": [
    "Offline distillation aligns FHE-friendly blocks with the original foundation model",
    "Online adaptation enables private local training via block-by-block encrypted inference",
    "Secure aggregation via MPC combines client updates without exposing local parameters"
  ],
  "audio_content": "BlindFed uses a two-stage strategy to bridge the gap between models. First, offline distillation aligns the FHE-friendly student with the original teacher using auxiliary data. Then, online adaptation uses block-by-block encrypted inference for private local training. Finally, secure multi-party computation aggregates updates into a global model without exposing individual parameters."
}


Your job is to **draft the actual content** (title, bullets, audio, figure choice, and duration) that fits into this layout. You do NOT decide the layout — that is already set. You also do NOT decide builds or animations — those will be planned later based on your drafted content.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "title": "A clear, concise slide title",
  "audio_content": "Full narration transcript for this entire scene. Should be natural, conversational, and cover all key points. The duration should be based on the length of this transcript.",
  "duration_sec": 8.5,
  "bullets": [
    "First concise bullet point",
    "Second concise bullet point",
    "Third concise bullet point"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure X",
    "caption": "Brief caption describing the figure"
  },
  "video": {
    "type": "asset_video",
    "path": "clip1.mp4",
    "caption": "Brief caption describing the video contents"
  },
  "source": ["Figure 1", "Section 3.1"],
  "prompt": "Visual description of the scene for generation"
}

## STRICT RULES:
1. **Number of bullets**: Write 2-4 concise, impactful bullets that cover the key points from the extracted content.
2. **Figure/Video assignment**: 
   - Assign `figure` ONLY if the content summary's `key_figures` has relevant images. 
   - Assign `video` ONLY if the `scene_context` assigns an `asset_video`.
   - If the style plan omits `has_figure` or `has_video`, omit the respective block completely.
3. **Bullet text**: Each bullet should be concise (under 15 words preferred), impactful, and directly derived from `extracted_content`. Not a copy — a focused summary.
4. **audio_content**: Natural narration covering all bullet points AND the video clip action if a video is present. 
5. **duration_sec**: First, draft the `audio_content`. Then, CALCULATE the duration: `duration_sec = word_count_of_audio / 2.5`. Do NOT guess. If the stats say 8s but you wrote 40 words, `duration_sec` MUST be 16.0.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "title": "Privacy-Boosting Mechanisms",
  "audio_content": "BlindFed thwarts model extraction with two defenses. Sample-level permutations shuffle data at every block to hide sample mappings. Simultaneously, Stochastic Block Sampling reveals only a subset of non-consecutive outputs. This breaks representation continuity, making it computationally infeasible for clients to reconstruct the model.",
  "duration_sec": 16.4,
  "bullets": [
    "Sample-level permutations shuffle data at every block to hide sample mappings",
    "Stochastic Block Sampling (SBS) reveals only a subset of non-consecutive outputs",
    "Defenses make model extraction computationally infeasible for malicious clients"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 5",
    "caption": "Stochastic block sampling strategy to prevent model extraction."
  },
  "source": [
    "Section 4.3",
    "Section 4.3.1",
    "Section 4.3.2",
    "Figure 5",
    "Figure 7"
  ],
  "prompt": "A two-column slide showing bullet points on the left and a diagram of the stochastic block sampling strategy on the right. The diagram illustrates a Markov-chain transition between sampled and non-sampled states for transformer blocks."
}"""

Token usage so far: 253639 prompt tokens, 9698 completion tokens

Cost so far: $2.82733

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "Privacy-Boosting Mechanisms",
  "audio_content": "BlindFed thwarts model extraction with two defenses. Sample-level permutations shuffle data at every block to hide sample mappings. Simultaneously, Stochastic Block Sampling reveals only a subset of non-consecutive outputs. This breaks representation continuity, making it computationally infeasible for clients to reconstruct the model.",
  "duration_sec": 16.4,
  "bullets": [
    "Sample-level permutations shuffle data at every block to hide sample mappings",
    "Stochastic Block Sampling (SBS) reveals only a subset of non-consecutive outputs",
    "Defenses make model extraction computationally infeasible for malicious clients"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 5",
    "caption": "Stochastic block sampling strategy to prevent model extraction."
  },
  "source": [
    "Section 4.3",
    "Section 4.3.1",
    "Section 4.3.2",
    "Figure 5",
    "Figure 7"
  ],
  "prompt": "A two-column slide showing bullet points on the left and a diagram of the stochastic block sampling strategy on the right. The diagram illustrates a Markov-chain transition between sampled and non-sampled states for transformer blocks."
}

Layout information:
{
  "layout_template": "two_col_fig_right",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "bullets": {
      "x": 0.05,
      "y": 0.2,
      "w": 0.45,
      "h": 0.7
    },
    "figure": {
      "x": 0.55,
      "y": 0.2,
      "w": 0.4,
      "h": 0.7
    }
  },
  "has_figure": true,
  "total_time_sec": 16.4
}

Your job is to:
1. **Decide the build plan** — how many build steps, and what gets revealed in each step.
2. **Assign the drafted bullets to specific build steps** in the best storytelling order.
3. **Split the audio into per-build segments** so each build has matching narration.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "style": "Slides",
  "expected_build_steps": 3,
  "elements": {
    "title": "The slide title from the draft",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure X",
      "caption": "Caption from draft"
    },
    "bullets": [
      "First bullet",
      "Second bullet"
    ]
  },
  "builds": [
    {
      "step_index": 0,
      "time_offset_sec": 0.0,
      "actions": [
        {"type": "show", "target": "title"},
        {"type": "show", "target": "figure"}
      ],
      "audio_segment": "Opening narration for this build step.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 3.0,
      "actions": [
        {"type": "fade_in", "target": "bullets[0]"}
      ],
      "audio_segment": "Narration for the first bullet point.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 6.0,
      "actions": [
        {"type": "fade_in", "target": "bullets[1]"}
      ],
      "audio_segment": "Narration for the second bullet point.",
      "visual_emphasis": []
    }
  ]
}

## STRICT RULES:
1. **Build count**: `expected_build_steps` = 1 + number_of_bullets. Build 0 shows title (and figure/video if present), then one build per bullet.
2. **One bullet per build**: After build 0, each build reveals exactly ONE bullet. `bullets[0]` in build 1, `bullets[1]` in build 2, etc.
3. **Build 0**: Always shows `title` (and `figure`/`video` if present). Never shows bullets in build 0.
4. **Audio segments**: Split the `audio_content` from the draft into segments. Each build's `audio_segment` must be non-empty and correspond to what that build reveals.
5. **Bullet ordering**: Assign bullets to builds in the order that creates the best storytelling flow for the audience.
6. **time_offset_sec**: Space evenly across the total time. For N builds over T seconds: offsets at 0, T/N, 2T/N, etc.
7. **visual_emphasis**: Always set to empty list `[]`.
8. **Action targets**: Only use targets that exist in `elements`: `title`, `figure`, `video`, `bullets[0]`, `bullets[1]`, etc.
9. **elements**: Copy the drafted title, figure, video, and bullets exactly — do not modify the text content.
10. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "style": "Slides",
  "expected_build_steps": 4,
  "elements": {
    "title": "Privacy-Boosting Mechanisms",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 5",
      "caption": "Stochastic block sampling strategy to prevent model extraction."
    },
    "bullets": [
      "Sample-level permutations shuffle data at every block to hide sample mappings",
      "Stochastic Block Sampling (SBS) reveals only a subset of non-consecutive outputs",
      "Defenses make model extraction computationally infeasible for malicious clients"
    ]
  },
  "builds": [
    {
      "step_index": 0,
      "time_offset_sec": 0.0,
      "actions": [
        {
          "type": "show",
          "target": "title"
        },
        {
          "type": "show",
          "target": "figure"
        }
      ],
      "audio_segment": "BlindFed thwarts model extraction with two defenses.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 4.1,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[0]"
        }
      ],
      "audio_segment": "Sample-level permutations shuffle data at every block to hide sample mappings.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 8.2,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[1]"
        }
      ],
      "audio_segment": "Simultaneously, Stochastic Block Sampling reveals only a subset of non-consecutive outputs.",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 12.3,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[2]"
        }
      ],
      "audio_segment": "This breaks representation continuity, making it computationally infeasible for clients to reconstruct the model.",
      "visual_emphasis": []
    }
  ]
}"""

Token usage so far: 264829 prompt tokens, 10260 completion tokens

Cost so far: $2.95609

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 6,
  "title": "Experimental Results and Accuracy",
  "summary": "Evaluated on CIFAR and SVHN datasets, BlindFed achieves accuracy levels comparable to LoRA and significantly outperforms linear probing, demonstrating that double-blind privacy can be maintained without sacrificing model performance.",
  "paper_section": "Results",
  "narrative_role": "results",
  "asset_video": null,
  "duration_stat": {
    "min": 10.0,
    "max": 15.0,
    "avg": 12.0
  }
}

## Previous Scenes Memory
The following content was extracted for the immediately preceding scenes. **This is provided as a memory of what the audience has JUST seen.**
You MUST NOT repeat the claims, figures, tables, or equations from these previous scenes in your current extraction, to ensure the presentation maintains forward momentum without redundant slides.
If you must reference the exactly same figure/table, the 'relevance' MUST be clearly unique to avoid narrative duplication.

{
  "extracted_content": "The BlindFed framework utilizes a two-stage split learning strategy to bridge the gap between the original Foundation Model (FM) and its FHE-friendly counterpart. In the first stage, Offline Distillation, the server acts as a teacher to train the approximated student model using an auxiliary dataset. This process is split into two phases: first, aligning embeddings, attention matrices, and hidden states; and second, distilling the final prediction layer. In the second stage, Online Adaptation, a block-by-block interactive protocol is used to perform encrypted inference. Because FHE has limited multiplicative depth, the server processes one transformer block at a time, sending the encrypted output to the client for decryption and re-encryption before proceeding. This interaction provides clients with the plaintext intermediate representations necessary to train their local parallel adapters and classification heads. Finally, secure multi-party computation (MPC) is used for secure aggregation, allowing the server to compute the average of client updates without accessing individual local parameters.",
  "key_figures": [
    {
      "ref": "Figure 9",
      "caption": "Schematic illustration of the layer-wise knowledge distillation (Equations 17 and 18).",
      "relevance": "Visualizes the teacher-student distillation process used in the offline stage to align the FHE-friendly student model's attention matrices and hidden representations with the original FM."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 7",
      "caption": "Computational and memory overhead for encrypted inference and encryption using FHE with the Tile Tensors framework.",
      "relevance": "Quantifies the practical costs of the online adaptation stage, showing the time and memory required for encryption, decryption, and encrypted inference per transformer block."
    }
  ],
  "key_equations": [
    {
      "ref": "Equation 21",
      "content": "\\mathcal{L} = \begin{cases} \\mathcal{L}_a + \\mathcal{L}_h & \triangleright \text{Stage I}, \\ \\mathcal{L}_p & \triangleright \text{Stage II}. \\end{cases}",
      "relevance": "Defines the two-stage loss objective for the distillation process, where Stage I focuses on internal layer alignment and Stage II focuses on logit-based prediction alignment."
    }
  ]
}
{
  "extracted_content": "BlindFed addresses the risk of model extraction attacks where a malicious client might use pairs of intermediate representations $(b_{\\ell-1}, b_\\ell)$ to learn the parameters of the transformer blocks. To counter this, the framework implements two primary privacy-boosting mechanisms. First, **Sample-level Permutation** applies a unique random permutation matrix $\\Pi_\\ell$ to each batch of intermediate representations at every block $\\ell$. By only sharing the product of these matrices $(\\Pi_{\\ell-1}^{-1} \\cdot \\Pi_\\ell)$ with the client, the server ensures that individual sample mappings remain hidden, a property formally supported by Proposition 1. Second, **Stochastic Block Sampling (SBS)** mitigates similarity-based attacks by only revealing a subset of block outputs. Based on a structured probabilistic rule, each block has a stationary probability of $1/3$ of being sampled, resulting in an expected $L/3$ blocks being revealed. This breaks the continuity of the representations, as non-consecutive blocks exhibit significantly lower feature similarity, making it computationally infeasible for clients to reconstruct the full model sequence.",
  "key_figures": [
    {
      "ref": "Figure 5",
      "caption": "Stochastic block sampling strategy.",
      "relevance": "Illustrates the Markov-chain-like transition states (0 for not sampled, 1 for sampled) used to determine which transformer block outputs are revealed to the client."
    },
    {
      "ref": "Figure 6",
      "caption": "Heatmap visualization of the similarity (L2 distance) between corresponding block outputs or hidden representations",
      "relevance": "Demonstrates that consecutive block outputs (e.g., $b_1$ and $b_2$) have high similarity, which could be exploited for model extraction if not for the proposed privacy mechanisms."
    },
    {
      "ref": "Figure 7",
      "caption": "Heatmap visualization of the similarity (L2 distance) between non-consecutive block outputs or hidden representations",
      "relevance": "Shows that non-consecutive blocks (e.g., $b_1$ and $b_3$) have negligible similarity, validating why the SBS strategy effectively thwarts similarity-based attacks."
    }
  ],
  "key_tables": [],
  "key_equations": [
    {
      "ref": "Proposition 1",
      "content": "Let A, B, and C be n \u00d7 n permutation matrices. Given only $A^{-1}B$, $B^{-1}C$, and $C^{-1}A$, it is computationally infeasible to uniquely recover the individual matrices A, B, and C without additional information.",
      "relevance": "Provides the mathematical foundation for the sample-level permutation's security, ensuring that clients cannot reverse-engineer the random permutations applied by the server."
    },
    {
      "ref": "Equation 12",
      "content": "p = 0.5(1 - p)",
      "relevance": "The equilibrium equation used to derive the stationary probability ($p=1/3$) of a block being sampled during the SBS process."
    },
    {
      "ref": "Equation 8",
      "content": "\\mathbf{H}_\\ell = g_\\ell(\\mathbf{B}_\\ell + \\mathbf{H}_{\\ell-1}) + \\mathbf{H}_{\\ell-1}",
      "relevance": "The reformulated adapter computation used when operating on batches of permuted samples to ensure consistent updates despite the random shuffling."
    }
  ]
}


Read the paper carefully and extract ALL relevant content from the section(s) referenced in this scene.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "extracted_content": "A comprehensive summary of the key information from this section. Include main claims, methods, results, or insights. This should contain enough detail for someone to write presentation bullets from it.",
  "key_figures": [
    {
      "ref": "Figure X",
      "caption": "The actual caption from the paper",
      "relevance": "Why this figure matters for this scene"
    }
  ],
  "key_tables": [
    {
      "ref": "Table X",
      "caption": "The actual caption from the paper",
      "relevance": "Why this table matters for this scene"
    }
  ],
  "key_equations": [
    {
      "ref": "Equation X or description",
      "content": "The equation in text form",
      "relevance": "Why this equation matters for this scene"
    }
  ],
  "section_refs": ["Section 3.1", "Section 3.2"]
}

## STRICT RULES:
1. **Only reference figures/tables that actually appear in the paper section.** Do NOT invent or guess figure/table numbers.
2. **key_figures** must list figures by their exact label in the paper (e.g., "Figure 1", "Fig. 2").
3. If no figures/tables/equations are relevant, use empty lists `[]`.
4. **extracted_content** must be detailed enough to create 2-4 meaningful bullet points from it.
5. **Memory Context**: The `Previous Scenes Memory` (if provided) shows what was ALREADY covered. You MUST NOT repeat its text content, claims, figures, tables, or equations. CRITICAL: Even if you MUST reference the same figure/table, the text content (`extracted_content`) and `relevance` MUST still be completely DIFFERENT.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "extracted_content": "BlindFed's performance was evaluated on CIFAR-10, CIFAR-100, SVHN, and Fed-ISIC2019 datasets across centralized and federated settings with varying data heterogeneity (Dirichlet $\\alpha$). The results demonstrate that BlindFed significantly outperforms the only other double-blind baseline, Linear Probing, particularly on challenging datasets like SVHN and under extreme heterogeneity ($\\alpha=0.01$). BlindFed achieves accuracy levels closely aligned with LoRA, despite LoRA not being double-blind and requiring backpropagation through the backbone. The addition of Stochastic Block Sampling (SBS) was found to have minimal impact on accuracy, and in some instances, slightly improved generalization. Scalability tests with up to 50 clients on CIFAR-10 show that BlindFed maintains stable performance, consistently outperforming linear probing as the number of clients increases. Furthermore, experiments on the Fed-ISIC2019 medical dataset confirm that the framework is effective even when the auxiliary dataset used for offline distillation (e.g., Tiny-ImageNet) is out-of-distribution (OOD) relative to the target task.",
  "key_figures": [],
  "key_tables": [
    {
      "ref": "Table 1",
      "caption": "Comparison of accuracy achieved by our proposed method against baseline approaches on three datasets (CIFAR-10, CIFAR-100, and SVHN) in both centralized and federated learning scenarios.",
      "relevance": "Provides the primary evidence that BlindFed achieves near-LoRA accuracy while maintaining double-blind privacy, significantly outperforming linear probing across multiple datasets and heterogeneity levels."
    },
    {
      "ref": "Table 2",
      "caption": "Performance comparison of our method with baseline approaches on the Fed-ISIC2019 dataset with five clients (K = 5), using two auxiliary datasets: Fed-ISIC2019 (center=0) as an in-distribution (InD) dataset and Tiny-ImageNet as an out-of-distribution (OOD) dataset.",
      "relevance": "Demonstrates the framework's effectiveness on medical imaging and proves that the offline distillation stage works well even with out-of-distribution auxiliary data."
    },
    {
      "ref": "Table 3",
      "caption": "Scalability analysis of the proposed method to baseline approaches on the CIFAR-10 dataset, with varying number of clients K ∈ {10, 20, 50} under a Dirichlet concentration parameter of 1.0 for data partitioning.",
      "relevance": "Shows that BlindFed scales effectively to a larger number of clients, maintaining a significant performance lead over linear probing."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "Section 5.3",
    "Section D.2"
  ]
}"""

Token usage so far: 276758 prompt tokens, 10900 completion tokens

Cost so far: $3.09458

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "BlindFed's performance was evaluated on CIFAR-10, CIFAR-100, SVHN, and Fed-ISIC2019 datasets across centralized and federated settings with varying data heterogeneity (Dirichlet $\\alpha$). The results demonstrate that BlindFed significantly outperforms the only other double-blind baseline, Linear Probing, particularly on challenging datasets like SVHN and under extreme heterogeneity ($\\alpha=0.01$). BlindFed achieves accuracy levels closely aligned with LoRA, despite LoRA not being double-blind and requiring backpropagation through the backbone. The addition of Stochastic Block Sampling (SBS) was found to have minimal impact on accuracy, and in some instances, slightly improved generalization. Scalability tests with up to 50 clients on CIFAR-10 show that BlindFed maintains stable performance, consistently outperforming linear probing as the number of clients increases. Furthermore, experiments on the Fed-ISIC2019 medical dataset confirm that the framework is effective even when the auxiliary dataset used for offline distillation (e.g., Tiny-ImageNet) is out-of-distribution (OOD) relative to the target task.",
  "key_figures": [],
  "key_tables": [
    {
      "ref": "Table 1",
      "caption": "Comparison of accuracy achieved by our proposed method against baseline approaches on three datasets (CIFAR-10, CIFAR-100, and SVHN) in both centralized and federated learning scenarios.",
      "relevance": "Provides the primary evidence that BlindFed achieves near-LoRA accuracy while maintaining double-blind privacy, significantly outperforming linear probing across multiple datasets and heterogeneity levels."
    },
    {
      "ref": "Table 2",
      "caption": "Performance comparison of our method with baseline approaches on the Fed-ISIC2019 dataset with five clients (K = 5), using two auxiliary datasets: Fed-ISIC2019 (center=0) as an in-distribution (InD) dataset and Tiny-ImageNet as an out-of-distribution (OOD) dataset.",
      "relevance": "Demonstrates the framework's effectiveness on medical imaging and proves that the offline distillation stage works well even with out-of-distribution auxiliary data."
    },
    {
      "ref": "Table 3",
      "caption": "Scalability analysis of the proposed method to baseline approaches on the CIFAR-10 dataset, with varying number of clients K \u2208 {10, 20, 50} under a Dirichlet concentration parameter of 1.0 for data partitioning.",
      "relevance": "Shows that BlindFed scales effectively to a larger number of clients, maintaining a significant performance lead over linear probing."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "Section 5.3",
    "Section D.2"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 6,
  "title": "Experimental Results and Accuracy",
  "summary": "Evaluated on CIFAR and SVHN datasets, BlindFed achieves accuracy levels comparable to LoRA and significantly outperforms linear probing, demonstrating that double-blind privacy can be maintained without sacrificing model performance.",
  "paper_section": "Results",
  "narrative_role": "results",
  "asset_video": null,
  "duration_stat": {
    "min": 10.0,
    "max": 15.0,
    "avg": 12.0
  }
}

Reference style advice:
Reference Layouts for 'results' section from similar papers:
- Example 1: The slide follows a top-down structure starting with a large, bold title in a serif font at the top-left. Below the title, the middle section contains two side-by-side line charts, labeled '(A) Idefics2' and '(B) LLaVA-NeXT'. A shared legend is centered above the charts, identifying four experimental conditions: 'Causal' (blue), 'Isolated' (green), 'Bidirectional' (brown), and 'Soft (Ours)' (purple). Both charts plot 'Accuracy (%)' on the y-axis against 'Image Position' (from 1 to 10) on the x-axis. The bottom section of the slide features three prominent bullet points that summarize the findings from the charts. Each bullet point consists of a single sentence in a bold, sans-serif font. The background is plain white, and the overall text density is moderate, focusing on the visual data and its interpretation.
- Example 2: The slide features a large, bold blue title 'Artifact Results' positioned at the top-left. Below the title, a centered red text label 'Prompt: A power drill.' introduces the visual content. The main body of the slide consists of a horizontal row of five side-by-side images showing generated power drills. The first image on the left, labeled 'SD 1.4', contains a red circle highlighting a visual artifact. Each image has a corresponding label centered directly beneath it: 'SD 1.4', 'Reward Guidance', 'Reward Guidance w/ Region Constraints', 'DraFT', and 'Focus-N-Fix (Ours)', with the final label highlighted in red to denote the proposed method. Below this row of images, a single bullet point provides technical context regarding the 'Reward Model' used. A small bibliographic citation is placed in the bottom-left corner. The slide uses a clean white background with a light text density, prioritizing qualitative visual comparison.
- Example 3: The slide follows a top-down structure starting with a large, bold title in the top-left corner. Immediately below the title is a two-line text block explaining the methodology's requirements. The middle section of the slide features two side-by-side line charts, labeled '(A) Idefics2' and '(B) LLaVA-NeXT' respectively. A horizontal legend is centered above these charts, identifying four different experimental conditions: Causal, Isolated, Bidirectional, and Soft (Ours). Both charts plot Accuracy (%) on the vertical axis against Image Position on the horizontal axis. The slide concludes with a bolded summary paragraph at the bottom that interprets the results shown in the charts. The background is a clean white, and the text density is moderate, focusing on the visual comparison of the data plots.
- Example 4: The slide features a large, bold serif title 'Experiment & Results' positioned at the top-left. The main body of the slide is organized vertically into two primary sections. The top section contains a wide, data-dense table (Table 1) that spans the full width of the slide, comparing various models across four benchmarks (BLINK, Mantis-Eval, MuirBench, MIRB) with and without a 'SoFA' modification. Below this table is a multi-line caption. The bottom section of the slide contains three graphical figures arranged horizontally. On the left, Figure 6 consists of two side-by-side bar charts (labeled A and B) showing attention distribution across image positions, using purple and green colors. To the right, Figure 7 is a single bar chart with green bars representing performance gains across different task types like 'Retrieval' and 'Analogy'. Each figure group has a corresponding caption placed directly beneath it. The slide has a high text and data density, set against a plain white background with a professional color scheme of green and purple accents in the charts.
- Example 5: The slide uses a two-column layout with a distinct color contrast between the left and right sides. The left column has a dark background and functions as a navigation menu or table of contents, featuring the main title 'Block Diffusion Language Modeling' at the top. Below the title is a dense, hierarchical list of bullet points with two levels of indentation, organized under headings like 'Model Design', 'Training and Sampling', and 'Experimental Evaluations'. Some text in this column is highlighted in orange to indicate the current section. The right column has a white background and contains content that looks like a page from an academic paper. It includes section headers '6.1 LIKELIHOOD EVALUATION' and '6.2 SAMPLE QUALITY AND VARIABLE-LENGTH SEQUENCE GENERATION'. This side is text-heavy, featuring several paragraphs, mathematical expressions, and three data tables (Table 4, Table 5, and Table 6). Certain key findings in the text are highlighted with a light green background. A small pixel-art dinosaur icon is positioned in the bottom right corner of the slide.

Duration statistics for this section (from references): min=1.0s, max=126.0s, avg=20.1s.

Your job is to decide the **visual layout** for this slide. Do NOT decide builds or animations — those will be planned later.

## CHOOSE THE BEST LAYOUT

Pick the layout template that best suits the content. Common templates include (but you are NOT limited to these):
- `two_col_fig_left` — Figure on left, bullets on right. Best for: method diagrams, architecture figures, or tall/vertical figures.
- `two_col_fig_right` — Bullets on left, figure on right. Best for: motivation slides with illustrative or tall/vertical figures.
- `full_fig_with_callouts` — Large figure with small bullet callouts below. Best for: results, data visualizations, or wide/horizontal figures.
- `one_col_bullets` — Full-width bullets, no figure. Best for: text-heavy overview or summary slides.
- `video_with_caption` — Large video region with small bullet callouts below. Best for: when an `asset_video` is provided.

If none of these fit, invent a descriptive template name and define its regions.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "video": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "bullets": {"x": 0.55, "y": 0.25, "w": 0.4, "h": 0.6}
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "Two-column layout with figure on left is ideal for showing the architecture diagram alongside explanatory bullets."
}

## STRICT RULES:
1. **Region keys**: Only use `title`, `bullets`, `figure`, `video` as region keys. Do NOT invent keys like `callout_1`, `table`, etc.
2. **Coordinates**: All x/y/w/h values must be normalized (0.0 to 1.0). Regions must not overlap.
3. **has_figure**: Set to `true` only if the content summary has relevant figures. If no figure is available, omit `figure` from regions.
4. **has_video**: Set to `true` only if `scene_context` specifically assigns an `asset_video`. If true, include the `video` region. Do not include both `figure` and `video` unless space permits.
5. **No builds**: Do NOT include `build_skeleton`, `expected_build_steps`, or any animation information.
6. Output ONLY valid JSON, no markdown fences, no explanation.

IMPORTANT FIGURE ASPECT RATIO RULE:
If the extracted figure is nearly square, its placement is flexible. However, if the figure has a much larger dimension horizontally (like a wide rectangle), choose a layout with a wide figure region (e.g., `full_fig_with_callouts` or placing it spanning top/bottom) so it is not shrunk awkwardly. If it is very tall/vertical, choose a side-by-side template (e.g., `two_col_fig_left`) where it has vertical space. Ensure your chosen template and `layout_regions` coordinates are decided accordingly to preserve the figure's aspect ratio without shrinking it.


**Answer (from GEMINI)**

"""{
  "layout_template": "full_fig_with_callouts",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.18, "w": 0.9, "h": 0.45},
    "bullets": {"x": 0.05, "y": 0.68, "w": 0.9, "h": 0.27}
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "A top-down layout with a wide figure region is best for displaying the comprehensive accuracy comparison table (Table 1), which is the core evidence for the results. Summary bullets at the bottom provide interpretation and highlight secondary findings like scalability and OOD robustness."
}"""

Token usage so far: 289394 prompt tokens, 11138 completion tokens

Cost so far: $3.22808

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "BlindFed's performance was evaluated on CIFAR-10, CIFAR-100, SVHN, and Fed-ISIC2019 datasets across centralized and federated settings with varying data heterogeneity (Dirichlet $\\alpha$). The results demonstrate that BlindFed significantly outperforms the only other double-blind baseline, Linear Probing, particularly on challenging datasets like SVHN and under extreme heterogeneity ($\\alpha=0.01$). BlindFed achieves accuracy levels closely aligned with LoRA, despite LoRA not being double-blind and requiring backpropagation through the backbone. The addition of Stochastic Block Sampling (SBS) was found to have minimal impact on accuracy, and in some instances, slightly improved generalization. Scalability tests with up to 50 clients on CIFAR-10 show that BlindFed maintains stable performance, consistently outperforming linear probing as the number of clients increases. Furthermore, experiments on the Fed-ISIC2019 medical dataset confirm that the framework is effective even when the auxiliary dataset used for offline distillation (e.g., Tiny-ImageNet) is out-of-distribution (OOD) relative to the target task.",
  "key_figures": [],
  "key_tables": [
    {
      "ref": "Table 1",
      "caption": "Comparison of accuracy achieved by our proposed method against baseline approaches on three datasets (CIFAR-10, CIFAR-100, and SVHN) in both centralized and federated learning scenarios.",
      "relevance": "Provides the primary evidence that BlindFed achieves near-LoRA accuracy while maintaining double-blind privacy, significantly outperforming linear probing across multiple datasets and heterogeneity levels."
    },
    {
      "ref": "Table 2",
      "caption": "Performance comparison of our method with baseline approaches on the Fed-ISIC2019 dataset with five clients (K = 5), using two auxiliary datasets: Fed-ISIC2019 (center=0) as an in-distribution (InD) dataset and Tiny-ImageNet as an out-of-distribution (OOD) dataset.",
      "relevance": "Demonstrates the framework's effectiveness on medical imaging and proves that the offline distillation stage works well even with out-of-distribution auxiliary data."
    },
    {
      "ref": "Table 3",
      "caption": "Scalability analysis of the proposed method to baseline approaches on the CIFAR-10 dataset, with varying number of clients K \u2208 {10, 20, 50} under a Dirichlet concentration parameter of 1.0 for data partitioning.",
      "relevance": "Shows that BlindFed scales effectively to a larger number of clients, maintaining a significant performance lead over linear probing."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "Section 5.3",
    "Section D.2"
  ]
}

The layout has been decided:
{
  "layout_template": "full_fig_with_callouts",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "figure": {
      "x": 0.05,
      "y": 0.18,
      "w": 0.9,
      "h": 0.45
    },
    "bullets": {
      "x": 0.05,
      "y": 0.68,
      "w": 0.9,
      "h": 0.27
    }
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "A top-down layout with a wide figure region is best for displaying the comprehensive accuracy comparison table (Table 1), which is the core evidence for the results. Summary bullets at the bottom provide interpretation and highlight secondary findings like scalability and OOD robustness."
}

Scene context:
{
  "scene_id": 6,
  "title": "Experimental Results and Accuracy",
  "summary": "Evaluated on CIFAR and SVHN datasets, BlindFed achieves accuracy levels comparable to LoRA and significantly outperforms linear probing, demonstrating that double-blind privacy can be maintained without sacrificing model performance.",
  "paper_section": "Results",
  "narrative_role": "results",
  "asset_video": null,
  "duration_stat": {
    "min": 10.0,
    "max": 15.0,
    "avg": 12.0
  }
}

## Previous Content
The following content was drafted for the immediately preceding scenes.
You MUST NOT repeat the exact text content or claims from these previous scenes in your current draft.

{
  "bullets": [
    "Sample-level permutations shuffle data at every block to hide sample mappings",
    "Stochastic Block Sampling (SBS) reveals only a subset of non-consecutive outputs",
    "Defenses make model extraction computationally infeasible for malicious clients"
  ],
  "audio_content": "BlindFed thwarts model extraction with two defenses. Sample-level permutations shuffle data at every block to hide sample mappings. Simultaneously, Stochastic Block Sampling reveals only a subset of non-consecutive outputs. This breaks representation continuity, making it computationally infeasible for clients to reconstruct the model."
}


Your job is to **draft the actual content** (title, bullets, audio, figure choice, and duration) that fits into this layout. You do NOT decide the layout — that is already set. You also do NOT decide builds or animations — those will be planned later based on your drafted content.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "title": "A clear, concise slide title",
  "audio_content": "Full narration transcript for this entire scene. Should be natural, conversational, and cover all key points. The duration should be based on the length of this transcript.",
  "duration_sec": 8.5,
  "bullets": [
    "First concise bullet point",
    "Second concise bullet point",
    "Third concise bullet point"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure X",
    "caption": "Brief caption describing the figure"
  },
  "video": {
    "type": "asset_video",
    "path": "clip1.mp4",
    "caption": "Brief caption describing the video contents"
  },
  "source": ["Figure 1", "Section 3.1"],
  "prompt": "Visual description of the scene for generation"
}

## STRICT RULES:
1. **Number of bullets**: Write 2-4 concise, impactful bullets that cover the key points from the extracted content.
2. **Figure/Video assignment**: 
   - Assign `figure` ONLY if the content summary's `key_figures` has relevant images. 
   - Assign `video` ONLY if the `scene_context` assigns an `asset_video`.
   - If the style plan omits `has_figure` or `has_video`, omit the respective block completely.
3. **Bullet text**: Each bullet should be concise (under 15 words preferred), impactful, and directly derived from `extracted_content`. Not a copy — a focused summary.
4. **audio_content**: Natural narration covering all bullet points AND the video clip action if a video is present. 
5. **duration_sec**: First, draft the `audio_content`. Then, CALCULATE the duration: `duration_sec = word_count_of_audio / 2.5`. Do NOT guess. If the stats say 8s but you wrote 40 words, `duration_sec` MUST be 16.0.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "title": "Experimental Results and Accuracy",
  "audio_content": "BlindFed achieves accuracy comparable to LoRA while maintaining double-blind privacy. It significantly outperforms linear probing, especially under extreme data heterogeneity. The framework scales reliably to fifty clients and remains effective even when the auxiliary distillation data is out-of-distribution.",
  "duration_sec": 15.2,
  "bullets": [
    "Achieves near-LoRA accuracy with double-blind privacy",
    "Outperforms linear probing under extreme data heterogeneity",
    "Scales effectively to 50 clients with stable performance",
    "Robust to out-of-distribution auxiliary distillation data"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Table 1",
    "caption": "Accuracy comparison of BlindFed against baselines across CIFAR and SVHN datasets"
  },
  "source": [
    "Table 1",
    "Section 5.3",
    "Section D.2"
  ],
  "prompt": "A slide showing a detailed accuracy comparison table (Table 1) from the paper, highlighting BlindFed's performance against LoRA and Linear Probing across different datasets and Dirichlet alpha values. Below the table, four concise bullet points summarize the key findings regarding accuracy, heterogeneity, scalability, and OOD robustness."
}"""

Token usage so far: 301099 prompt tokens, 11441 completion tokens

Cost so far: $3.35422

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "Experimental Results and Accuracy",
  "audio_content": "BlindFed achieves accuracy comparable to LoRA while maintaining double-blind privacy. It significantly outperforms linear probing, especially under extreme data heterogeneity. The framework scales reliably to fifty clients and remains effective even when the auxiliary distillation data is out-of-distribution.",
  "duration_sec": 15.2,
  "bullets": [
    "Achieves near-LoRA accuracy with double-blind privacy",
    "Outperforms linear probing under extreme data heterogeneity",
    "Scales effectively to 50 clients with stable performance",
    "Robust to out-of-distribution auxiliary distillation data"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Table 1",
    "caption": "Accuracy comparison of BlindFed against baselines across CIFAR and SVHN datasets"
  },
  "source": [
    "Table 1",
    "Section 5.3",
    "Section D.2"
  ],
  "prompt": "A slide showing a detailed accuracy comparison table (Table 1) from the paper, highlighting BlindFed's performance against LoRA and Linear Probing across different datasets and Dirichlet alpha values. Below the table, four concise bullet points summarize the key findings regarding accuracy, heterogeneity, scalability, and OOD robustness."
}

Layout information:
{
  "layout_template": "full_fig_with_callouts",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "figure": {
      "x": 0.05,
      "y": 0.18,
      "w": 0.9,
      "h": 0.45
    },
    "bullets": {
      "x": 0.05,
      "y": 0.68,
      "w": 0.9,
      "h": 0.27
    }
  },
  "has_figure": true,
  "total_time_sec": 15.2
}

Your job is to:
1. **Decide the build plan** — how many build steps, and what gets revealed in each step.
2. **Assign the drafted bullets to specific build steps** in the best storytelling order.
3. **Split the audio into per-build segments** so each build has matching narration.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "style": "Slides",
  "expected_build_steps": 3,
  "elements": {
    "title": "The slide title from the draft",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure X",
      "caption": "Caption from draft"
    },
    "bullets": [
      "First bullet",
      "Second bullet"
    ]
  },
  "builds": [
    {
      "step_index": 0,
      "time_offset_sec": 0.0,
      "actions": [
        {"type": "show", "target": "title"},
        {"type": "show", "target": "figure"}
      ],
      "audio_segment": "Opening narration for this build step.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 3.0,
      "actions": [
        {"type": "fade_in", "target": "bullets[0]"}
      ],
      "audio_segment": "Narration for the first bullet point.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 6.0,
      "actions": [
        {"type": "fade_in", "target": "bullets[1]"}
      ],
      "audio_segment": "Narration for the second bullet point.",
      "visual_emphasis": []
    }
  ]
}

## STRICT RULES:
1. **Build count**: `expected_build_steps` = 1 + number_of_bullets. Build 0 shows title (and figure/video if present), then one build per bullet.
2. **One bullet per build**: After build 0, each build reveals exactly ONE bullet. `bullets[0]` in build 1, `bullets[1]` in build 2, etc.
3. **Build 0**: Always shows `title` (and `figure`/`video` if present). Never shows bullets in build 0.
4. **Audio segments**: Split the `audio_content` from the draft into segments. Each build's `audio_segment` must be non-empty and correspond to what that build reveals.
5. **Bullet ordering**: Assign bullets to builds in the order that creates the best storytelling flow for the audience.
6. **time_offset_sec**: Space evenly across the total time. For N builds over T seconds: offsets at 0, T/N, 2T/N, etc.
7. **visual_emphasis**: Always set to empty list `[]`.
8. **Action targets**: Only use targets that exist in `elements`: `title`, `figure`, `video`, `bullets[0]`, `bullets[1]`, etc.
9. **elements**: Copy the drafted title, figure, video, and bullets exactly — do not modify the text content.
10. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "style": "Slides",
  "expected_build_steps": 5,
  "elements": {
    "title": "Experimental Results and Accuracy",
    "figure": {
      "type": "paper_figure",
      "ref": "Table 1",
      "caption": "Accuracy comparison of BlindFed against baselines across CIFAR and SVHN datasets"
    },
    "bullets": [
      "Achieves near-LoRA accuracy with double-blind privacy",
      "Outperforms linear probing under extreme data heterogeneity",
      "Scales effectively to 50 clients with stable performance",
      "Robust to out-of-distribution auxiliary distillation data"
    ]
  },
  "builds": [
    {
      "step_index": 0,
      "time_offset_sec": 0.0,
      "actions": [
        {
          "type": "show",
          "target": "title"
        },
        {
          "type": "show",
          "target": "figure"
        }
      ],
      "audio_segment": "BlindFed achieves accuracy comparable to LoRA",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 3.04,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[0]"
        }
      ],
      "audio_segment": "while maintaining double-blind privacy.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 6.08,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[1]"
        }
      ],
      "audio_segment": "It significantly outperforms linear probing, especially under extreme data heterogeneity.",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 9.12,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[2]"
        }
      ],
      "audio_segment": "The framework scales reliably to fifty clients",
      "visual_emphasis": []
    },
    {
      "step_index": 4,
      "time_offset_sec": 12.16,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[3]"
        }
      ],
      "audio_segment": "and remains effective even when the auxiliary distillation data is out-of-distribution.",
      "visual_emphasis": []
    }
  ]
}"""

Token usage so far: 312294 prompt tokens, 12091 completion tokens

Cost so far: $3.48567

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 7,
  "title": "Efficiency and Scalability Analysis",
  "summary": "While BlindFed incurs high communication costs and server-side computational complexity due to FHE, it maintains a low memory footprint for clients and demonstrates robust scalability across varying numbers of participants in federated settings.",
  "paper_section": "Results",
  "narrative_role": "results",
  "asset_video": null,
  "duration_stat": {
    "min": 8.0,
    "max": 14.0,
    "avg": 11.0
  }
}

## Previous Scenes Memory
The following content was extracted for the immediately preceding scenes. **This is provided as a memory of what the audience has JUST seen.**
You MUST NOT repeat the claims, figures, tables, or equations from these previous scenes in your current extraction, to ensure the presentation maintains forward momentum without redundant slides.
If you must reference the exactly same figure/table, the 'relevance' MUST be clearly unique to avoid narrative duplication.

{
  "extracted_content": "BlindFed addresses the risk of model extraction attacks where a malicious client might use pairs of intermediate representations $(b_{\\ell-1}, b_\\ell)$ to learn the parameters of the transformer blocks. To counter this, the framework implements two primary privacy-boosting mechanisms. First, **Sample-level Permutation** applies a unique random permutation matrix $\\Pi_\\ell$ to each batch of intermediate representations at every block $\\ell$. By only sharing the product of these matrices $(\\Pi_{\\ell-1}^{-1} \\cdot \\Pi_\\ell)$ with the client, the server ensures that individual sample mappings remain hidden, a property formally supported by Proposition 1. Second, **Stochastic Block Sampling (SBS)** mitigates similarity-based attacks by only revealing a subset of block outputs. Based on a structured probabilistic rule, each block has a stationary probability of $1/3$ of being sampled, resulting in an expected $L/3$ blocks being revealed. This breaks the continuity of the representations, as non-consecutive blocks exhibit significantly lower feature similarity, making it computationally infeasible for clients to reconstruct the full model sequence.",
  "key_figures": [
    {
      "ref": "Figure 5",
      "caption": "Stochastic block sampling strategy.",
      "relevance": "Illustrates the Markov-chain-like transition states (0 for not sampled, 1 for sampled) used to determine which transformer block outputs are revealed to the client."
    },
    {
      "ref": "Figure 6",
      "caption": "Heatmap visualization of the similarity (L2 distance) between corresponding block outputs or hidden representations",
      "relevance": "Demonstrates that consecutive block outputs (e.g., $b_1$ and $b_2$) have high similarity, which could be exploited for model extraction if not for the proposed privacy mechanisms."
    },
    {
      "ref": "Figure 7",
      "caption": "Heatmap visualization of the similarity (L2 distance) between non-consecutive block outputs or hidden representations",
      "relevance": "Shows that non-consecutive blocks (e.g., $b_1$ and $b_3$) have negligible similarity, validating why the SBS strategy effectively thwarts similarity-based attacks."
    }
  ],
  "key_tables": [],
  "key_equations": [
    {
      "ref": "Proposition 1",
      "content": "Let A, B, and C be n \u00d7 n permutation matrices. Given only $A^{-1}B$, $B^{-1}C$, and $C^{-1}A$, it is computationally infeasible to uniquely recover the individual matrices A, B, and C without additional information.",
      "relevance": "Provides the mathematical foundation for the sample-level permutation's security, ensuring that clients cannot reverse-engineer the random permutations applied by the server."
    },
    {
      "ref": "Equation 12",
      "content": "p = 0.5(1 - p)",
      "relevance": "The equilibrium equation used to derive the stationary probability ($p=1/3$) of a block being sampled during the SBS process."
    },
    {
      "ref": "Equation 8",
      "content": "\\mathbf{H}_\\ell = g_\\ell(\\mathbf{B}_\\ell + \\mathbf{H}_{\\ell-1}) + \\mathbf{H}_{\\ell-1}",
      "relevance": "The reformulated adapter computation used when operating on batches of permuted samples to ensure consistent updates despite the random shuffling."
    }
  ]
}
{
  "extracted_content": "BlindFed's performance was evaluated on CIFAR-10, CIFAR-100, SVHN, and Fed-ISIC2019 datasets across centralized and federated settings with varying data heterogeneity (Dirichlet $\\alpha$). The results demonstrate that BlindFed significantly outperforms the only other double-blind baseline, Linear Probing, particularly on challenging datasets like SVHN and under extreme heterogeneity ($\\alpha=0.01$). BlindFed achieves accuracy levels closely aligned with LoRA, despite LoRA not being double-blind and requiring backpropagation through the backbone. The addition of Stochastic Block Sampling (SBS) was found to have minimal impact on accuracy, and in some instances, slightly improved generalization. Scalability tests with up to 50 clients on CIFAR-10 show that BlindFed maintains stable performance, consistently outperforming linear probing as the number of clients increases. Furthermore, experiments on the Fed-ISIC2019 medical dataset confirm that the framework is effective even when the auxiliary dataset used for offline distillation (e.g., Tiny-ImageNet) is out-of-distribution (OOD) relative to the target task.",
  "key_figures": [],
  "key_tables": [
    {
      "ref": "Table 1",
      "caption": "Comparison of accuracy achieved by our proposed method against baseline approaches on three datasets (CIFAR-10, CIFAR-100, and SVHN) in both centralized and federated learning scenarios.",
      "relevance": "Provides the primary evidence that BlindFed achieves near-LoRA accuracy while maintaining double-blind privacy, significantly outperforming linear probing across multiple datasets and heterogeneity levels."
    },
    {
      "ref": "Table 2",
      "caption": "Performance comparison of our method with baseline approaches on the Fed-ISIC2019 dataset with five clients (K = 5), using two auxiliary datasets: Fed-ISIC2019 (center=0) as an in-distribution (InD) dataset and Tiny-ImageNet as an out-of-distribution (OOD) dataset.",
      "relevance": "Demonstrates the framework's effectiveness on medical imaging and proves that the offline distillation stage works well even with out-of-distribution auxiliary data."
    },
    {
      "ref": "Table 3",
      "caption": "Scalability analysis of the proposed method to baseline approaches on the CIFAR-10 dataset, with varying number of clients K \u2208 {10, 20, 50} under a Dirichlet concentration parameter of 1.0 for data partitioning.",
      "relevance": "Shows that BlindFed scales effectively to a larger number of clients, maintaining a significant performance lead over linear probing."
    }
  ],
  "key_equations": []
}


Read the paper carefully and extract ALL relevant content from the section(s) referenced in this scene.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "extracted_content": "A comprehensive summary of the key information from this section. Include main claims, methods, results, or insights. This should contain enough detail for someone to write presentation bullets from it.",
  "key_figures": [
    {
      "ref": "Figure X",
      "caption": "The actual caption from the paper",
      "relevance": "Why this figure matters for this scene"
    }
  ],
  "key_tables": [
    {
      "ref": "Table X",
      "caption": "The actual caption from the paper",
      "relevance": "Why this table matters for this scene"
    }
  ],
  "key_equations": [
    {
      "ref": "Equation X or description",
      "content": "The equation in text form",
      "relevance": "Why this equation matters for this scene"
    }
  ],
  "section_refs": ["Section 3.1", "Section 3.2"]
}

## STRICT RULES:
1. **Only reference figures/tables that actually appear in the paper section.** Do NOT invent or guess figure/table numbers.
2. **key_figures** must list figures by their exact label in the paper (e.g., "Figure 1", "Fig. 2").
3. If no figures/tables/equations are relevant, use empty lists `[]`.
4. **extracted_content** must be detailed enough to create 2-4 meaningful bullet points from it.
5. **Memory Context**: The `Previous Scenes Memory` (if provided) shows what was ALREADY covered. You MUST NOT repeat its text content, claims, figures, tables, or equations. CRITICAL: Even if you MUST reference the same figure/table, the text content (`extracted_content`) and `relevance` MUST still be completely DIFFERENT.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "extracted_content": "BlindFed achieves a favorable balance between efficiency and performance by significantly reducing the computational burden on clients. It requires 34x to 48x fewer trainable parameters than full fine-tuning and maintains a client-side memory footprint of approximately 9GB, which is nearly half that of full fine-tuning (~18GB). In terms of latency, BlindFed is remarkably efficient, operating at only a 4% increase over linear probing because it eliminates the need for backpropagation through the foundation model backbone. However, the framework's primary bottlenecks are server-side: encrypted inference for a single transformer block takes approximately 136 seconds per sample and requires over 22GB of server memory. Additionally, the use of Fully Homomorphic Encryption (FHE) results in a 2.8x data expansion, increasing the size of intermediate representations from 6.21MB to 17.33MB, which contributes to high communication overhead.",
  "key_figures": [
    {
      "ref": "Figure 10",
      "caption": "Comparison of the efficiency of different adaptation methods in terms of the number of parameters, latency, and memory usage across three datasets: CIFAR-10/SVHN, CIFAR-100, and Fed-ISIC2019.",
      "relevance": "Visually demonstrates that BlindFed achieves near-optimal latency and low memory usage (comparable to linear probing) while providing significantly more adaptability than simple head-only tuning."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 4",
      "caption": "Comparison of the efficiency of our method with baseline approaches in terms of the number of parameters, latency and the memory requirement across four datasets (CIFAR-10/SVHN, CIFAR-100, and Fed-ISIC2019).",
      "relevance": "Provides the exact metrics for trainable parameters, latency per data point, and GPU memory requirements, highlighting BlindFed's efficiency for thin clients."
    },
    {
      "ref": "Table 7",
      "caption": "Computational and memory overhead for encrypted inference and encryption using FHE with the Tile Tensors framework.",
      "relevance": "Details the specific costs associated with FHE, including the time taken for encryption/decryption and the expansion of ciphertext size compared to plaintext."
    }
  ],
  "key_equations": [
    {
      "ref": "Communication Cost Formula",
      "content": "Total Cost = (N_k * L * C)",
      "relevance": "Defines the total communication overhead where $N_k$ is the local training dataset size, $L$ is the number of transformer blocks, and $C$ is the size of the encrypted intermediate representation."
    }
  ],
  "section_refs": [
    "Section 5.3",
    "Section 6",
    "Appendix D.2",
    "Appendix D.5"
  ]
}"""

Token usage so far: 324324 prompt tokens, 12759 completion tokens

Cost so far: $3.62601

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "BlindFed achieves a favorable balance between efficiency and performance by significantly reducing the computational burden on clients. It requires 34x to 48x fewer trainable parameters than full fine-tuning and maintains a client-side memory footprint of approximately 9GB, which is nearly half that of full fine-tuning (~18GB). In terms of latency, BlindFed is remarkably efficient, operating at only a 4% increase over linear probing because it eliminates the need for backpropagation through the foundation model backbone. However, the framework's primary bottlenecks are server-side: encrypted inference for a single transformer block takes approximately 136 seconds per sample and requires over 22GB of server memory. Additionally, the use of Fully Homomorphic Encryption (FHE) results in a 2.8x data expansion, increasing the size of intermediate representations from 6.21MB to 17.33MB, which contributes to high communication overhead.",
  "key_figures": [
    {
      "ref": "Figure 10",
      "caption": "Comparison of the efficiency of different adaptation methods in terms of the number of parameters, latency, and memory usage across three datasets: CIFAR-10/SVHN, CIFAR-100, and Fed-ISIC2019.",
      "relevance": "Visually demonstrates that BlindFed achieves near-optimal latency and low memory usage (comparable to linear probing) while providing significantly more adaptability than simple head-only tuning."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 4",
      "caption": "Comparison of the efficiency of our method with baseline approaches in terms of the number of parameters, latency and the memory requirement across four datasets (CIFAR-10/SVHN, CIFAR-100, and Fed-ISIC2019).",
      "relevance": "Provides the exact metrics for trainable parameters, latency per data point, and GPU memory requirements, highlighting BlindFed's efficiency for thin clients."
    },
    {
      "ref": "Table 7",
      "caption": "Computational and memory overhead for encrypted inference and encryption using FHE with the Tile Tensors framework.",
      "relevance": "Details the specific costs associated with FHE, including the time taken for encryption/decryption and the expansion of ciphertext size compared to plaintext."
    }
  ],
  "key_equations": [
    {
      "ref": "Communication Cost Formula",
      "content": "Total Cost = (N_k * L * C)",
      "relevance": "Defines the total communication overhead where $N_k$ is the local training dataset size, $L$ is the number of transformer blocks, and $C$ is the size of the encrypted intermediate representation."
    }
  ],
  "section_refs": [
    "Section 5.3",
    "Section 6",
    "Appendix D.2",
    "Appendix D.5"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 7,
  "title": "Efficiency and Scalability Analysis",
  "summary": "While BlindFed incurs high communication costs and server-side computational complexity due to FHE, it maintains a low memory footprint for clients and demonstrates robust scalability across varying numbers of participants in federated settings.",
  "paper_section": "Results",
  "narrative_role": "results",
  "asset_video": null,
  "duration_stat": {
    "min": 8.0,
    "max": 14.0,
    "avg": 11.0
  }
}

Reference style advice:
Reference Layouts for 'results' section from similar papers:
- Example 1: The slide features a large, bold serif title 'Experiment & Results' positioned at the top-left. The main body of the slide is organized vertically into two primary sections. The top section contains a wide, data-dense table (Table 1) that spans the full width of the slide, comparing various models across four benchmarks (BLINK, Mantis-Eval, MuirBench, MIRB) with and without a 'SoFA' modification. Below this table is a multi-line caption. The bottom section of the slide contains three graphical figures arranged horizontally. On the left, Figure 6 consists of two side-by-side bar charts (labeled A and B) showing attention distribution across image positions, using purple and green colors. To the right, Figure 7 is a single bar chart with green bars representing performance gains across different task types like 'Retrieval' and 'Analogy'. Each figure group has a corresponding caption placed directly beneath it. The slide has a high text and data density, set against a plain white background with a professional color scheme of green and purple accents in the charts.
- Example 2: The slide uses a two-column structure. The left column is a dark-background sidebar containing a detailed, hierarchical outline of the presentation with multiple levels of indentation and color-coded headings (green, blue, orange). The right column is a larger, white-background content area that mimics the layout of a research paper. This main area starts with a centered mathematical equation at the top. Below the equation is a section titled '4.2 CASE STUDY: SINGLE TOKEN GENERATION' containing text with several green-highlighted passages. To the right of this text is a small table (Table 1) comparing perplexity scores. Centered in the middle of the right column is a line chart (Figure 2) showing training NLL curves for various models, followed by a descriptive caption. The bottom of the slide begins section '4.3 DIFFUSION GAP FROM HIGH VARIANCE TRAINING'. A small green pixel-art dinosaur icon is placed in the bottom right corner. The slide is text-dense, integrating technical prose, equations, a table, and a complex data plot.
- Example 3: The slide follows a top-down structure starting with a large, bold serif title in the top-left corner. Directly below the title is a single sentence of introductory text. The middle section of the slide contains a horizontal row of four similar bar charts, labeled (A) through (D), representing different models: OpenFlamingo, Idefics2, LLaVA-NeXT, and GPT-4o. Each chart uses a dual-axis system to plot accuracy (blue stacked bars) and inconsistency (tan bars) across four benchmarks listed on the x-axis. A legend for the chart elements is positioned in the top-left chart. The bottom section of the slide consists of two prominent bullet points that provide a qualitative analysis of the data shown in the charts. The background is plain white, and the text density is moderate, focusing on the relationship between the visual data and the concluding statements.
- Example 4: The slide features a clean white background with a large, bold serif title 'Identifying Position Bias' at the top-left. Below the title is a single line of introductory text describing the dataset. The central portion of the slide contains a horizontal row of four line charts, each representing a different number of images (5, 10, 15, and 20). These charts plot 'Accuracy (%)' against 'Image Position' for several models. A shared legend is positioned horizontally below the first two charts, identifying the models: OpenFlamingo, Idefics2, LLaVA-NeXT, GPT-4o, and a 'random guessing' baseline. The bottom third of the slide consists of two prominent bullet points in a bold serif font that summarize the key findings regarding recency bias in open-source VLMs and 'lost in the middle' bias in proprietary models like GPT-4o. The text density is moderate, with a clear vertical flow from the title to the data and then to the conclusions.
- Example 5: The slide follows a clean, minimalist layout featuring a large, plain-text title 'Results' at the top-left. The main body of the slide is occupied by a single, wide table that presents quantitative performance metrics. This table is organized into two primary sections based on datasets: 'Scannet' and 'Co3D', listed vertically on the left. For each dataset, four methods are compared: 'NeRFmm', 'NoPe-NeRF', 'CF3DGS', and 'Ours'. The table headers are divided into three main evaluation categories: 'Novel-View Synthesis' (with PSNR, SSIM, and LPIPS metrics), 'Depth Estimation' (with AbRel, SqRel, and delta_1 metrics), and 'Pose Estimation' (with RPE_t, RPE_r, and ATE metrics). Arrows next to metric names indicate whether higher or lower values are better. Within the table, the best results are highlighted in bold, and the second-best results are underlined. The overall design uses a white background with black text and horizontal lines to separate table sections, resulting in a moderate to high text density focused entirely on data comparison.

Duration statistics for this section (from references): min=1.0s, max=126.0s, avg=20.1s.

Your job is to decide the **visual layout** for this slide. Do NOT decide builds or animations — those will be planned later.

## CHOOSE THE BEST LAYOUT

Pick the layout template that best suits the content. Common templates include (but you are NOT limited to these):
- `two_col_fig_left` — Figure on left, bullets on right. Best for: method diagrams, architecture figures, or tall/vertical figures.
- `two_col_fig_right` — Bullets on left, figure on right. Best for: motivation slides with illustrative or tall/vertical figures.
- `full_fig_with_callouts` — Large figure with small bullet callouts below. Best for: results, data visualizations, or wide/horizontal figures.
- `one_col_bullets` — Full-width bullets, no figure. Best for: text-heavy overview or summary slides.
- `video_with_caption` — Large video region with small bullet callouts below. Best for: when an `asset_video` is provided.

If none of these fit, invent a descriptive template name and define its regions.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "video": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "bullets": {"x": 0.55, "y": 0.25, "w": 0.4, "h": 0.6}
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "Two-column layout with figure on left is ideal for showing the architecture diagram alongside explanatory bullets."
}

## STRICT RULES:
1. **Region keys**: Only use `title`, `bullets`, `figure`, `video` as region keys. Do NOT invent keys like `callout_1`, `table`, etc.
2. **Coordinates**: All x/y/w/h values must be normalized (0.0 to 1.0). Regions must not overlap.
3. **has_figure**: Set to `true` only if the content summary has relevant figures. If no figure is available, omit `figure` from regions.
4. **has_video**: Set to `true` only if `scene_context` specifically assigns an `asset_video`. If true, include the `video` region. Do not include both `figure` and `video` unless space permits.
5. **No builds**: Do NOT include `build_skeleton`, `expected_build_steps`, or any animation information.
6. Output ONLY valid JSON, no markdown fences, no explanation.

IMPORTANT FIGURE ASPECT RATIO RULE:
If the extracted figure is nearly square, its placement is flexible. However, if the figure has a much larger dimension horizontally (like a wide rectangle), choose a layout with a wide figure region (e.g., `full_fig_with_callouts` or placing it spanning top/bottom) so it is not shrunk awkwardly. If it is very tall/vertical, choose a side-by-side template (e.g., `two_col_fig_left`) where it has vertical space. Ensure your chosen template and `layout_regions` coordinates are decided accordingly to preserve the figure's aspect ratio without shrinking it.


**Answer (from GEMINI)**

"""{
  "layout_template": "full_fig_with_callouts",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "figure": {
      "x": 0.05,
      "y": 0.18,
      "w": 0.9,
      "h": 0.45
    },
    "bullets": {
      "x": 0.05,
      "y": 0.65,
      "w": 0.9,
      "h": 0.3
    }
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "Figure 10 is a wide horizontal composite of three bar charts comparing parameters, latency, and memory. A layout with a wide central figure region is essential to maintain the legibility of these side-by-side charts. Placing bullets at the bottom follows the structure of academic results presentations (like Examples 3 and 4), providing a clear vertical flow from the visual data to the quantitative summary of client-side efficiency and server-side bottlenecks."
}"""

Token usage so far: 337055 prompt tokens, 13068 completion tokens

Cost so far: $3.76259

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "BlindFed achieves a favorable balance between efficiency and performance by significantly reducing the computational burden on clients. It requires 34x to 48x fewer trainable parameters than full fine-tuning and maintains a client-side memory footprint of approximately 9GB, which is nearly half that of full fine-tuning (~18GB). In terms of latency, BlindFed is remarkably efficient, operating at only a 4% increase over linear probing because it eliminates the need for backpropagation through the foundation model backbone. However, the framework's primary bottlenecks are server-side: encrypted inference for a single transformer block takes approximately 136 seconds per sample and requires over 22GB of server memory. Additionally, the use of Fully Homomorphic Encryption (FHE) results in a 2.8x data expansion, increasing the size of intermediate representations from 6.21MB to 17.33MB, which contributes to high communication overhead.",
  "key_figures": [
    {
      "ref": "Figure 10",
      "caption": "Comparison of the efficiency of different adaptation methods in terms of the number of parameters, latency, and memory usage across three datasets: CIFAR-10/SVHN, CIFAR-100, and Fed-ISIC2019.",
      "relevance": "Visually demonstrates that BlindFed achieves near-optimal latency and low memory usage (comparable to linear probing) while providing significantly more adaptability than simple head-only tuning."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 4",
      "caption": "Comparison of the efficiency of our method with baseline approaches in terms of the number of parameters, latency and the memory requirement across four datasets (CIFAR-10/SVHN, CIFAR-100, and Fed-ISIC2019).",
      "relevance": "Provides the exact metrics for trainable parameters, latency per data point, and GPU memory requirements, highlighting BlindFed's efficiency for thin clients."
    },
    {
      "ref": "Table 7",
      "caption": "Computational and memory overhead for encrypted inference and encryption using FHE with the Tile Tensors framework.",
      "relevance": "Details the specific costs associated with FHE, including the time taken for encryption/decryption and the expansion of ciphertext size compared to plaintext."
    }
  ],
  "key_equations": [
    {
      "ref": "Communication Cost Formula",
      "content": "Total Cost = (N_k * L * C)",
      "relevance": "Defines the total communication overhead where $N_k$ is the local training dataset size, $L$ is the number of transformer blocks, and $C$ is the size of the encrypted intermediate representation."
    }
  ],
  "section_refs": [
    "Section 5.3",
    "Section 6",
    "Appendix D.2",
    "Appendix D.5"
  ]
}

The layout has been decided:
{
  "layout_template": "full_fig_with_callouts",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "figure": {
      "x": 0.05,
      "y": 0.18,
      "w": 0.9,
      "h": 0.45
    },
    "bullets": {
      "x": 0.05,
      "y": 0.65,
      "w": 0.9,
      "h": 0.3
    }
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "Figure 10 is a wide horizontal composite of three bar charts comparing parameters, latency, and memory. A layout with a wide central figure region is essential to maintain the legibility of these side-by-side charts. Placing bullets at the bottom follows the structure of academic results presentations (like Examples 3 and 4), providing a clear vertical flow from the visual data to the quantitative summary of client-side efficiency and server-side bottlenecks."
}

Scene context:
{
  "scene_id": 7,
  "title": "Efficiency and Scalability Analysis",
  "summary": "While BlindFed incurs high communication costs and server-side computational complexity due to FHE, it maintains a low memory footprint for clients and demonstrates robust scalability across varying numbers of participants in federated settings.",
  "paper_section": "Results",
  "narrative_role": "results",
  "asset_video": null,
  "duration_stat": {
    "min": 8.0,
    "max": 14.0,
    "avg": 11.0
  }
}

## Previous Content
The following content was drafted for the immediately preceding scenes.
You MUST NOT repeat the exact text content or claims from these previous scenes in your current draft.

{
  "bullets": [
    "Achieves near-LoRA accuracy with double-blind privacy",
    "Outperforms linear probing under extreme data heterogeneity",
    "Scales effectively to 50 clients with stable performance",
    "Robust to out-of-distribution auxiliary distillation data"
  ],
  "audio_content": "BlindFed achieves accuracy comparable to LoRA while maintaining double-blind privacy. It significantly outperforms linear probing, especially under extreme data heterogeneity. The framework scales reliably to fifty clients and remains effective even when the auxiliary distillation data is out-of-distribution."
}


Your job is to **draft the actual content** (title, bullets, audio, figure choice, and duration) that fits into this layout. You do NOT decide the layout — that is already set. You also do NOT decide builds or animations — those will be planned later based on your drafted content.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "title": "A clear, concise slide title",
  "audio_content": "Full narration transcript for this entire scene. Should be natural, conversational, and cover all key points. The duration should be based on the length of this transcript.",
  "duration_sec": 8.5,
  "bullets": [
    "First concise bullet point",
    "Second concise bullet point",
    "Third concise bullet point"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure X",
    "caption": "Brief caption describing the figure"
  },
  "video": {
    "type": "asset_video",
    "path": "clip1.mp4",
    "caption": "Brief caption describing the video contents"
  },
  "source": ["Figure 1", "Section 3.1"],
  "prompt": "Visual description of the scene for generation"
}

## STRICT RULES:
1. **Number of bullets**: Write 2-4 concise, impactful bullets that cover the key points from the extracted content.
2. **Figure/Video assignment**: 
   - Assign `figure` ONLY if the content summary's `key_figures` has relevant images. 
   - Assign `video` ONLY if the `scene_context` assigns an `asset_video`.
   - If the style plan omits `has_figure` or `has_video`, omit the respective block completely.
3. **Bullet text**: Each bullet should be concise (under 15 words preferred), impactful, and directly derived from `extracted_content`. Not a copy — a focused summary.
4. **audio_content**: Natural narration covering all bullet points AND the video clip action if a video is present. 
5. **duration_sec**: First, draft the `audio_content`. Then, CALCULATE the duration: `duration_sec = word_count_of_audio / 2.5`. Do NOT guess. If the stats say 8s but you wrote 40 words, `duration_sec` MUST be 16.0.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "title": "Efficiency and Resource Analysis",
  "audio_content": "BlindFed is highly efficient for clients, requiring up to 48 times fewer parameters and half the memory of full fine-tuning. Latency is nearly identical to linear probing, with only a 4 percent overhead. However, server-side encrypted inference remains a bottleneck, taking 136 seconds per sample with a 2.8-times data expansion due to homomorphic encryption.",
  "duration_sec": 18.4,
  "bullets": [
    "Client-side: 34x-48x fewer parameters and 50% less memory than full fine-tuning",
    "Near-optimal latency: Only 4% overhead compared to simple linear probing",
    "Server-side bottlenecks: 136s inference per sample and 2.8x FHE data expansion"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 10",
    "caption": "Efficiency comparison of adaptation methods across parameters, latency, and memory"
  },
  "source": [
    "Table 4",
    "Table 7",
    "Figure 10",
    "Appendix D.2"
  ],
  "prompt": "A slide showing Figure 10, which contains three bar charts comparing trainable parameters, latency, and GPU memory across different datasets. Below the figure, three bullet points summarize the client-side efficiency gains and the server-side computational bottlenecks mentioned in the text."
}"""

Token usage so far: 348819 prompt tokens, 13413 completion tokens

Cost so far: $3.89058

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "Efficiency and Resource Analysis",
  "audio_content": "BlindFed is highly efficient for clients, requiring up to 48 times fewer parameters and half the memory of full fine-tuning. Latency is nearly identical to linear probing, with only a 4 percent overhead. However, server-side encrypted inference remains a bottleneck, taking 136 seconds per sample with a 2.8-times data expansion due to homomorphic encryption.",
  "duration_sec": 18.4,
  "bullets": [
    "Client-side: 34x-48x fewer parameters and 50% less memory than full fine-tuning",
    "Near-optimal latency: Only 4% overhead compared to simple linear probing",
    "Server-side bottlenecks: 136s inference per sample and 2.8x FHE data expansion"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 10",
    "caption": "Efficiency comparison of adaptation methods across parameters, latency, and memory"
  },
  "source": [
    "Table 4",
    "Table 7",
    "Figure 10",
    "Appendix D.2"
  ],
  "prompt": "A slide showing Figure 10, which contains three bar charts comparing trainable parameters, latency, and GPU memory across different datasets. Below the figure, three bullet points summarize the client-side efficiency gains and the server-side computational bottlenecks mentioned in the text."
}

Layout information:
{
  "layout_template": "full_fig_with_callouts",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "figure": {
      "x": 0.05,
      "y": 0.18,
      "w": 0.9,
      "h": 0.45
    },
    "bullets": {
      "x": 0.05,
      "y": 0.65,
      "w": 0.9,
      "h": 0.3
    }
  },
  "has_figure": true,
  "total_time_sec": 18.4
}

Your job is to:
1. **Decide the build plan** — how many build steps, and what gets revealed in each step.
2. **Assign the drafted bullets to specific build steps** in the best storytelling order.
3. **Split the audio into per-build segments** so each build has matching narration.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "style": "Slides",
  "expected_build_steps": 3,
  "elements": {
    "title": "The slide title from the draft",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure X",
      "caption": "Caption from draft"
    },
    "bullets": [
      "First bullet",
      "Second bullet"
    ]
  },
  "builds": [
    {
      "step_index": 0,
      "time_offset_sec": 0.0,
      "actions": [
        {"type": "show", "target": "title"},
        {"type": "show", "target": "figure"}
      ],
      "audio_segment": "Opening narration for this build step.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 3.0,
      "actions": [
        {"type": "fade_in", "target": "bullets[0]"}
      ],
      "audio_segment": "Narration for the first bullet point.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 6.0,
      "actions": [
        {"type": "fade_in", "target": "bullets[1]"}
      ],
      "audio_segment": "Narration for the second bullet point.",
      "visual_emphasis": []
    }
  ]
}

## STRICT RULES:
1. **Build count**: `expected_build_steps` = 1 + number_of_bullets. Build 0 shows title (and figure/video if present), then one build per bullet.
2. **One bullet per build**: After build 0, each build reveals exactly ONE bullet. `bullets[0]` in build 1, `bullets[1]` in build 2, etc.
3. **Build 0**: Always shows `title` (and `figure`/`video` if present). Never shows bullets in build 0.
4. **Audio segments**: Split the `audio_content` from the draft into segments. Each build's `audio_segment` must be non-empty and correspond to what that build reveals.
5. **Bullet ordering**: Assign bullets to builds in the order that creates the best storytelling flow for the audience.
6. **time_offset_sec**: Space evenly across the total time. For N builds over T seconds: offsets at 0, T/N, 2T/N, etc.
7. **visual_emphasis**: Always set to empty list `[]`.
8. **Action targets**: Only use targets that exist in `elements`: `title`, `figure`, `video`, `bullets[0]`, `bullets[1]`, etc.
9. **elements**: Copy the drafted title, figure, video, and bullets exactly — do not modify the text content.
10. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""```json
{
  "style": "Slides",
  "expected_build_steps": 4,
  "elements": {
    "title": "Efficiency and Resource Analysis",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 10",
      "caption": "Efficiency comparison of adaptation methods across parameters, latency, and memory"
    },
    "bullets": [
      "Client-side: 34x-48x fewer parameters and 50% less memory than full fine-tuning",
      "Near-optimal latency: Only 4% overhead compared to simple linear probing",
      "Server-side bottlenecks: 136s inference per sample and 2.8x FHE data expansion"
    ]
  },
  "builds": [
    {
      "step_index": 0,
      "time_offset_sec": 0.0,
      "actions": [
        {
          "type": "show",
          "target": "title"
        },
        {
          "type": "show",
          "target": "figure"
        }
      ],
      "audio_segment": "BlindFed is highly efficient for clients,",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 4.6,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[0]"
        }
      ],
      "audio_segment": "requiring up to 48 times fewer parameters and half the memory of full fine-tuning.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 9.2,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[1]"
        }
      ],
      "audio_segment": "Latency is nearly identical to linear probing, with only a 4 percent overhead.",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 13.8,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[2]"
        }
      ],
      "audio_segment": "However, server-side encrypted inference remains a bottleneck, taking 136 seconds per sample with a 2.8-times data expansion due to homomorphic encryption.",
      "visual_emphasis": []
    }
  ]
}
```"""

Token usage so far: 360055 prompt tokens, 14027 completion tokens

Cost so far: $4.02136

_Note: These user-assistant interactions are independent and the system message is always attached in each turn for GPT._

**System message for GPT**

You are an expert in reading academic papers and creating video summaries based on them. 

_Note: These user-assistant interactions are independent and the system message is always attached in each turn for GPT._

**System message for GPT**

You are an expert in reading academic papers and creating video summaries based on them. 

_Note: These user-assistant interactions are independent and the system message is always attached in each turn for GPT._

**System message for GPT**

You are an expert in reading academic papers and creating video summaries based on them. 

**Question**

You are an expert presentation designer for academic video summaries.

You are designing the TITLE PAGE layout for a paper presentation video.

Paper metadata:
{
  "paper_title": "A Framework for Double-Blind Federated Adaptation of Foundation Models",
  "authors": [
    {
      "name": "Nurbek Tastan",
      "affiliation_id": 1
    },
    {
      "name": "Karthik Nandakumar",
      "affiliation_id": 2
    }
  ],
  "affiliations": [
    {
      "id": 1,
      "name": "Mohamed bin Zayed University of Artificial Intelligence (MBZUAI), UAE",
      "email_domain": "mbzuai.ac.ae"
    },
    {
      "id": 2,
      "name": "Michigan State University (MSU), USA",
      "email_domain": "msu.edu"
    }
  ],
  "venue": ""
}

Available logos:
No logos available.

Design a visually clean, professional title page layout. Use the reference style of academic presentation title slides:
- Conference logo in a top corner
- Affiliation logos grouped together (top row or below authors)
- Paper title large and centered
- Authors centered below title
- Affiliation text small, centered
- Venue name at bottom

IMPORTANT: Vary the placement naturally — do NOT always put logos in the same position. Sometimes conference logo goes top-left, sometimes top-right. Sometimes affiliation logos go in the top row, sometimes below authors. Be creative but professional.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "layout_template": "title_page",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "conference_logo": {"x": 0.0, "y": 0.0, "w": 0.15, "h": 0.12},
    "affiliation_logos": {"x": 0.5, "y": 0.0, "w": 0.45, "h": 0.12},
    "title": {"x": 0.05, "y": 0.25, "w": 0.9, "h": 0.25},
    "authors": {"x": 0.1, "y": 0.55, "w": 0.8, "h": 0.12},
    "affiliations": {"x": 0.1, "y": 0.7, "w": 0.8, "h": 0.08},
    "venue": {"x": 0.3, "y": 0.82, "w": 0.4, "h": 0.06}
  },
  "style_rationale": "Brief explanation of why this positioning works."
}

## STRICT RULES:
1. All x/y/w/h values must be normalized (0.0 to 1.0). Regions must not overlap.
2. If no conference logo is available, omit the conference_logo region.
3. If no affiliation logos are available, omit the affiliation_logos region.
4. The title region should be generous — wide enough for long titles to wrap.
5. Keep at least 5% margin from all edges.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "layout_template": "title_page",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.2,
      "w": 0.9,
      "h": 0.25
    },
    "authors": {
      "x": 0.1,
      "y": 0.5,
      "w": 0.8,
      "h": 0.1
    },
    "affiliations": {
      "x": 0.1,
      "y": 0.62,
      "w": 0.8,
      "h": 0.15
    },
    "venue": {
      "x": 0.2,
      "y": 0.85,
      "w": 0.6,
      "h": 0.05
    }
  },
  "style_rationale": "A clean, centered layout is chosen to maintain a professional academic aesthetic. Since no logos are available, the focus is entirely on the title and author information, with generous spacing to ensure readability of the long paper title."
}"""

Token usage so far: 10654 prompt tokens, 287 completion tokens

Cost so far: $0.11515

