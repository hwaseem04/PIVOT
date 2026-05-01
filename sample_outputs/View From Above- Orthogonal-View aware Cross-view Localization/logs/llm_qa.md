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
    "title": "Challenges in Cross-view Localization",
    "summary": "Visual-based cross-view localization aims to match street-level query images with aerial maps. However, significant viewpoint differences, domain gaps, and the neglect of off-ground features like streetlights and trees often lead to unreliable localization in challenging scenarios.",
    "paper_section": "Introduction",
    "narrative_role": "introduction",
    "asset_video": null,
    "duration_stat": {
      "min": 5.0,
      "max": 12.0,
      "avg": 8.0
    }
  },
  {
    "scene_id": 2,
    "title": "Top-to-Ground Aggregation (T2GA) Module",
    "summary": "The proposed T2GA module aggregates features from elevated pixels onto the corresponding on-ground pixel features. By leveraging reliable off-ground information and handling visual occlusions, it improves feature alignment between ground and aerial orthographic views.",
    "paper_section": "Method",
    "narrative_role": "method",
    "asset_video": null,
    "duration_stat": {
      "min": 8.0,
      "max": 15.0,
      "avg": 11.0
    }
  },
  {
    "scene_id": 3,
    "title": "Cycle Domain Adaptation (CycDA) Loss",
    "summary": "To address variations in camera types, lighting, and resolutions, the Cycle Domain Adaptation (CycDA) loss is introduced. It enforces view-invariant representations by minimizing discrepancies between domain-adapted features and their target counterparts across ground and aerial views.",
    "paper_section": "Method",
    "narrative_role": "method",
    "asset_video": null,
    "duration_stat": {
      "min": 7.0,
      "max": 14.0,
      "avg": 10.0
    }
  },
  {
    "scene_id": 4,
    "title": "Equidistant Re-projection (ERP) Loss",
    "summary": "The Equidistant Re-projection (ERP) loss mitigates the bias toward closer keypoints by applying a distance-weighted approach. This ensures orientation errors are independent of keypoint distance, leading to a more uniform distribution of keypoints and precise orientation estimation.",
    "paper_section": "Method",
    "narrative_role": "method",
    "asset_video": null,
    "duration_stat": {
      "min": 7.0,
      "max": 14.0,
      "avg": 10.0
    }
  },
  {
    "scene_id": 5,
    "title": "Experimental Results on KITTI and Ford Datasets",
    "summary": "Evaluations on KITTI and Ford Multi-AV datasets show that the method consistently achieves the lowest mean longitudinal and lateral translation errors. It demonstrates superior robustness, particularly when the initial pose is less accurate, outperforming existing pixel-wise and patch-wise methods.",
    "paper_section": "Experiments",
    "narrative_role": "experiments",
    "asset_video": null,
    "duration_stat": {
      "min": 8.0,
      "max": 15.0,
      "avg": 12.0
    }
  },
  {
    "scene_id": 6,
    "title": "Continual Vehicle Pose Estimation",
    "summary": "The system can complete entire routes through continual vehicle pose estimation, requiring only an initial pose at the starting point. This capability highlights its generalization ability and potential for practical deployment in autonomous driving and outdoor robotics.",
    "paper_section": "Results",
    "narrative_role": "results",
    "asset_video": null,
    "duration_stat": {
      "min": 6.0,
      "max": 13.0,
      "avg": 9.0
    }
  }
]
```"""

Token usage so far: 5656 prompt tokens, 952 completion tokens

Cost so far: $0.08512

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
  "paper_title": "View From Above: Orthogonal-View aware Cross-view Localization",
  "authors": [
    {"name": "Shan Wang", "affiliation_id": 1},
    {"name": "Chuong Nguyen", "affiliation_id": 1},
    {"name": "Jiawei Liu", "affiliation_id": 2},
    {"name": "Yanhao Zhang", "affiliation_id": 2},
    {"name": "Sundaram Muthu", "affiliation_id": 1},
    {"name": "Fahira Afzal Maken", "affiliation_id": 1},
    {"name": "Kaihao Zhang", "affiliation_id": 2},
    {"name": "Hongdong Li", "affiliation_id": 2}
  ],
  "affiliations": [
    {"id": 1, "name": "Data61, CSIRO", "email_domain": ""},
    {"id": 2, "name": "Australian National University", "email_domain": ""}
  ],
  "venue": "CVPR 2024"
}"""

Token usage so far: 11219 prompt tokens, 1207 completion tokens

Cost so far: $0.14840

**Question**

You are an expert presentation designer for academic video summaries.

You are designing the TITLE PAGE layout for a paper presentation video.

Paper metadata:
{
  "paper_title": "View From Above: Orthogonal-View aware Cross-view Localization",
  "authors": [
    {
      "name": "Shan Wang",
      "affiliation_id": 1
    },
    {
      "name": "Chuong Nguyen",
      "affiliation_id": 1
    },
    {
      "name": "Jiawei Liu",
      "affiliation_id": 2
    },
    {
      "name": "Yanhao Zhang",
      "affiliation_id": 2
    },
    {
      "name": "Sundaram Muthu",
      "affiliation_id": 1
    },
    {
      "name": "Fahira Afzal Maken",
      "affiliation_id": 1
    },
    {
      "name": "Kaihao Zhang",
      "affiliation_id": 2
    },
    {
      "name": "Hongdong Li",
      "affiliation_id": 2
    }
  ],
  "affiliations": [
    {
      "id": 1,
      "name": "Data61, CSIRO",
      "email_domain": ""
    },
    {
      "id": 2,
      "name": "Australian National University",
      "email_domain": ""
    }
  ],
  "venue": "CVPR 2024"
}

Available logos:
conference_logo: figure3.png
affiliation_1_logo: figure2.png (Data61, CSIRO)
affiliation_2_logo: figure.png (Australian National University)

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
    "conference_logo": {"x": 0.8, "y": 0.05, "w": 0.15, "h": 0.1},
    "affiliation_logos": {"x": 0.05, "y": 0.05, "w": 0.35, "h": 0.1},
    "title": {"x": 0.1, "y": 0.25, "w": 0.8, "h": 0.2},
    "authors": {"x": 0.1, "y": 0.5, "w": 0.8, "h": 0.15},
    "affiliations": {"x": 0.1, "y": 0.68, "w": 0.8, "h": 0.1},
    "venue": {"x": 0.3, "y": 0.85, "w": 0.4, "h": 0.06}
  },
  "style_rationale": "This layout uses a balanced top-row approach for logos, placing the affiliation logos on the left and the conference logo on the right to frame the slide. The title is given a large central area for readability, followed by a clear vertical hierarchy for authors, affiliation text, and the venue at the bottom, adhering to standard academic presentation aesthetics."
}"""

Token usage so far: 20930 prompt tokens, 1589 completion tokens

Cost so far: $0.25697

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 1,
  "title": "Challenges in Cross-view Localization",
  "summary": "Visual-based cross-view localization aims to match street-level query images with aerial maps. However, significant viewpoint differences, domain gaps, and the neglect of off-ground features like streetlights and trees often lead to unreliable localization in challenging scenarios.",
  "paper_section": "Introduction",
  "narrative_role": "introduction",
  "asset_video": null,
  "duration_stat": {
    "min": 5.0,
    "max": 12.0,
    "avg": 8.0
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
  "extracted_content": "Visual-based cross-view localization aims to determine the position of street-level query images within a satellite or aerial view map. While satellite imagery is now widely accessible via platforms like Google Maps, achieving accurate localization remains difficult due to the extreme viewpoint differences between ground and aerial perspectives. These differences create a significant domain gap that compromises feature alignment. Existing research typically follows two paths: generative-based methods that transform view styles, which can introduce pose estimation ambiguities, and geometry-alignment-based methods that focus primarily on on-ground pixels. A major limitation of current techniques is the neglect of off-ground features (such as streetlights) and an inability to handle visual occlusions (such as treetops obscuring road details). This leads to a lack of robustness in scenarios where road markings are degraded or obscured, necessitating a method that can leverage reliable off-ground information to improve alignment.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Efficacy of T2GA. T2GA aggregates off-ground features (e.g., the streetlight within the green square) and addresses occlusions (e.g., the tree within the red square). Unlike conventional methods that often overlook such elements, T2GA integrates these features, thus improving appearance matching for groundlevel aligned pixels across views using ground plane homography. Insets are magnified for clarity, with dotted outlines indicating appearance misalignment and solid outlines indicating appearance alignment with the corresponding aerial view features.",
      "relevance": "This figure visually demonstrates the core challenges mentioned in the introduction: the misalignment of off-ground features and the problem of occlusions in standard cross-view matching."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": ["1. Introduction"]
}"""

Token usage so far: 26774 prompt tokens, 1978 completion tokens

Cost so far: $0.32708

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "Visual-based cross-view localization aims to determine the position of street-level query images within a satellite or aerial view map. While satellite imagery is now widely accessible via platforms like Google Maps, achieving accurate localization remains difficult due to the extreme viewpoint differences between ground and aerial perspectives. These differences create a significant domain gap that compromises feature alignment. Existing research typically follows two paths: generative-based methods that transform view styles, which can introduce pose estimation ambiguities, and geometry-alignment-based methods that focus primarily on on-ground pixels. A major limitation of current techniques is the neglect of off-ground features (such as streetlights) and an inability to handle visual occlusions (such as treetops obscuring road details). This leads to a lack of robustness in scenarios where road markings are degraded or obscured, necessitating a method that can leverage reliable off-ground information to improve alignment.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Efficacy of T2GA. T2GA aggregates off-ground features (e.g., the streetlight within the green square) and addresses occlusions (e.g., the tree within the red square). Unlike conventional methods that often overlook such elements, T2GA integrates these features, thus improving appearance matching for groundlevel aligned pixels across views using ground plane homography. Insets are magnified for clarity, with dotted outlines indicating appearance misalignment and solid outlines indicating appearance alignment with the corresponding aerial view features.",
      "relevance": "This figure visually demonstrates the core challenges mentioned in the introduction: the misalignment of off-ground features and the problem of occlusions in standard cross-view matching."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "1. Introduction"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 1,
  "title": "Challenges in Cross-view Localization",
  "summary": "Visual-based cross-view localization aims to match street-level query images with aerial maps. However, significant viewpoint differences, domain gaps, and the neglect of off-ground features like streetlights and trees often lead to unreliable localization in challenging scenarios.",
  "paper_section": "Introduction",
  "narrative_role": "introduction",
  "asset_video": null,
  "duration_stat": {
    "min": 5.0,
    "max": 12.0,
    "avg": 8.0
  }
}

Reference style advice:
Reference Layouts for 'introduction' section from similar papers:
- Example 1: The slide follows a clean, minimalist single-column layout on a plain white background. The title 'Motivation' is placed at the top-left in a large, bold serif font. The main body consists of three distinct text sections. The first section introduces a problem statement regarding trade-offs in previous works, followed by a single-level bulleted list containing three items: 'Generalization ability', 'Test-time efficiency', and 'Camera pose accuracy'. Below this, a second paragraph discusses the promise of recent foundation models like DUSt3R. The final text block is a single sentence that explicitly states the motivation for the current work. All body text is left-aligned and uses a serif typeface. A small citation footer is located at the bottom-left corner of the slide. The text density is light, leaving ample white space.
- Example 2: The slide uses a mixed layout to define a specific research task. The title is positioned at the top left in a large, bold font. Directly below it on the left side is a 'Definition' section with bolded text. In the bottom-left quadrant, there is a 3D diagram showing a camera's frustum directed at a dining table set, illustrating the concept of occlusion. The right half of the slide is dominated by a large, multi-part diagram. This diagram features a top-down grid representing a '3D distribution of chairs' and a vertical bar on its left representing an 'Outpainted image' and '2D distribution of chairs'. Within this grid, red circles labeled 'A' and 'B' identify specific regions, and a mathematical expression for conditional probability is included. A horizontal legend box at the bottom right defines the labels A (Occluded), B (Out-of-frame), and C (Camera Center). The top right corner contains a QR code and a university logo, and the page number '11' is located at the bottom right. The slide has a moderate text density and uses a clean white background.
- Example 3: The slide uses a clean white background with a large, serif-font title 'Problem definition' aligned to the top-left. Below the title, a single line of text states the primary goal: 'Reconstruct dense 3D point cloud of a scene from RGB videos'. This is followed by two bullet points that define the 'Input' (RGB video with unknown camera parameters) and 'Output' (dense 3D points in a unified coordinate system), with key terms highlighted in bold. The bottom section of the slide features a visual flow diagram: on the left is a sample frame from an indoor RGB video, followed by a bright blue horizontal arrow pointing to the right, which leads to a visualization of a dense 3D point cloud of the same scene. Each image has a centered label underneath it ('RGB video' and 'Dense 3D points'). The text density is light, prioritizing a clear visual representation of the problem statement.
- Example 4: The slide follows a minimalist single-column layout on a plain white background. The title, 'Problem definition', is located at the top-left in a large, black serif font. The main content consists of two distinct text blocks, each starting with a bolded sub-heading. The first block, titled 'Relative camera pose estimation', contains two bullet points defining the input as a pair of images and the output as the relative camera pose. The second block, titled 'Visual localization (absolute pose)', similarly uses two bullet points to define the input as a database of posed images plus a query image, and the output as the absolute camera pose. All text is left-aligned with standard indentation for the bullet points, resulting in a light text density and a clear, hierarchical structure.
- Example 5: The slide follows a clean, minimalist single-column layout with a plain white background and black text. The title 'Motivation' is located at the top-left in a large serif font. The main content consists of three distinct text sections. The first section introduces a problem statement followed by a single-level bulleted list containing three items: 'Generalization ability', 'Test-time efficiency', and 'Camera pose accuracy'. Below this list is a second paragraph discussing recent foundation models like DUSt3R. The third and final text block is a concluding sentence that states the research objective. A small citation for the DUSt3R paper is positioned at the bottom-left corner. The text density is light, with generous white space between the sections.

Duration statistics for this section (from references): min=1.0s, max=48.4s, avg=10.8s.

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
      "x": 0.48,
      "y": 0.2,
      "w": 0.47,
      "h": 0.7
    }
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "A two-column layout with bullets on the left and the figure on the right is chosen to introduce the core challenges. This allows the text to define the domain gap and viewpoint differences while Figure 1 provides a direct visual comparison of ground and aerial views, highlighting specific issues like occlusions and off-ground features. This follows the minimalist and clear style of the reference examples, prioritizing white space and a logical flow from problem definition to visual evidence."
}"""

Token usage so far: 34387 prompt tokens, 2283 completion tokens

Cost so far: $0.41236

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "Visual-based cross-view localization aims to determine the position of street-level query images within a satellite or aerial view map. While satellite imagery is now widely accessible via platforms like Google Maps, achieving accurate localization remains difficult due to the extreme viewpoint differences between ground and aerial perspectives. These differences create a significant domain gap that compromises feature alignment. Existing research typically follows two paths: generative-based methods that transform view styles, which can introduce pose estimation ambiguities, and geometry-alignment-based methods that focus primarily on on-ground pixels. A major limitation of current techniques is the neglect of off-ground features (such as streetlights) and an inability to handle visual occlusions (such as treetops obscuring road details). This leads to a lack of robustness in scenarios where road markings are degraded or obscured, necessitating a method that can leverage reliable off-ground information to improve alignment.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Efficacy of T2GA. T2GA aggregates off-ground features (e.g., the streetlight within the green square) and addresses occlusions (e.g., the tree within the red square). Unlike conventional methods that often overlook such elements, T2GA integrates these features, thus improving appearance matching for groundlevel aligned pixels across views using ground plane homography. Insets are magnified for clarity, with dotted outlines indicating appearance misalignment and solid outlines indicating appearance alignment with the corresponding aerial view features.",
      "relevance": "This figure visually demonstrates the core challenges mentioned in the introduction: the misalignment of off-ground features and the problem of occlusions in standard cross-view matching."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "1. Introduction"
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
      "x": 0.48,
      "y": 0.2,
      "w": 0.47,
      "h": 0.7
    }
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "A two-column layout with bullets on the left and the figure on the right is chosen to introduce the core challenges. This allows the text to define the domain gap and viewpoint differences while Figure 1 provides a direct visual comparison of ground and aerial views, highlighting specific issues like occlusions and off-ground features. This follows the minimalist and clear style of the reference examples, prioritizing white space and a logical flow from problem definition to visual evidence."
}

Scene context:
{
  "scene_id": 1,
  "title": "Challenges in Cross-view Localization",
  "summary": "Visual-based cross-view localization aims to match street-level query images with aerial maps. However, significant viewpoint differences, domain gaps, and the neglect of off-ground features like streetlights and trees often lead to unreliable localization in challenging scenarios.",
  "paper_section": "Introduction",
  "narrative_role": "introduction",
  "asset_video": null,
  "duration_stat": {
    "min": 5.0,
    "max": 12.0,
    "avg": 8.0
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
  "title": "Challenges in Cross-view Localization",
  "audio_content": "Matching street-level images to aerial maps is difficult due to extreme viewpoint differences. Standard methods often ignore off-ground features and struggle with occlusions, compromising localization accuracy in complex scenes.",
  "duration_sec": 11.6,
  "bullets": [
    "Extreme viewpoint differences create a significant domain gap",
    "Neglect of off-ground features like streetlights and poles",
    "Visual occlusions from trees compromise feature alignment"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 1",
    "caption": "Visualizing viewpoint differences and occlusions"
  },
  "source": [
    "Figure 1",
    "Section 1"
  ],
  "prompt": "A slide showing the challenges of cross-view localization. On the left, bullet points describe viewpoint differences and occlusions. On the right, Figure 1 from the paper illustrates these issues by comparing ground and aerial views of streetlights and trees."
}"""

Token usage so far: 41040 prompt tokens, 2527 completion tokens

Cost so far: $0.48621

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "Challenges in Cross-view Localization",
  "audio_content": "Matching street-level images to aerial maps is difficult due to extreme viewpoint differences. Standard methods often ignore off-ground features and struggle with occlusions, compromising localization accuracy in complex scenes.",
  "duration_sec": 11.6,
  "bullets": [
    "Extreme viewpoint differences create a significant domain gap",
    "Neglect of off-ground features like streetlights and poles",
    "Visual occlusions from trees compromise feature alignment"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 1",
    "caption": "Visualizing viewpoint differences and occlusions"
  },
  "source": [
    "Figure 1",
    "Section 1"
  ],
  "prompt": "A slide showing the challenges of cross-view localization. On the left, bullet points describe viewpoint differences and occlusions. On the right, Figure 1 from the paper illustrates these issues by comparing ground and aerial views of streetlights and trees."
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
      "x": 0.48,
      "y": 0.2,
      "w": 0.47,
      "h": 0.7
    }
  },
  "has_figure": true,
  "total_time_sec": 11.6
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
    "title": "Challenges in Cross-view Localization",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 1",
      "caption": "Visualizing viewpoint differences and occlusions"
    },
    "bullets": [
      "Extreme viewpoint differences create a significant domain gap",
      "Neglect of off-ground features like streetlights and poles",
      "Visual occlusions from trees compromise feature alignment"
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
      "audio_segment": "Matching street-level images to aerial maps is difficult",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 2.9,
      "actions": [
        {"type": "fade_in", "target": "bullets[0]"}
      ],
      "audio_segment": "due to extreme viewpoint differences.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 5.8,
      "actions": [
        {"type": "fade_in", "target": "bullets[1]"}
      ],
      "audio_segment": "Standard methods often ignore off-ground features",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 8.7,
      "actions": [
        {"type": "fade_in", "target": "bullets[2]"}
      ],
      "audio_segment": "and struggle with occlusions, compromising localization accuracy in complex scenes.",
      "visual_emphasis": []
    }
  ]
}"""

Token usage so far: 47492 prompt tokens, 3018 completion tokens

Cost so far: $0.56546

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 2,
  "title": "Top-to-Ground Aggregation (T2GA) Module",
  "summary": "The proposed T2GA module aggregates features from elevated pixels onto the corresponding on-ground pixel features. By leveraging reliable off-ground information and handling visual occlusions, it improves feature alignment between ground and aerial orthographic views.",
  "paper_section": "Method",
  "narrative_role": "method",
  "asset_video": null,
  "duration_stat": {
    "min": 8.0,
    "max": 15.0,
    "avg": 11.0
  }
}

## Previous Scenes Memory
The following content was extracted for the immediately preceding scenes. **This is provided as a memory of what the audience has JUST seen.**
You MUST NOT repeat the claims, figures, tables, or equations from these previous scenes in your current extraction, to ensure the presentation maintains forward momentum without redundant slides.
If you must reference the exactly same figure/table, the 'relevance' MUST be clearly unique to avoid narrative duplication.

{
  "extracted_content": "Visual-based cross-view localization aims to determine the position of street-level query images within a satellite or aerial view map. While satellite imagery is now widely accessible via platforms like Google Maps, achieving accurate localization remains difficult due to the extreme viewpoint differences between ground and aerial perspectives. These differences create a significant domain gap that compromises feature alignment. Existing research typically follows two paths: generative-based methods that transform view styles, which can introduce pose estimation ambiguities, and geometry-alignment-based methods that focus primarily on on-ground pixels. A major limitation of current techniques is the neglect of off-ground features (such as streetlights) and an inability to handle visual occlusions (such as treetops obscuring road details). This leads to a lack of robustness in scenarios where road markings are degraded or obscured, necessitating a method that can leverage reliable off-ground information to improve alignment.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Efficacy of T2GA. T2GA aggregates off-ground features (e.g., the streetlight within the green square) and addresses occlusions (e.g., the tree within the red square). Unlike conventional methods that often overlook such elements, T2GA integrates these features, thus improving appearance matching for groundlevel aligned pixels across views using ground plane homography. Insets are magnified for clarity, with dotted outlines indicating appearance misalignment and solid outlines indicating appearance alignment with the corresponding aerial view features.",
      "relevance": "This figure visually demonstrates the core challenges mentioned in the introduction: the misalignment of off-ground features and the problem of occlusions in standard cross-view matching."
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
  "extracted_content": "The Top-to-Ground Aggregation (T2GA) module is designed to bridge the appearance gap for tall structures and occluded objects by aligning their ground-level representations. It operates on the principle that while elevated objects look different from ground and aerial views, their base positions on the ground plane are geometrically consistent. T2GA uses a transformer-based attention mechanism where on-ground pixels serve as queries to aggregate features from elevated pixels in the same vertical column. This allows the model to either fuse features of the same object or replace occluded ground features with reliable information from above. The resulting aggregated feature map ($F^a$) is formed by vertically stacking these attention-weighted features with the original ground features. This process ensures that landmarks like traffic signal poles, which might be ignored by standard methods, receive higher confidence values and are sampled as keypoints for more precise vehicle pose estimation.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "Our method adopts PureACL [24] as the baseline model and introduces three novel components (highlighted in red): (1) T2GA (Sec.4.1): aggregates the features of elevated pixels onto the feature of the on-ground pixel that is directly beneath them to alleviate the representation gap of the same object across different views; (2) CycDA Loss (Sec.4.2): explicitly enforces a view-invariant representation for the same object; and (3) ERP Loss (Sec.4.3): allows the model to leverage key points that are farther away from the vehicle while allocating more emphasis on correcting the vehicle orientation estimation.",
      "relevance": "Provides the architectural context, showing how the T2GA module integrates into the feature extraction and matching pipeline."
    },
    {
      "ref": "Figure 3",
      "caption": "Attention between the on-ground pixels and their corresponding elevated pixels is displayed column-wise. (Left example): The attention between the base and top of the streetlight is high despite their distinct appearances. This allows the resultant aggregated ground feature to be aligned with the satellite feature corresponding to the matching geographic location. (Right example): In the absence of occlusion from above, ground pixels maintain minimal attention with their elevated pixels. This avoids unnecessary dilution of the ground features which are already well aligned with their satellite counterparts.",
      "relevance": "Visualizes the column-wise attention mechanism that allows on-ground pixels to 'pull' features from elevated structures like streetlights."
    },
    {
      "ref": "Figure 4",
      "caption": "Illustration on the effect of T2GA on the confidence map of the baseline model. The confidence map without T2GA (Left) predominantly highlights road marks and curbs, resulting in subsequent keypoint sampling missing important road landmarks, e.g. traffic signal poles, that provide important cues to vehicle pose estimation; The confidence map with T2GA (Right) has high confidence values distributed across various road marks and traffic poles. With more geographic cues provided by multiple sources, the resultant pose prediction becomes more precise and robust.",
      "relevance": "Demonstrates the practical impact of T2GA on the confidence map, showing it successfully identifies vertical landmarks that standard methods miss."
    }
  ],
  "key_tables": [],
  "key_equations": [
    {
      "ref": "Equation 2",
      "content": "F^{att}[p] = \\text{Softmax}(\\mathbf{Q}\\mathbf{K}^T)\\mathbf{V}",
      "relevance": "Defines the core attention mechanism used to aggregate elevated features (V) onto on-ground pixels (p) using queries (Q) and keys (K)."
    },
    {
      "ref": "Equation 3",
      "content": "F^a = F^g_{0:H^g-\\tau} \\oplus F^{att}",
      "relevance": "Shows how the aggregated feature map is constructed by vertically stacking the attention-weighted features with the original ground features."
    }
  ],
  "section_refs": [
    "Section 4.1"
  ]
}"""

Token usage so far: 53809 prompt tokens, 3917 completion tokens

Cost so far: $0.65560

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "The Top-to-Ground Aggregation (T2GA) module is designed to bridge the appearance gap for tall structures and occluded objects by aligning their ground-level representations. It operates on the principle that while elevated objects look different from ground and aerial views, their base positions on the ground plane are geometrically consistent. T2GA uses a transformer-based attention mechanism where on-ground pixels serve as queries to aggregate features from elevated pixels in the same vertical column. This allows the model to either fuse features of the same object or replace occluded ground features with reliable information from above. The resulting aggregated feature map ($F^a$) is formed by vertically stacking these attention-weighted features with the original ground features. This process ensures that landmarks like traffic signal poles, which might be ignored by standard methods, receive higher confidence values and are sampled as keypoints for more precise vehicle pose estimation.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "Our method adopts PureACL [24] as the baseline model and introduces three novel components (highlighted in red): (1) T2GA (Sec.4.1): aggregates the features of elevated pixels onto the feature of the on-ground pixel that is directly beneath them to alleviate the representation gap of the same object across different views; (2) CycDA Loss (Sec.4.2): explicitly enforces a view-invariant representation for the same object; and (3) ERP Loss (Sec.4.3): allows the model to leverage key points that are farther away from the vehicle while allocating more emphasis on correcting the vehicle orientation estimation.",
      "relevance": "Provides the architectural context, showing how the T2GA module integrates into the feature extraction and matching pipeline."
    },
    {
      "ref": "Figure 3",
      "caption": "Attention between the on-ground pixels and their corresponding elevated pixels is displayed column-wise. (Left example): The attention between the base and top of the streetlight is high despite their distinct appearances. This allows the resultant aggregated ground feature to be aligned with the satellite feature corresponding to the matching geographic location. (Right example): In the absence of occlusion from above, ground pixels maintain minimal attention with their elevated pixels. This avoids unnecessary dilution of the ground features which are already well aligned with their satellite counterparts.",
      "relevance": "Visualizes the column-wise attention mechanism that allows on-ground pixels to 'pull' features from elevated structures like streetlights."
    },
    {
      "ref": "Figure 4",
      "caption": "Illustration on the effect of T2GA on the confidence map of the baseline model. The confidence map without T2GA (Left) predominantly highlights road marks and curbs, resulting in subsequent keypoint sampling missing important road landmarks, e.g. traffic signal poles, that provide important cues to vehicle pose estimation; The confidence map with T2GA (Right) has high confidence values distributed across various road marks and traffic poles. With more geographic cues provided by multiple sources, the resultant pose prediction becomes more precise and robust.",
      "relevance": "Demonstrates the practical impact of T2GA on the confidence map, showing it successfully identifies vertical landmarks that standard methods miss."
    }
  ],
  "key_tables": [],
  "key_equations": [
    {
      "ref": "Equation 2",
      "content": "F^{att}[p] = \text{Softmax}(\\mathbf{Q}\\mathbf{K}^T)\\mathbf{V}",
      "relevance": "Defines the core attention mechanism used to aggregate elevated features (V) onto on-ground pixels (p) using queries (Q) and keys (K)."
    },
    {
      "ref": "Equation 3",
      "content": "F^a = F^g_{0:H^g-\tau} \\oplus F^{att}",
      "relevance": "Shows how the aggregated feature map is constructed by vertically stacking the attention-weighted features with the original ground features."
    }
  ],
  "section_refs": [
    "Section 4.1"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 2,
  "title": "Top-to-Ground Aggregation (T2GA) Module",
  "summary": "The proposed T2GA module aggregates features from elevated pixels onto the corresponding on-ground pixel features. By leveraging reliable off-ground information and handling visual occlusions, it improves feature alignment between ground and aerial orthographic views.",
  "paper_section": "Method",
  "narrative_role": "method",
  "asset_video": null,
  "duration_stat": {
    "min": 8.0,
    "max": 15.0,
    "avg": 11.0
  }
}

Reference style advice:
Reference Layouts for 'method' section from similar papers:
- Example 1: The slide features a large, bold title 'CycDA Loss' positioned at the top-left corner. The main content consists of a large, centered architectural diagram that illustrates a cyclic data flow. The diagram uses mathematical notation for its nodes, such as f_g, m_g, f_s, and m_s, connected by single-headed arrows representing transformations through an encoder (E) and a decoder (D). Small circles with a 'c' inside indicate concatenation or combination points. Vertical double-headed arrows connect corresponding top and bottom nodes, labeled with 'L2 loss' to indicate where loss functions are applied. The layout is clean and minimalist, using a black-and-white color scheme on a plain white background, with a light text density focused on the visual logic of the method.
- Example 2: The slide has a minimalist design with a solid black background. A single line of white, bold text is centered at the top, acting as the title. The main content is a large, centered image showing a first-person view of a street in a residential area. Overlaid on this image are several explanatory annotations: a horizontal purple line runs across the bottom, with a small yellow square labeled 'query pixel' on its right side. A vertical dashed white line extends from this yellow square towards the top of the image. A label 'Reference pixels' with a white arrow points to this dashed line, illustrating the spatial relationship described in the title. The text density is very light, relying primarily on the annotated image to convey information.
- Example 3: The slide features a clean, two-column layout on a white background. At the top-left, the title 'Task: Find chairs' is displayed in a simple sans-serif font. The left column contains a large, black-bordered box labeled 'Input Frame' which shows a 3D diagram of a camera on the left pointing towards a dining table with six blue chairs; orange perspective lines illustrate the camera's field of view. The right column displays a cropped, dark-background image showing a close-up of two blue chairs, each enclosed in a bright green rectangular bounding box to demonstrate object detection. In the top-right corner, there is a QR code next to a gold-colored institutional logo. A small page number '5' is positioned at the bottom-right corner. The text density is light, with the slide primarily using visual diagrams to explain a computer vision task.
- Example 4: The slide uses a clean white background with a two-column layout. At the top-left, the title 'Task: Find chairs' is displayed in a plain black sans-serif font. The top-right corner contains a QR code and a gold-colored shield-shaped institutional logo. The left column features a large, square-framed diagram showing a 3D perspective of a camera on the left with lines indicating its field of view directed at a dining table and four blue chairs. The right column contains a horizontal image strip with a black background showing a row of blue chairs, each highlighted with a bright yellow-green bounding box. Below this image, the phrase 'Possible Variations' is centered in a medium-sized font. A small page number '7' is positioned in the bottom-right corner. The slide has a light text density, relying primarily on visual diagrams to illustrate a computer vision task.
- Example 5: The slide uses a minimalist design with a solid black background. A single line of white, sans-serif text is centered at the top, serving as a descriptive title or caption. Below this text, a large photographic image spans the width of the slide, showing a street-level view of a residential road lined with trees and fences under a clear sky. A prominent horizontal dashed white line is overlaid across the lower third of the image. Scattered throughout the scene, particularly concentrated along this dashed line and trailing into the distance, are glowing purple and blue light effects that represent the 'query pixels' mentioned in the title. The overall text density is light, prioritizing the visual demonstration over textual information.

Duration statistics for this section (from references): min=1.0s, max=53.0s, avg=9.3s.

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
  "style_rationale": "The T2GA module is best explained through its wide horizontal visualizations (Figures 3 and 4) which show the column-wise attention and its impact on confidence maps. A full-width figure layout prevents these wide images from being shrunk, while providing space below for the mathematical formulation and key functional bullets."
}"""

Token usage so far: 61840 prompt tokens, 4198 completion tokens

Cost so far: $0.74434

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "The Top-to-Ground Aggregation (T2GA) module is designed to bridge the appearance gap for tall structures and occluded objects by aligning their ground-level representations. It operates on the principle that while elevated objects look different from ground and aerial views, their base positions on the ground plane are geometrically consistent. T2GA uses a transformer-based attention mechanism where on-ground pixels serve as queries to aggregate features from elevated pixels in the same vertical column. This allows the model to either fuse features of the same object or replace occluded ground features with reliable information from above. The resulting aggregated feature map ($F^a$) is formed by vertically stacking these attention-weighted features with the original ground features. This process ensures that landmarks like traffic signal poles, which might be ignored by standard methods, receive higher confidence values and are sampled as keypoints for more precise vehicle pose estimation.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "Our method adopts PureACL [24] as the baseline model and introduces three novel components (highlighted in red): (1) T2GA (Sec.4.1): aggregates the features of elevated pixels onto the feature of the on-ground pixel that is directly beneath them to alleviate the representation gap of the same object across different views; (2) CycDA Loss (Sec.4.2): explicitly enforces a view-invariant representation for the same object; and (3) ERP Loss (Sec.4.3): allows the model to leverage key points that are farther away from the vehicle while allocating more emphasis on correcting the vehicle orientation estimation.",
      "relevance": "Provides the architectural context, showing how the T2GA module integrates into the feature extraction and matching pipeline."
    },
    {
      "ref": "Figure 3",
      "caption": "Attention between the on-ground pixels and their corresponding elevated pixels is displayed column-wise. (Left example): The attention between the base and top of the streetlight is high despite their distinct appearances. This allows the resultant aggregated ground feature to be aligned with the satellite feature corresponding to the matching geographic location. (Right example): In the absence of occlusion from above, ground pixels maintain minimal attention with their elevated pixels. This avoids unnecessary dilution of the ground features which are already well aligned with their satellite counterparts.",
      "relevance": "Visualizes the column-wise attention mechanism that allows on-ground pixels to 'pull' features from elevated structures like streetlights."
    },
    {
      "ref": "Figure 4",
      "caption": "Illustration on the effect of T2GA on the confidence map of the baseline model. The confidence map without T2GA (Left) predominantly highlights road marks and curbs, resulting in subsequent keypoint sampling missing important road landmarks, e.g. traffic signal poles, that provide important cues to vehicle pose estimation; The confidence map with T2GA (Right) has high confidence values distributed across various road marks and traffic poles. With more geographic cues provided by multiple sources, the resultant pose prediction becomes more precise and robust.",
      "relevance": "Demonstrates the practical impact of T2GA on the confidence map, showing it successfully identifies vertical landmarks that standard methods miss."
    }
  ],
  "key_tables": [],
  "key_equations": [
    {
      "ref": "Equation 2",
      "content": "F^{att}[p] = \text{Softmax}(\\mathbf{Q}\\mathbf{K}^T)\\mathbf{V}",
      "relevance": "Defines the core attention mechanism used to aggregate elevated features (V) onto on-ground pixels (p) using queries (Q) and keys (K)."
    },
    {
      "ref": "Equation 3",
      "content": "F^a = F^g_{0:H^g-\tau} \\oplus F^{att}",
      "relevance": "Shows how the aggregated feature map is constructed by vertically stacking the attention-weighted features with the original ground features."
    }
  ],
  "section_refs": [
    "Section 4.1"
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
  "style_rationale": "The T2GA module is best explained through its wide horizontal visualizations (Figures 3 and 4) which show the column-wise attention and its impact on confidence maps. A full-width figure layout prevents these wide images from being shrunk, while providing space below for the mathematical formulation and key functional bullets."
}

Scene context:
{
  "scene_id": 2,
  "title": "Top-to-Ground Aggregation (T2GA) Module",
  "summary": "The proposed T2GA module aggregates features from elevated pixels onto the corresponding on-ground pixel features. By leveraging reliable off-ground information and handling visual occlusions, it improves feature alignment between ground and aerial orthographic views.",
  "paper_section": "Method",
  "narrative_role": "method",
  "asset_video": null,
  "duration_stat": {
    "min": 8.0,
    "max": 15.0,
    "avg": 11.0
  }
}

## Previous Content
The following content was drafted for the immediately preceding scenes.
You MUST NOT repeat the exact text content or claims from these previous scenes in your current draft.

{
  "bullets": [
    "Extreme viewpoint differences create a significant domain gap",
    "Neglect of off-ground features like streetlights and poles",
    "Visual occlusions from trees compromise feature alignment"
  ],
  "audio_content": "Matching street-level images to aerial maps is difficult due to extreme viewpoint differences. Standard methods often ignore off-ground features and struggle with occlusions, compromising localization accuracy in complex scenes."
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
  "title": "Top-to-Ground Aggregation (T2GA)",
  "audio_content": "T2GA uses transformer attention to aggregate features from elevated structures onto their ground-level base. By processing pixels column-wise, it fuses reliable off-ground cues into the feature map. This highlights vertical landmarks, providing the precise geometric cues needed for accurate localization.",
  "duration_sec": 16.0,
  "bullets": [
    "Transformer attention aligns elevated features with their ground-level base",
    "Column-wise aggregation fuses reliable off-ground cues into the feature map",
    "Enhances landmark detection for more precise vehicle pose estimation"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 3",
    "caption": "Column-wise attention mechanism aggregating features from elevated structures like streetlights."
  },
  "source": [
    "Section 4.1",
    "Figure 3",
    "Equation 2"
  ],
  "prompt": "A slide showing the T2GA module's attention mechanism. The top half features Figure 3 from the paper, illustrating how features from the top of a streetlight are pulled down to its base. Below the figure, three bullet points explain the transformer-based column-wise aggregation and its role in enhancing landmark detection for localization."
}"""

Token usage so far: 69110 prompt tokens, 4502 completion tokens

Cost so far: $0.82616

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "Top-to-Ground Aggregation (T2GA)",
  "audio_content": "T2GA uses transformer attention to aggregate features from elevated structures onto their ground-level base. By processing pixels column-wise, it fuses reliable off-ground cues into the feature map. This highlights vertical landmarks, providing the precise geometric cues needed for accurate localization.",
  "duration_sec": 16.0,
  "bullets": [
    "Transformer attention aligns elevated features with their ground-level base",
    "Column-wise aggregation fuses reliable off-ground cues into the feature map",
    "Enhances landmark detection for more precise vehicle pose estimation"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 3",
    "caption": "Column-wise attention mechanism aggregating features from elevated structures like streetlights."
  },
  "source": [
    "Section 4.1",
    "Figure 3",
    "Equation 2"
  ],
  "prompt": "A slide showing the T2GA module's attention mechanism. The top half features Figure 3 from the paper, illustrating how features from the top of a streetlight are pulled down to its base. Below the figure, three bullet points explain the transformer-based column-wise aggregation and its role in enhancing landmark detection for localization."
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
  "total_time_sec": 16.0
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
    "title": "Top-to-Ground Aggregation (T2GA)",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 3",
      "caption": "Column-wise attention mechanism aggregating features from elevated structures like streetlights."
    },
    "bullets": [
      "Transformer attention aligns elevated features with their ground-level base",
      "Column-wise aggregation fuses reliable off-ground cues into the feature map",
      "Enhances landmark detection for more precise vehicle pose estimation"
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
      "audio_segment": "T2GA uses transformer attention to aggregate features from elevated structures onto their ground-level base.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 4.0,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[0]"
        }
      ],
      "audio_segment": "This transformer attention mechanism specifically aligns elevated features with their corresponding ground-level base.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 8.0,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[1]"
        }
      ],
      "audio_segment": "By processing pixels column-wise, it fuses reliable off-ground cues into the feature map.",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 12.0,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[2]"
        }
      ],
      "audio_segment": "This highlights vertical landmarks, providing the precise geometric cues needed for accurate localization and vehicle pose estimation.",
      "visual_emphasis": []
    }
  ]
}"""

Token usage so far: 75625 prompt tokens, 5083 completion tokens

Cost so far: $0.90874

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 3,
  "title": "Cycle Domain Adaptation (CycDA) Loss",
  "summary": "To address variations in camera types, lighting, and resolutions, the Cycle Domain Adaptation (CycDA) loss is introduced. It enforces view-invariant representations by minimizing discrepancies between domain-adapted features and their target counterparts across ground and aerial views.",
  "paper_section": "Method",
  "narrative_role": "method",
  "asset_video": null,
  "duration_stat": {
    "min": 7.0,
    "max": 14.0,
    "avg": 10.0
  }
}

## Previous Scenes Memory
The following content was extracted for the immediately preceding scenes. **This is provided as a memory of what the audience has JUST seen.**
You MUST NOT repeat the claims, figures, tables, or equations from these previous scenes in your current extraction, to ensure the presentation maintains forward momentum without redundant slides.
If you must reference the exactly same figure/table, the 'relevance' MUST be clearly unique to avoid narrative duplication.

{
  "extracted_content": "Visual-based cross-view localization aims to determine the position of street-level query images within a satellite or aerial view map. While satellite imagery is now widely accessible via platforms like Google Maps, achieving accurate localization remains difficult due to the extreme viewpoint differences between ground and aerial perspectives. These differences create a significant domain gap that compromises feature alignment. Existing research typically follows two paths: generative-based methods that transform view styles, which can introduce pose estimation ambiguities, and geometry-alignment-based methods that focus primarily on on-ground pixels. A major limitation of current techniques is the neglect of off-ground features (such as streetlights) and an inability to handle visual occlusions (such as treetops obscuring road details). This leads to a lack of robustness in scenarios where road markings are degraded or obscured, necessitating a method that can leverage reliable off-ground information to improve alignment.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Efficacy of T2GA. T2GA aggregates off-ground features (e.g., the streetlight within the green square) and addresses occlusions (e.g., the tree within the red square). Unlike conventional methods that often overlook such elements, T2GA integrates these features, thus improving appearance matching for groundlevel aligned pixels across views using ground plane homography. Insets are magnified for clarity, with dotted outlines indicating appearance misalignment and solid outlines indicating appearance alignment with the corresponding aerial view features.",
      "relevance": "This figure visually demonstrates the core challenges mentioned in the introduction: the misalignment of off-ground features and the problem of occlusions in standard cross-view matching."
    }
  ],
  "key_tables": [],
  "key_equations": []
}
{
  "extracted_content": "The Top-to-Ground Aggregation (T2GA) module is designed to bridge the appearance gap for tall structures and occluded objects by aligning their ground-level representations. It operates on the principle that while elevated objects look different from ground and aerial views, their base positions on the ground plane are geometrically consistent. T2GA uses a transformer-based attention mechanism where on-ground pixels serve as queries to aggregate features from elevated pixels in the same vertical column. This allows the model to either fuse features of the same object or replace occluded ground features with reliable information from above. The resulting aggregated feature map ($F^a$) is formed by vertically stacking these attention-weighted features with the original ground features. This process ensures that landmarks like traffic signal poles, which might be ignored by standard methods, receive higher confidence values and are sampled as keypoints for more precise vehicle pose estimation.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "Our method adopts PureACL [24] as the baseline model and introduces three novel components (highlighted in red): (1) T2GA (Sec.4.1): aggregates the features of elevated pixels onto the feature of the on-ground pixel that is directly beneath them to alleviate the representation gap of the same object across different views; (2) CycDA Loss (Sec.4.2): explicitly enforces a view-invariant representation for the same object; and (3) ERP Loss (Sec.4.3): allows the model to leverage key points that are farther away from the vehicle while allocating more emphasis on correcting the vehicle orientation estimation.",
      "relevance": "Provides the architectural context, showing how the T2GA module integrates into the feature extraction and matching pipeline."
    },
    {
      "ref": "Figure 3",
      "caption": "Attention between the on-ground pixels and their corresponding elevated pixels is displayed column-wise. (Left example): The attention between the base and top of the streetlight is high despite their distinct appearances. This allows the resultant aggregated ground feature to be aligned with the satellite feature corresponding to the matching geographic location. (Right example): In the absence of occlusion from above, ground pixels maintain minimal attention with their elevated pixels. This avoids unnecessary dilution of the ground features which are already well aligned with their satellite counterparts.",
      "relevance": "Visualizes the column-wise attention mechanism that allows on-ground pixels to 'pull' features from elevated structures like streetlights."
    },
    {
      "ref": "Figure 4",
      "caption": "Illustration on the effect of T2GA on the confidence map of the baseline model. The confidence map without T2GA (Left) predominantly highlights road marks and curbs, resulting in subsequent keypoint sampling missing important road landmarks, e.g. traffic signal poles, that provide important cues to vehicle pose estimation; The confidence map with T2GA (Right) has high confidence values distributed across various road marks and traffic poles. With more geographic cues provided by multiple sources, the resultant pose prediction becomes more precise and robust.",
      "relevance": "Demonstrates the practical impact of T2GA on the confidence map, showing it successfully identifies vertical landmarks that standard methods miss."
    }
  ],
  "key_tables": [],
  "key_equations": [
    {
      "ref": "Equation 2",
      "content": "F^{att}[p] = \text{Softmax}(\\mathbf{Q}\\mathbf{K}^T)\\mathbf{V}",
      "relevance": "Defines the core attention mechanism used to aggregate elevated features (V) onto on-ground pixels (p) using queries (Q) and keys (K)."
    },
    {
      "ref": "Equation 3",
      "content": "F^a = F^g_{0:H^g-\tau} \\oplus F^{att}",
      "relevance": "Shows how the aggregated feature map is constructed by vertically stacking the attention-weighted features with the original ground features."
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
  "extracted_content": "The Cycle Domain Adaptation (CycDA) loss is designed to mitigate representation gaps arising from differences in camera specifications (e.g., tone, hue, resolution) and environmental changes between ground and aerial views. It explicitly enforces view-invariant feature extraction by minimizing the L2 distance between features across three distinct spaces: the ground feature space, the satellite feature space, and a shared latent feature space. This bidirectional adaptation ensures that features extracted from one domain are effectively translatable to the other. The process utilizes projection functions $\\mathcal{E}(\\cdot)$ and $\\mathcal{D}(\\cdot)$, which are guided by the focal lengths of the satellite and vehicle cameras ($c_s$ and $c_g$) to maintain geometric consistency during the feature transformation.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "Our method adopts PureACL [24] as the baseline model and introduces three novel components (highlighted in red): ... (2) CycDA Loss (Sec.4.2): explicitly enforces a view-invariant representation for the same object; ...",
      "relevance": "The figure illustrates the integration of the CycDA Loss within the overall architecture, showing how it supervises the feature extraction process to ensure domain invariance."
    }
  ],
  "key_tables": [],
  "key_equations": [
    {
      "ref": "Equation 4",
      "content": "\\mathcal{L}_{g} = \\frac{1}{N} \\sum_{i=1}^{N} \\| F^{a}[p^{g}_{i}] - \\mathcal{D} ( \\mathcal{E} ( F^{s}[p^{s}_{i}(\\mathbf{P}_{gt})] \\textcircled{c} c_{s} ) \\textcircled{c} c_{g} ) \\|_{2}",
      "relevance": "Defines the representation loss in the ground feature space, comparing aggregated ground features with projected satellite features."
    },
    {
      "ref": "Equation 5",
      "content": "\\mathcal{L}_{s} = \\frac{1}{N} \\sum_{i=1}^{N} \\| F^{s}[p^{s}_{i}(\\mathbf{P}_{gt})] - \\mathcal{D} ( \\mathcal{E} ( F^{a}[p^{g}_{i}] \\textcircled{c} c_{g} ) \\textcircled{c} c_{s} ) \\|_{2}",
      "relevance": "Defines the representation loss in the satellite feature space, comparing satellite features with projected ground features."
    },
    {
      "ref": "Equation 6",
      "content": "\\mathcal{L}_{m} = \\frac{1}{N} \\sum_{i=1}^{N} \\| \\mathcal{E} ( F^{a}[p^{g}_{i}] \\textcircled{c} c_{g}) - \\mathcal{E} ( F^{s}[p^{s}_{i}(\\mathbf{P}_{gt})] \\textcircled{c} c_{s} ) \\|_{2}",
      "relevance": "Defines the alignment loss in the shared latent feature space, ensuring both views map to a consistent representation."
    },
    {
      "ref": "Equation 7",
      "content": "\\mathcal{L}_{CycDA} = \\mathcal{L}_{g} + \\mathcal{L}_{s} + \\mathcal{L}_{m}",
      "relevance": "The total Cycle Domain Adaptation loss, combining the three feature space discrepancies."
    }
  ],
  "section_refs": [
    "Section 4.2"
  ]
}"""

Token usage so far: 82822 prompt tokens, 5905 completion tokens

Cost so far: $1.00537

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "The Cycle Domain Adaptation (CycDA) loss is designed to mitigate representation gaps arising from differences in camera specifications (e.g., tone, hue, resolution) and environmental changes between ground and aerial views. It explicitly enforces view-invariant feature extraction by minimizing the L2 distance between features across three distinct spaces: the ground feature space, the satellite feature space, and a shared latent feature space. This bidirectional adaptation ensures that features extracted from one domain are effectively translatable to the other. The process utilizes projection functions $\\mathcal{E}(\\cdot)$ and $\\mathcal{D}(\\cdot)$, which are guided by the focal lengths of the satellite and vehicle cameras ($c_s$ and $c_g$) to maintain geometric consistency during the feature transformation.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "Our method adopts PureACL [24] as the baseline model and introduces three novel components (highlighted in red): ... (2) CycDA Loss (Sec.4.2): explicitly enforces a view-invariant representation for the same object; ...",
      "relevance": "The figure illustrates the integration of the CycDA Loss within the overall architecture, showing how it supervises the feature extraction process to ensure domain invariance."
    }
  ],
  "key_tables": [],
  "key_equations": [
    {
      "ref": "Equation 4",
      "content": "\\mathcal{L}_{g} = \frac{1}{N} \\sum_{i=1}^{N} \\| F^{a}[p^{g}_{i}] - \\mathcal{D} ( \\mathcal{E} ( F^{s}[p^{s}_{i}(\\mathbf{P}_{gt})] \textcircled{c} c_{s} ) \textcircled{c} c_{g} ) \\|_{2}",
      "relevance": "Defines the representation loss in the ground feature space, comparing aggregated ground features with projected satellite features."
    },
    {
      "ref": "Equation 5",
      "content": "\\mathcal{L}_{s} = \frac{1}{N} \\sum_{i=1}^{N} \\| F^{s}[p^{s}_{i}(\\mathbf{P}_{gt})] - \\mathcal{D} ( \\mathcal{E} ( F^{a}[p^{g}_{i}] \textcircled{c} c_{g} ) \textcircled{c} c_{s} ) \\|_{2}",
      "relevance": "Defines the representation loss in the satellite feature space, comparing satellite features with projected ground features."
    },
    {
      "ref": "Equation 6",
      "content": "\\mathcal{L}_{m} = \frac{1}{N} \\sum_{i=1}^{N} \\| \\mathcal{E} ( F^{a}[p^{g}_{i}] \textcircled{c} c_{g}) - \\mathcal{E} ( F^{s}[p^{s}_{i}(\\mathbf{P}_{gt})] \textcircled{c} c_{s} ) \\|_{2}",
      "relevance": "Defines the alignment loss in the shared latent feature space, ensuring both views map to a consistent representation."
    },
    {
      "ref": "Equation 7",
      "content": "\\mathcal{L}_{CycDA} = \\mathcal{L}_{g} + \\mathcal{L}_{s} + \\mathcal{L}_{m}",
      "relevance": "The total Cycle Domain Adaptation loss, combining the three feature space discrepancies."
    }
  ],
  "section_refs": [
    "Section 4.2"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 3,
  "title": "Cycle Domain Adaptation (CycDA) Loss",
  "summary": "To address variations in camera types, lighting, and resolutions, the Cycle Domain Adaptation (CycDA) loss is introduced. It enforces view-invariant representations by minimizing discrepancies between domain-adapted features and their target counterparts across ground and aerial views.",
  "paper_section": "Method",
  "narrative_role": "method",
  "asset_video": null,
  "duration_stat": {
    "min": 7.0,
    "max": 14.0,
    "avg": 10.0
  }
}

Reference style advice:
Reference Layouts for 'method' section from similar papers:
- Example 1: The slide has a centered main title 'P o s 3 R' at the top, followed by a sub-heading 'Step 1: Template Rendering' aligned to the top-left. The middle section contains a horizontal diagram showing the rendering process: on the left, a CAD model of a watering can is shown inside a blue wireframe bounding box with RGB axes; an arrow labeled '1) rendering' points to a sequence of five rendered images of the watering can in different orientations. These images are contained within a light blue rounded rectangle, with the text 'forty templates' centered underneath. At the bottom of the slide, there are two bullet points centered horizontally that describe the template generation logic. The background is white, and there is a faint watermark in the top-left corner. The overall text density is light, focusing on the visual diagram.
- Example 2: The slide features a large, bold title 'CycDA Loss' positioned at the top-left corner. The main content consists of a large, centered architectural diagram that illustrates a cyclic data flow. The diagram uses mathematical notation for its nodes, such as f_g, m_g, f_s, and m_s, connected by single-headed arrows representing transformations through an encoder (E) and a decoder (D). Small circles with a 'c' inside indicate concatenation or combination points. Vertical double-headed arrows connect corresponding top and bottom nodes, labeled with 'L2 loss' to indicate where loss functions are applied. The layout is clean and minimalist, using a black-and-white color scheme on a plain white background, with a light text density focused on the visual logic of the method.
- Example 3: The slide features a large, bold serif title 'Reloc3r' positioned at the top-left. The main body is organized into a two-column structure separated by a vertical dashed line. The left column is dedicated to 'Relative camera pose regression' and contains a detailed architectural flowchart. This flowchart illustrates a dual-stream process where two input images (Image I1 and Image I2) are processed through 'Patchify', 'ViT encoder', 'ViT decoder', and 'Head' blocks to produce relative camera poses. Red dashed arrows highlight 'Weights sharing' and 'Cross-attention' between the two streams. Below the flowchart, there is a 'Key insights:' section with two bullet points. The right column, titled 'Motion averaging', displays a 3D geometric diagram showing various camera frustums and their spatial relationships, accompanied by the subtitle '(A minimalist approach)'. The slide uses a clean white background with moderate text density, relying heavily on diagrams to explain the proposed method.
- Example 4: The slide features a clean, white background with a large, sans-serif title at the top-left. In the top-right corner, there is a QR code and a gold-colored institutional crest logo. The central content is a flowchart illustrating a pipeline. On the left, an 'Input image' of a kitchen interior is shown, with a blurred block of text below it representing a prompt. A blue line originates from the image and branches into two diagonal paths. The upper path, labeled 'Right', leads to the text 'Yes/No' and a stack of red circular icons with white 'thumbs down' symbols, topped with a bracket labeled 'N samples'. The lower path, labeled 'Left', leads to the text 'Yes/No' and a stack of green circular icons with white 'thumbs up' symbols. The slide has a light text density and includes a page number '13' in the bottom-right corner.
- Example 5: The slide features a clean white background with a large, black title positioned at the top-left. In the top-right corner, there is a QR code next to a gold-colored institutional logo. The main content is a visual representation of a pipeline: on the left, there is a small photograph of a bedroom labeled 'Input image Pose 1'. To its right is a central diagram of a semi-transparent 3D cube containing colorful volumetric data, captioned 'Diffusion with Forward Model'. Several blurred camera icons are arranged around this cube, suggesting multiple viewpoints. At the bottom-right, there are two lines of bibliographic references in a small font, and the page number '15' is located in the far bottom-right corner. The text density is light, with the focus being on the diagrammatic flow.

Duration statistics for this section (from references): min=1.0s, max=53.0s, avg=9.3s.

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
  "style_rationale": "The CycDA Loss is a key component of the architecture. Using a wide figure region at the top allows the horizontal system diagram (Figure 2) to be shown clearly, while the bullets and equations below explain the mathematical formulation and the bidirectional adaptation process."
}"""

Token usage so far: 90858 prompt tokens, 6176 completion tokens

Cost so far: $1.09386

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "The Cycle Domain Adaptation (CycDA) loss is designed to mitigate representation gaps arising from differences in camera specifications (e.g., tone, hue, resolution) and environmental changes between ground and aerial views. It explicitly enforces view-invariant feature extraction by minimizing the L2 distance between features across three distinct spaces: the ground feature space, the satellite feature space, and a shared latent feature space. This bidirectional adaptation ensures that features extracted from one domain are effectively translatable to the other. The process utilizes projection functions $\\mathcal{E}(\\cdot)$ and $\\mathcal{D}(\\cdot)$, which are guided by the focal lengths of the satellite and vehicle cameras ($c_s$ and $c_g$) to maintain geometric consistency during the feature transformation.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "Our method adopts PureACL [24] as the baseline model and introduces three novel components (highlighted in red): ... (2) CycDA Loss (Sec.4.2): explicitly enforces a view-invariant representation for the same object; ...",
      "relevance": "The figure illustrates the integration of the CycDA Loss within the overall architecture, showing how it supervises the feature extraction process to ensure domain invariance."
    }
  ],
  "key_tables": [],
  "key_equations": [
    {
      "ref": "Equation 4",
      "content": "\\mathcal{L}_{g} = \frac{1}{N} \\sum_{i=1}^{N} \\| F^{a}[p^{g}_{i}] - \\mathcal{D} ( \\mathcal{E} ( F^{s}[p^{s}_{i}(\\mathbf{P}_{gt})] \textcircled{c} c_{s} ) \textcircled{c} c_{g} ) \\|_{2}",
      "relevance": "Defines the representation loss in the ground feature space, comparing aggregated ground features with projected satellite features."
    },
    {
      "ref": "Equation 5",
      "content": "\\mathcal{L}_{s} = \frac{1}{N} \\sum_{i=1}^{N} \\| F^{s}[p^{s}_{i}(\\mathbf{P}_{gt})] - \\mathcal{D} ( \\mathcal{E} ( F^{a}[p^{g}_{i}] \textcircled{c} c_{g} ) \textcircled{c} c_{s} ) \\|_{2}",
      "relevance": "Defines the representation loss in the satellite feature space, comparing satellite features with projected ground features."
    },
    {
      "ref": "Equation 6",
      "content": "\\mathcal{L}_{m} = \frac{1}{N} \\sum_{i=1}^{N} \\| \\mathcal{E} ( F^{a}[p^{g}_{i}] \textcircled{c} c_{g}) - \\mathcal{E} ( F^{s}[p^{s}_{i}(\\mathbf{P}_{gt})] \textcircled{c} c_{s} ) \\|_{2}",
      "relevance": "Defines the alignment loss in the shared latent feature space, ensuring both views map to a consistent representation."
    },
    {
      "ref": "Equation 7",
      "content": "\\mathcal{L}_{CycDA} = \\mathcal{L}_{g} + \\mathcal{L}_{s} + \\mathcal{L}_{m}",
      "relevance": "The total Cycle Domain Adaptation loss, combining the three feature space discrepancies."
    }
  ],
  "section_refs": [
    "Section 4.2"
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
  "style_rationale": "The CycDA Loss is a key component of the architecture. Using a wide figure region at the top allows the horizontal system diagram (Figure 2) to be shown clearly, while the bullets and equations below explain the mathematical formulation and the bidirectional adaptation process."
}

Scene context:
{
  "scene_id": 3,
  "title": "Cycle Domain Adaptation (CycDA) Loss",
  "summary": "To address variations in camera types, lighting, and resolutions, the Cycle Domain Adaptation (CycDA) loss is introduced. It enforces view-invariant representations by minimizing discrepancies between domain-adapted features and their target counterparts across ground and aerial views.",
  "paper_section": "Method",
  "narrative_role": "method",
  "asset_video": null,
  "duration_stat": {
    "min": 7.0,
    "max": 14.0,
    "avg": 10.0
  }
}

## Previous Content
The following content was drafted for the immediately preceding scenes.
You MUST NOT repeat the exact text content or claims from these previous scenes in your current draft.

{
  "bullets": [
    "Transformer attention aligns elevated features with their ground-level base",
    "Column-wise aggregation fuses reliable off-ground cues into the feature map",
    "Enhances landmark detection for more precise vehicle pose estimation"
  ],
  "audio_content": "T2GA uses transformer attention to aggregate features from elevated structures onto their ground-level base. By processing pixels column-wise, it fuses reliable off-ground cues into the feature map. This highlights vertical landmarks, providing the precise geometric cues needed for accurate localization."
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
  "title": "Cycle Domain Adaptation (CycDA) Loss",
  "audio_content": "CycDA loss bridges the domain gap from varying camera specs and lighting. It minimizes L2 distances across ground, satellite, and shared latent spaces. This bidirectional adaptation ensures features are view-invariant and translatable, providing a robust foundation for cross-view matching.",
  "duration_sec": 15.6,
  "bullets": [
    "Mitigates domain gaps from camera specifications and environmental changes",
    "Minimizes L2 discrepancies across ground, satellite, and latent feature spaces",
    "Enforces view-invariant representations for robust bidirectional feature translation"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 2",
    "caption": "Integration of CycDA Loss within the feature extraction architecture"
  },
  "source": [
    "Section 4.2",
    "Equation 7"
  ],
  "prompt": "A diagram showing the CycDA loss component within a neural network architecture, highlighting the bidirectional flow between ground and satellite feature maps and the shared latent space."
}"""

Token usage so far: 98064 prompt tokens, 6436 completion tokens

Cost so far: $1.17372

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "Cycle Domain Adaptation (CycDA) Loss",
  "audio_content": "CycDA loss bridges the domain gap from varying camera specs and lighting. It minimizes L2 distances across ground, satellite, and shared latent spaces. This bidirectional adaptation ensures features are view-invariant and translatable, providing a robust foundation for cross-view matching.",
  "duration_sec": 15.6,
  "bullets": [
    "Mitigates domain gaps from camera specifications and environmental changes",
    "Minimizes L2 discrepancies across ground, satellite, and latent feature spaces",
    "Enforces view-invariant representations for robust bidirectional feature translation"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 2",
    "caption": "Integration of CycDA Loss within the feature extraction architecture"
  },
  "source": [
    "Section 4.2",
    "Equation 7"
  ],
  "prompt": "A diagram showing the CycDA loss component within a neural network architecture, highlighting the bidirectional flow between ground and satellite feature maps and the shared latent space."
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
  "total_time_sec": 15.6
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
    "title": "Cycle Domain Adaptation (CycDA) Loss",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 2",
      "caption": "Integration of CycDA Loss within the feature extraction architecture"
    },
    "bullets": [
      "Mitigates domain gaps from camera specifications and environmental changes",
      "Minimizes L2 discrepancies across ground, satellite, and latent feature spaces",
      "Enforces view-invariant representations for robust bidirectional feature translation"
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
      "audio_segment": "CycDA loss bridges the domain gap from varying camera specs and lighting.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 3.9,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[0]"
        }
      ],
      "audio_segment": "This component mitigates domain gaps arising from different camera specifications and environmental changes.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 7.8,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[1]"
        }
      ],
      "audio_segment": "It minimizes L2 distances across ground, satellite, and shared latent spaces.",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 11.7,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[2]"
        }
      ],
      "audio_segment": "This bidirectional adaptation ensures features are view-invariant and translatable, providing a robust foundation for cross-view matching.",
      "visual_emphasis": []
    }
  ]
}
```"""

Token usage so far: 104535 prompt tokens, 7015 completion tokens

Cost so far: $1.25580

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 4,
  "title": "Equidistant Re-projection (ERP) Loss",
  "summary": "The Equidistant Re-projection (ERP) loss mitigates the bias toward closer keypoints by applying a distance-weighted approach. This ensures orientation errors are independent of keypoint distance, leading to a more uniform distribution of keypoints and precise orientation estimation.",
  "paper_section": "Method",
  "narrative_role": "method",
  "asset_video": null,
  "duration_stat": {
    "min": 7.0,
    "max": 14.0,
    "avg": 10.0
  }
}

## Previous Scenes Memory
The following content was extracted for the immediately preceding scenes. **This is provided as a memory of what the audience has JUST seen.**
You MUST NOT repeat the claims, figures, tables, or equations from these previous scenes in your current extraction, to ensure the presentation maintains forward momentum without redundant slides.
If you must reference the exactly same figure/table, the 'relevance' MUST be clearly unique to avoid narrative duplication.

{
  "extracted_content": "The Top-to-Ground Aggregation (T2GA) module is designed to bridge the appearance gap for tall structures and occluded objects by aligning their ground-level representations. It operates on the principle that while elevated objects look different from ground and aerial views, their base positions on the ground plane are geometrically consistent. T2GA uses a transformer-based attention mechanism where on-ground pixels serve as queries to aggregate features from elevated pixels in the same vertical column. This allows the model to either fuse features of the same object or replace occluded ground features with reliable information from above. The resulting aggregated feature map ($F^a$) is formed by vertically stacking these attention-weighted features with the original ground features. This process ensures that landmarks like traffic signal poles, which might be ignored by standard methods, receive higher confidence values and are sampled as keypoints for more precise vehicle pose estimation.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "Our method adopts PureACL [24] as the baseline model and introduces three novel components (highlighted in red): (1) T2GA (Sec.4.1): aggregates the features of elevated pixels onto the feature of the on-ground pixel that is directly beneath them to alleviate the representation gap of the same object across different views; (2) CycDA Loss (Sec.4.2): explicitly enforces a view-invariant representation for the same object; and (3) ERP Loss (Sec.4.3): allows the model to leverage key points that are farther away from the vehicle while allocating more emphasis on correcting the vehicle orientation estimation.",
      "relevance": "Provides the architectural context, showing how the T2GA module integrates into the feature extraction and matching pipeline."
    },
    {
      "ref": "Figure 3",
      "caption": "Attention between the on-ground pixels and their corresponding elevated pixels is displayed column-wise. (Left example): The attention between the base and top of the streetlight is high despite their distinct appearances. This allows the resultant aggregated ground feature to be aligned with the satellite feature corresponding to the matching geographic location. (Right example): In the absence of occlusion from above, ground pixels maintain minimal attention with their elevated pixels. This avoids unnecessary dilution of the ground features which are already well aligned with their satellite counterparts.",
      "relevance": "Visualizes the column-wise attention mechanism that allows on-ground pixels to 'pull' features from elevated structures like streetlights."
    },
    {
      "ref": "Figure 4",
      "caption": "Illustration on the effect of T2GA on the confidence map of the baseline model. The confidence map without T2GA (Left) predominantly highlights road marks and curbs, resulting in subsequent keypoint sampling missing important road landmarks, e.g. traffic signal poles, that provide important cues to vehicle pose estimation; The confidence map with T2GA (Right) has high confidence values distributed across various road marks and traffic poles. With more geographic cues provided by multiple sources, the resultant pose prediction becomes more precise and robust.",
      "relevance": "Demonstrates the practical impact of T2GA on the confidence map, showing it successfully identifies vertical landmarks that standard methods miss."
    }
  ],
  "key_tables": [],
  "key_equations": [
    {
      "ref": "Equation 2",
      "content": "F^{att}[p] = \text{Softmax}(\\mathbf{Q}\\mathbf{K}^T)\\mathbf{V}",
      "relevance": "Defines the core attention mechanism used to aggregate elevated features (V) onto on-ground pixels (p) using queries (Q) and keys (K)."
    },
    {
      "ref": "Equation 3",
      "content": "F^a = F^g_{0:H^g-\tau} \\oplus F^{att}",
      "relevance": "Shows how the aggregated feature map is constructed by vertically stacking the attention-weighted features with the original ground features."
    }
  ]
}
{
  "extracted_content": "The Cycle Domain Adaptation (CycDA) loss is designed to mitigate representation gaps arising from differences in camera specifications (e.g., tone, hue, resolution) and environmental changes between ground and aerial views. It explicitly enforces view-invariant feature extraction by minimizing the L2 distance between features across three distinct spaces: the ground feature space, the satellite feature space, and a shared latent feature space. This bidirectional adaptation ensures that features extracted from one domain are effectively translatable to the other. The process utilizes projection functions $\\mathcal{E}(\\cdot)$ and $\\mathcal{D}(\\cdot)$, which are guided by the focal lengths of the satellite and vehicle cameras ($c_s$ and $c_g$) to maintain geometric consistency during the feature transformation.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "Our method adopts PureACL [24] as the baseline model and introduces three novel components (highlighted in red): ... (2) CycDA Loss (Sec.4.2): explicitly enforces a view-invariant representation for the same object; ...",
      "relevance": "The figure illustrates the integration of the CycDA Loss within the overall architecture, showing how it supervises the feature extraction process to ensure domain invariance."
    }
  ],
  "key_tables": [],
  "key_equations": [
    {
      "ref": "Equation 4",
      "content": "\\mathcal{L}_{g} = \frac{1}{N} \\sum_{i=1}^{N} \\| F^{a}[p^{g}_{i}] - \\mathcal{D} ( \\mathcal{E} ( F^{s}[p^{s}_{i}(\\mathbf{P}_{gt})] \textcircled{c} c_{s} ) \textcircled{c} c_{g} ) \\|_{2}",
      "relevance": "Defines the representation loss in the ground feature space, comparing aggregated ground features with projected satellite features."
    },
    {
      "ref": "Equation 5",
      "content": "\\mathcal{L}_{s} = \frac{1}{N} \\sum_{i=1}^{N} \\| F^{s}[p^{s}_{i}(\\mathbf{P}_{gt})] - \\mathcal{D} ( \\mathcal{E} ( F^{a}[p^{g}_{i}] \textcircled{c} c_{g} ) \textcircled{c} c_{s} ) \\|_{2}",
      "relevance": "Defines the representation loss in the satellite feature space, comparing satellite features with projected ground features."
    },
    {
      "ref": "Equation 6",
      "content": "\\mathcal{L}_{m} = \frac{1}{N} \\sum_{i=1}^{N} \\| \\mathcal{E} ( F^{a}[p^{g}_{i}] \textcircled{c} c_{g}) - \\mathcal{E} ( F^{s}[p^{s}_{i}(\\mathbf{P}_{gt})] \textcircled{c} c_{s} ) \\|_{2}",
      "relevance": "Defines the alignment loss in the shared latent feature space, ensuring both views map to a consistent representation."
    },
    {
      "ref": "Equation 7",
      "content": "\\mathcal{L}_{CycDA} = \\mathcal{L}_{g} + \\mathcal{L}_{s} + \\mathcal{L}_{m}",
      "relevance": "The total Cycle Domain Adaptation loss, combining the three feature space discrepancies."
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
  "extracted_content": "The Equidistant Re-projection (ERP) loss is designed to address a common bias in keypoint-based localization where standard re-projection losses ($L_{RP}$) tend to favor keypoints closer to the vehicle. This bias occurs because orientation errors for distant points result in larger L2 distances in the image plane, causing the model to over-penalize them and cluster keypoint detections in the immediate vicinity of the vehicle. The ERP loss ($L_{ERP}$) mitigates this by applying a distance-weighted approach, dividing the re-projection error by the L2 distance ($D_{p^s_i}$) between the keypoint and the vehicle in the satellite view. This normalization ensures that orientation errors are independent of keypoint distance, leading to a more uniform and extended distribution of keypoints across the scene. This dispersed distribution provides more robust geometric constraints, significantly improving the precision of vehicle orientation estimation, especially in challenging scenarios with inaccurate initial poses.",
  "key_figures": [
    {
      "ref": "Figure 5",
      "caption": "Comparison of detected keypoints with and without ERP Loss. (Left) Without the ERP Loss, keypoints are predominantly located in close proximity to the vehicle. (Right) With the ERP Loss, there is a more dispersed distribution of keypoints.",
      "relevance": "Visually demonstrates how the ERP loss prevents keypoint clustering near the vehicle and encourages the detection of distant landmarks for better orientation cues."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 4",
      "caption": "Ablation study on the KITTI-CVL dataset ‘Cross’ area with initial noise (±45°, ±20m).",
      "relevance": "Shows the quantitative impact of the ERP loss, specifically highlighting the reduction in mean orientation error from 3.38° to 2.88° when added to the T2GA and CycDA components."
    }
  ],
  "key_equations": [
    {
      "ref": "Equation 8",
      "content": "L_{RP} = \\frac{1}{N} \\sum_{i=1}^{N}\\|p_{i}^{s}(\\mathbf{P}_{pred})-p^{s}_{i}(\\mathbf{P}_{gt}) \\|_2^2",
      "relevance": "Defines the baseline re-projection loss which suffers from distance-based bias in orientation error penalization."
    },
    {
      "ref": "Equation 9",
      "content": "L_{ERP} = \\frac{1}{N} \\sum^{N}_{i=1}\\|\\frac{p_{i}^{s}(\\mathbf{P}_{pred})-p_{i}^{s}(\\mathbf{P}_{gt})}{\\mathbf{D}_{p^{s}_{i}}} \\|_2^2",
      "relevance": "Defines the proposed Equidistant Re-projection loss that normalizes error by distance to ensure equitable impact of all keypoints on orientation estimation."
    }
  ],
  "section_refs": ["Section 4.3", "Section 6"]
}"""

Token usage so far: 112161 prompt tokens, 7709 completion tokens

Cost so far: $1.35288

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "The Equidistant Re-projection (ERP) loss is designed to address a common bias in keypoint-based localization where standard re-projection losses ($L_{RP}$) tend to favor keypoints closer to the vehicle. This bias occurs because orientation errors for distant points result in larger L2 distances in the image plane, causing the model to over-penalize them and cluster keypoint detections in the immediate vicinity of the vehicle. The ERP loss ($L_{ERP}$) mitigates this by applying a distance-weighted approach, dividing the re-projection error by the L2 distance ($D_{p^s_i}$) between the keypoint and the vehicle in the satellite view. This normalization ensures that orientation errors are independent of keypoint distance, leading to a more uniform and extended distribution of keypoints across the scene. This dispersed distribution provides more robust geometric constraints, significantly improving the precision of vehicle orientation estimation, especially in challenging scenarios with inaccurate initial poses.",
  "key_figures": [
    {
      "ref": "Figure 5",
      "caption": "Comparison of detected keypoints with and without ERP Loss. (Left) Without the ERP Loss, keypoints are predominantly located in close proximity to the vehicle. (Right) With the ERP Loss, there is a more dispersed distribution of keypoints.",
      "relevance": "Visually demonstrates how the ERP loss prevents keypoint clustering near the vehicle and encourages the detection of distant landmarks for better orientation cues."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 4",
      "caption": "Ablation study on the KITTI-CVL dataset \u2018Cross\u2019 area with initial noise (\u00b145\u00b0, \u00b120m).",
      "relevance": "Shows the quantitative impact of the ERP loss, specifically highlighting the reduction in mean orientation error from 3.38\u00b0 to 2.88\u00b0 when added to the T2GA and CycDA components."
    }
  ],
  "key_equations": [
    {
      "ref": "Equation 8",
      "content": "L_{RP} = \frac{1}{N} \\sum_{i=1}^{N}\\|p_{i}^{s}(\\mathbf{P}_{pred})-p^{s}_{i}(\\mathbf{P}_{gt}) \\|_2^2",
      "relevance": "Defines the baseline re-projection loss which suffers from distance-based bias in orientation error penalization."
    },
    {
      "ref": "Equation 9",
      "content": "L_{ERP} = \frac{1}{N} \\sum^{N}_{i=1}\\|\frac{p_{i}^{s}(\\mathbf{P}_{pred})-p_{i}^{s}(\\mathbf{P}_{gt})}{\\mathbf{D}_{p^{s}_{i}}} \\|_2^2",
      "relevance": "Defines the proposed Equidistant Re-projection loss that normalizes error by distance to ensure equitable impact of all keypoints on orientation estimation."
    }
  ],
  "section_refs": [
    "Section 4.3",
    "Section 6"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 4,
  "title": "Equidistant Re-projection (ERP) Loss",
  "summary": "The Equidistant Re-projection (ERP) loss mitigates the bias toward closer keypoints by applying a distance-weighted approach. This ensures orientation errors are independent of keypoint distance, leading to a more uniform distribution of keypoints and precise orientation estimation.",
  "paper_section": "Method",
  "narrative_role": "method",
  "asset_video": null,
  "duration_stat": {
    "min": 7.0,
    "max": 14.0,
    "avg": 10.0
  }
}

Reference style advice:
Reference Layouts for 'method' section from similar papers:
- Example 1: The slide uses a two-column layout with a white background. A large, bold title is positioned at the top-left. The left column features a framed diagram showing a 3D perspective of a camera's field of view directed at a dining table and chairs. The right column contains a horizontal image strip showing several blue chairs against a black background, each enclosed in a bright green bounding box. Below this image, the text 'Possible Variations' is centered. In the top-right corner, there is a QR code and a gold institutional logo. A small page number '7' is located at the bottom-right. The text density is light, with the focus being on the visual diagrams and images.
- Example 2: The slide uses a two-column layout with a clear title at the top-left. The left column features a large square box labeled 'Input' containing a 3D diagram of a camera pointing at a dining table with six blue chairs; orange lines project from the camera to show its field of view. The right column contains a smaller rectangular image showing the resulting camera view, where two chairs are highlighted with bright green bounding boxes against a black background. In the top-right corner, there is a QR code and a gold shield-shaped logo. A small page number '5' is positioned at the bottom-right. The slide has a very light text density, relying primarily on visual diagrams to explain the task.
- Example 3: The slide features a large, plain-text title at the top left. In the top right corner, there is a QR code and a gold-colored institutional logo. The central content is organized into three columns, each illustrating a transformation process. Each column contains a top image showing a 3D rendered scene of blue chairs with yellow bounding boxes, a downward-pointing black arrow, and a bottom image showing a simplified heatmap representation of those bounding boxes. Below these three columns is a centered text caption: 'Bounding box representations of the Object Detector'. At the bottom center, a horizontal color scale bar transitions from dark blue (labeled '0') to yellow (labeled '1'). A small page number '9' is positioned in the bottom right corner. The background is white, creating a clean and light text density.
- Example 4: The slide uses a white background with a large, plain-text title at the top-left. The central focus is a flowchart depicting a processing pipeline. On the left, an 'Input image' of a kitchen is shown, with a sample 'VLM Prompt' text block below it. A blue arrow originates from the image and splits into two paths labeled 'Right' and 'Left'. Each path leads to a 'Yes/No' decision point. The 'Right' path is accompanied by a stack of red 'thumbs down' icons labeled 'N samples', while the 'Left' path has a stack of green 'thumbs up' icons. Both paths converge at an 'Aggregate' node, which points to a horizontal stacked bar chart on the right. Above this chart is a numbered list of four specific vision-language models (ChatGPT-4o, Claude-3.5-Sonnet, LLaVA-v1.6, Gemini-1.5-Ultra). The top-right corner features a QR code and a gold university logo. Small text citations and the page number '13' are located in the bottom-right corner. The text density is moderate, balanced by visual diagrams and icons.
- Example 5: The slide features a clean white background with a large, black title positioned at the top-left. In the top-right corner, there is a QR code next to a gold-colored institutional logo. The main content is a visual representation of a pipeline: on the left, there is a small photograph of a bedroom labeled 'Input image Pose 1'. To its right is a central diagram of a semi-transparent 3D cube containing colorful volumetric data, captioned 'Diffusion with Forward Model'. Several blurred camera icons are arranged around this cube, suggesting multiple viewpoints. At the bottom-right, there are two lines of bibliographic references in a small font, and the page number '15' is located in the far bottom-right corner. The text density is light, with the focus being on the diagrammatic flow.

Duration statistics for this section (from references): min=1.0s, max=53.0s, avg=9.3s.

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
    "figure": {"x": 0.05, "y": 0.18, "w": 0.9, "h": 0.42},
    "bullets": {"x": 0.05, "y": 0.62, "w": 0.9, "h": 0.33}
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "The ERP loss is best explained by showing the visual impact on keypoint distribution (Figure 5). Since Figure 5 is a wide horizontal comparison, a full-width figure region is used to preserve its aspect ratio. Bullets and equations are placed below to provide the mathematical context and quantitative results from Table 4."
}"""

Token usage so far: 120083 prompt tokens, 7959 completion tokens

Cost so far: $1.43960

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "The Equidistant Re-projection (ERP) loss is designed to address a common bias in keypoint-based localization where standard re-projection losses ($L_{RP}$) tend to favor keypoints closer to the vehicle. This bias occurs because orientation errors for distant points result in larger L2 distances in the image plane, causing the model to over-penalize them and cluster keypoint detections in the immediate vicinity of the vehicle. The ERP loss ($L_{ERP}$) mitigates this by applying a distance-weighted approach, dividing the re-projection error by the L2 distance ($D_{p^s_i}$) between the keypoint and the vehicle in the satellite view. This normalization ensures that orientation errors are independent of keypoint distance, leading to a more uniform and extended distribution of keypoints across the scene. This dispersed distribution provides more robust geometric constraints, significantly improving the precision of vehicle orientation estimation, especially in challenging scenarios with inaccurate initial poses.",
  "key_figures": [
    {
      "ref": "Figure 5",
      "caption": "Comparison of detected keypoints with and without ERP Loss. (Left) Without the ERP Loss, keypoints are predominantly located in close proximity to the vehicle. (Right) With the ERP Loss, there is a more dispersed distribution of keypoints.",
      "relevance": "Visually demonstrates how the ERP loss prevents keypoint clustering near the vehicle and encourages the detection of distant landmarks for better orientation cues."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 4",
      "caption": "Ablation study on the KITTI-CVL dataset \u2018Cross\u2019 area with initial noise (\u00b145\u00b0, \u00b120m).",
      "relevance": "Shows the quantitative impact of the ERP loss, specifically highlighting the reduction in mean orientation error from 3.38\u00b0 to 2.88\u00b0 when added to the T2GA and CycDA components."
    }
  ],
  "key_equations": [
    {
      "ref": "Equation 8",
      "content": "L_{RP} = \frac{1}{N} \\sum_{i=1}^{N}\\|p_{i}^{s}(\\mathbf{P}_{pred})-p^{s}_{i}(\\mathbf{P}_{gt}) \\|_2^2",
      "relevance": "Defines the baseline re-projection loss which suffers from distance-based bias in orientation error penalization."
    },
    {
      "ref": "Equation 9",
      "content": "L_{ERP} = \frac{1}{N} \\sum^{N}_{i=1}\\|\frac{p_{i}^{s}(\\mathbf{P}_{pred})-p_{i}^{s}(\\mathbf{P}_{gt})}{\\mathbf{D}_{p^{s}_{i}}} \\|_2^2",
      "relevance": "Defines the proposed Equidistant Re-projection loss that normalizes error by distance to ensure equitable impact of all keypoints on orientation estimation."
    }
  ],
  "section_refs": [
    "Section 4.3",
    "Section 6"
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
      "h": 0.42
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
  "style_rationale": "The ERP loss is best explained by showing the visual impact on keypoint distribution (Figure 5). Since Figure 5 is a wide horizontal comparison, a full-width figure region is used to preserve its aspect ratio. Bullets and equations are placed below to provide the mathematical context and quantitative results from Table 4."
}

Scene context:
{
  "scene_id": 4,
  "title": "Equidistant Re-projection (ERP) Loss",
  "summary": "The Equidistant Re-projection (ERP) loss mitigates the bias toward closer keypoints by applying a distance-weighted approach. This ensures orientation errors are independent of keypoint distance, leading to a more uniform distribution of keypoints and precise orientation estimation.",
  "paper_section": "Method",
  "narrative_role": "method",
  "asset_video": null,
  "duration_stat": {
    "min": 7.0,
    "max": 14.0,
    "avg": 10.0
  }
}

## Previous Content
The following content was drafted for the immediately preceding scenes.
You MUST NOT repeat the exact text content or claims from these previous scenes in your current draft.

{
  "bullets": [
    "Mitigates domain gaps from camera specifications and environmental changes",
    "Minimizes L2 discrepancies across ground, satellite, and latent feature spaces",
    "Enforces view-invariant representations for robust bidirectional feature translation"
  ],
  "audio_content": "CycDA loss bridges the domain gap from varying camera specs and lighting. It minimizes L2 distances across ground, satellite, and shared latent spaces. This bidirectional adaptation ensures features are view-invariant and translatable, providing a robust foundation for cross-view matching."
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
  "title": "Equidistant Re-projection (ERP) Loss",
  "audio_content": "Standard re-projection losses bias keypoints toward the vehicle because distant errors are over-penalized. Our ERP loss normalizes error by distance, ensuring equitable impact across the scene. This promotes a dispersed distribution of landmarks, providing the geometric constraints needed to significantly improve orientation accuracy.",
  "duration_sec": 15.2,
  "bullets": [
    "Normalizes re-projection error by distance to eliminate proximity bias",
    "Promotes a dispersed keypoint distribution for robust geometric constraints",
    "Significantly improves orientation precision in challenging scenarios"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 5",
    "caption": "Comparison of keypoint distribution without ERP loss (left) and with ERP loss (right)."
  },
  "source": [
    "Section 4.3",
    "Figure 5",
    "Table 4",
    "Equation 9"
  ],
  "prompt": "A slide showing Figure 5 from the paper, which compares keypoint distributions. On the left, keypoints are clustered near the vehicle; on the right, they are widely dispersed across the scene. Below the figure, bullet points explain how the ERP loss normalizes error by distance to achieve this more robust distribution for orientation estimation."
}"""

Token usage so far: 127222 prompt tokens, 8272 completion tokens

Cost so far: $1.52038

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "Equidistant Re-projection (ERP) Loss",
  "audio_content": "Standard re-projection losses bias keypoints toward the vehicle because distant errors are over-penalized. Our ERP loss normalizes error by distance, ensuring equitable impact across the scene. This promotes a dispersed distribution of landmarks, providing the geometric constraints needed to significantly improve orientation accuracy.",
  "duration_sec": 15.2,
  "bullets": [
    "Normalizes re-projection error by distance to eliminate proximity bias",
    "Promotes a dispersed keypoint distribution for robust geometric constraints",
    "Significantly improves orientation precision in challenging scenarios"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 5",
    "caption": "Comparison of keypoint distribution without ERP loss (left) and with ERP loss (right)."
  },
  "source": [
    "Section 4.3",
    "Figure 5",
    "Table 4",
    "Equation 9"
  ],
  "prompt": "A slide showing Figure 5 from the paper, which compares keypoint distributions. On the left, keypoints are clustered near the vehicle; on the right, they are widely dispersed across the scene. Below the figure, bullet points explain how the ERP loss normalizes error by distance to achieve this more robust distribution for orientation estimation."
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
      "h": 0.42
    },
    "bullets": {
      "x": 0.05,
      "y": 0.62,
      "w": 0.9,
      "h": 0.33
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
  "expected_build_steps": 4,
  "elements": {
    "title": "Equidistant Re-projection (ERP) Loss",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 5",
      "caption": "Comparison of keypoint distribution without ERP loss (left) and with ERP loss (right)."
    },
    "bullets": [
      "Normalizes re-projection error by distance to eliminate proximity bias",
      "Promotes a dispersed keypoint distribution for robust geometric constraints",
      "Significantly improves orientation precision in challenging scenarios"
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
      "audio_segment": "Standard re-projection losses bias keypoints toward the vehicle because distant errors are over-penalized.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 3.8,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[0]"
        }
      ],
      "audio_segment": "Our ERP loss normalizes error by distance, ensuring equitable impact across the scene.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 7.6,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[1]"
        }
      ],
      "audio_segment": "This promotes a dispersed distribution of landmarks, providing the geometric constraints needed",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 11.4,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[2]"
        }
      ],
      "audio_segment": "to significantly improve orientation accuracy.",
      "visual_emphasis": []
    }
  ]
}"""

Token usage so far: 133747 prompt tokens, 8836 completion tokens

Cost so far: $1.60255

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 5,
  "title": "Experimental Results on KITTI and Ford Datasets",
  "summary": "Evaluations on KITTI and Ford Multi-AV datasets show that the method consistently achieves the lowest mean longitudinal and lateral translation errors. It demonstrates superior robustness, particularly when the initial pose is less accurate, outperforming existing pixel-wise and patch-wise methods.",
  "paper_section": "Experiments",
  "narrative_role": "experiments",
  "asset_video": null,
  "duration_stat": {
    "min": 8.0,
    "max": 15.0,
    "avg": 12.0
  }
}

## Previous Scenes Memory
The following content was extracted for the immediately preceding scenes. **This is provided as a memory of what the audience has JUST seen.**
You MUST NOT repeat the claims, figures, tables, or equations from these previous scenes in your current extraction, to ensure the presentation maintains forward momentum without redundant slides.
If you must reference the exactly same figure/table, the 'relevance' MUST be clearly unique to avoid narrative duplication.

{
  "extracted_content": "The Cycle Domain Adaptation (CycDA) loss is designed to mitigate representation gaps arising from differences in camera specifications (e.g., tone, hue, resolution) and environmental changes between ground and aerial views. It explicitly enforces view-invariant feature extraction by minimizing the L2 distance between features across three distinct spaces: the ground feature space, the satellite feature space, and a shared latent feature space. This bidirectional adaptation ensures that features extracted from one domain are effectively translatable to the other. The process utilizes projection functions $\\mathcal{E}(\\cdot)$ and $\\mathcal{D}(\\cdot)$, which are guided by the focal lengths of the satellite and vehicle cameras ($c_s$ and $c_g$) to maintain geometric consistency during the feature transformation.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "Our method adopts PureACL [24] as the baseline model and introduces three novel components (highlighted in red): ... (2) CycDA Loss (Sec.4.2): explicitly enforces a view-invariant representation for the same object; ...",
      "relevance": "The figure illustrates the integration of the CycDA Loss within the overall architecture, showing how it supervises the feature extraction process to ensure domain invariance."
    }
  ],
  "key_tables": [],
  "key_equations": [
    {
      "ref": "Equation 4",
      "content": "\\mathcal{L}_{g} = \frac{1}{N} \\sum_{i=1}^{N} \\| F^{a}[p^{g}_{i}] - \\mathcal{D} ( \\mathcal{E} ( F^{s}[p^{s}_{i}(\\mathbf{P}_{gt})] \textcircled{c} c_{s} ) \textcircled{c} c_{g} ) \\|_{2}",
      "relevance": "Defines the representation loss in the ground feature space, comparing aggregated ground features with projected satellite features."
    },
    {
      "ref": "Equation 5",
      "content": "\\mathcal{L}_{s} = \frac{1}{N} \\sum_{i=1}^{N} \\| F^{s}[p^{s}_{i}(\\mathbf{P}_{gt})] - \\mathcal{D} ( \\mathcal{E} ( F^{a}[p^{g}_{i}] \textcircled{c} c_{g} ) \textcircled{c} c_{s} ) \\|_{2}",
      "relevance": "Defines the representation loss in the satellite feature space, comparing satellite features with projected ground features."
    },
    {
      "ref": "Equation 6",
      "content": "\\mathcal{L}_{m} = \frac{1}{N} \\sum_{i=1}^{N} \\| \\mathcal{E} ( F^{a}[p^{g}_{i}] \textcircled{c} c_{g}) - \\mathcal{E} ( F^{s}[p^{s}_{i}(\\mathbf{P}_{gt})] \textcircled{c} c_{s} ) \\|_{2}",
      "relevance": "Defines the alignment loss in the shared latent feature space, ensuring both views map to a consistent representation."
    },
    {
      "ref": "Equation 7",
      "content": "\\mathcal{L}_{CycDA} = \\mathcal{L}_{g} + \\mathcal{L}_{s} + \\mathcal{L}_{m}",
      "relevance": "The total Cycle Domain Adaptation loss, combining the three feature space discrepancies."
    }
  ]
}
{
  "extracted_content": "The Equidistant Re-projection (ERP) loss is designed to address a common bias in keypoint-based localization where standard re-projection losses ($L_{RP}$) tend to favor keypoints closer to the vehicle. This bias occurs because orientation errors for distant points result in larger L2 distances in the image plane, causing the model to over-penalize them and cluster keypoint detections in the immediate vicinity of the vehicle. The ERP loss ($L_{ERP}$) mitigates this by applying a distance-weighted approach, dividing the re-projection error by the L2 distance ($D_{p^s_i}$) between the keypoint and the vehicle in the satellite view. This normalization ensures that orientation errors are independent of keypoint distance, leading to a more uniform and extended distribution of keypoints across the scene. This dispersed distribution provides more robust geometric constraints, significantly improving the precision of vehicle orientation estimation, especially in challenging scenarios with inaccurate initial poses.",
  "key_figures": [
    {
      "ref": "Figure 5",
      "caption": "Comparison of detected keypoints with and without ERP Loss. (Left) Without the ERP Loss, keypoints are predominantly located in close proximity to the vehicle. (Right) With the ERP Loss, there is a more dispersed distribution of keypoints.",
      "relevance": "Visually demonstrates how the ERP loss prevents keypoint clustering near the vehicle and encourages the detection of distant landmarks for better orientation cues."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 4",
      "caption": "Ablation study on the KITTI-CVL dataset \u2018Cross\u2019 area with initial noise (\u00b145\u00b0, \u00b120m).",
      "relevance": "Shows the quantitative impact of the ERP loss, specifically highlighting the reduction in mean orientation error from 3.38\u00b0 to 2.88\u00b0 when added to the T2GA and CycDA components."
    }
  ],
  "key_equations": [
    {
      "ref": "Equation 8",
      "content": "L_{RP} = \frac{1}{N} \\sum_{i=1}^{N}\\|p_{i}^{s}(\\mathbf{P}_{pred})-p^{s}_{i}(\\mathbf{P}_{gt}) \\|_2^2",
      "relevance": "Defines the baseline re-projection loss which suffers from distance-based bias in orientation error penalization."
    },
    {
      "ref": "Equation 9",
      "content": "L_{ERP} = \frac{1}{N} \\sum^{N}_{i=1}\\|\frac{p_{i}^{s}(\\mathbf{P}_{pred})-p_{i}^{s}(\\mathbf{P}_{gt})}{\\mathbf{D}_{p^{s}_{i}}} \\|_2^2",
      "relevance": "Defines the proposed Equidistant Re-projection loss that normalizes error by distance to ensure equitable impact of all keypoints on orientation estimation."
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
  "extracted_content": "The proposed method was rigorously evaluated on the KITTI-CVL and Ford Multi-AV datasets, consistently outperforming state-of-the-art pixel-wise and patch-wise localization methods. Under standard noise conditions (±10°, ±20m), it achieves a mean location error of 0.20m on KITTI, a significant improvement over the baseline PureACL (2.42m). The method's robustness is most evident under extreme initial noise (±45°, ±20m), where it maintains high precision (e.g., 0.17m mean lateral error) and superior convergence compared to baselines that struggle with large orientation errors. Furthermore, in continual pose estimation scenarios where only the starting pose is provided, the method successfully completes 100% of the evaluation routes, whereas competing methods like BoostAcc and PureACL suffer from severe drift and fail early in the trajectory. Multi-camera setups (F-4C) further enhance performance, reducing mean lateral error to 0.13m on the Ford dataset.",
  "key_figures": [
    {
      "ref": "Figure 6",
      "caption": "Comparison of the baseline method PureACL and our proposed method under varying initial noise ranges in the ‘cross’ area of the KITTI-CVL dataset.",
      "relevance": "Illustrates the robust convergence of the proposed method across increasing noise levels, specifically showing a much smaller gap between mean and median errors compared to the baseline."
    },
    {
      "ref": "Figure 7",
      "caption": "Accumulated pose estimation performance on a KITTI CVL dataset trajectory.",
      "relevance": "Provides a visual comparison of trajectory tracking, showing the proposed method (blue) closely matching the ground truth (red) over a 3676-meter route while others drift significantly."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 1",
      "caption": "Comparison on the KITTI-CVL Dataset Under Initial Noise Conditions (±10°, ±20m).",
      "relevance": "Presents the primary comparative results against numerous state-of-the-art methods, establishing the proposed model's superior accuracy in location and orientation."
    },
    {
      "ref": "Table 2",
      "caption": "Comparison with Initial Noise Conditions (±45°, ±20m).",
      "relevance": "Demonstrates the method's performance in the most challenging noise settings across both KITTI and Ford datasets, highlighting its consistent lead in longitudinal and lateral accuracy."
    },
    {
      "ref": "Table 3",
      "caption": "Comparison on Accumulated Pose Estimation.",
      "relevance": "Quantifies the method's ability to maintain localization over long distances, achieving 100% route completion where baselines fail."
    }
  ],
  "key_equations": [],
  "section_refs": ["Section 5.2", "Section 5.3", "Section 5.4"]
}"""

Token usage so far: 141202 prompt tokens, 9518 completion tokens

Cost so far: $1.69756

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "The proposed method was rigorously evaluated on the KITTI-CVL and Ford Multi-AV datasets, consistently outperforming state-of-the-art pixel-wise and patch-wise localization methods. Under standard noise conditions (\u00b110\u00b0, \u00b120m), it achieves a mean location error of 0.20m on KITTI, a significant improvement over the baseline PureACL (2.42m). The method's robustness is most evident under extreme initial noise (\u00b145\u00b0, \u00b120m), where it maintains high precision (e.g., 0.17m mean lateral error) and superior convergence compared to baselines that struggle with large orientation errors. Furthermore, in continual pose estimation scenarios where only the starting pose is provided, the method successfully completes 100% of the evaluation routes, whereas competing methods like BoostAcc and PureACL suffer from severe drift and fail early in the trajectory. Multi-camera setups (F-4C) further enhance performance, reducing mean lateral error to 0.13m on the Ford dataset.",
  "key_figures": [
    {
      "ref": "Figure 6",
      "caption": "Comparison of the baseline method PureACL and our proposed method under varying initial noise ranges in the \u2018cross\u2019 area of the KITTI-CVL dataset.",
      "relevance": "Illustrates the robust convergence of the proposed method across increasing noise levels, specifically showing a much smaller gap between mean and median errors compared to the baseline."
    },
    {
      "ref": "Figure 7",
      "caption": "Accumulated pose estimation performance on a KITTI CVL dataset trajectory.",
      "relevance": "Provides a visual comparison of trajectory tracking, showing the proposed method (blue) closely matching the ground truth (red) over a 3676-meter route while others drift significantly."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 1",
      "caption": "Comparison on the KITTI-CVL Dataset Under Initial Noise Conditions (\u00b110\u00b0, \u00b120m).",
      "relevance": "Presents the primary comparative results against numerous state-of-the-art methods, establishing the proposed model's superior accuracy in location and orientation."
    },
    {
      "ref": "Table 2",
      "caption": "Comparison with Initial Noise Conditions (\u00b145\u00b0, \u00b120m).",
      "relevance": "Demonstrates the method's performance in the most challenging noise settings across both KITTI and Ford datasets, highlighting its consistent lead in longitudinal and lateral accuracy."
    },
    {
      "ref": "Table 3",
      "caption": "Comparison on Accumulated Pose Estimation.",
      "relevance": "Quantifies the method's ability to maintain localization over long distances, achieving 100% route completion where baselines fail."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "Section 5.2",
    "Section 5.3",
    "Section 5.4"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 5,
  "title": "Experimental Results on KITTI and Ford Datasets",
  "summary": "Evaluations on KITTI and Ford Multi-AV datasets show that the method consistently achieves the lowest mean longitudinal and lateral translation errors. It demonstrates superior robustness, particularly when the initial pose is less accurate, outperforming existing pixel-wise and patch-wise methods.",
  "paper_section": "Experiments",
  "narrative_role": "experiments",
  "asset_video": null,
  "duration_stat": {
    "min": 8.0,
    "max": 15.0,
    "avg": 12.0
  }
}

Reference style advice:
Reference Layouts for 'experiments' section from similar papers:
- Example 1: The slide follows a clean, minimalist layout. A large, bold title 'Video Analysis' is positioned at the top-left. Directly below it, a single grey bullet point introduces a line of text: 'Test whether short video clips are approximately geodesic.' The central and lower portion of the slide is occupied by four square images arranged in a single horizontal row. These images appear to be frames from video clips, each showing a different 3D rendered object on a plain grey surface: a red cube, a teal cylinder, a dark grey cube, and a lime green sphere. The background of the slide is plain white, and the overall text density is light, emphasizing the visual content.
- Example 2: The slide uses a minimalist horizontal split-screen layout. The top half of the slide has a solid teal background, featuring the word 'Experiments' centered horizontally and vertically within that section in a white, sans-serif font. The bottom half of the slide is solid white and contains institutional branding. In the bottom-left corner, the phrase 'Australia's National Science Agency' is printed in a small, light-grey font. In the bottom-right corner, two logos are positioned side-by-side: the Australian National University crest and name, followed by the CSIRO logo, which consists of a teal circular icon with white vertical bars and the text 'CSIRO' underneath. The slide has a very light text density and serves as a clear transition to the experimental section of the presentation.

Duration statistics for this section (from references): min=1.9s, max=7.0s, avg=4.5s.

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
    "figure": {"x": 0.05, "y": 0.18, "w": 0.9, "h": 0.52},
    "bullets": {"x": 0.05, "y": 0.72, "w": 0.9, "h": 0.23}
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "A wide figure region is chosen to accommodate Figure 7's trajectory maps or Figure 6's side-by-side charts, following the minimalist and visual-heavy style suggested in the reference examples. This layout allows the key experimental results to be displayed prominently with supporting summary bullets below."
}"""

Token usage so far: 148564 prompt tokens, 9764 completion tokens

Cost so far: $1.77856

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "The proposed method was rigorously evaluated on the KITTI-CVL and Ford Multi-AV datasets, consistently outperforming state-of-the-art pixel-wise and patch-wise localization methods. Under standard noise conditions (\u00b110\u00b0, \u00b120m), it achieves a mean location error of 0.20m on KITTI, a significant improvement over the baseline PureACL (2.42m). The method's robustness is most evident under extreme initial noise (\u00b145\u00b0, \u00b120m), where it maintains high precision (e.g., 0.17m mean lateral error) and superior convergence compared to baselines that struggle with large orientation errors. Furthermore, in continual pose estimation scenarios where only the starting pose is provided, the method successfully completes 100% of the evaluation routes, whereas competing methods like BoostAcc and PureACL suffer from severe drift and fail early in the trajectory. Multi-camera setups (F-4C) further enhance performance, reducing mean lateral error to 0.13m on the Ford dataset.",
  "key_figures": [
    {
      "ref": "Figure 6",
      "caption": "Comparison of the baseline method PureACL and our proposed method under varying initial noise ranges in the \u2018cross\u2019 area of the KITTI-CVL dataset.",
      "relevance": "Illustrates the robust convergence of the proposed method across increasing noise levels, specifically showing a much smaller gap between mean and median errors compared to the baseline."
    },
    {
      "ref": "Figure 7",
      "caption": "Accumulated pose estimation performance on a KITTI CVL dataset trajectory.",
      "relevance": "Provides a visual comparison of trajectory tracking, showing the proposed method (blue) closely matching the ground truth (red) over a 3676-meter route while others drift significantly."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 1",
      "caption": "Comparison on the KITTI-CVL Dataset Under Initial Noise Conditions (\u00b110\u00b0, \u00b120m).",
      "relevance": "Presents the primary comparative results against numerous state-of-the-art methods, establishing the proposed model's superior accuracy in location and orientation."
    },
    {
      "ref": "Table 2",
      "caption": "Comparison with Initial Noise Conditions (\u00b145\u00b0, \u00b120m).",
      "relevance": "Demonstrates the method's performance in the most challenging noise settings across both KITTI and Ford datasets, highlighting its consistent lead in longitudinal and lateral accuracy."
    },
    {
      "ref": "Table 3",
      "caption": "Comparison on Accumulated Pose Estimation.",
      "relevance": "Quantifies the method's ability to maintain localization over long distances, achieving 100% route completion where baselines fail."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "Section 5.2",
    "Section 5.3",
    "Section 5.4"
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
      "h": 0.52
    },
    "bullets": {
      "x": 0.05,
      "y": 0.72,
      "w": 0.9,
      "h": 0.23
    }
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "A wide figure region is chosen to accommodate Figure 7's trajectory maps or Figure 6's side-by-side charts, following the minimalist and visual-heavy style suggested in the reference examples. This layout allows the key experimental results to be displayed prominently with supporting summary bullets below."
}

Scene context:
{
  "scene_id": 5,
  "title": "Experimental Results on KITTI and Ford Datasets",
  "summary": "Evaluations on KITTI and Ford Multi-AV datasets show that the method consistently achieves the lowest mean longitudinal and lateral translation errors. It demonstrates superior robustness, particularly when the initial pose is less accurate, outperforming existing pixel-wise and patch-wise methods.",
  "paper_section": "Experiments",
  "narrative_role": "experiments",
  "asset_video": null,
  "duration_stat": {
    "min": 8.0,
    "max": 15.0,
    "avg": 12.0
  }
}

## Previous Content
The following content was drafted for the immediately preceding scenes.
You MUST NOT repeat the exact text content or claims from these previous scenes in your current draft.

{
  "bullets": [
    "Normalizes re-projection error by distance to eliminate proximity bias",
    "Promotes a dispersed keypoint distribution for robust geometric constraints",
    "Significantly improves orientation precision in challenging scenarios"
  ],
  "audio_content": "Standard re-projection losses bias keypoints toward the vehicle because distant errors are over-penalized. Our ERP loss normalizes error by distance, ensuring equitable impact across the scene. This promotes a dispersed distribution of landmarks, providing the geometric constraints needed to significantly improve orientation accuracy."
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
  "title": "State-of-the-Art Performance and Robustness",
  "audio_content": "Our method achieves a zero-point-two meter mean error on KITTI, a significant leap over the baseline. It maintains high precision under extreme noise and successfully completes one hundred percent of evaluation routes, whereas competing methods drift and fail early.",
  "duration_sec": 15.2,
  "bullets": [
    "Achieves 0.20m mean location error on KITTI, a 90% improvement over PureACL",
    "Maintains high precision and superior convergence under extreme initial noise",
    "Completes 100% of evaluation routes where baselines suffer from severe drift"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 7",
    "caption": "Trajectory tracking comparison over a 3676-meter route"
  },
  "source": ["Section 5.2", "Section 5.4", "Figure 7", "Table 3"],
  "prompt": "A slide showing Figure 7 from the paper, which displays trajectory maps comparing the proposed method's tracking accuracy against PureACL and BoostAcc. Below the figure, three bullet points summarize the quantitative performance gains and robustness to noise."
}"""

Token usage so far: 155720 prompt tokens, 10057 completion tokens

Cost so far: $1.85891

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "State-of-the-Art Performance and Robustness",
  "audio_content": "Our method achieves a zero-point-two meter mean error on KITTI, a significant leap over the baseline. It maintains high precision under extreme noise and successfully completes one hundred percent of evaluation routes, whereas competing methods drift and fail early.",
  "duration_sec": 15.2,
  "bullets": [
    "Achieves 0.20m mean location error on KITTI, a 90% improvement over PureACL",
    "Maintains high precision and superior convergence under extreme initial noise",
    "Completes 100% of evaluation routes where baselines suffer from severe drift"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 7",
    "caption": "Trajectory tracking comparison over a 3676-meter route"
  },
  "source": [
    "Section 5.2",
    "Section 5.4",
    "Figure 7",
    "Table 3"
  ],
  "prompt": "A slide showing Figure 7 from the paper, which displays trajectory maps comparing the proposed method's tracking accuracy against PureACL and BoostAcc. Below the figure, three bullet points summarize the quantitative performance gains and robustness to noise."
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
      "h": 0.52
    },
    "bullets": {
      "x": 0.05,
      "y": 0.72,
      "w": 0.9,
      "h": 0.23
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

"""```json
{
  "style": "Slides",
  "expected_build_steps": 4,
  "elements": {
    "title": "State-of-the-Art Performance and Robustness",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 7",
      "caption": "Trajectory tracking comparison over a 3676-meter route"
    },
    "bullets": [
      "Achieves 0.20m mean location error on KITTI, a 90% improvement over PureACL",
      "Maintains high precision and superior convergence under extreme initial noise",
      "Completes 100% of evaluation routes where baselines suffer from severe drift"
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
      "audio_segment": "Our method achieves a zero-point-two meter mean error on KITTI,",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 3.8,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[0]"
        }
      ],
      "audio_segment": "a significant leap over the baseline.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 7.6,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[1]"
        }
      ],
      "audio_segment": "It maintains high precision under extreme noise",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 11.4,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[2]"
        }
      ],
      "audio_segment": "and successfully completes one hundred percent of evaluation routes, whereas competing methods drift and fail early.",
      "visual_emphasis": []
    }
  ]
}
```"""

Token usage so far: 162237 prompt tokens, 10636 completion tokens

Cost so far: $1.94145

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 6,
  "title": "Continual Vehicle Pose Estimation",
  "summary": "The system can complete entire routes through continual vehicle pose estimation, requiring only an initial pose at the starting point. This capability highlights its generalization ability and potential for practical deployment in autonomous driving and outdoor robotics.",
  "paper_section": "Results",
  "narrative_role": "results",
  "asset_video": null,
  "duration_stat": {
    "min": 6.0,
    "max": 13.0,
    "avg": 9.0
  }
}

## Previous Scenes Memory
The following content was extracted for the immediately preceding scenes. **This is provided as a memory of what the audience has JUST seen.**
You MUST NOT repeat the claims, figures, tables, or equations from these previous scenes in your current extraction, to ensure the presentation maintains forward momentum without redundant slides.
If you must reference the exactly same figure/table, the 'relevance' MUST be clearly unique to avoid narrative duplication.

{
  "extracted_content": "The Equidistant Re-projection (ERP) loss is designed to address a common bias in keypoint-based localization where standard re-projection losses ($L_{RP}$) tend to favor keypoints closer to the vehicle. This bias occurs because orientation errors for distant points result in larger L2 distances in the image plane, causing the model to over-penalize them and cluster keypoint detections in the immediate vicinity of the vehicle. The ERP loss ($L_{ERP}$) mitigates this by applying a distance-weighted approach, dividing the re-projection error by the L2 distance ($D_{p^s_i}$) between the keypoint and the vehicle in the satellite view. This normalization ensures that orientation errors are independent of keypoint distance, leading to a more uniform and extended distribution of keypoints across the scene. This dispersed distribution provides more robust geometric constraints, significantly improving the precision of vehicle orientation estimation, especially in challenging scenarios with inaccurate initial poses.",
  "key_figures": [
    {
      "ref": "Figure 5",
      "caption": "Comparison of detected keypoints with and without ERP Loss. (Left) Without the ERP Loss, keypoints are predominantly located in close proximity to the vehicle. (Right) With the ERP Loss, there is a more dispersed distribution of keypoints.",
      "relevance": "Visually demonstrates how the ERP loss prevents keypoint clustering near the vehicle and encourages the detection of distant landmarks for better orientation cues."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 4",
      "caption": "Ablation study on the KITTI-CVL dataset \u2018Cross\u2019 area with initial noise (\u00b145\u00b0, \u00b120m).",
      "relevance": "Shows the quantitative impact of the ERP loss, specifically highlighting the reduction in mean orientation error from 3.38\u00b0 to 2.88\u00b0 when added to the T2GA and CycDA components."
    }
  ],
  "key_equations": [
    {
      "ref": "Equation 8",
      "content": "L_{RP} = \frac{1}{N} \\sum_{i=1}^{N}\\|p_{i}^{s}(\\mathbf{P}_{pred})-p^{s}_{i}(\\mathbf{P}_{gt}) \\|_2^2",
      "relevance": "Defines the baseline re-projection loss which suffers from distance-based bias in orientation error penalization."
    },
    {
      "ref": "Equation 9",
      "content": "L_{ERP} = \frac{1}{N} \\sum^{N}_{i=1}\\|\frac{p_{i}^{s}(\\mathbf{P}_{pred})-p_{i}^{s}(\\mathbf{P}_{gt})}{\\mathbf{D}_{p^{s}_{i}}} \\|_2^2",
      "relevance": "Defines the proposed Equidistant Re-projection loss that normalizes error by distance to ensure equitable impact of all keypoints on orientation estimation."
    }
  ]
}
{
  "extracted_content": "The proposed method was rigorously evaluated on the KITTI-CVL and Ford Multi-AV datasets, consistently outperforming state-of-the-art pixel-wise and patch-wise localization methods. Under standard noise conditions (\u00b110\u00b0, \u00b120m), it achieves a mean location error of 0.20m on KITTI, a significant improvement over the baseline PureACL (2.42m). The method's robustness is most evident under extreme initial noise (\u00b145\u00b0, \u00b120m), where it maintains high precision (e.g., 0.17m mean lateral error) and superior convergence compared to baselines that struggle with large orientation errors. Furthermore, in continual pose estimation scenarios where only the starting pose is provided, the method successfully completes 100% of the evaluation routes, whereas competing methods like BoostAcc and PureACL suffer from severe drift and fail early in the trajectory. Multi-camera setups (F-4C) further enhance performance, reducing mean lateral error to 0.13m on the Ford dataset.",
  "key_figures": [
    {
      "ref": "Figure 6",
      "caption": "Comparison of the baseline method PureACL and our proposed method under varying initial noise ranges in the \u2018cross\u2019 area of the KITTI-CVL dataset.",
      "relevance": "Illustrates the robust convergence of the proposed method across increasing noise levels, specifically showing a much smaller gap between mean and median errors compared to the baseline."
    },
    {
      "ref": "Figure 7",
      "caption": "Accumulated pose estimation performance on a KITTI CVL dataset trajectory.",
      "relevance": "Provides a visual comparison of trajectory tracking, showing the proposed method (blue) closely matching the ground truth (red) over a 3676-meter route while others drift significantly."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 1",
      "caption": "Comparison on the KITTI-CVL Dataset Under Initial Noise Conditions (\u00b110\u00b0, \u00b120m).",
      "relevance": "Presents the primary comparative results against numerous state-of-the-art methods, establishing the proposed model's superior accuracy in location and orientation."
    },
    {
      "ref": "Table 2",
      "caption": "Comparison with Initial Noise Conditions (\u00b145\u00b0, \u00b120m).",
      "relevance": "Demonstrates the method's performance in the most challenging noise settings across both KITTI and Ford datasets, highlighting its consistent lead in longitudinal and lateral accuracy."
    },
    {
      "ref": "Table 3",
      "caption": "Comparison on Accumulated Pose Estimation.",
      "relevance": "Quantifies the method's ability to maintain localization over long distances, achieving 100% route completion where baselines fail."
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
  "extracted_content": "To simulate real-world GPS-denied navigation, the system employs an accumulated pose estimation strategy, using the previous frame's estimate as the initial pose for the current frame. Evaluation over a 3676-meter route reveals that the method is uniquely robust against dynamic scene changes; for instance, it avoids the significant drifts caused by moving vehicles that plague methods like BoostAcc, which suffer from incorrect query data from projected vehicle pixels. Additionally, it overcomes the orientation reversal issues seen in PureACL. A key feature of the system is its 'rapid recovery' capability, where it quickly corrects minor drifts upon encountering distinct localization landmarks. This level of stability and self-correction across entire routes, regardless of whether using single or multi-camera setups, establishes a viable path for integrating cross-view localization into autonomous driving and outdoor robotics SLAM systems to remove loop closure dependency.",
  "key_figures": [
    {
      "ref": "Figure 7",
      "caption": "Accumulated pose estimation performance on a KITTI CVL dataset trajectory.",
      "relevance": "Visualizes the 'rapid recovery' mechanism and the system's immunity to drifts caused by moving vehicles, contrasting its stable trajectory against the severe failures of baseline models over a long-distance route."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 3",
      "caption": "Comparison on Accumulated Pose Estimation.",
      "relevance": "Validates the method's reliability across different sensor configurations (single-camera F-1C vs. multi-camera F-4C), showing consistent 100% route completion which is essential for practical deployment on various vehicle types."
    }
  ],
  "key_equations": [],
  "section_refs": ["Section 5.4", "Section 7"]
}"""

Token usage so far: 169597 prompt tokens, 11038 completion tokens

Cost so far: $2.02711

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "To simulate real-world GPS-denied navigation, the system employs an accumulated pose estimation strategy, using the previous frame's estimate as the initial pose for the current frame. Evaluation over a 3676-meter route reveals that the method is uniquely robust against dynamic scene changes; for instance, it avoids the significant drifts caused by moving vehicles that plague methods like BoostAcc, which suffer from incorrect query data from projected vehicle pixels. Additionally, it overcomes the orientation reversal issues seen in PureACL. A key feature of the system is its 'rapid recovery' capability, where it quickly corrects minor drifts upon encountering distinct localization landmarks. This level of stability and self-correction across entire routes, regardless of whether using single or multi-camera setups, establishes a viable path for integrating cross-view localization into autonomous driving and outdoor robotics SLAM systems to remove loop closure dependency.",
  "key_figures": [
    {
      "ref": "Figure 7",
      "caption": "Accumulated pose estimation performance on a KITTI CVL dataset trajectory.",
      "relevance": "Visualizes the 'rapid recovery' mechanism and the system's immunity to drifts caused by moving vehicles, contrasting its stable trajectory against the severe failures of baseline models over a long-distance route."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 3",
      "caption": "Comparison on Accumulated Pose Estimation.",
      "relevance": "Validates the method's reliability across different sensor configurations (single-camera F-1C vs. multi-camera F-4C), showing consistent 100% route completion which is essential for practical deployment on various vehicle types."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "Section 5.4",
    "Section 7"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 6,
  "title": "Continual Vehicle Pose Estimation",
  "summary": "The system can complete entire routes through continual vehicle pose estimation, requiring only an initial pose at the starting point. This capability highlights its generalization ability and potential for practical deployment in autonomous driving and outdoor robotics.",
  "paper_section": "Results",
  "narrative_role": "results",
  "asset_video": null,
  "duration_stat": {
    "min": 6.0,
    "max": 13.0,
    "avg": 9.0
  }
}

Reference style advice:
Reference Layouts for 'results' section from similar papers:
- Example 1: The slide features a large, centered title at the top against a plain white background. The main body of the slide is occupied by a large composite figure that is divided into three panels by dashed gray lines: two panels on the top half and one wide panel spanning the bottom half. Each panel demonstrates a visual localization result, showing a sequence of camera poses represented by small blue wireframe frustums along a trajectory. Several keyframes from the videos are displayed as inset images, each connected to its specific camera pose by a thin blue line. The top-left panel depicts an indoor desk environment, the top-right panel shows a hallway with a sign, and the bottom panel shows an outdoor courtyard. The slide has a very light text density, relying almost entirely on visual diagrams to convey information.
- Example 2: The slide features a large, centered title at the top in a black serif font. Below the title, the main content consists of a horizontal arrangement of four visual elements for qualitative comparison. The first three elements from the left are large 3D visualizations showing complex camera trajectories and poses represented by small frustums and connecting lines. Each of these is labeled directly underneath with its corresponding method: 'Map-free (Regress)', 'ExReNet (SUNCG)', and 'Reloc3r-512 (Ours)'. The fourth element on the far right is a vertical stack of three smaller, more linear trajectory visualizations, each labeled to its right with the same three method names for a secondary comparison. The background is a solid white, and the overall text density is light, focusing entirely on the visual representation of the pose estimation results.
- Example 3: The slide features a large, left-aligned title at the top in a serif font. Below the title, a wide, detailed table occupies the central and lower portions of the slide. The table is structured with multiple columns representing different outdoor scenes (GreatCourt, KingsCollege, OldHospital, ShopFacade, StMarysChurch), two average columns, and a column for 'Dataset-specific training time'. Vertically, the table is divided into three main categories labeled on the far left: 'APR', 'RPR (Seen)', and 'RPR (Unseen)'. Each category contains several rows corresponding to different localization methods, with the authors' proposed methods ('Reloc3r-224' and 'Reloc3r-512') listed at the bottom. Numerical data within the table represents pose accuracy, with some values highlighted in bold to indicate superior performance. A centered caption, 'Absolute pose accuracy on Cambridge dataset.', is placed directly underneath the table. The slide has a clean white background with no additional decorative elements, resulting in a moderate to high text density focused on quantitative results.
- Example 4: The slide uses a dark background to showcase a large, full-width image of a street-level view. This main image features blue highlights, likely representing an attention map, concentrated on the road and adjacent walls. In the top-left corner, a smaller inset image provides a top-down aerial view of the same neighborhood, with a white circle marking a specific area. A thick white arrow connects the inset aerial view to the corresponding location in the street-level view. To the right of the inset, a block of yellow text serves as a descriptive heading or caption, explaining the visual data. The layout is designed for qualitative analysis, emphasizing the spatial relationship between different camera perspectives. Text density is light, prioritizing the visual elements.
- Example 5: The slide is dominated by a large, full-width image showing a first-person street view from a vehicle. At the top of the slide, a black horizontal bar contains a single paragraph of yellow text that explains the visual findings. Positioned at the top-left and top-right corners, overlapping the black bar and the main image, are two small square inset images showing a top-down satellite view of the same area. Each inset features a white circle and an arrow pointing to specific landmarks (trees and walls) to correlate the two perspectives. Overlaid on the main street-view image are glowing purple and blue horizontal lines and scattered points, which appear to be attention maps or feature visualizations, concentrated along the road and the tops of roadside structures. The layout is designed for qualitative analysis, with a light text density and a focus on visual comparison.

Duration statistics for this section (from references): min=1.0s, max=36.0s, avg=8.7s.

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
      "h": 0.55
    },
    "bullets": {
      "x": 0.05,
      "y": 0.75,
      "w": 0.9,
      "h": 0.2
    }
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "Following the visual-heavy style of successful localization papers, this layout prioritizes the multi-panel trajectory comparison in Figure 7. The wide figure region preserves the aspect ratio of the 2x2 grid of plots, while the bottom bullet region provides space to highlight the 100% route completion metric from Table 3 and the 'rapid recovery' capability."
}"""

Token usage so far: 177181 prompt tokens, 11331 completion tokens

Cost so far: $2.11174

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "To simulate real-world GPS-denied navigation, the system employs an accumulated pose estimation strategy, using the previous frame's estimate as the initial pose for the current frame. Evaluation over a 3676-meter route reveals that the method is uniquely robust against dynamic scene changes; for instance, it avoids the significant drifts caused by moving vehicles that plague methods like BoostAcc, which suffer from incorrect query data from projected vehicle pixels. Additionally, it overcomes the orientation reversal issues seen in PureACL. A key feature of the system is its 'rapid recovery' capability, where it quickly corrects minor drifts upon encountering distinct localization landmarks. This level of stability and self-correction across entire routes, regardless of whether using single or multi-camera setups, establishes a viable path for integrating cross-view localization into autonomous driving and outdoor robotics SLAM systems to remove loop closure dependency.",
  "key_figures": [
    {
      "ref": "Figure 7",
      "caption": "Accumulated pose estimation performance on a KITTI CVL dataset trajectory.",
      "relevance": "Visualizes the 'rapid recovery' mechanism and the system's immunity to drifts caused by moving vehicles, contrasting its stable trajectory against the severe failures of baseline models over a long-distance route."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 3",
      "caption": "Comparison on Accumulated Pose Estimation.",
      "relevance": "Validates the method's reliability across different sensor configurations (single-camera F-1C vs. multi-camera F-4C), showing consistent 100% route completion which is essential for practical deployment on various vehicle types."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "Section 5.4",
    "Section 7"
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
      "h": 0.55
    },
    "bullets": {
      "x": 0.05,
      "y": 0.75,
      "w": 0.9,
      "h": 0.2
    }
  },
  "has_figure": true,
  "has_video": false,
  "style_rationale": "Following the visual-heavy style of successful localization papers, this layout prioritizes the multi-panel trajectory comparison in Figure 7. The wide figure region preserves the aspect ratio of the 2x2 grid of plots, while the bottom bullet region provides space to highlight the 100% route completion metric from Table 3 and the 'rapid recovery' capability."
}

Scene context:
{
  "scene_id": 6,
  "title": "Continual Vehicle Pose Estimation",
  "summary": "The system can complete entire routes through continual vehicle pose estimation, requiring only an initial pose at the starting point. This capability highlights its generalization ability and potential for practical deployment in autonomous driving and outdoor robotics.",
  "paper_section": "Results",
  "narrative_role": "results",
  "asset_video": null,
  "duration_stat": {
    "min": 6.0,
    "max": 13.0,
    "avg": 9.0
  }
}

## Previous Content
The following content was drafted for the immediately preceding scenes.
You MUST NOT repeat the exact text content or claims from these previous scenes in your current draft.

{
  "bullets": [
    "Achieves 0.20m mean location error on KITTI, a 90% improvement over PureACL",
    "Maintains high precision and superior convergence under extreme initial noise",
    "Completes 100% of evaluation routes where baselines suffer from severe drift"
  ],
  "audio_content": "Our method achieves a zero-point-two meter mean error on KITTI, a significant leap over the baseline. It maintains high precision under extreme noise and successfully completes one hundred percent of evaluation routes, whereas competing methods drift and fail early."
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
  "title": "Robust Continual Pose Estimation",
  "audio_content": "The system maintains stable navigation over three-point-six kilometers from just one initial pose. It resists drifts from moving vehicles and uses a rapid recovery mechanism to self-correct at landmarks, ensuring reliable performance for GPS-denied autonomous driving.",
  "duration_sec": 14.4,
  "bullets": [
    "Maintains stability over 3.6km routes from a single initial pose",
    "Resists significant drifts caused by dynamic objects and moving vehicles",
    "Rapidly recovers and self-corrects upon encountering distinct landmarks"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 7",
    "caption": "Accumulated pose estimation performance showing stable trajectory and rapid recovery compared to baselines."
  },
  "source": [
    "Section 5.4",
    "Figure 7",
    "Table 3"
  ],
  "prompt": "A slide showing a 2x2 grid of trajectory plots from Figure 7, comparing the stable blue line of the proposed method against the drifting green and cyan lines of baselines. Callouts highlight the 'rapid recovery' points and the system's immunity to moving vehicles."
}"""

Token usage so far: 183995 prompt tokens, 11619 completion tokens

Cost so far: $2.18852

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "Robust Continual Pose Estimation",
  "audio_content": "The system maintains stable navigation over three-point-six kilometers from just one initial pose. It resists drifts from moving vehicles and uses a rapid recovery mechanism to self-correct at landmarks, ensuring reliable performance for GPS-denied autonomous driving.",
  "duration_sec": 14.4,
  "bullets": [
    "Maintains stability over 3.6km routes from a single initial pose",
    "Resists significant drifts caused by dynamic objects and moving vehicles",
    "Rapidly recovers and self-corrects upon encountering distinct landmarks"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 7",
    "caption": "Accumulated pose estimation performance showing stable trajectory and rapid recovery compared to baselines."
  },
  "source": [
    "Section 5.4",
    "Figure 7",
    "Table 3"
  ],
  "prompt": "A slide showing a 2x2 grid of trajectory plots from Figure 7, comparing the stable blue line of the proposed method against the drifting green and cyan lines of baselines. Callouts highlight the 'rapid recovery' points and the system's immunity to moving vehicles."
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
      "h": 0.55
    },
    "bullets": {
      "x": 0.05,
      "y": 0.75,
      "w": 0.9,
      "h": 0.2
    }
  },
  "has_figure": true,
  "total_time_sec": 14.4
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
    "title": "Robust Continual Pose Estimation",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 7",
      "caption": "Accumulated pose estimation performance showing stable trajectory and rapid recovery compared to baselines."
    },
    "bullets": [
      "Maintains stability over 3.6km routes from a single initial pose",
      "Resists significant drifts caused by dynamic objects and moving vehicles",
      "Rapidly recovers and self-corrects upon encountering distinct landmarks"
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
      "audio_segment": "The system maintains stable navigation over three-point-six kilometers from just one initial pose.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 3.6,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[0]"
        }
      ],
      "audio_segment": "This stability is demonstrated over long routes, starting from only a single initial pose.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 7.2,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[1]"
        }
      ],
      "audio_segment": "It resists drifts from moving vehicles and dynamic objects that often compromise baseline methods.",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 10.8,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[2]"
        }
      ],
      "audio_segment": "Furthermore, it uses a rapid recovery mechanism to self-correct at landmarks, ensuring reliable performance for GPS-denied autonomous driving.",
      "visual_emphasis": []
    }
  ]
}
```"""

Token usage so far: 190494 prompt tokens, 12206 completion tokens

Cost so far: $2.27112

