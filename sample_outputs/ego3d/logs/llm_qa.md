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



Requirements: 
1. Each scene must include strong relationship between last and next scene, but there must be no overlap of content.
2. STRICTLY No overlapping content between scenes.
3. Collectively present all key findings in a coherent narrative.
4. Maintain high technical accuracy and professionalism.
5. Deliver only core content; omit acknowledgements and references.
6. Do NOT create a title/introduction scene. Scene 0 (title page with paper title, authors, logos) is auto-generated separately. Start your scenes from the paper's technical content.

You MUST output the scenes in the following STRICT JSON format (list of objects):
```json
[
  {
    "scene_id": 1,
    "title": "Brief title",
    "summary": "content covered in this scene",
    "paper_section": "Introduction/Method/etc",
    "narrative_role": "one of [introduction/experiments/method/results]",
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
    "title": "Motivation for Ego-View 3D Action Recognition",
    "summary": "Explains the need for 3D point cloud action recognition in ego-view scenarios, particularly for head-mounted devices where RGB data may be degraded or insufficient for safety-critical applications.",
    "paper_section": "1. Introduction",
    "narrative_role": "introduction",
    "duration_stat": {
      "min": 8.0,
      "max": 15.0,
      "avg": 10.0
    }
  },
  {
    "scene_id": 2,
    "title": "IKEA Ego 3D Dataset Overview",
    "summary": "Introduces the IKEA Ego 3D dataset, featuring 174 assembly sequences and approximately 493k frames of humans performing intricate furniture assembly actions captured from an ego-view.",
    "paper_section": "3. The IKEA Ego3D dataset",
    "narrative_role": "method",
    "duration_stat": {
      "min": 7.0,
      "max": 12.0,
      "avg": 9.0
    }
  },
  {
    "scene_id": 3,
    "title": "Data Collection and Processing Pipeline",
    "summary": "Details the hardware setup using Microsoft HoloLens 2 and the post-processing stage where RGB and depth streams are synced and projected to form oriented 3D point cloud sequences.",
    "paper_section": "3.1 Data collection",
    "narrative_role": "method",
    "duration_stat": {
      "min": 8.0,
      "max": 14.0,
      "avg": 10.0
    }
  },
  {
    "scene_id": 4,
    "title": "Fine-Grained Action Taxonomy",
    "summary": "Describes the hierarchical annotation of 56 atomic actions composed of verb-noun pairs, including 12 verb classes for temporal semantics and 22 noun classes for object identification.",
    "paper_section": "3.2 Data annotations",
    "narrative_role": "method",
    "duration_stat": {
      "min": 7.0,
      "max": 12.0,
      "avg": 9.0
    }
  },
  {
    "scene_id": 5,
    "title": "Unique Dataset Challenges",
    "summary": "Highlights the inherent challenges of the dataset, including significant camera motion, sensor noise, high class imbalance, and the visual similarity of small furniture components.",
    "paper_section": "3.5 Dataset unique challenges",
    "narrative_role": "method",
    "duration_stat": {
      "min": 8.0,
      "max": 13.0,
      "avg": 10.0
    }
  },
  {
    "scene_id": 6,
    "title": "Benchmark and Experimental Setup",
    "summary": "Outlines the evaluation protocol using state-of-the-art 3D action recognition methods such as PSTNet, P4Transformer, and 3DinAction, measured by top-1 accuracy and mean average precision.",
    "paper_section": "4. Benchmark and Experiments",
    "narrative_role": "experiments",
    "duration_stat": {
      "min": 7.0,
      "max": 12.0,
      "avg": 9.0
    }
  },
  {
    "scene_id": 7,
    "title": "Performance Analysis and Temporal Smoothing",
    "summary": "Discusses benchmark results showing that incorporating temporal smoothing significantly boosts performance, with PointNet++ with temporal smoothing emerging as a surprisingly strong baseline.",
    "paper_section": "4.2 Benchmark results discussion",
    "narrative_role": "results",
    "duration_stat": {
      "min": 9.0,
      "max": 15.0,
      "avg": 11.0
    }
  },
  {
    "scene_id": 8,
    "title": "Noun and Verb Clustering Insights",
    "summary": "Presents findings from decoupling spatial and temporal power, revealing that verbs are inherently harder to recognize than nouns and rely more heavily on temporal sequence information.",
    "paper_section": "4.3 Noun and Verb clustering experiment",
    "narrative_role": "results",
    "duration_stat": {
      "min": 8.0,
      "max": 14.0,
      "avg": 10.0
    }
  },
  {
    "scene_id": 9,
    "title": "Conclusion and Future Directions",
    "summary": "Summarizes the dataset's role as a challenging testbed for 3D computer vision and suggests future research in multi-modal fusion, action anticipation, and AR human assistive systems.",
    "paper_section": "6. Conclusions",
    "narrative_role": "results",
    "duration_stat": {
      "min": 6.0,
      "max": 10.0,
      "avg": 8.0
    }
  }
]
```"""

Token usage so far: 5587 prompt tokens, 1239 completion tokens

Cost so far: $0.09304

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
  "paper_title": "IKEA Ego 3D Dataset: Understanding furniture assembly actions from ego-view 3D Point Clouds",
  "authors": [
    {"name": "Yizhak Ben-Shabat", "affiliation_id": 1},
    {"name": "Jonathan Paul", "affiliation_id": 2},
    {"name": "Eviatar Segev", "affiliation_id": 2},
    {"name": "Oren Shrout", "affiliation_id": 2},
    {"name": "Stephen Gould", "affiliation_id": 1}
  ],
  "affiliations": [
    {"id": 1, "name": "Australian National University", "email_domain": "anu.edu.au"},
    {"id": 2, "name": "Technion, Israel Institute of Technology", "email_domain": "gmail.com"}
  ],
  "venue": "WACV 2023"
}"""

Token usage so far: 11150 prompt tokens, 1459 completion tokens

Cost so far: $0.15527

**Question**

You are an expert presentation designer for academic video summaries.

You are designing the TITLE PAGE layout for a paper presentation video.

Paper metadata:
{
  "paper_title": "IKEA Ego 3D Dataset: Understanding furniture assembly actions from ego-view 3D Point Clouds",
  "authors": [
    {
      "name": "Yizhak Ben-Shabat",
      "affiliation_id": 1
    },
    {
      "name": "Jonathan Paul",
      "affiliation_id": 2
    },
    {
      "name": "Eviatar Segev",
      "affiliation_id": 2
    },
    {
      "name": "Oren Shrout",
      "affiliation_id": 2
    },
    {
      "name": "Stephen Gould",
      "affiliation_id": 1
    }
  ],
  "affiliations": [
    {
      "id": 1,
      "name": "Australian National University",
      "email_domain": "anu.edu.au"
    },
    {
      "id": 2,
      "name": "Technion, Israel Institute of Technology",
      "email_domain": "gmail.com"
    }
  ],
  "venue": "WACV 2023"
}

Available logos:
conference_logo: conference.png
affiliation_1_logo: affiliation_1.png (Australian National University)
affiliation_2_logo: affiliation_2.png (Technion, Israel Institute of Technology)

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
    "affiliation_logos": {"x": 0.05, "y": 0.05, "w": 0.25, "h": 0.1},
    "title": {"x": 0.05, "y": 0.25, "w": 0.9, "h": 0.25},
    "authors": {"x": 0.1, "y": 0.55, "w": 0.8, "h": 0.1},
    "affiliations": {"x": 0.1, "y": 0.68, "w": 0.8, "h": 0.08},
    "venue": {"x": 0.3, "y": 0.85, "w": 0.4, "h": 0.05}
  },
  "style_rationale": "This layout uses a balanced header with the affiliation logos on the top-left and the conference logo on the top-right. The title is centrally positioned for maximum impact, followed by a clear hierarchy of authors and their respective institutions. The venue is placed at the bottom to provide a clean, professional finish."
}"""

Token usage so far: 17245 prompt tokens, 1805 completion tokens

Cost so far: $0.22660

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 1,
  "title": "Motivation for Ego-View 3D Action Recognition",
  "summary": "Explains the need for 3D point cloud action recognition in ego-view scenarios, particularly for head-mounted devices where RGB data may be degraded or insufficient for safety-critical applications.",
  "paper_section": "1. Introduction",
  "narrative_role": "introduction",
  "duration_stat": {
    "min": 8.0,
    "max": 15.0,
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
  "extracted_content": "The research is motivated by the rapid proliferation of head-mounted virtual, augmented, and mixed reality devices (e.g., Apple Vision Pro, Microsoft HoloLens 2, Meta Quest 3) which produce ego-view RGB and 3D point cloud streams. While RGB video is the standard modality for action recognition, it can be insufficient in scenarios with poor lighting or in safety-critical applications where sensor redundancy is required. 3D point clouds offer a robust alternative modality, yet their potential remains largely untapped due to a lack of annotated data. Existing 3D datasets are primarily captured from static, distant sensors, which fail to account for camera motion and hinder the recognition of fine-grained actions involving small objects. There is a significant gap in the literature for datasets that combine ego-view perspectives with 3D point cloud sequences, which is essential for developing applications in wearable-device scenarios.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Overview of the IKEA Ego 3D dataset. The dataset includes 174 assembly sequences captured using a Microsoft HoloLens 2. The captured RGB and Depth streams are labelled with 56 action labels per frame. The data is then aligned and synced to form 3D point cloud sequences that are the input to 3D action recognition algorithms.",
      "relevance": "Illustrates the ego-view capture process and the multi-modal nature (RGB, Depth, Point Cloud) of the data required for modern head-mounted device applications."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 1",
      "caption": "Dataset comparison. The proposed dataset is the first to have ego-view 3D point cloud data in an assembly context.",
      "relevance": "Highlights the 'gap' mentioned in the motivation by showing that previous datasets lack the combination of 3D data and ego-view perspective."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "1. Introduction",
    "2.1 3D action understanding datasets"
  ]
}"""

Token usage so far: 23075 prompt tokens, 2277 completion tokens

Cost so far: $0.29906

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "The research is motivated by the rapid proliferation of head-mounted virtual, augmented, and mixed reality devices (e.g., Apple Vision Pro, Microsoft HoloLens 2, Meta Quest 3) which produce ego-view RGB and 3D point cloud streams. While RGB video is the standard modality for action recognition, it can be insufficient in scenarios with poor lighting or in safety-critical applications where sensor redundancy is required. 3D point clouds offer a robust alternative modality, yet their potential remains largely untapped due to a lack of annotated data. Existing 3D datasets are primarily captured from static, distant sensors, which fail to account for camera motion and hinder the recognition of fine-grained actions involving small objects. There is a significant gap in the literature for datasets that combine ego-view perspectives with 3D point cloud sequences, which is essential for developing applications in wearable-device scenarios.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Overview of the IKEA Ego 3D dataset. The dataset includes 174 assembly sequences captured using a Microsoft HoloLens 2. The captured RGB and Depth streams are labelled with 56 action labels per frame. The data is then aligned and synced to form 3D point cloud sequences that are the input to 3D action recognition algorithms.",
      "relevance": "Illustrates the ego-view capture process and the multi-modal nature (RGB, Depth, Point Cloud) of the data required for modern head-mounted device applications."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 1",
      "caption": "Dataset comparison. The proposed dataset is the first to have ego-view 3D point cloud data in an assembly context.",
      "relevance": "Highlights the 'gap' mentioned in the motivation by showing that previous datasets lack the combination of 3D data and ego-view perspective."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "1. Introduction",
    "2.1 3D action understanding datasets"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 1,
  "title": "Motivation for Ego-View 3D Action Recognition",
  "summary": "Explains the need for 3D point cloud action recognition in ego-view scenarios, particularly for head-mounted devices where RGB data may be degraded or insufficient for safety-critical applications.",
  "paper_section": "1. Introduction",
  "narrative_role": "introduction",
  "duration_stat": {
    "min": 8.0,
    "max": 15.0,
    "avg": 10.0
  }
}

Reference style advice:
Reference Layouts for 'introduction' section from similar papers:
- Example 1: The slide uses a simple single-column layout on a plain white background. The title is located at the top left and is distinctive for its multi-colored text: 'Open-world' is orange, 'part' is blue, 'segmentation in' is black, and '3D' is purple. Below the title, the content is structured as a short list introduced by the word 'But:'. There are two bullet points describing challenges: the first states 'No large-scale data' followed by a red 'X' mark, and the second states 'Collecting human annotations for 3D is difficult' followed by a worried face emoji. The text density is very light, leaving significant white space in the center and bottom. A circular video inset of the presenter is positioned in the bottom right corner of the frame.
- Example 2: The slide uses a clean three-column grid layout on a white background. The title 'Introduction and Motivation' is placed at the top-left in a large, black, sans-serif font. In the top-right corner, the ICLR logo is visible alongside the conference dates 'Apr 24 – 28, 2025'. The main body of the slide consists of three vertical columns, each featuring two stacked images or diagrams with a descriptive label centered at the bottom. The left column, labeled 'Virtual Reality', contains two photographs of people wearing VR headsets. The middle column, labeled 'Character Animation', shows two 3D-style animated character busts. The right column, labeled 'Human Behavior Analysis', features a photo of a child playing with blocks above a technical diagram showing human spatial positioning and interaction vectors. A small credit line is positioned at the very bottom-left of the slide. The overall text density is light, relying heavily on visual examples to convey the application domains.
- Example 3: The slide features a clean, white background with a title positioned at the top-left. In the top-right corner, there is a QR code and a university logo. The main content is a horizontal process diagram consisting of two large rectangular panels connected by a central arrow. The left panel contains a 3D schematic showing a camera on the far left projecting lines toward a dining set (a table and six blue chairs) in the center. The right panel displays the resulting 2D rendered image of the scene, showing a close-up view of the chairs and table against a solid black background. Above the connecting arrow is a mathematical symbol (the Greek letter pi). A small page number '2' is located in the bottom-right corner. The text density is light, with the focus being on the visual explanation of the imaging process.
- Example 4: The slide features a clean, two-part horizontal split. The top half is a solid teal-colored rectangular block that serves as a header, containing the title 'Motivation' in a large, white, sans-serif font centered within the block. The bottom half of the slide has a plain white background. A single sentence of black text is centered horizontally in the upper portion of this white section, stating the core problem. In the bottom-left corner, there is a small text footer that reads 'Australia's National Science Agency'. The bottom-right corner contains two institutional logos: the Australian National University crest and name, and the CSIRO logo. The overall text density is very light, emphasizing a single motivational statement.
- Example 5: The slide features a clean, white background with a large title at the top-left. In the top-right corner, there is a QR code and a university logo. The main content consists of two large visual panels arranged side-by-side, connected by a central horizontal arrow. The left panel is a framed diagram showing a 3D scene with a camera on the left projecting a field of view (indicated by orange lines) onto a dining table and chairs. The central arrow pointing to the right has a mathematical symbol 'π' above it and a small 3D cube icon below it, suggesting a projection or transformation process. The right panel shows the resulting 2D rendered image of the chairs and table against a solid black background. A small page number '3' is located in the bottom-right corner. The text density is very light, relying primarily on visual diagrams to explain a concept.

Duration statistics for this section (from references): min=1.9s, max=48.4s, avg=11.5s.

Your job is to decide the **visual layout** for this slide. Do NOT decide builds or animations — those will be planned later.

## CHOOSE THE BEST LAYOUT

Pick the layout template that best suits the content. Common templates include (but you are NOT limited to these):
- `two_col_fig_left` — Figure on left, bullets on right. Best for: method diagrams, architecture figures.
- `two_col_fig_right` — Bullets on left, figure on right. Best for: motivation slides with illustrative figures.
- `full_fig_with_callouts` — Large figure with small bullet callouts below. Best for: results, data visualizations.
- `one_col_bullets` — Full-width bullets, no figure. Best for: text-heavy overview or summary slides.

If none of these fit, invent a descriptive template name and define its regions.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "bullets": {"x": 0.55, "y": 0.25, "w": 0.4, "h": 0.6}
  },
  "has_figure": true,
  "style_rationale": "Two-column layout with figure on left is ideal for showing the architecture diagram alongside explanatory bullets."
}

## STRICT RULES:
1. **Region keys**: Only use `title`, `bullets`, `figure` as region keys. Do NOT invent keys like `callout_1`, `table`, etc.
2. **Coordinates**: All x/y/w/h values must be normalized (0.0 to 1.0). Regions must not overlap.
3. **has_figure**: Set to `true` only if the content summary has relevant figures. If no figure is available, omit `figure` from regions.
4. **No builds**: Do NOT include `build_skeleton`, `expected_build_steps`, or any animation information.
5. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "layout_template": "two_col_fig_right",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "bullets": {"x": 0.05, "y": 0.2, "w": 0.4, "h": 0.7},
    "figure": {"x": 0.5, "y": 0.2, "w": 0.45, "h": 0.7}
  },
  "has_figure": true,
  "style_rationale": "A two-column layout with bullets on the left and a figure on the right is a classic motivational structure. The bullets outline the need for 3D ego-view data (RGB degradation, safety), while Figure 1 provides visual context of the head-mounted capture process and the resulting data streams."
}"""

Token usage so far: 30425 prompt tokens, 2511 completion tokens

Cost so far: $0.37958

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "The research is motivated by the rapid proliferation of head-mounted virtual, augmented, and mixed reality devices (e.g., Apple Vision Pro, Microsoft HoloLens 2, Meta Quest 3) which produce ego-view RGB and 3D point cloud streams. While RGB video is the standard modality for action recognition, it can be insufficient in scenarios with poor lighting or in safety-critical applications where sensor redundancy is required. 3D point clouds offer a robust alternative modality, yet their potential remains largely untapped due to a lack of annotated data. Existing 3D datasets are primarily captured from static, distant sensors, which fail to account for camera motion and hinder the recognition of fine-grained actions involving small objects. There is a significant gap in the literature for datasets that combine ego-view perspectives with 3D point cloud sequences, which is essential for developing applications in wearable-device scenarios.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Overview of the IKEA Ego 3D dataset. The dataset includes 174 assembly sequences captured using a Microsoft HoloLens 2. The captured RGB and Depth streams are labelled with 56 action labels per frame. The data is then aligned and synced to form 3D point cloud sequences that are the input to 3D action recognition algorithms.",
      "relevance": "Illustrates the ego-view capture process and the multi-modal nature (RGB, Depth, Point Cloud) of the data required for modern head-mounted device applications."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 1",
      "caption": "Dataset comparison. The proposed dataset is the first to have ego-view 3D point cloud data in an assembly context.",
      "relevance": "Highlights the 'gap' mentioned in the motivation by showing that previous datasets lack the combination of 3D data and ego-view perspective."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "1. Introduction",
    "2.1 3D action understanding datasets"
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
  "style_rationale": "A two-column layout with bullets on the left and a figure on the right is a classic motivational structure. The bullets outline the need for 3D ego-view data (RGB degradation, safety), while Figure 1 provides visual context of the head-mounted capture process and the resulting data streams."
}

Scene context:
{
  "scene_id": 1,
  "title": "Motivation for Ego-View 3D Action Recognition",
  "summary": "Explains the need for 3D point cloud action recognition in ego-view scenarios, particularly for head-mounted devices where RGB data may be degraded or insufficient for safety-critical applications.",
  "paper_section": "1. Introduction",
  "narrative_role": "introduction",
  "duration_stat": {
    "min": 8.0,
    "max": 15.0,
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
  "source": ["Figure 1", "Section 3.1"],
  "prompt": "Visual description of the scene for generation"
}

## STRICT RULES:
1. **Number of bullets**: Write 2-4 concise, impactful bullets that cover the key points from the extracted content.
2. **Figure reference**: ONLY use figures listed in the content summary's `key_figures`. Do NOT invent figure references. If the style plan has `has_figure: false`, omit `figure` entirely.
3. **Bullet text**: Each bullet should be concise (under 15 words preferred), impactful, and directly derived from `extracted_content`. Not a copy — a focused summary.
4. **audio_content**: Natural narration covering all bullet points. 
5. **duration_sec**: First, draft the `audio_content`. Then, CALCULATE the duration: `duration_sec = word_count_of_audio / 2.5`. Do NOT guess. If the stats say 8s but you wrote 40 words, `duration_sec` MUST be 16.0.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "title": "Motivation for Ego-View 3D Action Recognition",
  "audio_content": "As head-mounted devices proliferate, relying solely on RGB video is insufficient for low-light or safety-critical tasks. 3D point clouds provide essential sensor redundancy, yet ego-view 3D datasets are currently scarce. We bridge this gap to enable fine-grained action recognition from a first-person perspective.",
  "duration_sec": 15.2,
  "bullets": [
    "Proliferation of head-mounted devices like HoloLens 2 and Vision Pro",
    "RGB limitations in low-light or safety-critical applications",
    "3D point clouds offer robust sensor redundancy and fine-grained detail",
    "Existing 3D datasets lack the essential ego-view perspective"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 1",
    "caption": "Overview of the IKEA Ego 3D dataset capture and multi-modal processing"
  },
  "source": [
    "1. Introduction",
    "Figure 1",
    "Table 1"
  ],
  "prompt": "A slide showing the motivation for the research. On the left, four bullet points explain the need for 3D ego-view data due to HMD proliferation and RGB limitations. On the right, Figure 1 from the paper illustrates the IKEA Ego 3D dataset overview, showing the capture process with a HoloLens 2 and the resulting RGB, depth, and point cloud streams."
}"""

Token usage so far: 37013 prompt tokens, 2860 completion tokens

Cost so far: $0.45593

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "Motivation for Ego-View 3D Action Recognition",
  "audio_content": "As head-mounted devices proliferate, relying solely on RGB video is insufficient for low-light or safety-critical tasks. 3D point clouds provide essential sensor redundancy, yet ego-view 3D datasets are currently scarce. We bridge this gap to enable fine-grained action recognition from a first-person perspective.",
  "duration_sec": 15.2,
  "bullets": [
    "Proliferation of head-mounted devices like HoloLens 2 and Vision Pro",
    "RGB limitations in low-light or safety-critical applications",
    "3D point clouds offer robust sensor redundancy and fine-grained detail",
    "Existing 3D datasets lack the essential ego-view perspective"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 1",
    "caption": "Overview of the IKEA Ego 3D dataset capture and multi-modal processing"
  },
  "source": [
    "1. Introduction",
    "Figure 1",
    "Table 1"
  ],
  "prompt": "A slide showing the motivation for the research. On the left, four bullet points explain the need for 3D ego-view data due to HMD proliferation and RGB limitations. On the right, Figure 1 from the paper illustrates the IKEA Ego 3D dataset overview, showing the capture process with a HoloLens 2 and the resulting RGB, depth, and point cloud streams."
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
1. **Build count**: `expected_build_steps` = 1 + number_of_bullets. Build 0 shows title (and figure if present), then one build per bullet.
2. **One bullet per build**: After build 0, each build reveals exactly ONE bullet. `bullets[0]` in build 1, `bullets[1]` in build 2, etc.
3. **Build 0**: Always shows `title` (and `figure` if present). Never shows bullets in build 0.
4. **Audio segments**: Split the `audio_content` from the draft into segments. Each build's `audio_segment` must be non-empty and correspond to what that build reveals.
5. **Bullet ordering**: Assign bullets to builds in the order that creates the best storytelling flow for the audience.
6. **time_offset_sec**: Space evenly across the total time. For N builds over T seconds: offsets at 0, T/N, 2T/N, etc.
7. **visual_emphasis**: Always set to empty list `[]`.
8. **Action targets**: Only use targets that exist in `elements`: `title`, `figure`, `bullets[0]`, `bullets[1]`, etc.
9. **elements**: Copy the drafted title, figure, and bullets exactly — do not modify the text content.
10. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""```json
{
  "style": "Slides",
  "expected_build_steps": 5,
  "elements": {
    "title": "Motivation for Ego-View 3D Action Recognition",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 1",
      "caption": "Overview of the IKEA Ego 3D dataset capture and multi-modal processing"
    },
    "bullets": [
      "Proliferation of head-mounted devices like HoloLens 2 and Vision Pro",
      "RGB limitations in low-light or safety-critical applications",
      "3D point clouds offer robust sensor redundancy and fine-grained detail",
      "Existing 3D datasets lack the essential ego-view perspective"
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
      "audio_segment": "As head-mounted devices proliferate,",
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
      "audio_segment": "relying solely on RGB video is insufficient for low-light or safety-critical tasks.",
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
      "audio_segment": "3D point clouds provide essential sensor redundancy,",
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
      "audio_segment": "yet ego-view 3D datasets are currently scarce.",
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
      "audio_segment": "We bridge this gap to enable fine-grained action recognition from a first-person perspective.",
      "visual_emphasis": []
    }
  ]
}
```"""

Token usage so far: 43559 prompt tokens, 3545 completion tokens

Cost so far: $0.54194

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 2,
  "title": "IKEA Ego 3D Dataset Overview",
  "summary": "Introduces the IKEA Ego 3D dataset, featuring 174 assembly sequences and approximately 493k frames of humans performing intricate furniture assembly actions captured from an ego-view.",
  "paper_section": "3. The IKEA Ego3D dataset",
  "narrative_role": "method",
  "duration_stat": {
    "min": 7.0,
    "max": 12.0,
    "avg": 9.0
  }
}

## Previous Scenes Memory
The following content was extracted for the immediately preceding scenes. **This is provided as a memory of what the audience has JUST seen.**
You MUST NOT repeat the claims, figures, tables, or equations from these previous scenes in your current extraction, to ensure the presentation maintains forward momentum without redundant slides.
If you must reference the exactly same figure/table, the 'relevance' MUST be clearly unique to avoid narrative duplication.

{
  "extracted_content": "The research is motivated by the rapid proliferation of head-mounted virtual, augmented, and mixed reality devices (e.g., Apple Vision Pro, Microsoft HoloLens 2, Meta Quest 3) which produce ego-view RGB and 3D point cloud streams. While RGB video is the standard modality for action recognition, it can be insufficient in scenarios with poor lighting or in safety-critical applications where sensor redundancy is required. 3D point clouds offer a robust alternative modality, yet their potential remains largely untapped due to a lack of annotated data. Existing 3D datasets are primarily captured from static, distant sensors, which fail to account for camera motion and hinder the recognition of fine-grained actions involving small objects. There is a significant gap in the literature for datasets that combine ego-view perspectives with 3D point cloud sequences, which is essential for developing applications in wearable-device scenarios.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Overview of the IKEA Ego 3D dataset. The dataset includes 174 assembly sequences captured using a Microsoft HoloLens 2. The captured RGB and Depth streams are labelled with 56 action labels per frame. The data is then aligned and synced to form 3D point cloud sequences that are the input to 3D action recognition algorithms.",
      "relevance": "Illustrates the ego-view capture process and the multi-modal nature (RGB, Depth, Point Cloud) of the data required for modern head-mounted device applications."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 1",
      "caption": "Dataset comparison. The proposed dataset is the first to have ego-view 3D point cloud data in an assembly context.",
      "relevance": "Highlights the 'gap' mentioned in the motivation by showing that previous datasets lack the combination of 3D data and ego-view perspective."
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
  "extracted_content": "The IKEA Ego 3D dataset comprises 174 unique assembly sequences across four furniture types: LACK side table, LACK TV bench, KALLAX drawer, and BEKVAM stool. Data was captured using a Microsoft HoloLens 2, specifically utilizing the long-throw depth sensor (~5 FPS) and RGB camera (~30 FPS). To ensure data quality, a hologram was projected to guide participants to keep the assembly within the sensor's frustum. In post-processing, RGB and depth streams were synchronized and projected to generate oriented 3D point clouds containing spatial coordinates, color, and normal vectors $(x, y, z, R, G, B, N_x, N_y, N_z)$. The dataset contains 493,568 frames annotated with 56 atomic action classes. These actions are structured as hierarchical (verb, noun) pairs, involving 12 verb classes (e.g., align, attach, spin) and 22 noun classes (e.g., coffee table shelf, screw, leg). The dataset is split into 121 training and 53 testing sequences, further subdivided into 32-frame clips (10,689 training and 4,566 testing clips). Key challenges include significant class imbalance, ego-view camera motion, and the presence of fine-grained actions involving visually similar small components like different screw types.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "IKEA Ego3D Furniture. The assemblies in the IKEA Ego3D dataset include the (a) LACK Side table, (b) LACK TV bench, (c) KALLAX Drawer, and BEKVAM (d) Stepping stool.",
      "relevance": "Identifies the specific furniture items that define the scope of the assembly tasks in the dataset."
    },
    {
      "ref": "Figure 3",
      "caption": "IKEA Ego 3D Dataset actions. Visualizing the RGB image (top), 3D point cloud (middle), and action label (bottom) for the Drawer (a-d) and Stool (e-h) assemblies.",
      "relevance": "Provides a visual representation of the synchronized multi-modal data and the fine-grained action labels like 'spin screwdriver' or 'attach side panel'."
    },
    {
      "ref": "Figure 4",
      "caption": "IKEA Ego 3D dataset action occurrence. A highly imbalanced dataset provides a challenge for learning-based algorithms. Note the y-axis is log scaled, therefore a small gap in this axis reflects a significant gap in proportions.",
      "relevance": "Highlights the significant class imbalance within the 56 action classes, which is a major technical challenge for models trained on this data."
    },
    {
      "ref": "Figure 5",
      "caption": "Duration statistics. Sequence (a) and action (b) duration distributions in the IKEA Ego 3D dataset.",
      "relevance": "Shows the distribution of sequence and action lengths, illustrating the temporal variety in the dataset."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Section 3.1",
    "Section 3.2",
    "Section 3.3",
    "Section 3.4",
    "Section 3.5"
  ]
}"""

Token usage so far: 49926 prompt tokens, 4314 completion tokens

Cost so far: $0.62868

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "The IKEA Ego 3D dataset comprises 174 unique assembly sequences across four furniture types: LACK side table, LACK TV bench, KALLAX drawer, and BEKVAM stool. Data was captured using a Microsoft HoloLens 2, specifically utilizing the long-throw depth sensor (~5 FPS) and RGB camera (~30 FPS). To ensure data quality, a hologram was projected to guide participants to keep the assembly within the sensor's frustum. In post-processing, RGB and depth streams were synchronized and projected to generate oriented 3D point clouds containing spatial coordinates, color, and normal vectors $(x, y, z, R, G, B, N_x, N_y, N_z)$. The dataset contains 493,568 frames annotated with 56 atomic action classes. These actions are structured as hierarchical (verb, noun) pairs, involving 12 verb classes (e.g., align, attach, spin) and 22 noun classes (e.g., coffee table shelf, screw, leg). The dataset is split into 121 training and 53 testing sequences, further subdivided into 32-frame clips (10,689 training and 4,566 testing clips). Key challenges include significant class imbalance, ego-view camera motion, and the presence of fine-grained actions involving visually similar small components like different screw types.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "IKEA Ego3D Furniture. The assemblies in the IKEA Ego3D dataset include the (a) LACK Side table, (b) LACK TV bench, (c) KALLAX Drawer, and BEKVAM (d) Stepping stool.",
      "relevance": "Identifies the specific furniture items that define the scope of the assembly tasks in the dataset."
    },
    {
      "ref": "Figure 3",
      "caption": "IKEA Ego 3D Dataset actions. Visualizing the RGB image (top), 3D point cloud (middle), and action label (bottom) for the Drawer (a-d) and Stool (e-h) assemblies.",
      "relevance": "Provides a visual representation of the synchronized multi-modal data and the fine-grained action labels like 'spin screwdriver' or 'attach side panel'."
    },
    {
      "ref": "Figure 4",
      "caption": "IKEA Ego 3D dataset action occurrence. A highly imbalanced dataset provides a challenge for learning-based algorithms. Note the y-axis is log scaled, therefore a small gap in this axis reflects a significant gap in proportions.",
      "relevance": "Highlights the significant class imbalance within the 56 action classes, which is a major technical challenge for models trained on this data."
    },
    {
      "ref": "Figure 5",
      "caption": "Duration statistics. Sequence (a) and action (b) duration distributions in the IKEA Ego 3D dataset.",
      "relevance": "Shows the distribution of sequence and action lengths, illustrating the temporal variety in the dataset."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Section 3.1",
    "Section 3.2",
    "Section 3.3",
    "Section 3.4",
    "Section 3.5"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 2,
  "title": "IKEA Ego 3D Dataset Overview",
  "summary": "Introduces the IKEA Ego 3D dataset, featuring 174 assembly sequences and approximately 493k frames of humans performing intricate furniture assembly actions captured from an ego-view.",
  "paper_section": "3. The IKEA Ego3D dataset",
  "narrative_role": "method",
  "duration_stat": {
    "min": 7.0,
    "max": 12.0,
    "avg": 9.0
  }
}

Reference style advice:
Reference Layouts for 'method' section from similar papers:
- Example 1: The slide uses a two-column layout with a clear title at the top-left. The left column features a large, framed diagram showing a 3D perspective of a camera's field of view (frustum) directed at a table with two blue chairs. The right column contains a cropped image representing the camera's actual view, where chairs are identified with bright yellow bounding boxes. Below this right-side image, the word 'Possible' is written above a 'V' symbol. The top-right corner of the slide includes a QR code and a gold-colored institutional logo. A page number '8' is positioned in the bottom-right corner. The background is plain white, and the text density is light, prioritizing visual diagrams over text.
- Example 2: The slide features a large, plain-text title at the top left. In the top right corner, there is a QR code and a gold-colored institutional logo. The central content is organized into three columns, each illustrating a transformation process. Each column contains a top image showing a 3D rendered scene of blue chairs with yellow bounding boxes, a downward-pointing black arrow, and a bottom image showing a simplified heatmap representation of those bounding boxes. Below these three columns is a centered text caption: 'Bounding box representations of the Object Detector'. At the bottom center, a horizontal color scale bar transitions from dark blue (labeled '0') to yellow (labeled '1'). A small page number '9' is positioned in the bottom right corner. The background is white, creating a clean and light text density.
- Example 3: The slide follows a top-down structure. At the very top, the main title 'Pos3R' is centered in a large, spaced-out font. Below it, a secondary heading 'Step 3: Pose Fitting' is left-aligned. The middle section contains a horizontal process diagram. On the left, a light-colored box groups three images: two showing '2D-2D correspondence' with yellow lines connecting feature points on a watering can, and one 'coordinate map' showing the same object in a multi-colored gradient. A blue arrow labeled '3) PnP-RANSAC' points from this group to a final image on the right, which shows the '6-DoF Pose' as a green 3D bounding box overlaid on a real-world photo of the object. At the bottom of the slide, two bullet points are left-aligned, providing explanatory text for the visual process. The overall background is white, and a faint watermark is visible in the top-left corner.
- Example 4: The slide features a large, centered title at the top in a clean sans-serif font. The main body of the slide is occupied by a large diagram illustrating a 't-patch construction' process. This diagram consists of five vertical columns, each outlined by a dashed gray rectangular border and labeled with a time index 't' from 0 to 4 at the bottom. Each column contains several black dots representing data points. In the first column (t=0), a specific point is highlighted as a green dot labeled 'x_q^0' (T-Patch origin), and a subset of three tan dots is enclosed in a light blue box labeled 'psi_q^0' (Nearest neighbor set). A light blue shaded trapezoidal region extends from the box in column 0 to a corresponding box in column 1, which also contains three tan dots. At the bottom of the slide, a horizontal legend provides definitions for the visual symbols: a black dot for 'x^t Non-t-patch points', a green dot for 'x_q^0 T-Patch origin', and a tan dot with a blue box for 'psi_q^t Nearest neighbor set'. The background is plain white, and the overall text density is light, focusing on the visual representation of the method.
- Example 5: The slide features a large, black, sans-serif title 'Example t-patches 3D' positioned at the top-left. The main content consists of three 3D human models arranged horizontally across the center of the slide. Each model is constructed from numerous small brown spheres, resembling a point cloud. Specific clusters of these spheres are highlighted in various bright colors (such as pink, cyan, purple, and green) to illustrate 't-patches' on different body parts. The leftmost model is a female figure with patches on the abdomen, hands, and feet. The middle model is a male figure with arms raised, showing patches on the hands, forearms, and thighs. The rightmost model is a male figure with patches on the arm, hip, and thigh. In the bottom-right corner, a small text caption states 'Here, k=64 neighbors'. The background is plain white, and the overall text density is very light, prioritizing visual examples over textual explanation.

Duration statistics for this section (from references): min=1.0s, max=52.0s, avg=10.5s.

Your job is to decide the **visual layout** for this slide. Do NOT decide builds or animations — those will be planned later.

## CHOOSE THE BEST LAYOUT

Pick the layout template that best suits the content. Common templates include (but you are NOT limited to these):
- `two_col_fig_left` — Figure on left, bullets on right. Best for: method diagrams, architecture figures.
- `two_col_fig_right` — Bullets on left, figure on right. Best for: motivation slides with illustrative figures.
- `full_fig_with_callouts` — Large figure with small bullet callouts below. Best for: results, data visualizations.
- `one_col_bullets` — Full-width bullets, no figure. Best for: text-heavy overview or summary slides.

If none of these fit, invent a descriptive template name and define its regions.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "bullets": {"x": 0.55, "y": 0.25, "w": 0.4, "h": 0.6}
  },
  "has_figure": true,
  "style_rationale": "Two-column layout with figure on left is ideal for showing the architecture diagram alongside explanatory bullets."
}

## STRICT RULES:
1. **Region keys**: Only use `title`, `bullets`, `figure` as region keys. Do NOT invent keys like `callout_1`, `table`, etc.
2. **Coordinates**: All x/y/w/h values must be normalized (0.0 to 1.0). Regions must not overlap.
3. **has_figure**: Set to `true` only if the content summary has relevant figures. If no figure is available, omit `figure` from regions.
4. **No builds**: Do NOT include `build_skeleton`, `expected_build_steps`, or any animation information.
5. Output ONLY valid JSON, no markdown fences, no explanation.


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
      "w": 0.45,
      "h": 0.7
    },
    "bullets": {
      "x": 0.55,
      "y": 0.2,
      "w": 0.4,
      "h": 0.7
    }
  },
  "has_figure": true,
  "style_rationale": "A two-column layout with the figure on the left is ideal for showcasing the multi-modal data (RGB and 3D point clouds) from Figure 3, while the right column provides space for the key dataset statistics and hierarchical action structure."
}"""

Token usage so far: 57699 prompt tokens, 4571 completion tokens

Cost so far: $0.71412

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "The IKEA Ego 3D dataset comprises 174 unique assembly sequences across four furniture types: LACK side table, LACK TV bench, KALLAX drawer, and BEKVAM stool. Data was captured using a Microsoft HoloLens 2, specifically utilizing the long-throw depth sensor (~5 FPS) and RGB camera (~30 FPS). To ensure data quality, a hologram was projected to guide participants to keep the assembly within the sensor's frustum. In post-processing, RGB and depth streams were synchronized and projected to generate oriented 3D point clouds containing spatial coordinates, color, and normal vectors $(x, y, z, R, G, B, N_x, N_y, N_z)$. The dataset contains 493,568 frames annotated with 56 atomic action classes. These actions are structured as hierarchical (verb, noun) pairs, involving 12 verb classes (e.g., align, attach, spin) and 22 noun classes (e.g., coffee table shelf, screw, leg). The dataset is split into 121 training and 53 testing sequences, further subdivided into 32-frame clips (10,689 training and 4,566 testing clips). Key challenges include significant class imbalance, ego-view camera motion, and the presence of fine-grained actions involving visually similar small components like different screw types.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "IKEA Ego3D Furniture. The assemblies in the IKEA Ego3D dataset include the (a) LACK Side table, (b) LACK TV bench, (c) KALLAX Drawer, and BEKVAM (d) Stepping stool.",
      "relevance": "Identifies the specific furniture items that define the scope of the assembly tasks in the dataset."
    },
    {
      "ref": "Figure 3",
      "caption": "IKEA Ego 3D Dataset actions. Visualizing the RGB image (top), 3D point cloud (middle), and action label (bottom) for the Drawer (a-d) and Stool (e-h) assemblies.",
      "relevance": "Provides a visual representation of the synchronized multi-modal data and the fine-grained action labels like 'spin screwdriver' or 'attach side panel'."
    },
    {
      "ref": "Figure 4",
      "caption": "IKEA Ego 3D dataset action occurrence. A highly imbalanced dataset provides a challenge for learning-based algorithms. Note the y-axis is log scaled, therefore a small gap in this axis reflects a significant gap in proportions.",
      "relevance": "Highlights the significant class imbalance within the 56 action classes, which is a major technical challenge for models trained on this data."
    },
    {
      "ref": "Figure 5",
      "caption": "Duration statistics. Sequence (a) and action (b) duration distributions in the IKEA Ego 3D dataset.",
      "relevance": "Shows the distribution of sequence and action lengths, illustrating the temporal variety in the dataset."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Section 3.1",
    "Section 3.2",
    "Section 3.3",
    "Section 3.4",
    "Section 3.5"
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
      "w": 0.45,
      "h": 0.7
    },
    "bullets": {
      "x": 0.55,
      "y": 0.2,
      "w": 0.4,
      "h": 0.7
    }
  },
  "has_figure": true,
  "style_rationale": "A two-column layout with the figure on the left is ideal for showcasing the multi-modal data (RGB and 3D point clouds) from Figure 3, while the right column provides space for the key dataset statistics and hierarchical action structure."
}

Scene context:
{
  "scene_id": 2,
  "title": "IKEA Ego 3D Dataset Overview",
  "summary": "Introduces the IKEA Ego 3D dataset, featuring 174 assembly sequences and approximately 493k frames of humans performing intricate furniture assembly actions captured from an ego-view.",
  "paper_section": "3. The IKEA Ego3D dataset",
  "narrative_role": "method",
  "duration_stat": {
    "min": 7.0,
    "max": 12.0,
    "avg": 9.0
  }
}

## Previous Content
The following content was drafted for the immediately preceding scenes.
You MUST NOT repeat the exact text content or claims from these previous scenes in your current draft.

{
  "bullets": [
    "Proliferation of head-mounted devices like HoloLens 2 and Vision Pro",
    "RGB limitations in low-light or safety-critical applications",
    "3D point clouds offer robust sensor redundancy and fine-grained detail",
    "Existing 3D datasets lack the essential ego-view perspective"
  ],
  "audio_content": "As head-mounted devices proliferate, relying solely on RGB video is insufficient for low-light or safety-critical tasks. 3D point clouds provide essential sensor redundancy, yet ego-view 3D datasets are currently scarce. We bridge this gap to enable fine-grained action recognition from a first-person perspective."
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
  "source": ["Figure 1", "Section 3.1"],
  "prompt": "Visual description of the scene for generation"
}

## STRICT RULES:
1. **Number of bullets**: Write 2-4 concise, impactful bullets that cover the key points from the extracted content.
2. **Figure reference**: ONLY use figures listed in the content summary's `key_figures`. Do NOT invent figure references. If the style plan has `has_figure: false`, omit `figure` entirely.
3. **Bullet text**: Each bullet should be concise (under 15 words preferred), impactful, and directly derived from `extracted_content`. Not a copy — a focused summary.
4. **audio_content**: Natural narration covering all bullet points. 
5. **duration_sec**: First, draft the `audio_content`. Then, CALCULATE the duration: `duration_sec = word_count_of_audio / 2.5`. Do NOT guess. If the stats say 8s but you wrote 40 words, `duration_sec` MUST be 16.0.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "title": "IKEA Ego 3D Dataset Overview",
  "audio_content": "The IKEA Ego 3D dataset contains 174 assembly sequences and nearly 500,000 frames captured via HoloLens 2. It synchronizes RGB and depth into oriented 3D point clouds, annotated with 56 hierarchical action classes. This structure enables the recognition of fine-grained tasks involving small components like screws and tools.",
  "duration_sec": 19.2,
  "bullets": [
    "174 sequences and ~493k frames across four furniture types",
    "Synchronized RGB and oriented 3D point clouds from HoloLens 2",
    "56 atomic action classes using a hierarchical (verb, noun) structure",
    "Focuses on fine-grained interactions with small assembly components"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 3",
    "caption": "Visualization of synchronized RGB, 3D point clouds, and action labels for assembly tasks."
  },
  "source": [
    "Figure 3",
    "Section 3.1",
    "Section 3.2",
    "Section 3.3"
  ],
  "prompt": "A slide showing a multi-modal dataset visualization on the left, featuring side-by-side comparisons of RGB video frames, their corresponding 3D point clouds, and the associated action labels like 'spin screwdriver' or 'attach side panel'. On the right, bullet points detail the dataset's scale, the use of HoloLens 2 for capture, and the hierarchical verb-noun annotation structure."
}"""

Token usage so far: 64767 prompt tokens, 4949 completion tokens

Cost so far: $0.79614

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "IKEA Ego 3D Dataset Overview",
  "audio_content": "The IKEA Ego 3D dataset contains 174 assembly sequences and nearly 500,000 frames captured via HoloLens 2. It synchronizes RGB and depth into oriented 3D point clouds, annotated with 56 hierarchical action classes. This structure enables the recognition of fine-grained tasks involving small components like screws and tools.",
  "duration_sec": 19.2,
  "bullets": [
    "174 sequences and ~493k frames across four furniture types",
    "Synchronized RGB and oriented 3D point clouds from HoloLens 2",
    "56 atomic action classes using a hierarchical (verb, noun) structure",
    "Focuses on fine-grained interactions with small assembly components"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 3",
    "caption": "Visualization of synchronized RGB, 3D point clouds, and action labels for assembly tasks."
  },
  "source": [
    "Figure 3",
    "Section 3.1",
    "Section 3.2",
    "Section 3.3"
  ],
  "prompt": "A slide showing a multi-modal dataset visualization on the left, featuring side-by-side comparisons of RGB video frames, their corresponding 3D point clouds, and the associated action labels like 'spin screwdriver' or 'attach side panel'. On the right, bullet points detail the dataset's scale, the use of HoloLens 2 for capture, and the hierarchical verb-noun annotation structure."
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
      "w": 0.45,
      "h": 0.7
    },
    "bullets": {
      "x": 0.55,
      "y": 0.2,
      "w": 0.4,
      "h": 0.7
    }
  },
  "has_figure": true,
  "total_time_sec": 19.2
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
1. **Build count**: `expected_build_steps` = 1 + number_of_bullets. Build 0 shows title (and figure if present), then one build per bullet.
2. **One bullet per build**: After build 0, each build reveals exactly ONE bullet. `bullets[0]` in build 1, `bullets[1]` in build 2, etc.
3. **Build 0**: Always shows `title` (and `figure` if present). Never shows bullets in build 0.
4. **Audio segments**: Split the `audio_content` from the draft into segments. Each build's `audio_segment` must be non-empty and correspond to what that build reveals.
5. **Bullet ordering**: Assign bullets to builds in the order that creates the best storytelling flow for the audience.
6. **time_offset_sec**: Space evenly across the total time. For N builds over T seconds: offsets at 0, T/N, 2T/N, etc.
7. **visual_emphasis**: Always set to empty list `[]`.
8. **Action targets**: Only use targets that exist in `elements`: `title`, `figure`, `bullets[0]`, `bullets[1]`, etc.
9. **elements**: Copy the drafted title, figure, and bullets exactly — do not modify the text content.
10. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "style": "Slides",
  "expected_build_steps": 5,
  "elements": {
    "title": "IKEA Ego 3D Dataset Overview",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 3",
      "caption": "Visualization of synchronized RGB, 3D point clouds, and action labels for assembly tasks."
    },
    "bullets": [
      "174 sequences and ~493k frames across four furniture types",
      "Synchronized RGB and oriented 3D point clouds from HoloLens 2",
      "56 atomic action classes using a hierarchical (verb, noun) structure",
      "Focuses on fine-grained interactions with small assembly components"
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
      "audio_segment": "The IKEA Ego 3D dataset provides a comprehensive look at furniture assembly from an ego-view perspective.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 3.84,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[0]"
        }
      ],
      "audio_segment": "It contains 174 assembly sequences and nearly 500,000 frames captured via HoloLens 2 across four furniture types.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 7.68,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[1]"
        }
      ],
      "audio_segment": "The dataset synchronizes RGB and depth streams into oriented 3D point clouds, providing a rich multi-modal representation.",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 11.52,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[2]"
        }
      ],
      "audio_segment": "Data is annotated with 56 hierarchical action classes, using a verb-noun structure to categorize assembly steps.",
      "visual_emphasis": []
    },
    {
      "step_index": 4,
      "time_offset_sec": 15.36,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[3]"
        }
      ],
      "audio_segment": "This detailed structure enables the recognition of fine-grained tasks involving small components like screws and tools.",
      "visual_emphasis": []
    }
  ]
}"""

Token usage so far: 71343 prompt tokens, 5686 completion tokens

Cost so far: $0.88401

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 3,
  "title": "Data Collection and Processing Pipeline",
  "summary": "Details the hardware setup using Microsoft HoloLens 2 and the post-processing stage where RGB and depth streams are synced and projected to form oriented 3D point cloud sequences.",
  "paper_section": "3.1 Data collection",
  "narrative_role": "method",
  "duration_stat": {
    "min": 8.0,
    "max": 14.0,
    "avg": 10.0
  }
}

## Previous Scenes Memory
The following content was extracted for the immediately preceding scenes. **This is provided as a memory of what the audience has JUST seen.**
You MUST NOT repeat the claims, figures, tables, or equations from these previous scenes in your current extraction, to ensure the presentation maintains forward momentum without redundant slides.
If you must reference the exactly same figure/table, the 'relevance' MUST be clearly unique to avoid narrative duplication.

{
  "extracted_content": "The research is motivated by the rapid proliferation of head-mounted virtual, augmented, and mixed reality devices (e.g., Apple Vision Pro, Microsoft HoloLens 2, Meta Quest 3) which produce ego-view RGB and 3D point cloud streams. While RGB video is the standard modality for action recognition, it can be insufficient in scenarios with poor lighting or in safety-critical applications where sensor redundancy is required. 3D point clouds offer a robust alternative modality, yet their potential remains largely untapped due to a lack of annotated data. Existing 3D datasets are primarily captured from static, distant sensors, which fail to account for camera motion and hinder the recognition of fine-grained actions involving small objects. There is a significant gap in the literature for datasets that combine ego-view perspectives with 3D point cloud sequences, which is essential for developing applications in wearable-device scenarios.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Overview of the IKEA Ego 3D dataset. The dataset includes 174 assembly sequences captured using a Microsoft HoloLens 2. The captured RGB and Depth streams are labelled with 56 action labels per frame. The data is then aligned and synced to form 3D point cloud sequences that are the input to 3D action recognition algorithms.",
      "relevance": "Illustrates the ego-view capture process and the multi-modal nature (RGB, Depth, Point Cloud) of the data required for modern head-mounted device applications."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 1",
      "caption": "Dataset comparison. The proposed dataset is the first to have ego-view 3D point cloud data in an assembly context.",
      "relevance": "Highlights the 'gap' mentioned in the motivation by showing that previous datasets lack the combination of 3D data and ego-view perspective."
    }
  ],
  "key_equations": []
}
{
  "extracted_content": "The IKEA Ego 3D dataset comprises 174 unique assembly sequences across four furniture types: LACK side table, LACK TV bench, KALLAX drawer, and BEKVAM stool. Data was captured using a Microsoft HoloLens 2, specifically utilizing the long-throw depth sensor (~5 FPS) and RGB camera (~30 FPS). To ensure data quality, a hologram was projected to guide participants to keep the assembly within the sensor's frustum. In post-processing, RGB and depth streams were synchronized and projected to generate oriented 3D point clouds containing spatial coordinates, color, and normal vectors $(x, y, z, R, G, B, N_x, N_y, N_z)$. The dataset contains 493,568 frames annotated with 56 atomic action classes. These actions are structured as hierarchical (verb, noun) pairs, involving 12 verb classes (e.g., align, attach, spin) and 22 noun classes (e.g., coffee table shelf, screw, leg). The dataset is split into 121 training and 53 testing sequences, further subdivided into 32-frame clips (10,689 training and 4,566 testing clips). Key challenges include significant class imbalance, ego-view camera motion, and the presence of fine-grained actions involving visually similar small components like different screw types.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "IKEA Ego3D Furniture. The assemblies in the IKEA Ego3D dataset include the (a) LACK Side table, (b) LACK TV bench, (c) KALLAX Drawer, and BEKVAM (d) Stepping stool.",
      "relevance": "Identifies the specific furniture items that define the scope of the assembly tasks in the dataset."
    },
    {
      "ref": "Figure 3",
      "caption": "IKEA Ego 3D Dataset actions. Visualizing the RGB image (top), 3D point cloud (middle), and action label (bottom) for the Drawer (a-d) and Stool (e-h) assemblies.",
      "relevance": "Provides a visual representation of the synchronized multi-modal data and the fine-grained action labels like 'spin screwdriver' or 'attach side panel'."
    },
    {
      "ref": "Figure 4",
      "caption": "IKEA Ego 3D dataset action occurrence. A highly imbalanced dataset provides a challenge for learning-based algorithms. Note the y-axis is log scaled, therefore a small gap in this axis reflects a significant gap in proportions.",
      "relevance": "Highlights the significant class imbalance within the 56 action classes, which is a major technical challenge for models trained on this data."
    },
    {
      "ref": "Figure 5",
      "caption": "Duration statistics. Sequence (a) and action (b) duration distributions in the IKEA Ego 3D dataset.",
      "relevance": "Shows the distribution of sequence and action lengths, illustrating the temporal variety in the dataset."
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
  "extracted_content": "The data collection hardware consists of a Microsoft HoloLens 2, utilizing its long-throw depth sensor for 3D sequences and an RGB camera for visual context. A specific challenge addressed is the flexible nature of the head-mount; the depth sensor is positioned a few centimeters above the eyes, and its relative location to the RGB camera is not fixed, which complicates the alignment of the user's field of view with the sensor's frustum. To mitigate this, a thin opaque rectangular hologram is projected to guide the assembler. The post-processing pipeline synchronizes the ~30 FPS RGB stream with the ~5 FPS depth stream using nearest timestamp matching. Because the RGB camera's receptive field is smaller than that of the depth sensor, the final oriented 3D point clouds contain some points without color values, though all points retain spatial $(x, y, z)$ and normal vector $(N_x, N_y, N_z)$ data.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Overview of the IKEA Ego 3D dataset. The dataset includes 174 assembly sequences captured using a Microsoft HoloLens 2. The captured RGB and Depth streams are labelled with 56 action labels per frame. The data is then aligned and synced to form 3D point cloud sequences that are the input to 3D action recognition algorithms.",
      "relevance": "Specifically highlights the 'Capture' and 'Process' stages of the pipeline, showing the transition from raw multi-modal sensor streams to synchronized 3D point clouds."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Section 3.1"
  ]
}"""

Token usage so far: 78416 prompt tokens, 6075 completion tokens

Cost so far: $0.96641

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "The data collection hardware consists of a Microsoft HoloLens 2, utilizing its long-throw depth sensor for 3D sequences and an RGB camera for visual context. A specific challenge addressed is the flexible nature of the head-mount; the depth sensor is positioned a few centimeters above the eyes, and its relative location to the RGB camera is not fixed, which complicates the alignment of the user's field of view with the sensor's frustum. To mitigate this, a thin opaque rectangular hologram is projected to guide the assembler. The post-processing pipeline synchronizes the ~30 FPS RGB stream with the ~5 FPS depth stream using nearest timestamp matching. Because the RGB camera's receptive field is smaller than that of the depth sensor, the final oriented 3D point clouds contain some points without color values, though all points retain spatial $(x, y, z)$ and normal vector $(N_x, N_y, N_z)$ data.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Overview of the IKEA Ego 3D dataset. The dataset includes 174 assembly sequences captured using a Microsoft HoloLens 2. The captured RGB and Depth streams are labelled with 56 action labels per frame. The data is then aligned and synced to form 3D point cloud sequences that are the input to 3D action recognition algorithms.",
      "relevance": "Specifically highlights the 'Capture' and 'Process' stages of the pipeline, showing the transition from raw multi-modal sensor streams to synchronized 3D point clouds."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Section 3.1"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 3,
  "title": "Data Collection and Processing Pipeline",
  "summary": "Details the hardware setup using Microsoft HoloLens 2 and the post-processing stage where RGB and depth streams are synced and projected to form oriented 3D point cloud sequences.",
  "paper_section": "3.1 Data collection",
  "narrative_role": "method",
  "duration_stat": {
    "min": 8.0,
    "max": 14.0,
    "avg": 10.0
  }
}

Reference style advice:
Reference Layouts for 'method' section from similar papers:
- Example 1: The slide features a large, centered title 't-patch construction' at the top in a plain black font. The main body of the slide is a diagram showing five vertical columns of black dots, each enclosed within a light gray dashed rectangular box. Below each box is a numerical label for 't', ranging from 0 to 4. To the left of the first column (t=0), there is a mathematical label 'x_q^0'. At the very bottom, a horizontal legend explains the symbols used: a black dot represents 'x^t Non-t-patch points', a light green dot represents 'x_q^0 T-Patch origin', and a light orange dot represents 'ψ_q^t Nearest neighbor set'. The overall layout is clean and minimalist, with a white background and light text density, focusing on the visual explanation of a data construction process.
- Example 2: The slide features a clean, two-column layout on a white background. At the top-left, the title 'Task: Find chairs' is displayed in a simple sans-serif font. The left column contains a large, black-bordered box labeled 'Input Frame' which shows a 3D diagram of a camera on the left pointing towards a dining table with six blue chairs; orange perspective lines illustrate the camera's field of view. The right column displays a cropped, dark-background image showing a close-up of two blue chairs, each enclosed in a bright green rectangular bounding box to demonstrate object detection. In the top-right corner, there is a QR code next to a gold-colored institutional logo. A small page number '5' is positioned at the bottom-right corner. The text density is light, with the slide primarily using visual diagrams to explain a computer vision task.
- Example 3: The slide uses a two-column layout with a white background. A large, bold title is positioned at the top-left. The left column features a framed diagram showing a 3D perspective of a camera's field of view directed at a dining table and chairs. The right column contains a horizontal image strip showing several blue chairs against a black background, each enclosed in a bright green bounding box. Below this image, the text 'Possible Variations' is centered. In the top-right corner, there is a QR code and a gold institutional logo. A small page number '7' is located at the bottom-right. The text density is light, with the focus being on the visual diagrams and images.
- Example 4: The slide features a large, plain-text title at the top left. In the top right corner, there is a QR code and a gold-colored institutional logo. The central content is organized into three columns, each illustrating a transformation process. Each column contains a top image showing a 3D rendered scene of blue chairs with yellow bounding boxes, a downward-pointing black arrow, and a bottom image showing a simplified heatmap representation of those bounding boxes. Below these three columns is a centered text caption: 'Bounding box representations of the Object Detector'. At the bottom center, a horizontal color scale bar transitions from dark blue (labeled '0') to yellow (labeled '1'). A small page number '9' is positioned in the bottom right corner. The background is white, creating a clean and light text density.
- Example 5: The slide features a large, bold title 'Method' positioned at the top-left. The main body of the slide is dominated by a horizontal flowchart-style diagram. On the left, two primary components are stacked: a grey box labeled 'inference' showing a 'Find3D transformer' processing a 3D snowman model, and a pink box labeled 'Data Engine'. These components feed into a contrastive learning framework on the right. This framework shows pairs of snowman images with specific parts highlighted (like the base or hat) being mapped to corresponding feature vectors, represented by yellow and pink vertical bars. These are labeled as 'positive pair' and grouped together by a large bracket at the bottom labeled 'Contrastive loss'. Below this diagram, there is a list of three key features, each marked with a green checkmark icon: 'Simple model, simple training recipe', 'Handles ambiguity', and 'Scalable'. A circular video feed of the presenter is visible in the bottom-right corner of the slide.

Duration statistics for this section (from references): min=1.0s, max=52.0s, avg=10.5s.

Your job is to decide the **visual layout** for this slide. Do NOT decide builds or animations — those will be planned later.

## CHOOSE THE BEST LAYOUT

Pick the layout template that best suits the content. Common templates include (but you are NOT limited to these):
- `two_col_fig_left` — Figure on left, bullets on right. Best for: method diagrams, architecture figures.
- `two_col_fig_right` — Bullets on left, figure on right. Best for: motivation slides with illustrative figures.
- `full_fig_with_callouts` — Large figure with small bullet callouts below. Best for: results, data visualizations.
- `one_col_bullets` — Full-width bullets, no figure. Best for: text-heavy overview or summary slides.

If none of these fit, invent a descriptive template name and define its regions.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "bullets": {"x": 0.55, "y": 0.25, "w": 0.4, "h": 0.6}
  },
  "has_figure": true,
  "style_rationale": "Two-column layout with figure on left is ideal for showing the architecture diagram alongside explanatory bullets."
}

## STRICT RULES:
1. **Region keys**: Only use `title`, `bullets`, `figure` as region keys. Do NOT invent keys like `callout_1`, `table`, etc.
2. **Coordinates**: All x/y/w/h values must be normalized (0.0 to 1.0). Regions must not overlap.
3. **has_figure**: Set to `true` only if the content summary has relevant figures. If no figure is available, omit `figure` from regions.
4. **No builds**: Do NOT include `build_skeleton`, `expected_build_steps`, or any animation information.
5. Output ONLY valid JSON, no markdown fences, no explanation.


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
      "w": 0.5,
      "h": 0.7
    },
    "bullets": {
      "x": 0.6,
      "y": 0.2,
      "w": 0.35,
      "h": 0.7
    }
  },
  "has_figure": true,
  "style_rationale": "A two-column layout with the figure on the left is chosen to showcase the 'Capture' and 'Process' stages of the pipeline from Figure 1. This provides a visual anchor for the technical details regarding hardware setup, sensor alignment, and data synchronization described in the bullets on the right, following the clean and minimalist aesthetic of the reference slides."
}"""

Token usage so far: 85683 prompt tokens, 6351 completion tokens

Cost so far: $1.04736

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "The data collection hardware consists of a Microsoft HoloLens 2, utilizing its long-throw depth sensor for 3D sequences and an RGB camera for visual context. A specific challenge addressed is the flexible nature of the head-mount; the depth sensor is positioned a few centimeters above the eyes, and its relative location to the RGB camera is not fixed, which complicates the alignment of the user's field of view with the sensor's frustum. To mitigate this, a thin opaque rectangular hologram is projected to guide the assembler. The post-processing pipeline synchronizes the ~30 FPS RGB stream with the ~5 FPS depth stream using nearest timestamp matching. Because the RGB camera's receptive field is smaller than that of the depth sensor, the final oriented 3D point clouds contain some points without color values, though all points retain spatial $(x, y, z)$ and normal vector $(N_x, N_y, N_z)$ data.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Overview of the IKEA Ego 3D dataset. The dataset includes 174 assembly sequences captured using a Microsoft HoloLens 2. The captured RGB and Depth streams are labelled with 56 action labels per frame. The data is then aligned and synced to form 3D point cloud sequences that are the input to 3D action recognition algorithms.",
      "relevance": "Specifically highlights the 'Capture' and 'Process' stages of the pipeline, showing the transition from raw multi-modal sensor streams to synchronized 3D point clouds."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Section 3.1"
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
      "w": 0.5,
      "h": 0.7
    },
    "bullets": {
      "x": 0.6,
      "y": 0.2,
      "w": 0.35,
      "h": 0.7
    }
  },
  "has_figure": true,
  "style_rationale": "A two-column layout with the figure on the left is chosen to showcase the 'Capture' and 'Process' stages of the pipeline from Figure 1. This provides a visual anchor for the technical details regarding hardware setup, sensor alignment, and data synchronization described in the bullets on the right, following the clean and minimalist aesthetic of the reference slides."
}

Scene context:
{
  "scene_id": 3,
  "title": "Data Collection and Processing Pipeline",
  "summary": "Details the hardware setup using Microsoft HoloLens 2 and the post-processing stage where RGB and depth streams are synced and projected to form oriented 3D point cloud sequences.",
  "paper_section": "3.1 Data collection",
  "narrative_role": "method",
  "duration_stat": {
    "min": 8.0,
    "max": 14.0,
    "avg": 10.0
  }
}

## Previous Content
The following content was drafted for the immediately preceding scenes.
You MUST NOT repeat the exact text content or claims from these previous scenes in your current draft.

{
  "bullets": [
    "174 sequences and ~493k frames across four furniture types",
    "Synchronized RGB and oriented 3D point clouds from HoloLens 2",
    "56 atomic action classes using a hierarchical (verb, noun) structure",
    "Focuses on fine-grained interactions with small assembly components"
  ],
  "audio_content": "The IKEA Ego 3D dataset contains 174 assembly sequences and nearly 500,000 frames captured via HoloLens 2. It synchronizes RGB and depth into oriented 3D point clouds, annotated with 56 hierarchical action classes. This structure enables the recognition of fine-grained tasks involving small components like screws and tools."
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
  "source": ["Figure 1", "Section 3.1"],
  "prompt": "Visual description of the scene for generation"
}

## STRICT RULES:
1. **Number of bullets**: Write 2-4 concise, impactful bullets that cover the key points from the extracted content.
2. **Figure reference**: ONLY use figures listed in the content summary's `key_figures`. Do NOT invent figure references. If the style plan has `has_figure: false`, omit `figure` entirely.
3. **Bullet text**: Each bullet should be concise (under 15 words preferred), impactful, and directly derived from `extracted_content`. Not a copy — a focused summary.
4. **audio_content**: Natural narration covering all bullet points. 
5. **duration_sec**: First, draft the `audio_content`. Then, CALCULATE the duration: `duration_sec = word_count_of_audio / 2.5`. Do NOT guess. If the stats say 8s but you wrote 40 words, `duration_sec` MUST be 16.0.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "title": "Data Collection and Processing Pipeline",
  "audio_content": "Using HoloLens 2, we capture depth and RGB streams guided by a holographic alignment frame. The pipeline syncs these multi-rate sensors to generate oriented 3D point clouds. Each point includes spatial coordinates, RGB color, and surface normals.",
  "duration_sec": 15.2,
  "bullets": [
    "HoloLens 2 setup with depth and RGB sensors",
    "Holographic guidance for sensor frustum alignment",
    "Multi-rate stream synchronization and RGB-D projection",
    "Oriented point clouds with spatial, color, and normal data"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 1",
    "caption": "Overview of the IKEA Ego 3D dataset capture and processing pipeline"
  },
  "source": [
    "Figure 1",
    "Section 3.1"
  ],
  "prompt": "A slide showing the data collection pipeline. On the left is Figure 1 from the paper, highlighting the 'Capture' and 'Process' steps. On the right are bullet points describing the HoloLens 2 hardware, holographic guidance, and the synchronization of RGB and depth streams into oriented 3D point clouds."
}"""

Token usage so far: 92395 prompt tokens, 6649 completion tokens

Cost so far: $1.12342

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "Data Collection and Processing Pipeline",
  "audio_content": "Using HoloLens 2, we capture depth and RGB streams guided by a holographic alignment frame. The pipeline syncs these multi-rate sensors to generate oriented 3D point clouds. Each point includes spatial coordinates, RGB color, and surface normals.",
  "duration_sec": 15.2,
  "bullets": [
    "HoloLens 2 setup with depth and RGB sensors",
    "Holographic guidance for sensor frustum alignment",
    "Multi-rate stream synchronization and RGB-D projection",
    "Oriented point clouds with spatial, color, and normal data"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 1",
    "caption": "Overview of the IKEA Ego 3D dataset capture and processing pipeline"
  },
  "source": [
    "Figure 1",
    "Section 3.1"
  ],
  "prompt": "A slide showing the data collection pipeline. On the left is Figure 1 from the paper, highlighting the 'Capture' and 'Process' steps. On the right are bullet points describing the HoloLens 2 hardware, holographic guidance, and the synchronization of RGB and depth streams into oriented 3D point clouds."
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
      "w": 0.5,
      "h": 0.7
    },
    "bullets": {
      "x": 0.6,
      "y": 0.2,
      "w": 0.35,
      "h": 0.7
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
1. **Build count**: `expected_build_steps` = 1 + number_of_bullets. Build 0 shows title (and figure if present), then one build per bullet.
2. **One bullet per build**: After build 0, each build reveals exactly ONE bullet. `bullets[0]` in build 1, `bullets[1]` in build 2, etc.
3. **Build 0**: Always shows `title` (and `figure` if present). Never shows bullets in build 0.
4. **Audio segments**: Split the `audio_content` from the draft into segments. Each build's `audio_segment` must be non-empty and correspond to what that build reveals.
5. **Bullet ordering**: Assign bullets to builds in the order that creates the best storytelling flow for the audience.
6. **time_offset_sec**: Space evenly across the total time. For N builds over T seconds: offsets at 0, T/N, 2T/N, etc.
7. **visual_emphasis**: Always set to empty list `[]`.
8. **Action targets**: Only use targets that exist in `elements`: `title`, `figure`, `bullets[0]`, `bullets[1]`, etc.
9. **elements**: Copy the drafted title, figure, and bullets exactly — do not modify the text content.
10. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""```json
{
  "style": "Slides",
  "expected_build_steps": 5,
  "elements": {
    "title": "Data Collection and Processing Pipeline",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 1",
      "caption": "Overview of the IKEA Ego 3D dataset capture and processing pipeline"
    },
    "bullets": [
      "HoloLens 2 setup with depth and RGB sensors",
      "Holographic guidance for sensor frustum alignment",
      "Multi-rate stream synchronization and RGB-D projection",
      "Oriented point clouds with spatial, color, and normal data"
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
      "audio_segment": "Using HoloLens 2, we capture depth and RGB streams",
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
      "audio_segment": "guided by a holographic alignment frame.",
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
      "audio_segment": "The pipeline syncs these multi-rate sensors",
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
      "audio_segment": "to generate oriented 3D point clouds.",
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
      "audio_segment": "Each point includes spatial coordinates, RGB color, and surface normals.",
      "visual_emphasis": []
    }
  ]
}
```"""

Token usage so far: 98890 prompt tokens, 7305 completion tokens

Cost so far: $1.20805

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 4,
  "title": "Fine-Grained Action Taxonomy",
  "summary": "Describes the hierarchical annotation of 56 atomic actions composed of verb-noun pairs, including 12 verb classes for temporal semantics and 22 noun classes for object identification.",
  "paper_section": "3.2 Data annotations",
  "narrative_role": "method",
  "duration_stat": {
    "min": 7.0,
    "max": 12.0,
    "avg": 9.0
  }
}

## Previous Scenes Memory
The following content was extracted for the immediately preceding scenes. **This is provided as a memory of what the audience has JUST seen.**
You MUST NOT repeat the claims, figures, tables, or equations from these previous scenes in your current extraction, to ensure the presentation maintains forward momentum without redundant slides.
If you must reference the exactly same figure/table, the 'relevance' MUST be clearly unique to avoid narrative duplication.

{
  "extracted_content": "The IKEA Ego 3D dataset comprises 174 unique assembly sequences across four furniture types: LACK side table, LACK TV bench, KALLAX drawer, and BEKVAM stool. Data was captured using a Microsoft HoloLens 2, specifically utilizing the long-throw depth sensor (~5 FPS) and RGB camera (~30 FPS). To ensure data quality, a hologram was projected to guide participants to keep the assembly within the sensor's frustum. In post-processing, RGB and depth streams were synchronized and projected to generate oriented 3D point clouds containing spatial coordinates, color, and normal vectors $(x, y, z, R, G, B, N_x, N_y, N_z)$. The dataset contains 493,568 frames annotated with 56 atomic action classes. These actions are structured as hierarchical (verb, noun) pairs, involving 12 verb classes (e.g., align, attach, spin) and 22 noun classes (e.g., coffee table shelf, screw, leg). The dataset is split into 121 training and 53 testing sequences, further subdivided into 32-frame clips (10,689 training and 4,566 testing clips). Key challenges include significant class imbalance, ego-view camera motion, and the presence of fine-grained actions involving visually similar small components like different screw types.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "IKEA Ego3D Furniture. The assemblies in the IKEA Ego3D dataset include the (a) LACK Side table, (b) LACK TV bench, (c) KALLAX Drawer, and BEKVAM (d) Stepping stool.",
      "relevance": "Identifies the specific furniture items that define the scope of the assembly tasks in the dataset."
    },
    {
      "ref": "Figure 3",
      "caption": "IKEA Ego 3D Dataset actions. Visualizing the RGB image (top), 3D point cloud (middle), and action label (bottom) for the Drawer (a-d) and Stool (e-h) assemblies.",
      "relevance": "Provides a visual representation of the synchronized multi-modal data and the fine-grained action labels like 'spin screwdriver' or 'attach side panel'."
    },
    {
      "ref": "Figure 4",
      "caption": "IKEA Ego 3D dataset action occurrence. A highly imbalanced dataset provides a challenge for learning-based algorithms. Note the y-axis is log scaled, therefore a small gap in this axis reflects a significant gap in proportions.",
      "relevance": "Highlights the significant class imbalance within the 56 action classes, which is a major technical challenge for models trained on this data."
    },
    {
      "ref": "Figure 5",
      "caption": "Duration statistics. Sequence (a) and action (b) duration distributions in the IKEA Ego 3D dataset.",
      "relevance": "Shows the distribution of sequence and action lengths, illustrating the temporal variety in the dataset."
    }
  ],
  "key_tables": [],
  "key_equations": []
}
{
  "extracted_content": "The data collection hardware consists of a Microsoft HoloLens 2, utilizing its long-throw depth sensor for 3D sequences and an RGB camera for visual context. A specific challenge addressed is the flexible nature of the head-mount; the depth sensor is positioned a few centimeters above the eyes, and its relative location to the RGB camera is not fixed, which complicates the alignment of the user's field of view with the sensor's frustum. To mitigate this, a thin opaque rectangular hologram is projected to guide the assembler. The post-processing pipeline synchronizes the ~30 FPS RGB stream with the ~5 FPS depth stream using nearest timestamp matching. Because the RGB camera's receptive field is smaller than that of the depth sensor, the final oriented 3D point clouds contain some points without color values, though all points retain spatial $(x, y, z)$ and normal vector $(N_x, N_y, N_z)$ data.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Overview of the IKEA Ego 3D dataset. The dataset includes 174 assembly sequences captured using a Microsoft HoloLens 2. The captured RGB and Depth streams are labelled with 56 action labels per frame. The data is then aligned and synced to form 3D point cloud sequences that are the input to 3D action recognition algorithms.",
      "relevance": "Specifically highlights the 'Capture' and 'Process' stages of the pipeline, showing the transition from raw multi-modal sensor streams to synchronized 3D point clouds."
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
  "extracted_content": "The IKEA Ego 3D dataset utilizes a hierarchical annotation scheme where 56 atomic actions are decomposed into (verb, noun) pairs. The verb set (12 classes) focuses on temporal semantics, representing how different objects are manipulated in similar ways (e.g., 'spin', 'attach', 'align'). Conversely, the noun set (22 classes) identifies specific assembly components or tools (e.g., 'cam lock', 'dowel', 'screwdriver') based on their geometric properties. This hierarchical approach is designed to decouple spatial object recognition from temporal action understanding. The taxonomy also includes an 'NA' class (class 0) to account for unlabeled frames during transitions between assembly steps. Furthermore, the dataset captures the inherent repetition in furniture assembly, where certain actions like 'spin leg' occur multiple times, while others like 'spin drawer knob' are unique occurrences. On average, an action lasts 46.2 frames, and each of the 56 classes is represented by at least 100 frames to ensure sufficient data for learning.",
  "key_figures": [
    {
      "ref": "Figure 3",
      "caption": "IKEA Ego 3D Dataset actions. Visualizing the RGB image (top), 3D point cloud (middle), and action label (bottom) for the Drawer (a-d) and Stool (e-h) assemblies.",
      "relevance": "Demonstrates the practical application of the (verb, noun) taxonomy, showing how different verbs ('spin' vs 'use') are applied to various nouns ('screwdriver', 'drill', 'drawer knob') to form specific atomic action labels."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Section 3.2",
    "Section 3.3"
  ]
}"""

Token usage so far: 105891 prompt tokens, 7713 completion tokens

Cost so far: $1.29030

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "The IKEA Ego 3D dataset utilizes a hierarchical annotation scheme where 56 atomic actions are decomposed into (verb, noun) pairs. The verb set (12 classes) focuses on temporal semantics, representing how different objects are manipulated in similar ways (e.g., 'spin', 'attach', 'align'). Conversely, the noun set (22 classes) identifies specific assembly components or tools (e.g., 'cam lock', 'dowel', 'screwdriver') based on their geometric properties. This hierarchical approach is designed to decouple spatial object recognition from temporal action understanding. The taxonomy also includes an 'NA' class (class 0) to account for unlabeled frames during transitions between assembly steps. Furthermore, the dataset captures the inherent repetition in furniture assembly, where certain actions like 'spin leg' occur multiple times, while others like 'spin drawer knob' are unique occurrences. On average, an action lasts 46.2 frames, and each of the 56 classes is represented by at least 100 frames to ensure sufficient data for learning.",
  "key_figures": [
    {
      "ref": "Figure 3",
      "caption": "IKEA Ego 3D Dataset actions. Visualizing the RGB image (top), 3D point cloud (middle), and action label (bottom) for the Drawer (a-d) and Stool (e-h) assemblies.",
      "relevance": "Demonstrates the practical application of the (verb, noun) taxonomy, showing how different verbs ('spin' vs 'use') are applied to various nouns ('screwdriver', 'drill', 'drawer knob') to form specific atomic action labels."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Section 3.2",
    "Section 3.3"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 4,
  "title": "Fine-Grained Action Taxonomy",
  "summary": "Describes the hierarchical annotation of 56 atomic actions composed of verb-noun pairs, including 12 verb classes for temporal semantics and 22 noun classes for object identification.",
  "paper_section": "3.2 Data annotations",
  "narrative_role": "method",
  "duration_stat": {
    "min": 7.0,
    "max": 12.0,
    "avg": 9.0
  }
}

Reference style advice:
Reference Layouts for 'method' section from similar papers:
- Example 1: The slide follows a top-down structure. At the very top, the main title 'Pos3R' is centered in a large, spaced-out font. Below it, a secondary heading 'Step 3: Pose Fitting' is left-aligned. The middle section contains a horizontal process diagram. On the left, a light-colored box groups three images: two showing '2D-2D correspondence' with yellow lines connecting feature points on a watering can, and one 'coordinate map' showing the same object in a multi-colored gradient. A blue arrow labeled '3) PnP-RANSAC' points from this group to a final image on the right, which shows the '6-DoF Pose' as a green 3D bounding box overlaid on a real-world photo of the object. At the bottom of the slide, two bullet points are left-aligned, providing explanatory text for the visual process. The overall background is white, and a faint watermark is visible in the top-left corner.
- Example 2: The slide has a clean, white background with a centered title 'Key idea' at the top, followed by a larger, bolded heading 'Temporal local patches (t-patches)'. The central content is a horizontal flow diagram illustrating a methodology. On the left, a sequence of four 3D human point-cloud models is shown at different time steps (labeled t1, ..., ti, ..., tT), with specific body parts like hands, feet, and torso highlighted in distinct colors (purple, pink, green, cyan). An arrow points from this sequence to a group of 't-patches' in the center-right, which represent the isolated temporal trajectories of those colored segments. A final arrow on the far right leads to the text 'Action prediction' and the specific result 'Jumping jacks'. The overall text density is light, relying on visual representation to explain the core concept.
- Example 3: The slide follows a clean, single-column structure starting with a large, left-aligned title at the top, underlined by a thin horizontal black line. Below the line, the content begins with a 'Definition' section where the term 't-patch' is highlighted in green within a short paragraph of text. Centered in the middle of the slide are two mathematical equations that formally define the t-patch and its temporal mapping function. Following the equations, there is a list of three variable definitions aligned to the left, providing clear explanations for the symbols used in the math. The bottom-left corner contains a footer with the conference information '3DinAction, CVPR 2024 Highlight' and the author's name. The slide has a light text density and uses a minimalist white background to emphasize the mathematical definitions.
- Example 4: The slide has a centered main title 'P o s 3 R' at the top, followed by a sub-heading 'Step 1: Template Rendering' aligned to the top-left. The middle section contains a horizontal diagram showing the rendering process: on the left, a CAD model of a watering can is shown inside a blue wireframe bounding box with RGB axes; an arrow labeled '1) rendering' points to a sequence of five rendered images of the watering can in different orientations. These images are contained within a light blue rounded rectangle, with the text 'forty templates' centered underneath. At the bottom of the slide, there are two bullet points centered horizontally that describe the template generation logic. The background is white, and there is a faint watermark in the top-left corner. The overall text density is light, focusing on the visual diagram.
- Example 5: The slide uses a two-column layout with a clear title at the top-left. The left column features a large, framed diagram showing a 3D perspective of a camera's field of view (frustum) directed at a table with two blue chairs. The right column contains a cropped image representing the camera's actual view, where chairs are identified with bright yellow bounding boxes. Below this right-side image, the word 'Possible' is written above a 'V' symbol. The top-right corner of the slide includes a QR code and a gold-colored institutional logo. A page number '8' is positioned in the bottom-right corner. The background is plain white, and the text density is light, prioritizing visual diagrams over text.

Duration statistics for this section (from references): min=1.0s, max=52.0s, avg=10.5s.

Your job is to decide the **visual layout** for this slide. Do NOT decide builds or animations — those will be planned later.

## CHOOSE THE BEST LAYOUT

Pick the layout template that best suits the content. Common templates include (but you are NOT limited to these):
- `two_col_fig_left` — Figure on left, bullets on right. Best for: method diagrams, architecture figures.
- `two_col_fig_right` — Bullets on left, figure on right. Best for: motivation slides with illustrative figures.
- `full_fig_with_callouts` — Large figure with small bullet callouts below. Best for: results, data visualizations.
- `one_col_bullets` — Full-width bullets, no figure. Best for: text-heavy overview or summary slides.

If none of these fit, invent a descriptive template name and define its regions.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "bullets": {"x": 0.55, "y": 0.25, "w": 0.4, "h": 0.6}
  },
  "has_figure": true,
  "style_rationale": "Two-column layout with figure on left is ideal for showing the architecture diagram alongside explanatory bullets."
}

## STRICT RULES:
1. **Region keys**: Only use `title`, `bullets`, `figure` as region keys. Do NOT invent keys like `callout_1`, `table`, etc.
2. **Coordinates**: All x/y/w/h values must be normalized (0.0 to 1.0). Regions must not overlap.
3. **has_figure**: Set to `true` only if the content summary has relevant figures. If no figure is available, omit `figure` from regions.
4. **No builds**: Do NOT include `build_skeleton`, `expected_build_steps`, or any animation information.
5. Output ONLY valid JSON, no markdown fences, no explanation.


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
      "w": 0.5,
      "h": 0.7
    },
    "bullets": {
      "x": 0.6,
      "y": 0.2,
      "w": 0.35,
      "h": 0.7
    }
  },
  "has_figure": true,
  "style_rationale": "A two-column layout is chosen to present the visual examples of the action taxonomy (Figure 3) alongside the textual description of the hierarchical verb-noun decomposition. This allows the viewer to immediately connect the abstract classes (verbs/nouns) to the concrete ego-view data."
}"""

Token usage so far: 113188 prompt tokens, 7975 completion tokens

Cost so far: $1.37113

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "The IKEA Ego 3D dataset utilizes a hierarchical annotation scheme where 56 atomic actions are decomposed into (verb, noun) pairs. The verb set (12 classes) focuses on temporal semantics, representing how different objects are manipulated in similar ways (e.g., 'spin', 'attach', 'align'). Conversely, the noun set (22 classes) identifies specific assembly components or tools (e.g., 'cam lock', 'dowel', 'screwdriver') based on their geometric properties. This hierarchical approach is designed to decouple spatial object recognition from temporal action understanding. The taxonomy also includes an 'NA' class (class 0) to account for unlabeled frames during transitions between assembly steps. Furthermore, the dataset captures the inherent repetition in furniture assembly, where certain actions like 'spin leg' occur multiple times, while others like 'spin drawer knob' are unique occurrences. On average, an action lasts 46.2 frames, and each of the 56 classes is represented by at least 100 frames to ensure sufficient data for learning.",
  "key_figures": [
    {
      "ref": "Figure 3",
      "caption": "IKEA Ego 3D Dataset actions. Visualizing the RGB image (top), 3D point cloud (middle), and action label (bottom) for the Drawer (a-d) and Stool (e-h) assemblies.",
      "relevance": "Demonstrates the practical application of the (verb, noun) taxonomy, showing how different verbs ('spin' vs 'use') are applied to various nouns ('screwdriver', 'drill', 'drawer knob') to form specific atomic action labels."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Section 3.2",
    "Section 3.3"
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
      "w": 0.5,
      "h": 0.7
    },
    "bullets": {
      "x": 0.6,
      "y": 0.2,
      "w": 0.35,
      "h": 0.7
    }
  },
  "has_figure": true,
  "style_rationale": "A two-column layout is chosen to present the visual examples of the action taxonomy (Figure 3) alongside the textual description of the hierarchical verb-noun decomposition. This allows the viewer to immediately connect the abstract classes (verbs/nouns) to the concrete ego-view data."
}

Scene context:
{
  "scene_id": 4,
  "title": "Fine-Grained Action Taxonomy",
  "summary": "Describes the hierarchical annotation of 56 atomic actions composed of verb-noun pairs, including 12 verb classes for temporal semantics and 22 noun classes for object identification.",
  "paper_section": "3.2 Data annotations",
  "narrative_role": "method",
  "duration_stat": {
    "min": 7.0,
    "max": 12.0,
    "avg": 9.0
  }
}

## Previous Content
The following content was drafted for the immediately preceding scenes.
You MUST NOT repeat the exact text content or claims from these previous scenes in your current draft.

{
  "bullets": [
    "HoloLens 2 setup with depth and RGB sensors",
    "Holographic guidance for sensor frustum alignment",
    "Multi-rate stream synchronization and RGB-D projection",
    "Oriented point clouds with spatial, color, and normal data"
  ],
  "audio_content": "Using HoloLens 2, we capture depth and RGB streams guided by a holographic alignment frame. The pipeline syncs these multi-rate sensors to generate oriented 3D point clouds. Each point includes spatial coordinates, RGB color, and surface normals."
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
  "source": ["Figure 1", "Section 3.1"],
  "prompt": "Visual description of the scene for generation"
}

## STRICT RULES:
1. **Number of bullets**: Write 2-4 concise, impactful bullets that cover the key points from the extracted content.
2. **Figure reference**: ONLY use figures listed in the content summary's `key_figures`. Do NOT invent figure references. If the style plan has `has_figure: false`, omit `figure` entirely.
3. **Bullet text**: Each bullet should be concise (under 15 words preferred), impactful, and directly derived from `extracted_content`. Not a copy — a focused summary.
4. **audio_content**: Natural narration covering all bullet points. 
5. **duration_sec**: First, draft the `audio_content`. Then, CALCULATE the duration: `duration_sec = word_count_of_audio / 2.5`. Do NOT guess. If the stats say 8s but you wrote 40 words, `duration_sec` MUST be 16.0.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "title": "Hierarchical Action Taxonomy",
  "audio_content": "We decompose 56 atomic actions into verb-noun pairs. Twelve verb classes capture temporal semantics, while twenty-two noun classes identify specific components. This hierarchy decouples spatial object recognition from temporal action understanding.",
  "duration_sec": 12.4,
  "bullets": [
    "56 atomic actions decomposed into hierarchical verb-noun pairs",
    "12 verb classes represent temporal semantics and manipulation",
    "22 noun classes identify specific assembly components and tools",
    "Decouples spatial recognition from temporal action understanding"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 3",
    "caption": "Visualizing RGB, 3D point clouds, and action labels for assembly tasks"
  },
  "source": [
    "Section 3.2",
    "Figure 3"
  ],
  "prompt": "A slide showing Figure 3 from the paper on the left, which displays a grid of RGB images, corresponding 3D point clouds, and action labels like 'spin screwdriver' and 'use drill'. On the right, there are bullet points explaining the hierarchical verb-noun taxonomy used for action recognition."
}"""

Token usage so far: 119868 prompt tokens, 8260 completion tokens

Cost so far: $1.44648

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "Hierarchical Action Taxonomy",
  "audio_content": "We decompose 56 atomic actions into verb-noun pairs. Twelve verb classes capture temporal semantics, while twenty-two noun classes identify specific components. This hierarchy decouples spatial object recognition from temporal action understanding.",
  "duration_sec": 12.4,
  "bullets": [
    "56 atomic actions decomposed into hierarchical verb-noun pairs",
    "12 verb classes represent temporal semantics and manipulation",
    "22 noun classes identify specific assembly components and tools",
    "Decouples spatial recognition from temporal action understanding"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 3",
    "caption": "Visualizing RGB, 3D point clouds, and action labels for assembly tasks"
  },
  "source": [
    "Section 3.2",
    "Figure 3"
  ],
  "prompt": "A slide showing Figure 3 from the paper on the left, which displays a grid of RGB images, corresponding 3D point clouds, and action labels like 'spin screwdriver' and 'use drill'. On the right, there are bullet points explaining the hierarchical verb-noun taxonomy used for action recognition."
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
      "w": 0.5,
      "h": 0.7
    },
    "bullets": {
      "x": 0.6,
      "y": 0.2,
      "w": 0.35,
      "h": 0.7
    }
  },
  "has_figure": true,
  "total_time_sec": 12.4
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
1. **Build count**: `expected_build_steps` = 1 + number_of_bullets. Build 0 shows title (and figure if present), then one build per bullet.
2. **One bullet per build**: After build 0, each build reveals exactly ONE bullet. `bullets[0]` in build 1, `bullets[1]` in build 2, etc.
3. **Build 0**: Always shows `title` (and `figure` if present). Never shows bullets in build 0.
4. **Audio segments**: Split the `audio_content` from the draft into segments. Each build's `audio_segment` must be non-empty and correspond to what that build reveals.
5. **Bullet ordering**: Assign bullets to builds in the order that creates the best storytelling flow for the audience.
6. **time_offset_sec**: Space evenly across the total time. For N builds over T seconds: offsets at 0, T/N, 2T/N, etc.
7. **visual_emphasis**: Always set to empty list `[]`.
8. **Action targets**: Only use targets that exist in `elements`: `title`, `figure`, `bullets[0]`, `bullets[1]`, etc.
9. **elements**: Copy the drafted title, figure, and bullets exactly — do not modify the text content.
10. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "style": "Slides",
  "expected_build_steps": 5,
  "elements": {
    "title": "Hierarchical Action Taxonomy",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 3",
      "caption": "Visualizing RGB, 3D point clouds, and action labels for assembly tasks"
    },
    "bullets": [
      "56 atomic actions decomposed into hierarchical verb-noun pairs",
      "12 verb classes represent temporal semantics and manipulation",
      "22 noun classes identify specific assembly components and tools",
      "Decouples spatial recognition from temporal action understanding"
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
      "audio_segment": "We decompose 56 atomic actions into verb-noun pairs.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 2.48,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[0]"
        }
      ],
      "audio_segment": "Twelve verb classes capture temporal semantics,",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 4.96,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[1]"
        }
      ],
      "audio_segment": "while twenty-two noun classes identify specific components.",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 7.44,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[2]"
        }
      ],
      "audio_segment": "This hierarchy decouples spatial object recognition",
      "visual_emphasis": []
    },
    {
      "step_index": 4,
      "time_offset_sec": 9.92,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[3]"
        }
      ],
      "audio_segment": "from temporal action understanding.",
      "visual_emphasis": []
    }
  ]
}"""

Token usage so far: 126350 prompt tokens, 8899 completion tokens

Cost so far: $1.53047

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 5,
  "title": "Unique Dataset Challenges",
  "summary": "Highlights the inherent challenges of the dataset, including significant camera motion, sensor noise, high class imbalance, and the visual similarity of small furniture components.",
  "paper_section": "3.5 Dataset unique challenges",
  "narrative_role": "method",
  "duration_stat": {
    "min": 8.0,
    "max": 13.0,
    "avg": 10.0
  }
}

## Previous Scenes Memory
The following content was extracted for the immediately preceding scenes. **This is provided as a memory of what the audience has JUST seen.**
You MUST NOT repeat the claims, figures, tables, or equations from these previous scenes in your current extraction, to ensure the presentation maintains forward momentum without redundant slides.
If you must reference the exactly same figure/table, the 'relevance' MUST be clearly unique to avoid narrative duplication.

{
  "extracted_content": "The data collection hardware consists of a Microsoft HoloLens 2, utilizing its long-throw depth sensor for 3D sequences and an RGB camera for visual context. A specific challenge addressed is the flexible nature of the head-mount; the depth sensor is positioned a few centimeters above the eyes, and its relative location to the RGB camera is not fixed, which complicates the alignment of the user's field of view with the sensor's frustum. To mitigate this, a thin opaque rectangular hologram is projected to guide the assembler. The post-processing pipeline synchronizes the ~30 FPS RGB stream with the ~5 FPS depth stream using nearest timestamp matching. Because the RGB camera's receptive field is smaller than that of the depth sensor, the final oriented 3D point clouds contain some points without color values, though all points retain spatial $(x, y, z)$ and normal vector $(N_x, N_y, N_z)$ data.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Overview of the IKEA Ego 3D dataset. The dataset includes 174 assembly sequences captured using a Microsoft HoloLens 2. The captured RGB and Depth streams are labelled with 56 action labels per frame. The data is then aligned and synced to form 3D point cloud sequences that are the input to 3D action recognition algorithms.",
      "relevance": "Specifically highlights the 'Capture' and 'Process' stages of the pipeline, showing the transition from raw multi-modal sensor streams to synchronized 3D point clouds."
    }
  ],
  "key_tables": [],
  "key_equations": []
}
{
  "extracted_content": "The IKEA Ego 3D dataset utilizes a hierarchical annotation scheme where 56 atomic actions are decomposed into (verb, noun) pairs. The verb set (12 classes) focuses on temporal semantics, representing how different objects are manipulated in similar ways (e.g., 'spin', 'attach', 'align'). Conversely, the noun set (22 classes) identifies specific assembly components or tools (e.g., 'cam lock', 'dowel', 'screwdriver') based on their geometric properties. This hierarchical approach is designed to decouple spatial object recognition from temporal action understanding. The taxonomy also includes an 'NA' class (class 0) to account for unlabeled frames during transitions between assembly steps. Furthermore, the dataset captures the inherent repetition in furniture assembly, where certain actions like 'spin leg' occur multiple times, while others like 'spin drawer knob' are unique occurrences. On average, an action lasts 46.2 frames, and each of the 56 classes is represented by at least 100 frames to ensure sufficient data for learning.",
  "key_figures": [
    {
      "ref": "Figure 3",
      "caption": "IKEA Ego 3D Dataset actions. Visualizing the RGB image (top), 3D point cloud (middle), and action label (bottom) for the Drawer (a-d) and Stool (e-h) assemblies.",
      "relevance": "Demonstrates the practical application of the (verb, noun) taxonomy, showing how different verbs ('spin' vs 'use') are applied to various nouns ('screwdriver', 'drill', 'drawer knob') to form specific atomic action labels."
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
  "extracted_content": "The IKEA Ego 3D dataset introduces several unique challenges at both the data and class levels. A primary difficulty is the ego-view perspective, which incorporates significant camera motion that must be distinguished from action-related motion and sensor noise. This is further complicated by the visual similarity of small components; for example, screws of different lengths are contextually distinct but visually nearly identical in 3D point clouds. Additionally, the dataset exhibits extreme class imbalance caused by two factors: the frequency of repetitions (e.g., 'spin leg' occurs multiple times per assembly) and the high variance in action durations (e.g., 'spin leg' is significantly longer than 'spin drawer knob'). Finally, the fine-grained nature of furniture assembly creates temporal ambiguity, making it difficult to define precise start and end boundaries for specific actions.",
  "key_figures": [
    {
      "ref": "Figure 4",
      "caption": "IKEA Ego 3D dataset action occurrence. A highly imbalanced dataset provides a challenge for learning-based algorithms. Note the y-axis is log scaled, therefore a small gap in this axis reflects a significant gap in proportions.",
      "relevance": "Provides quantitative evidence of the extreme class imbalance mentioned as a core dataset challenge."
    },
    {
      "ref": "Figure 5",
      "caption": "Duration statistics. Sequence (a) and action (b) duration distributions in the IKEA Ego 3D dataset.",
      "relevance": "Illustrates the high variance in action durations, which contributes to the dataset's inherent imbalance and complexity."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Section 3.3",
    "Section 3.5"
  ]
}"""

Token usage so far: 133009 prompt tokens, 9296 completion tokens

Cost so far: $1.60897

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "The IKEA Ego 3D dataset introduces several unique challenges at both the data and class levels. A primary difficulty is the ego-view perspective, which incorporates significant camera motion that must be distinguished from action-related motion and sensor noise. This is further complicated by the visual similarity of small components; for example, screws of different lengths are contextually distinct but visually nearly identical in 3D point clouds. Additionally, the dataset exhibits extreme class imbalance caused by two factors: the frequency of repetitions (e.g., 'spin leg' occurs multiple times per assembly) and the high variance in action durations (e.g., 'spin leg' is significantly longer than 'spin drawer knob'). Finally, the fine-grained nature of furniture assembly creates temporal ambiguity, making it difficult to define precise start and end boundaries for specific actions.",
  "key_figures": [
    {
      "ref": "Figure 4",
      "caption": "IKEA Ego 3D dataset action occurrence. A highly imbalanced dataset provides a challenge for learning-based algorithms. Note the y-axis is log scaled, therefore a small gap in this axis reflects a significant gap in proportions.",
      "relevance": "Provides quantitative evidence of the extreme class imbalance mentioned as a core dataset challenge."
    },
    {
      "ref": "Figure 5",
      "caption": "Duration statistics. Sequence (a) and action (b) duration distributions in the IKEA Ego 3D dataset.",
      "relevance": "Illustrates the high variance in action durations, which contributes to the dataset's inherent imbalance and complexity."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Section 3.3",
    "Section 3.5"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 5,
  "title": "Unique Dataset Challenges",
  "summary": "Highlights the inherent challenges of the dataset, including significant camera motion, sensor noise, high class imbalance, and the visual similarity of small furniture components.",
  "paper_section": "3.5 Dataset unique challenges",
  "narrative_role": "method",
  "duration_stat": {
    "min": 8.0,
    "max": 13.0,
    "avg": 10.0
  }
}

Reference style advice:
Reference Layouts for 'method' section from similar papers:
- Example 1: The slide features a clean, white background with a large, sans-serif title at the top-left. In the top-right corner, there is a QR code and a gold-colored institutional crest logo. The central content is organized into three vertical columns that demonstrate a process. The top row consists of three photographic images showing a dining table with blue chairs, where yellow bounding boxes are drawn around the chairs. Below each of these images is a thick black arrow pointing downwards to a corresponding visualization in the bottom row. These bottom visualizations represent the bounding boxes as solid colored rectangles (lime green, red, and purple) on a dark blue background. A centered text caption, 'Bounding box representations of the Object Detector', is placed below the bottom row of images. At the very bottom of the slide, there is a horizontal color scale bar transitioning from purple (0) to yellow (1), and a page number '9' is located in the bottom-right corner.
- Example 2: The slide has a centered main title 'P o s 3 R' at the top, followed by a sub-heading 'Step 1: Template Rendering' aligned to the top-left. The middle section contains a horizontal diagram showing the rendering process: on the left, a CAD model of a watering can is shown inside a blue wireframe bounding box with RGB axes; an arrow labeled '1) rendering' points to a sequence of five rendered images of the watering can in different orientations. These images are contained within a light blue rounded rectangle, with the text 'forty templates' centered underneath. At the bottom of the slide, there are two bullet points centered horizontally that describe the template generation logic. The background is white, and there is a faint watermark in the top-left corner. The overall text density is light, focusing on the visual diagram.
- Example 3: The slide features a large title at the top-left and a QR code and university logo at the top-right. The central focus is a complex diagram illustrating a 3D diffusion pipeline. At the center is a colorful 3D cube labeled 'Neural Field' with camera icons positioned around it, connected by lines to represent 'Diffusion with Forward Model'. To the left, an 'Input image Pose 1' is shown. Below this, a stack of 'Generated images from Pose 4' is labeled 'N samples'. To the right of the central cube, there are two more stacks of 'Generated images' corresponding to 'Pose 3' (top) and 'Pose 2' (bottom). An arrow leads from the Pose 2 images to a final stack of 'Depth Map' visualizations on the far right. The bottom-right corner contains two small-text bibliographic references and the slide number '15'. The background is plain white, and the text density is light, primarily consisting of labels for the visual components.
- Example 4: The slide uses a white background with a large, plain-text title at the top-left. The central focus is a flowchart depicting a processing pipeline. On the left, an 'Input image' of a kitchen is shown, with a sample 'VLM Prompt' text block below it. A blue arrow originates from the image and splits into two paths labeled 'Right' and 'Left'. Each path leads to a 'Yes/No' decision point. The 'Right' path is accompanied by a stack of red 'thumbs down' icons labeled 'N samples', while the 'Left' path has a stack of green 'thumbs up' icons. Both paths converge at an 'Aggregate' node, which points to a horizontal stacked bar chart on the right. Above this chart is a numbered list of four specific vision-language models (ChatGPT-4o, Claude-3.5-Sonnet, LLaVA-v1.6, Gemini-1.5-Ultra). The top-right corner features a QR code and a gold university logo. Small text citations and the page number '13' are located in the bottom-right corner. The text density is moderate, balanced by visual diagrams and icons.
- Example 5: The slide presents a detailed architecture diagram for a neural network model. On the far left, a vertical dashed box contains a sequence of 3D human mesh models labeled from S^0 to S^T, representing temporal frames. The top half of the slide shows a sequential pipeline where data flows through three green 't-patch Module' blocks. The output of the final module passes through a pooling layer and a set of feature maps to a blue 'FC' (Fully Connected) block, which generates an 'Action prediction (per frame)'. Below this main pipeline, a large light-green box provides a detailed 'zoom-in' view of a single 't-patch Module'. Inside this detailed view, a pink 't-patch Extractor' processes inputs to identify various 3D temporal patches shown in a dashed box. These patches are then fed into multiple orange 't-patch Net' blocks with shared weights, producing feature maps of size T x C. The diagram uses a variety of colors (green, pink, orange, blue) to distinguish different components and includes mathematical notation for data dimensions and feature labels throughout.

Duration statistics for this section (from references): min=1.0s, max=52.0s, avg=10.5s.

Your job is to decide the **visual layout** for this slide. Do NOT decide builds or animations — those will be planned later.

## CHOOSE THE BEST LAYOUT

Pick the layout template that best suits the content. Common templates include (but you are NOT limited to these):
- `two_col_fig_left` — Figure on left, bullets on right. Best for: method diagrams, architecture figures.
- `two_col_fig_right` — Bullets on left, figure on right. Best for: motivation slides with illustrative figures.
- `full_fig_with_callouts` — Large figure with small bullet callouts below. Best for: results, data visualizations.
- `one_col_bullets` — Full-width bullets, no figure. Best for: text-heavy overview or summary slides.

If none of these fit, invent a descriptive template name and define its regions.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "bullets": {"x": 0.55, "y": 0.25, "w": 0.4, "h": 0.6}
  },
  "has_figure": true,
  "style_rationale": "Two-column layout with figure on left is ideal for showing the architecture diagram alongside explanatory bullets."
}

## STRICT RULES:
1. **Region keys**: Only use `title`, `bullets`, `figure` as region keys. Do NOT invent keys like `callout_1`, `table`, etc.
2. **Coordinates**: All x/y/w/h values must be normalized (0.0 to 1.0). Regions must not overlap.
3. **has_figure**: Set to `true` only if the content summary has relevant figures. If no figure is available, omit `figure` from regions.
4. **No builds**: Do NOT include `build_skeleton`, `expected_build_steps`, or any animation information.
5. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "layout_template": "two_col_fig_right",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.8,
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
  "style_rationale": "A two-column layout with bullets on the left and figures on the right is chosen to balance the descriptive text of the challenges with the quantitative evidence provided by Figures 4 and 5. This follows the clean, academic style seen in the reference examples, prioritizing visual data to support the narrative."
}"""

Token usage so far: 140456 prompt tokens, 9561 completion tokens

Cost so far: $1.69139

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "The IKEA Ego 3D dataset introduces several unique challenges at both the data and class levels. A primary difficulty is the ego-view perspective, which incorporates significant camera motion that must be distinguished from action-related motion and sensor noise. This is further complicated by the visual similarity of small components; for example, screws of different lengths are contextually distinct but visually nearly identical in 3D point clouds. Additionally, the dataset exhibits extreme class imbalance caused by two factors: the frequency of repetitions (e.g., 'spin leg' occurs multiple times per assembly) and the high variance in action durations (e.g., 'spin leg' is significantly longer than 'spin drawer knob'). Finally, the fine-grained nature of furniture assembly creates temporal ambiguity, making it difficult to define precise start and end boundaries for specific actions.",
  "key_figures": [
    {
      "ref": "Figure 4",
      "caption": "IKEA Ego 3D dataset action occurrence. A highly imbalanced dataset provides a challenge for learning-based algorithms. Note the y-axis is log scaled, therefore a small gap in this axis reflects a significant gap in proportions.",
      "relevance": "Provides quantitative evidence of the extreme class imbalance mentioned as a core dataset challenge."
    },
    {
      "ref": "Figure 5",
      "caption": "Duration statistics. Sequence (a) and action (b) duration distributions in the IKEA Ego 3D dataset.",
      "relevance": "Illustrates the high variance in action durations, which contributes to the dataset's inherent imbalance and complexity."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Section 3.3",
    "Section 3.5"
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
      "w": 0.8,
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
  "style_rationale": "A two-column layout with bullets on the left and figures on the right is chosen to balance the descriptive text of the challenges with the quantitative evidence provided by Figures 4 and 5. This follows the clean, academic style seen in the reference examples, prioritizing visual data to support the narrative."
}

Scene context:
{
  "scene_id": 5,
  "title": "Unique Dataset Challenges",
  "summary": "Highlights the inherent challenges of the dataset, including significant camera motion, sensor noise, high class imbalance, and the visual similarity of small furniture components.",
  "paper_section": "3.5 Dataset unique challenges",
  "narrative_role": "method",
  "duration_stat": {
    "min": 8.0,
    "max": 13.0,
    "avg": 10.0
  }
}

## Previous Content
The following content was drafted for the immediately preceding scenes.
You MUST NOT repeat the exact text content or claims from these previous scenes in your current draft.

{
  "bullets": [
    "56 atomic actions decomposed into hierarchical verb-noun pairs",
    "12 verb classes represent temporal semantics and manipulation",
    "22 noun classes identify specific assembly components and tools",
    "Decouples spatial recognition from temporal action understanding"
  ],
  "audio_content": "We decompose 56 atomic actions into verb-noun pairs. Twelve verb classes capture temporal semantics, while twenty-two noun classes identify specific components. This hierarchy decouples spatial object recognition from temporal action understanding."
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
  "source": ["Figure 1", "Section 3.1"],
  "prompt": "Visual description of the scene for generation"
}

## STRICT RULES:
1. **Number of bullets**: Write 2-4 concise, impactful bullets that cover the key points from the extracted content.
2. **Figure reference**: ONLY use figures listed in the content summary's `key_figures`. Do NOT invent figure references. If the style plan has `has_figure: false`, omit `figure` entirely.
3. **Bullet text**: Each bullet should be concise (under 15 words preferred), impactful, and directly derived from `extracted_content`. Not a copy — a focused summary.
4. **audio_content**: Natural narration covering all bullet points. 
5. **duration_sec**: First, draft the `audio_content`. Then, CALCULATE the duration: `duration_sec = word_count_of_audio / 2.5`. Do NOT guess. If the stats say 8s but you wrote 40 words, `duration_sec` MUST be 16.0.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "title": "Unique Dataset Challenges",
  "audio_content": "The ego-view perspective introduces significant camera motion and sensor noise that must be distinguished from actual actions. We also face extreme class imbalance in action frequency and duration, alongside the visual similarity of small components like screws. These factors, plus the temporal ambiguity of fine-grained assembly, make this a highly challenging benchmark.",
  "duration_sec": 17.6,
  "bullets": [
    "Significant ego-view camera motion and sensor noise",
    "Visual similarity of contextually distinct small components",
    "Extreme class imbalance in action frequency and duration",
    "Temporal ambiguity in fine-grained action boundaries"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 4",
    "caption": "Action occurrence distribution showing extreme class imbalance across the dataset."
  },
  "source": [
    "Section 3.3",
    "Section 3.5",
    "Figure 4"
  ],
  "prompt": "A slide showing a list of dataset challenges on the left, such as camera motion and class imbalance. On the right, a bar chart from the paper (Figure 4) illustrates the highly imbalanced action occurrences on a log scale."
}"""

Token usage so far: 147108 prompt tokens, 9848 completion tokens

Cost so far: $1.76652

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "Unique Dataset Challenges",
  "audio_content": "The ego-view perspective introduces significant camera motion and sensor noise that must be distinguished from actual actions. We also face extreme class imbalance in action frequency and duration, alongside the visual similarity of small components like screws. These factors, plus the temporal ambiguity of fine-grained assembly, make this a highly challenging benchmark.",
  "duration_sec": 17.6,
  "bullets": [
    "Significant ego-view camera motion and sensor noise",
    "Visual similarity of contextually distinct small components",
    "Extreme class imbalance in action frequency and duration",
    "Temporal ambiguity in fine-grained action boundaries"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 4",
    "caption": "Action occurrence distribution showing extreme class imbalance across the dataset."
  },
  "source": [
    "Section 3.3",
    "Section 3.5",
    "Figure 4"
  ],
  "prompt": "A slide showing a list of dataset challenges on the left, such as camera motion and class imbalance. On the right, a bar chart from the paper (Figure 4) illustrates the highly imbalanced action occurrences on a log scale."
}

Layout information:
{
  "layout_template": "two_col_fig_right",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.8,
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
  "total_time_sec": 17.6
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
1. **Build count**: `expected_build_steps` = 1 + number_of_bullets. Build 0 shows title (and figure if present), then one build per bullet.
2. **One bullet per build**: After build 0, each build reveals exactly ONE bullet. `bullets[0]` in build 1, `bullets[1]` in build 2, etc.
3. **Build 0**: Always shows `title` (and `figure` if present). Never shows bullets in build 0.
4. **Audio segments**: Split the `audio_content` from the draft into segments. Each build's `audio_segment` must be non-empty and correspond to what that build reveals.
5. **Bullet ordering**: Assign bullets to builds in the order that creates the best storytelling flow for the audience.
6. **time_offset_sec**: Space evenly across the total time. For N builds over T seconds: offsets at 0, T/N, 2T/N, etc.
7. **visual_emphasis**: Always set to empty list `[]`.
8. **Action targets**: Only use targets that exist in `elements`: `title`, `figure`, `bullets[0]`, `bullets[1]`, etc.
9. **elements**: Copy the drafted title, figure, and bullets exactly — do not modify the text content.
10. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""```json
{
  "style": "Slides",
  "expected_build_steps": 5,
  "elements": {
    "title": "Unique Dataset Challenges",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 4",
      "caption": "Action occurrence distribution showing extreme class imbalance across the dataset."
    },
    "bullets": [
      "Significant ego-view camera motion and sensor noise",
      "Extreme class imbalance in action frequency and duration",
      "Visual similarity of contextually distinct small components",
      "Temporal ambiguity in fine-grained action boundaries"
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
      "audio_segment": "The ego-view perspective introduces significant camera motion and sensor noise",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 3.52,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[0]"
        }
      ],
      "audio_segment": "that must be distinguished from actual actions.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 7.04,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[1]"
        }
      ],
      "audio_segment": "We also face extreme class imbalance in action frequency and duration,",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 10.56,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[2]"
        }
      ],
      "audio_segment": "alongside the visual similarity of small components like screws.",
      "visual_emphasis": []
    },
    {
      "step_index": 4,
      "time_offset_sec": 14.08,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[3]"
        }
      ],
      "audio_segment": "These factors, plus the temporal ambiguity of fine-grained assembly, make this a highly challenging benchmark.",
      "visual_emphasis": []
    }
  ]
}
```"""

Token usage so far: 153592 prompt tokens, 10502 completion tokens

Cost so far: $1.85098

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 6,
  "title": "Benchmark and Experimental Setup",
  "summary": "Outlines the evaluation protocol using state-of-the-art 3D action recognition methods such as PSTNet, P4Transformer, and 3DinAction, measured by top-1 accuracy and mean average precision.",
  "paper_section": "4. Benchmark and Experiments",
  "narrative_role": "experiments",
  "duration_stat": {
    "min": 7.0,
    "max": 12.0,
    "avg": 9.0
  }
}

## Previous Scenes Memory
The following content was extracted for the immediately preceding scenes. **This is provided as a memory of what the audience has JUST seen.**
You MUST NOT repeat the claims, figures, tables, or equations from these previous scenes in your current extraction, to ensure the presentation maintains forward momentum without redundant slides.
If you must reference the exactly same figure/table, the 'relevance' MUST be clearly unique to avoid narrative duplication.

{
  "extracted_content": "The IKEA Ego 3D dataset utilizes a hierarchical annotation scheme where 56 atomic actions are decomposed into (verb, noun) pairs. The verb set (12 classes) focuses on temporal semantics, representing how different objects are manipulated in similar ways (e.g., 'spin', 'attach', 'align'). Conversely, the noun set (22 classes) identifies specific assembly components or tools (e.g., 'cam lock', 'dowel', 'screwdriver') based on their geometric properties. This hierarchical approach is designed to decouple spatial object recognition from temporal action understanding. The taxonomy also includes an 'NA' class (class 0) to account for unlabeled frames during transitions between assembly steps. Furthermore, the dataset captures the inherent repetition in furniture assembly, where certain actions like 'spin leg' occur multiple times, while others like 'spin drawer knob' are unique occurrences. On average, an action lasts 46.2 frames, and each of the 56 classes is represented by at least 100 frames to ensure sufficient data for learning.",
  "key_figures": [
    {
      "ref": "Figure 3",
      "caption": "IKEA Ego 3D Dataset actions. Visualizing the RGB image (top), 3D point cloud (middle), and action label (bottom) for the Drawer (a-d) and Stool (e-h) assemblies.",
      "relevance": "Demonstrates the practical application of the (verb, noun) taxonomy, showing how different verbs ('spin' vs 'use') are applied to various nouns ('screwdriver', 'drill', 'drawer knob') to form specific atomic action labels."
    }
  ],
  "key_tables": [],
  "key_equations": []
}
{
  "extracted_content": "The IKEA Ego 3D dataset introduces several unique challenges at both the data and class levels. A primary difficulty is the ego-view perspective, which incorporates significant camera motion that must be distinguished from action-related motion and sensor noise. This is further complicated by the visual similarity of small components; for example, screws of different lengths are contextually distinct but visually nearly identical in 3D point clouds. Additionally, the dataset exhibits extreme class imbalance caused by two factors: the frequency of repetitions (e.g., 'spin leg' occurs multiple times per assembly) and the high variance in action durations (e.g., 'spin leg' is significantly longer than 'spin drawer knob'). Finally, the fine-grained nature of furniture assembly creates temporal ambiguity, making it difficult to define precise start and end boundaries for specific actions.",
  "key_figures": [
    {
      "ref": "Figure 4",
      "caption": "IKEA Ego 3D dataset action occurrence. A highly imbalanced dataset provides a challenge for learning-based algorithms. Note the y-axis is log scaled, therefore a small gap in this axis reflects a significant gap in proportions.",
      "relevance": "Provides quantitative evidence of the extreme class imbalance mentioned as a core dataset challenge."
    },
    {
      "ref": "Figure 5",
      "caption": "Duration statistics. Sequence (a) and action (b) duration distributions in the IKEA Ego 3D dataset.",
      "relevance": "Illustrates the high variance in action durations, which contributes to the dataset's inherent imbalance and complexity."
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
  "extracted_content": "The experimental setup utilizes a unified protocol for all baselines, involving Farthest Point Sampling (FPS) to reduce each frame to 4096 points and subdividing sequences into 32-frame clips for computational efficiency. Models are trained for 100 epochs using an Adam optimizer with an initial learning rate of $10^{-3}$ and a weighted random sampler to address the dataset's inherent class imbalance. Evaluation is conducted using standard metrics: top-1 and top-3 frame-wise accuracy, macro-recall, and mean average precision (mAP). The benchmark compares per-frame architectures (PointNet, PointNet++, Set Transformer) against their temporally smoothed counterparts (+TS) and specialized spatio-temporal methods (PSTNet, P4Transformer, 3DinAction). Results demonstrate that temporal smoothing provides a significant performance boost across all per-frame approaches. While PointNet++ with temporal smoothing achieves the highest top-1 accuracy (52.98%), PSTNet leads in mAP (0.4024). A secondary clustering experiment decouples spatial and temporal representation power by evaluating performance on 12 verb and 22 noun classes, revealing that verbs are inherently more difficult to recognize than nouns because they require the accumulation of sequence information.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Overview of the IKEA Ego 3D dataset. The dataset includes 174 assembly sequences captured using a Microsoft HoloLens 2. The captured RGB and Depth streams are labelled with 56 action labels per frame. The data is then aligned and synced to form 3D point cloud sequences that are the input to 3D action recognition algorithms.",
      "relevance": "Illustrates the end-to-end data processing pipeline, from sensor capture to the synchronized 3D point cloud sequences that serve as the input for the benchmarked algorithms."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 2",
      "caption": "Action recognition results on IKEA Ego 3D. Comparing between recent state-of-the-art approaches using frame accuracy (top1 and top3), macro recall and mAP metrics.",
      "relevance": "The primary benchmark table showing the performance of various 3D action recognition methods on the new dataset."
    },
    {
      "ref": "Table 3",
      "caption": "Noun recognition results. We cluster the action classes by nouns and report the performance of state-of-the-art approaches. This experiment demonstrates the spatial quality of the methods (how well they capture objects).",
      "relevance": "Evaluates the spatial representation capabilities of the models by measuring their ability to identify the assembly components (nouns)."
    },
    {
      "ref": "Table 4",
      "caption": "Verb recognition results. We cluster the action classes by verbs and report the performance of state-of-the-art approaches. This experiment demonstrates the temporal quality of the methods (how well they distinguish motions).",
      "relevance": "Evaluates the temporal representation capabilities of the models by measuring their ability to distinguish different assembly motions (verbs)."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "Section 4. Benchmark and Experiments",
    "Section 4.1 Experiment setup",
    "Section 4.2 Benchmark results discussion",
    "Section 4.3 Noun and Verb clustering experiment"
  ]
}"""

Token usage so far: 160265 prompt tokens, 11273 completion tokens

Cost so far: $1.94084

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "The experimental setup utilizes a unified protocol for all baselines, involving Farthest Point Sampling (FPS) to reduce each frame to 4096 points and subdividing sequences into 32-frame clips for computational efficiency. Models are trained for 100 epochs using an Adam optimizer with an initial learning rate of $10^{-3}$ and a weighted random sampler to address the dataset's inherent class imbalance. Evaluation is conducted using standard metrics: top-1 and top-3 frame-wise accuracy, macro-recall, and mean average precision (mAP). The benchmark compares per-frame architectures (PointNet, PointNet++, Set Transformer) against their temporally smoothed counterparts (+TS) and specialized spatio-temporal methods (PSTNet, P4Transformer, 3DinAction). Results demonstrate that temporal smoothing provides a significant performance boost across all per-frame approaches. While PointNet++ with temporal smoothing achieves the highest top-1 accuracy (52.98%), PSTNet leads in mAP (0.4024). A secondary clustering experiment decouples spatial and temporal representation power by evaluating performance on 12 verb and 22 noun classes, revealing that verbs are inherently more difficult to recognize than nouns because they require the accumulation of sequence information.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Overview of the IKEA Ego 3D dataset. The dataset includes 174 assembly sequences captured using a Microsoft HoloLens 2. The captured RGB and Depth streams are labelled with 56 action labels per frame. The data is then aligned and synced to form 3D point cloud sequences that are the input to 3D action recognition algorithms.",
      "relevance": "Illustrates the end-to-end data processing pipeline, from sensor capture to the synchronized 3D point cloud sequences that serve as the input for the benchmarked algorithms."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 2",
      "caption": "Action recognition results on IKEA Ego 3D. Comparing between recent state-of-the-art approaches using frame accuracy (top1 and top3), macro recall and mAP metrics.",
      "relevance": "The primary benchmark table showing the performance of various 3D action recognition methods on the new dataset."
    },
    {
      "ref": "Table 3",
      "caption": "Noun recognition results. We cluster the action classes by nouns and report the performance of state-of-the-art approaches. This experiment demonstrates the spatial quality of the methods (how well they capture objects).",
      "relevance": "Evaluates the spatial representation capabilities of the models by measuring their ability to identify the assembly components (nouns)."
    },
    {
      "ref": "Table 4",
      "caption": "Verb recognition results. We cluster the action classes by verbs and report the performance of state-of-the-art approaches. This experiment demonstrates the temporal quality of the methods (how well they distinguish motions).",
      "relevance": "Evaluates the temporal representation capabilities of the models by measuring their ability to distinguish different assembly motions (verbs)."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "Section 4. Benchmark and Experiments",
    "Section 4.1 Experiment setup",
    "Section 4.2 Benchmark results discussion",
    "Section 4.3 Noun and Verb clustering experiment"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 6,
  "title": "Benchmark and Experimental Setup",
  "summary": "Outlines the evaluation protocol using state-of-the-art 3D action recognition methods such as PSTNet, P4Transformer, and 3DinAction, measured by top-1 accuracy and mean average precision.",
  "paper_section": "4. Benchmark and Experiments",
  "narrative_role": "experiments",
  "duration_stat": {
    "min": 7.0,
    "max": 12.0,
    "avg": 9.0
  }
}

Reference style advice:
Reference Layouts for 'experiments' section from similar papers:
- Example 1: The slide features a centered title at the top, enclosed within a light blue rounded rectangle. Directly below the title is a prominent line of text providing dataset statistics: '2.1 million parts, 761 categories, \>1500x # unique parts in existing datasets combined', with the '\>1500x' highlighted in red. The main body of the slide is occupied by a large grid of 3D model visualizations. This grid is organized into rows where the leftmost image shows a complete object (e.g., a milkshake, hair dryer, chicken, machine gun) and subsequent images in the same row show individual parts of that object highlighted in bright purple. Each image in the grid has a small text label underneath it. A circular video inset of the presenter is positioned in the bottom right corner of the slide. The overall background is white, and the text density is moderate due to the numerous labels in the image grid.
- Example 2: The slide follows a minimalist, centered layout on a plain white background. The main title, 'ziggy_in_the_arena_1350_1650', is positioned in the middle of the frame in a standard black sans-serif font. Directly beneath it is a subtitle, 'EDS Dataset – 640 x 480 px', which provides technical details about the data being referenced. There are no bullet points, columns, figures, or decorative elements. The text density is very light, focusing the viewer's attention entirely on the centered text block.
- Example 3: The slide has a minimalist, clean layout with a plain white background. In the top-left corner, there is a small heading in a green font that reads 'New Groundtruth!'. The primary focus of the slide is centered horizontally and vertically, featuring a large black title 'Fidget spinner'. Directly beneath this title is a smaller subtitle in black text that specifies the dataset and resolution: 'E2D2 Dataset – 640 x 480 px'. There are no bullet points, images, tables, or other decorative elements, resulting in a very light text density.
- Example 4: The slide follows a top-down single-column structure. At the top, the main title is centered within a light blue rounded rectangular box. Below this, a bold sub-heading provides key statistics about a dataset, with the text '\>1500x' highlighted in red for emphasis. The central and largest portion of the slide is a dense grid of images showing 3D object models. These models are rendered in grey, with specific segments highlighted in purple to illustrate part-level annotations. Each small image has a corresponding text label directly underneath it. The grid is organized by object category (e.g., milkshake, hair dryer, tripod, chicken, etc.), showing the full object followed by its individual parts. In the bottom right corner, there is a circular video overlay of the presenter. The background is plain white, and the overall text density is moderate due to the numerous labels in the image grid.
- Example 5: The slide features a minimalist design on a plain white background. A small heading in a green font, 'New Groundtruth!', is positioned in the top-left corner. The primary content is centered in the middle of the slide, consisting of two lines of black text. The top line is a larger, sans-serif font displaying a scene identifier: 'scene14_dyn_test_03'. Directly below it is a subtitle in a smaller font providing dataset details: 'EVIMO2 Dataset – 640 x 480 px'. There are no other visual elements, such as images, bullet points, or logos, resulting in a very light text density.

Duration statistics for this section (from references): min=1.0s, max=14.0s, avg=4.7s.

Your job is to decide the **visual layout** for this slide. Do NOT decide builds or animations — those will be planned later.

## CHOOSE THE BEST LAYOUT

Pick the layout template that best suits the content. Common templates include (but you are NOT limited to these):
- `two_col_fig_left` — Figure on left, bullets on right. Best for: method diagrams, architecture figures.
- `two_col_fig_right` — Bullets on left, figure on right. Best for: motivation slides with illustrative figures.
- `full_fig_with_callouts` — Large figure with small bullet callouts below. Best for: results, data visualizations.
- `one_col_bullets` — Full-width bullets, no figure. Best for: text-heavy overview or summary slides.

If none of these fit, invent a descriptive template name and define its regions.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "bullets": {"x": 0.55, "y": 0.25, "w": 0.4, "h": 0.6}
  },
  "has_figure": true,
  "style_rationale": "Two-column layout with figure on left is ideal for showing the architecture diagram alongside explanatory bullets."
}

## STRICT RULES:
1. **Region keys**: Only use `title`, `bullets`, `figure` as region keys. Do NOT invent keys like `callout_1`, `table`, etc.
2. **Coordinates**: All x/y/w/h values must be normalized (0.0 to 1.0). Regions must not overlap.
3. **has_figure**: Set to `true` only if the content summary has relevant figures. If no figure is available, omit `figure` from regions.
4. **No builds**: Do NOT include `build_skeleton`, `expected_build_steps`, or any animation information.
5. Output ONLY valid JSON, no markdown fences, no explanation.


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
      "w": 0.45,
      "h": 0.7
    },
    "bullets": {
      "x": 0.55,
      "y": 0.2,
      "w": 0.4,
      "h": 0.7
    }
  },
  "has_figure": true,
  "style_rationale": "A two-column layout is chosen to present the data processing pipeline (Figure 1) or the main benchmark results (Table 2) on the left, providing a visual anchor for the experimental setup. The right column concisely lists the unified protocol, training details, and evaluation metrics, ensuring a clear mapping between the methodology and the visual evidence."
}"""

Token usage so far: 167800 prompt tokens, 11549 completion tokens

Cost so far: $2.02447

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "The experimental setup utilizes a unified protocol for all baselines, involving Farthest Point Sampling (FPS) to reduce each frame to 4096 points and subdividing sequences into 32-frame clips for computational efficiency. Models are trained for 100 epochs using an Adam optimizer with an initial learning rate of $10^{-3}$ and a weighted random sampler to address the dataset's inherent class imbalance. Evaluation is conducted using standard metrics: top-1 and top-3 frame-wise accuracy, macro-recall, and mean average precision (mAP). The benchmark compares per-frame architectures (PointNet, PointNet++, Set Transformer) against their temporally smoothed counterparts (+TS) and specialized spatio-temporal methods (PSTNet, P4Transformer, 3DinAction). Results demonstrate that temporal smoothing provides a significant performance boost across all per-frame approaches. While PointNet++ with temporal smoothing achieves the highest top-1 accuracy (52.98%), PSTNet leads in mAP (0.4024). A secondary clustering experiment decouples spatial and temporal representation power by evaluating performance on 12 verb and 22 noun classes, revealing that verbs are inherently more difficult to recognize than nouns because they require the accumulation of sequence information.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Overview of the IKEA Ego 3D dataset. The dataset includes 174 assembly sequences captured using a Microsoft HoloLens 2. The captured RGB and Depth streams are labelled with 56 action labels per frame. The data is then aligned and synced to form 3D point cloud sequences that are the input to 3D action recognition algorithms.",
      "relevance": "Illustrates the end-to-end data processing pipeline, from sensor capture to the synchronized 3D point cloud sequences that serve as the input for the benchmarked algorithms."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 2",
      "caption": "Action recognition results on IKEA Ego 3D. Comparing between recent state-of-the-art approaches using frame accuracy (top1 and top3), macro recall and mAP metrics.",
      "relevance": "The primary benchmark table showing the performance of various 3D action recognition methods on the new dataset."
    },
    {
      "ref": "Table 3",
      "caption": "Noun recognition results. We cluster the action classes by nouns and report the performance of state-of-the-art approaches. This experiment demonstrates the spatial quality of the methods (how well they capture objects).",
      "relevance": "Evaluates the spatial representation capabilities of the models by measuring their ability to identify the assembly components (nouns)."
    },
    {
      "ref": "Table 4",
      "caption": "Verb recognition results. We cluster the action classes by verbs and report the performance of state-of-the-art approaches. This experiment demonstrates the temporal quality of the methods (how well they distinguish motions).",
      "relevance": "Evaluates the temporal representation capabilities of the models by measuring their ability to distinguish different assembly motions (verbs)."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "Section 4. Benchmark and Experiments",
    "Section 4.1 Experiment setup",
    "Section 4.2 Benchmark results discussion",
    "Section 4.3 Noun and Verb clustering experiment"
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
      "w": 0.45,
      "h": 0.7
    },
    "bullets": {
      "x": 0.55,
      "y": 0.2,
      "w": 0.4,
      "h": 0.7
    }
  },
  "has_figure": true,
  "style_rationale": "A two-column layout is chosen to present the data processing pipeline (Figure 1) or the main benchmark results (Table 2) on the left, providing a visual anchor for the experimental setup. The right column concisely lists the unified protocol, training details, and evaluation metrics, ensuring a clear mapping between the methodology and the visual evidence."
}

Scene context:
{
  "scene_id": 6,
  "title": "Benchmark and Experimental Setup",
  "summary": "Outlines the evaluation protocol using state-of-the-art 3D action recognition methods such as PSTNet, P4Transformer, and 3DinAction, measured by top-1 accuracy and mean average precision.",
  "paper_section": "4. Benchmark and Experiments",
  "narrative_role": "experiments",
  "duration_stat": {
    "min": 7.0,
    "max": 12.0,
    "avg": 9.0
  }
}

## Previous Content
The following content was drafted for the immediately preceding scenes.
You MUST NOT repeat the exact text content or claims from these previous scenes in your current draft.

{
  "bullets": [
    "Significant ego-view camera motion and sensor noise",
    "Visual similarity of contextually distinct small components",
    "Extreme class imbalance in action frequency and duration",
    "Temporal ambiguity in fine-grained action boundaries"
  ],
  "audio_content": "The ego-view perspective introduces significant camera motion and sensor noise that must be distinguished from actual actions. We also face extreme class imbalance in action frequency and duration, alongside the visual similarity of small components like screws. These factors, plus the temporal ambiguity of fine-grained assembly, make this a highly challenging benchmark."
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
  "source": ["Figure 1", "Section 3.1"],
  "prompt": "Visual description of the scene for generation"
}

## STRICT RULES:
1. **Number of bullets**: Write 2-4 concise, impactful bullets that cover the key points from the extracted content.
2. **Figure reference**: ONLY use figures listed in the content summary's `key_figures`. Do NOT invent figure references. If the style plan has `has_figure: false`, omit `figure` entirely.
3. **Bullet text**: Each bullet should be concise (under 15 words preferred), impactful, and directly derived from `extracted_content`. Not a copy — a focused summary.
4. **audio_content**: Natural narration covering all bullet points. 
5. **duration_sec**: First, draft the `audio_content`. Then, CALCULATE the duration: `duration_sec = word_count_of_audio / 2.5`. Do NOT guess. If the stats say 8s but you wrote 40 words, `duration_sec` MUST be 16.0.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "title": "Benchmark and Experimental Setup",
  "audio_content": "We evaluate the dataset using a unified protocol with 4096 points per frame and 32-frame clips. We compare per-frame baselines against spatio-temporal methods, using weighted sampling to address class imbalance and measuring performance through accuracy and mean average precision.",
  "duration_sec": 13.6,
  "bullets": [
    "Unified protocol: 4096 points per frame and 32-frame clips",
    "Comparison of per-frame baselines against spatio-temporal methods",
    "Weighted sampling to address inherent dataset class imbalance",
    "Evaluation via top-1/3 accuracy and mean average precision (mAP)"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 1",
    "caption": "Overview of the IKEA Ego 3D data processing pipeline"
  },
  "source": [
    "Figure 1",
    "Section 4.1",
    "Table 2"
  ],
  "prompt": "A split-screen slide. On the left, Figure 1 from the paper shows the data pipeline from HoloLens capture to 3D point clouds. On the right, a list of experimental parameters and evaluation metrics."
}"""

Token usage so far: 174866 prompt tokens, 11849 completion tokens

Cost so far: $2.10413

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "Benchmark and Experimental Setup",
  "audio_content": "We evaluate the dataset using a unified protocol with 4096 points per frame and 32-frame clips. We compare per-frame baselines against spatio-temporal methods, using weighted sampling to address class imbalance and measuring performance through accuracy and mean average precision.",
  "duration_sec": 13.6,
  "bullets": [
    "Unified protocol: 4096 points per frame and 32-frame clips",
    "Comparison of per-frame baselines against spatio-temporal methods",
    "Weighted sampling to address inherent dataset class imbalance",
    "Evaluation via top-1/3 accuracy and mean average precision (mAP)"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 1",
    "caption": "Overview of the IKEA Ego 3D data processing pipeline"
  },
  "source": [
    "Figure 1",
    "Section 4.1",
    "Table 2"
  ],
  "prompt": "A split-screen slide. On the left, Figure 1 from the paper shows the data pipeline from HoloLens capture to 3D point clouds. On the right, a list of experimental parameters and evaluation metrics."
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
      "w": 0.45,
      "h": 0.7
    },
    "bullets": {
      "x": 0.55,
      "y": 0.2,
      "w": 0.4,
      "h": 0.7
    }
  },
  "has_figure": true,
  "total_time_sec": 13.6
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
1. **Build count**: `expected_build_steps` = 1 + number_of_bullets. Build 0 shows title (and figure if present), then one build per bullet.
2. **One bullet per build**: After build 0, each build reveals exactly ONE bullet. `bullets[0]` in build 1, `bullets[1]` in build 2, etc.
3. **Build 0**: Always shows `title` (and `figure` if present). Never shows bullets in build 0.
4. **Audio segments**: Split the `audio_content` from the draft into segments. Each build's `audio_segment` must be non-empty and correspond to what that build reveals.
5. **Bullet ordering**: Assign bullets to builds in the order that creates the best storytelling flow for the audience.
6. **time_offset_sec**: Space evenly across the total time. For N builds over T seconds: offsets at 0, T/N, 2T/N, etc.
7. **visual_emphasis**: Always set to empty list `[]`.
8. **Action targets**: Only use targets that exist in `elements`: `title`, `figure`, `bullets[0]`, `bullets[1]`, etc.
9. **elements**: Copy the drafted title, figure, and bullets exactly — do not modify the text content.
10. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "style": "Slides",
  "expected_build_steps": 5,
  "elements": {
    "title": "Benchmark and Experimental Setup",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 1",
      "caption": "Overview of the IKEA Ego 3D data processing pipeline"
    },
    "bullets": [
      "Unified protocol: 4096 points per frame and 32-frame clips",
      "Comparison of per-frame baselines against spatio-temporal methods",
      "Weighted sampling to address inherent dataset class imbalance",
      "Evaluation via top-1/3 accuracy and mean average precision (mAP)"
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
      "audio_segment": "We evaluate the dataset using a unified protocol",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 2.72,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[0]"
        }
      ],
      "audio_segment": "with 4096 points per frame and 32-frame clips.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 5.44,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[1]"
        }
      ],
      "audio_segment": "We compare per-frame baselines against spatio-temporal methods,",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 8.16,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[2]"
        }
      ],
      "audio_segment": "using weighted sampling to address class imbalance",
      "visual_emphasis": []
    },
    {
      "step_index": 4,
      "time_offset_sec": 10.88,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[3]"
        }
      ],
      "audio_segment": "and measuring performance through accuracy and mean average precision.",
      "visual_emphasis": []
    }
  ]
}"""

Token usage so far: 181364 prompt tokens, 12514 completion tokens

Cost so far: $2.18906

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 7,
  "title": "Performance Analysis and Temporal Smoothing",
  "summary": "Discusses benchmark results showing that incorporating temporal smoothing significantly boosts performance, with PointNet++ with temporal smoothing emerging as a surprisingly strong baseline.",
  "paper_section": "4.2 Benchmark results discussion",
  "narrative_role": "results",
  "duration_stat": {
    "min": 9.0,
    "max": 15.0,
    "avg": 11.0
  }
}

## Previous Scenes Memory
The following content was extracted for the immediately preceding scenes. **This is provided as a memory of what the audience has JUST seen.**
You MUST NOT repeat the claims, figures, tables, or equations from these previous scenes in your current extraction, to ensure the presentation maintains forward momentum without redundant slides.
If you must reference the exactly same figure/table, the 'relevance' MUST be clearly unique to avoid narrative duplication.

{
  "extracted_content": "The IKEA Ego 3D dataset introduces several unique challenges at both the data and class levels. A primary difficulty is the ego-view perspective, which incorporates significant camera motion that must be distinguished from action-related motion and sensor noise. This is further complicated by the visual similarity of small components; for example, screws of different lengths are contextually distinct but visually nearly identical in 3D point clouds. Additionally, the dataset exhibits extreme class imbalance caused by two factors: the frequency of repetitions (e.g., 'spin leg' occurs multiple times per assembly) and the high variance in action durations (e.g., 'spin leg' is significantly longer than 'spin drawer knob'). Finally, the fine-grained nature of furniture assembly creates temporal ambiguity, making it difficult to define precise start and end boundaries for specific actions.",
  "key_figures": [
    {
      "ref": "Figure 4",
      "caption": "IKEA Ego 3D dataset action occurrence. A highly imbalanced dataset provides a challenge for learning-based algorithms. Note the y-axis is log scaled, therefore a small gap in this axis reflects a significant gap in proportions.",
      "relevance": "Provides quantitative evidence of the extreme class imbalance mentioned as a core dataset challenge."
    },
    {
      "ref": "Figure 5",
      "caption": "Duration statistics. Sequence (a) and action (b) duration distributions in the IKEA Ego 3D dataset.",
      "relevance": "Illustrates the high variance in action durations, which contributes to the dataset's inherent imbalance and complexity."
    }
  ],
  "key_tables": [],
  "key_equations": []
}
{
  "extracted_content": "The experimental setup utilizes a unified protocol for all baselines, involving Farthest Point Sampling (FPS) to reduce each frame to 4096 points and subdividing sequences into 32-frame clips for computational efficiency. Models are trained for 100 epochs using an Adam optimizer with an initial learning rate of $10^{-3}$ and a weighted random sampler to address the dataset's inherent class imbalance. Evaluation is conducted using standard metrics: top-1 and top-3 frame-wise accuracy, macro-recall, and mean average precision (mAP). The benchmark compares per-frame architectures (PointNet, PointNet++, Set Transformer) against their temporally smoothed counterparts (+TS) and specialized spatio-temporal methods (PSTNet, P4Transformer, 3DinAction). Results demonstrate that temporal smoothing provides a significant performance boost across all per-frame approaches. While PointNet++ with temporal smoothing achieves the highest top-1 accuracy (52.98%), PSTNet leads in mAP (0.4024). A secondary clustering experiment decouples spatial and temporal representation power by evaluating performance on 12 verb and 22 noun classes, revealing that verbs are inherently more difficult to recognize than nouns because they require the accumulation of sequence information.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Overview of the IKEA Ego 3D dataset. The dataset includes 174 assembly sequences captured using a Microsoft HoloLens 2. The captured RGB and Depth streams are labelled with 56 action labels per frame. The data is then aligned and synced to form 3D point cloud sequences that are the input to 3D action recognition algorithms.",
      "relevance": "Illustrates the end-to-end data processing pipeline, from sensor capture to the synchronized 3D point cloud sequences that serve as the input for the benchmarked algorithms."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 2",
      "caption": "Action recognition results on IKEA Ego 3D. Comparing between recent state-of-the-art approaches using frame accuracy (top1 and top3), macro recall and mAP metrics.",
      "relevance": "The primary benchmark table showing the performance of various 3D action recognition methods on the new dataset."
    },
    {
      "ref": "Table 3",
      "caption": "Noun recognition results. We cluster the action classes by nouns and report the performance of state-of-the-art approaches. This experiment demonstrates the spatial quality of the methods (how well they capture objects).",
      "relevance": "Evaluates the spatial representation capabilities of the models by measuring their ability to identify the assembly components (nouns)."
    },
    {
      "ref": "Table 4",
      "caption": "Verb recognition results. We cluster the action classes by verbs and report the performance of state-of-the-art approaches. This experiment demonstrates the temporal quality of the methods (how well they distinguish motions).",
      "relevance": "Evaluates the temporal representation capabilities of the models by measuring their ability to distinguish different assembly motions (verbs)."
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
  "extracted_content": "The benchmark results reveal that incorporating naive temporal smoothing (+TS) leads to a significant performance boost across all per-frame architectures, confirming that temporal information is essential for action inference in 3D point clouds. Surprisingly, PointNet++ with temporal smoothing emerges as the best-performing method in terms of top-1 accuracy, outperforming more complex spatio-temporal models. Among the specialized action recognition methods, PSTNet demonstrates superior performance compared to 3DinAction on this specific dataset. The authors attribute 3DinAction's relative underperformance to its t-patch construction method, which is prone to collapsing when faced with the large, non-action-related head and sensor motions inherent in ego-view data. This suggests that current specialized 3D action recognition methods may need to improve their global representation capabilities to better handle dynamic ego-centric perspectives.",
  "key_figures": [],
  "key_tables": [
    {
      "ref": "Table 2",
      "caption": "Action recognition results on IKEA Ego 3D. Comparing between recent state-of-the-art approaches using frame accuracy (top1 and top3), macro recall and mAP metrics.",
      "relevance": "Provides the quantitative basis for the analysis of the performance boost gained from temporal smoothing and the comparison between specialized spatio-temporal models like PSTNet and 3DinAction."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "Section 4.2"
  ]
}"""

Token usage so far: 188354 prompt tokens, 12845 completion tokens

Cost so far: $2.26889

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "The benchmark results reveal that incorporating naive temporal smoothing (+TS) leads to a significant performance boost across all per-frame architectures, confirming that temporal information is essential for action inference in 3D point clouds. Surprisingly, PointNet++ with temporal smoothing emerges as the best-performing method in terms of top-1 accuracy, outperforming more complex spatio-temporal models. Among the specialized action recognition methods, PSTNet demonstrates superior performance compared to 3DinAction on this specific dataset. The authors attribute 3DinAction's relative underperformance to its t-patch construction method, which is prone to collapsing when faced with the large, non-action-related head and sensor motions inherent in ego-view data. This suggests that current specialized 3D action recognition methods may need to improve their global representation capabilities to better handle dynamic ego-centric perspectives.",
  "key_figures": [],
  "key_tables": [
    {
      "ref": "Table 2",
      "caption": "Action recognition results on IKEA Ego 3D. Comparing between recent state-of-the-art approaches using frame accuracy (top1 and top3), macro recall and mAP metrics.",
      "relevance": "Provides the quantitative basis for the analysis of the performance boost gained from temporal smoothing and the comparison between specialized spatio-temporal models like PSTNet and 3DinAction."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "Section 4.2"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 7,
  "title": "Performance Analysis and Temporal Smoothing",
  "summary": "Discusses benchmark results showing that incorporating temporal smoothing significantly boosts performance, with PointNet++ with temporal smoothing emerging as a surprisingly strong baseline.",
  "paper_section": "4.2 Benchmark results discussion",
  "narrative_role": "results",
  "duration_stat": {
    "min": 9.0,
    "max": 15.0,
    "avg": 11.0
  }
}

Reference style advice:
Reference Layouts for 'results' section from similar papers:
- Example 1: The slide follows a clean, single-column layout centered around a large table. At the top, the title is centered in a large serif font. The main content is a wide table that occupies the middle and lower portions of the slide. This table is structured into two primary horizontal categories, 'Non-PR' and 'PR', labeled vertically on the left. It presents performance metrics across three datasets—ScanNet1500, RealEstate10K, and ACID—each subdivided into three AUC columns (AUC@5, AUC@10, AUC@20). An additional column on the far right lists 'Inference time'. The table uses horizontal rules for organization and bold text to highlight top-performing results. A single-line caption is centered directly beneath the table, providing a brief description of the data shown. The background is plain white, and the text density is moderate, primarily concentrated within the numerical data of the table.
- Example 2: The slide features a large, centered title at the top in a black serif font. Below the title, the main content consists of a horizontal arrangement of four visual elements for qualitative comparison. The first three elements from the left are large 3D visualizations showing complex camera trajectories and poses represented by small frustums and connecting lines. Each of these is labeled directly underneath with its corresponding method: 'Map-free (Regress)', 'ExReNet (SUNCG)', and 'Reloc3r-512 (Ours)'. The fourth element on the far right is a vertical stack of three smaller, more linear trajectory visualizations, each labeled to its right with the same three method names for a secondary comparison. The background is a solid white, and the overall text density is light, focusing entirely on the visual representation of the pose estimation results.
- Example 3: The slide features a minimalist design on a plain white background. A large title in a serif font is positioned at the top-left corner. The main body of the slide is occupied by six distinct 3D reconstruction visualizations, likely point clouds or textured meshes, arranged in a two-row by three-column grid. These visualizations depict various scenes and objects, including building interiors, a classical archway, a green train locomotive, and building facades. There are no bullet points, captions, or other textual elements besides the title, resulting in a very light text density that emphasizes qualitative visual findings.
- Example 4: The slide features a screenshot of a web browser displaying a Gradio-based interactive demo. At the top center, a 'Run' button is positioned above two configuration settings: a 'confidence threshold for the result' with an orange slider on the left, and a 'number of points sampled from the result' with a numeric input field on the right. The main body of the slide is dominated by a large, centered 3D visualization window with a gray background, displaying a point cloud reconstruction of an indoor scene. A small download icon is located in the top-right corner of this visualization area. The bottom of the page contains footer text in both Chinese and English, mentioning API usage and the Gradio framework. The layout is clean with light text density, prioritizing the qualitative 3D result.
- Example 5: The slide uses a grid-like layout organized into several rectangular compartments separated by dashed gray lines. A large, centered title in a serif font is positioned at the top. The content consists of multiple qualitative examples demonstrating relative pose estimation across various image pairs and groups. Each compartment contains two or more images of a specific subject—ranging from statues and monuments to sketches, portraits, and everyday objects like a backpack. Next to each set of images is a small 3D diagram showing camera frustums (in orange/yellow) and coordinate axes (in red, green, and blue) to visualize the estimated spatial relationship between the camera views. The images are arranged in two primary rows: the top row contains five distinct sections, while the bottom row contains four smaller sections and one larger section on the far right. This larger section features five different views of a Nike backpack arranged around a central 3D coordinate system. The overall text density is light, with a white background and thin colored borders around the individual images.

Duration statistics for this section (from references): min=1.0s, max=36.0s, avg=9.5s.

Your job is to decide the **visual layout** for this slide. Do NOT decide builds or animations — those will be planned later.

## CHOOSE THE BEST LAYOUT

Pick the layout template that best suits the content. Common templates include (but you are NOT limited to these):
- `two_col_fig_left` — Figure on left, bullets on right. Best for: method diagrams, architecture figures.
- `two_col_fig_right` — Bullets on left, figure on right. Best for: motivation slides with illustrative figures.
- `full_fig_with_callouts` — Large figure with small bullet callouts below. Best for: results, data visualizations.
- `one_col_bullets` — Full-width bullets, no figure. Best for: text-heavy overview or summary slides.

If none of these fit, invent a descriptive template name and define its regions.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "bullets": {"x": 0.55, "y": 0.25, "w": 0.4, "h": 0.6}
  },
  "has_figure": true,
  "style_rationale": "Two-column layout with figure on left is ideal for showing the architecture diagram alongside explanatory bullets."
}

## STRICT RULES:
1. **Region keys**: Only use `title`, `bullets`, `figure` as region keys. Do NOT invent keys like `callout_1`, `table`, etc.
2. **Coordinates**: All x/y/w/h values must be normalized (0.0 to 1.0). Regions must not overlap.
3. **has_figure**: Set to `true` only if the content summary has relevant figures. If no figure is available, omit `figure` from regions.
4. **No builds**: Do NOT include `build_skeleton`, `expected_build_steps`, or any animation information.
5. Output ONLY valid JSON, no markdown fences, no explanation.


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
      "w": 0.5,
      "h": 0.7
    },
    "bullets": {
      "x": 0.6,
      "y": 0.2,
      "w": 0.35,
      "h": 0.7
    }
  },
  "has_figure": true,
  "style_rationale": "A two-column layout is chosen to present the quantitative benchmark results (Table 2) on the left, allowing the viewer to see the data while reading the key analytical takeaways on the right. This follows the 'results' section style of providing a clear data-to-interpretation mapping."
}"""

Token usage so far: 195524 prompt tokens, 13109 completion tokens

Cost so far: $2.34851

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "The benchmark results reveal that incorporating naive temporal smoothing (+TS) leads to a significant performance boost across all per-frame architectures, confirming that temporal information is essential for action inference in 3D point clouds. Surprisingly, PointNet++ with temporal smoothing emerges as the best-performing method in terms of top-1 accuracy, outperforming more complex spatio-temporal models. Among the specialized action recognition methods, PSTNet demonstrates superior performance compared to 3DinAction on this specific dataset. The authors attribute 3DinAction's relative underperformance to its t-patch construction method, which is prone to collapsing when faced with the large, non-action-related head and sensor motions inherent in ego-view data. This suggests that current specialized 3D action recognition methods may need to improve their global representation capabilities to better handle dynamic ego-centric perspectives.",
  "key_figures": [],
  "key_tables": [
    {
      "ref": "Table 2",
      "caption": "Action recognition results on IKEA Ego 3D. Comparing between recent state-of-the-art approaches using frame accuracy (top1 and top3), macro recall and mAP metrics.",
      "relevance": "Provides the quantitative basis for the analysis of the performance boost gained from temporal smoothing and the comparison between specialized spatio-temporal models like PSTNet and 3DinAction."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "Section 4.2"
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
      "w": 0.5,
      "h": 0.7
    },
    "bullets": {
      "x": 0.6,
      "y": 0.2,
      "w": 0.35,
      "h": 0.7
    }
  },
  "has_figure": true,
  "style_rationale": "A two-column layout is chosen to present the quantitative benchmark results (Table 2) on the left, allowing the viewer to see the data while reading the key analytical takeaways on the right. This follows the 'results' section style of providing a clear data-to-interpretation mapping."
}

Scene context:
{
  "scene_id": 7,
  "title": "Performance Analysis and Temporal Smoothing",
  "summary": "Discusses benchmark results showing that incorporating temporal smoothing significantly boosts performance, with PointNet++ with temporal smoothing emerging as a surprisingly strong baseline.",
  "paper_section": "4.2 Benchmark results discussion",
  "narrative_role": "results",
  "duration_stat": {
    "min": 9.0,
    "max": 15.0,
    "avg": 11.0
  }
}

## Previous Content
The following content was drafted for the immediately preceding scenes.
You MUST NOT repeat the exact text content or claims from these previous scenes in your current draft.

{
  "bullets": [
    "Unified protocol: 4096 points per frame and 32-frame clips",
    "Comparison of per-frame baselines against spatio-temporal methods",
    "Weighted sampling to address inherent dataset class imbalance",
    "Evaluation via top-1/3 accuracy and mean average precision (mAP)"
  ],
  "audio_content": "We evaluate the dataset using a unified protocol with 4096 points per frame and 32-frame clips. We compare per-frame baselines against spatio-temporal methods, using weighted sampling to address class imbalance and measuring performance through accuracy and mean average precision."
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
  "source": ["Figure 1", "Section 3.1"],
  "prompt": "Visual description of the scene for generation"
}

## STRICT RULES:
1. **Number of bullets**: Write 2-4 concise, impactful bullets that cover the key points from the extracted content.
2. **Figure reference**: ONLY use figures listed in the content summary's `key_figures`. Do NOT invent figure references. If the style plan has `has_figure: false`, omit `figure` entirely.
3. **Bullet text**: Each bullet should be concise (under 15 words preferred), impactful, and directly derived from `extracted_content`. Not a copy — a focused summary.
4. **audio_content**: Natural narration covering all bullet points. 
5. **duration_sec**: First, draft the `audio_content`. Then, CALCULATE the duration: `duration_sec = word_count_of_audio / 2.5`. Do NOT guess. If the stats say 8s but you wrote 40 words, `duration_sec` MUST be 16.0.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "title": "Performance Analysis & Temporal Smoothing",
  "audio_content": "Benchmark results show that temporal smoothing significantly boosts performance, with PointNet plus plus emerging as a surprisingly strong baseline. While PSTNet performs well, 3DinAction struggles with the head motion inherent in ego-view data. This highlights the need for models that better handle dynamic, ego-centric perspectives.",
  "duration_sec": 15.6,
  "bullets": [
    "Temporal smoothing (+TS) significantly boosts performance across all architectures",
    "PointNet++ with smoothing achieves the highest top-1 accuracy",
    "PSTNet outperforms 3DinAction on ego-view sensor motion challenges",
    "Results suggest a need for improved global representations in dynamic 3D scenes"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Table 2",
    "caption": "Action recognition results comparing state-of-the-art methods on the IKEA Ego 3D dataset."
  },
  "source": [
    "Table 2",
    "Section 4.2"
  ],
  "prompt": "A slide showing Table 2 from the paper on the left side, which lists action recognition results for various methods like PointNet, PSTNet, and 3DinAction. On the right side, there are bullet points summarizing that temporal smoothing is essential and that PointNet++ with smoothing is a top performer despite the complexity of other spatio-temporal models."
}"""

Token usage so far: 202138 prompt tokens, 13441 completion tokens

Cost so far: $2.42461

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "Performance Analysis & Temporal Smoothing",
  "audio_content": "Benchmark results show that temporal smoothing significantly boosts performance, with PointNet plus plus emerging as a surprisingly strong baseline. While PSTNet performs well, 3DinAction struggles with the head motion inherent in ego-view data. This highlights the need for models that better handle dynamic, ego-centric perspectives.",
  "duration_sec": 15.6,
  "bullets": [
    "Temporal smoothing (+TS) significantly boosts performance across all architectures",
    "PointNet++ with smoothing achieves the highest top-1 accuracy",
    "PSTNet outperforms 3DinAction on ego-view sensor motion challenges",
    "Results suggest a need for improved global representations in dynamic 3D scenes"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Table 2",
    "caption": "Action recognition results comparing state-of-the-art methods on the IKEA Ego 3D dataset."
  },
  "source": [
    "Table 2",
    "Section 4.2"
  ],
  "prompt": "A slide showing Table 2 from the paper on the left side, which lists action recognition results for various methods like PointNet, PSTNet, and 3DinAction. On the right side, there are bullet points summarizing that temporal smoothing is essential and that PointNet++ with smoothing is a top performer despite the complexity of other spatio-temporal models."
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
      "w": 0.5,
      "h": 0.7
    },
    "bullets": {
      "x": 0.6,
      "y": 0.2,
      "w": 0.35,
      "h": 0.7
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
1. **Build count**: `expected_build_steps` = 1 + number_of_bullets. Build 0 shows title (and figure if present), then one build per bullet.
2. **One bullet per build**: After build 0, each build reveals exactly ONE bullet. `bullets[0]` in build 1, `bullets[1]` in build 2, etc.
3. **Build 0**: Always shows `title` (and `figure` if present). Never shows bullets in build 0.
4. **Audio segments**: Split the `audio_content` from the draft into segments. Each build's `audio_segment` must be non-empty and correspond to what that build reveals.
5. **Bullet ordering**: Assign bullets to builds in the order that creates the best storytelling flow for the audience.
6. **time_offset_sec**: Space evenly across the total time. For N builds over T seconds: offsets at 0, T/N, 2T/N, etc.
7. **visual_emphasis**: Always set to empty list `[]`.
8. **Action targets**: Only use targets that exist in `elements`: `title`, `figure`, `bullets[0]`, `bullets[1]`, etc.
9. **elements**: Copy the drafted title, figure, and bullets exactly — do not modify the text content.
10. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""```json
{
  "style": "Slides",
  "expected_build_steps": 5,
  "elements": {
    "title": "Performance Analysis & Temporal Smoothing",
    "figure": {
      "type": "paper_figure",
      "ref": "Table 2",
      "caption": "Action recognition results comparing state-of-the-art methods on the IKEA Ego 3D dataset."
    },
    "bullets": [
      "Temporal smoothing (+TS) significantly boosts performance across all architectures",
      "PointNet++ with smoothing achieves the highest top-1 accuracy",
      "PSTNet outperforms 3DinAction on ego-view sensor motion challenges",
      "Results suggest a need for improved global representations in dynamic 3D scenes"
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
      "audio_segment": "Benchmark results show that",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 3.12,
      "actions": [
        {"type": "fade_in", "target": "bullets[0]"}
      ],
      "audio_segment": "temporal smoothing significantly boosts performance,",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 6.24,
      "actions": [
        {"type": "fade_in", "target": "bullets[1]"}
      ],
      "audio_segment": "with PointNet plus plus emerging as a surprisingly strong baseline.",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 9.36,
      "actions": [
        {"type": "fade_in", "target": "bullets[2]"}
      ],
      "audio_segment": "While PSTNet performs well, 3DinAction struggles with the head motion inherent in ego-view data.",
      "visual_emphasis": []
    },
    {
      "step_index": 4,
      "time_offset_sec": 12.48,
      "actions": [
        {"type": "fade_in", "target": "bullets[3]"}
      ],
      "audio_segment": "This highlights the need for models that better handle dynamic, ego-centric perspectives.",
      "visual_emphasis": []
    }
  ]
}
```"""

Token usage so far: 208667 prompt tokens, 14078 completion tokens

Cost so far: $2.50901

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 8,
  "title": "Noun and Verb Clustering Insights",
  "summary": "Presents findings from decoupling spatial and temporal power, revealing that verbs are inherently harder to recognize than nouns and rely more heavily on temporal sequence information.",
  "paper_section": "4.3 Noun and Verb clustering experiment",
  "narrative_role": "results",
  "duration_stat": {
    "min": 8.0,
    "max": 14.0,
    "avg": 10.0
  }
}

## Previous Scenes Memory
The following content was extracted for the immediately preceding scenes. **This is provided as a memory of what the audience has JUST seen.**
You MUST NOT repeat the claims, figures, tables, or equations from these previous scenes in your current extraction, to ensure the presentation maintains forward momentum without redundant slides.
If you must reference the exactly same figure/table, the 'relevance' MUST be clearly unique to avoid narrative duplication.

{
  "extracted_content": "The experimental setup utilizes a unified protocol for all baselines, involving Farthest Point Sampling (FPS) to reduce each frame to 4096 points and subdividing sequences into 32-frame clips for computational efficiency. Models are trained for 100 epochs using an Adam optimizer with an initial learning rate of $10^{-3}$ and a weighted random sampler to address the dataset's inherent class imbalance. Evaluation is conducted using standard metrics: top-1 and top-3 frame-wise accuracy, macro-recall, and mean average precision (mAP). The benchmark compares per-frame architectures (PointNet, PointNet++, Set Transformer) against their temporally smoothed counterparts (+TS) and specialized spatio-temporal methods (PSTNet, P4Transformer, 3DinAction). Results demonstrate that temporal smoothing provides a significant performance boost across all per-frame approaches. While PointNet++ with temporal smoothing achieves the highest top-1 accuracy (52.98%), PSTNet leads in mAP (0.4024). A secondary clustering experiment decouples spatial and temporal representation power by evaluating performance on 12 verb and 22 noun classes, revealing that verbs are inherently more difficult to recognize than nouns because they require the accumulation of sequence information.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Overview of the IKEA Ego 3D dataset. The dataset includes 174 assembly sequences captured using a Microsoft HoloLens 2. The captured RGB and Depth streams are labelled with 56 action labels per frame. The data is then aligned and synced to form 3D point cloud sequences that are the input to 3D action recognition algorithms.",
      "relevance": "Illustrates the end-to-end data processing pipeline, from sensor capture to the synchronized 3D point cloud sequences that serve as the input for the benchmarked algorithms."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 2",
      "caption": "Action recognition results on IKEA Ego 3D. Comparing between recent state-of-the-art approaches using frame accuracy (top1 and top3), macro recall and mAP metrics.",
      "relevance": "The primary benchmark table showing the performance of various 3D action recognition methods on the new dataset."
    },
    {
      "ref": "Table 3",
      "caption": "Noun recognition results. We cluster the action classes by nouns and report the performance of state-of-the-art approaches. This experiment demonstrates the spatial quality of the methods (how well they capture objects).",
      "relevance": "Evaluates the spatial representation capabilities of the models by measuring their ability to identify the assembly components (nouns)."
    },
    {
      "ref": "Table 4",
      "caption": "Verb recognition results. We cluster the action classes by verbs and report the performance of state-of-the-art approaches. This experiment demonstrates the temporal quality of the methods (how well they distinguish motions).",
      "relevance": "Evaluates the temporal representation capabilities of the models by measuring their ability to distinguish different assembly motions (verbs)."
    }
  ],
  "key_equations": []
}
{
  "extracted_content": "The benchmark results reveal that incorporating naive temporal smoothing (+TS) leads to a significant performance boost across all per-frame architectures, confirming that temporal information is essential for action inference in 3D point clouds. Surprisingly, PointNet++ with temporal smoothing emerges as the best-performing method in terms of top-1 accuracy, outperforming more complex spatio-temporal models. Among the specialized action recognition methods, PSTNet demonstrates superior performance compared to 3DinAction on this specific dataset. The authors attribute 3DinAction's relative underperformance to its t-patch construction method, which is prone to collapsing when faced with the large, non-action-related head and sensor motions inherent in ego-view data. This suggests that current specialized 3D action recognition methods may need to improve their global representation capabilities to better handle dynamic ego-centric perspectives.",
  "key_figures": [],
  "key_tables": [
    {
      "ref": "Table 2",
      "caption": "Action recognition results on IKEA Ego 3D. Comparing between recent state-of-the-art approaches using frame accuracy (top1 and top3), macro recall and mAP metrics.",
      "relevance": "Provides the quantitative basis for the analysis of the performance boost gained from temporal smoothing and the comparison between specialized spatio-temporal models like PSTNet and 3DinAction."
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
  "extracted_content": "The clustering experiment decouples spatial and temporal representation power by grouping the 56 atomic actions into 12 verb and 22 noun classes. A primary insight is that nouns are significantly easier to recognize than verbs across all architectures, as assembly components (nouns) can often be identified from static spatial geometry. In contrast, verbs (motions) are inherently more difficult to recognize because they require the accumulation of temporal sequence information. Per-frame methods show a notable performance boost in noun recognition, indicating they are adept at capturing global geometric representations even without temporal context. The results suggest that while spatial features are sufficient for identifying objects, temporal modeling is the critical driver for distinguishing between different assembly motions.",
  "key_figures": [
    {
      "ref": "Figure 5",
      "caption": "Duration statistics. Sequence (a) and action (b) duration distributions in the IKEA Ego 3D dataset.",
      "relevance": "Provides statistical context for the difficulty of verb recognition; the distribution of action durations (5b) supports the claim that verbs require accumulating sequence information over time."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 3",
      "caption": "Noun recognition results. We cluster the action classes by nouns and report the performance of state-of-the-art approaches. This experiment demonstrates the spatial quality of the methods (how well they capture objects).",
      "relevance": "Quantifies the models' spatial representation capabilities, showing that identifying the 'what' (object) is significantly easier than identifying the full atomic action."
    },
    {
      "ref": "Table 4",
      "caption": "Verb recognition results. We cluster the action classes by verbs and report the performance of state-of-the-art approaches. This experiment demonstrates the temporal quality of the methods (how well they distinguish motions).",
      "relevance": "Serves as the primary evidence for the temporal quality of the methods, highlighting that motion-based classes are the main bottleneck in action recognition performance."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "Section 4.3"
  ]
}"""

Token usage so far: 215605 prompt tokens, 14560 completion tokens

Cost so far: $2.59285

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "The clustering experiment decouples spatial and temporal representation power by grouping the 56 atomic actions into 12 verb and 22 noun classes. A primary insight is that nouns are significantly easier to recognize than verbs across all architectures, as assembly components (nouns) can often be identified from static spatial geometry. In contrast, verbs (motions) are inherently more difficult to recognize because they require the accumulation of temporal sequence information. Per-frame methods show a notable performance boost in noun recognition, indicating they are adept at capturing global geometric representations even without temporal context. The results suggest that while spatial features are sufficient for identifying objects, temporal modeling is the critical driver for distinguishing between different assembly motions.",
  "key_figures": [
    {
      "ref": "Figure 5",
      "caption": "Duration statistics. Sequence (a) and action (b) duration distributions in the IKEA Ego 3D dataset.",
      "relevance": "Provides statistical context for the difficulty of verb recognition; the distribution of action durations (5b) supports the claim that verbs require accumulating sequence information over time."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 3",
      "caption": "Noun recognition results. We cluster the action classes by nouns and report the performance of state-of-the-art approaches. This experiment demonstrates the spatial quality of the methods (how well they capture objects).",
      "relevance": "Quantifies the models' spatial representation capabilities, showing that identifying the 'what' (object) is significantly easier than identifying the full atomic action."
    },
    {
      "ref": "Table 4",
      "caption": "Verb recognition results. We cluster the action classes by verbs and report the performance of state-of-the-art approaches. This experiment demonstrates the temporal quality of the methods (how well they distinguish motions).",
      "relevance": "Serves as the primary evidence for the temporal quality of the methods, highlighting that motion-based classes are the main bottleneck in action recognition performance."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "Section 4.3"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 8,
  "title": "Noun and Verb Clustering Insights",
  "summary": "Presents findings from decoupling spatial and temporal power, revealing that verbs are inherently harder to recognize than nouns and rely more heavily on temporal sequence information.",
  "paper_section": "4.3 Noun and Verb clustering experiment",
  "narrative_role": "results",
  "duration_stat": {
    "min": 8.0,
    "max": 14.0,
    "avg": 10.0
  }
}

Reference style advice:
Reference Layouts for 'results' section from similar papers:
- Example 1: The slide consists of a single, large 3D figure centered on a plain white background. There is no title, heading, or any text present on the slide. The figure is a point-cloud or voxel-based representation of a human body, constructed from many small spheres. The model is color-coded to show different segments: the head, torso, and limbs are primarily a tan/brown color. Specific parts are highlighted with distinct colors: a circular area on the abdomen is light pink, the right hand is purple, the left hand is magenta, the right foot is mint green, and the left foot is cyan. The layout is extremely minimalist with zero text density, focusing entirely on the visual data representation.
- Example 2: The slide has a clean, minimalist layout with a large title 'Scaling analysis' positioned at the top-left. The main content is a large line chart centered below the title, occupying most of the slide's area. The chart plots 'Zero-shot mIoU' on the vertical axis against 'Training Object Categories' on the horizontal axis. The data is represented by blue circular markers connected by a line, showing a clear upward trend as the number of categories increases. Two specific data points are emphasized with color-coded labels: a red point at the lower end of the scale labeled 'N Categories = Existing Datasets Combined' and a green point at the highest end labeled 'N Categories = Ours'. The background is plain white with light gray grid lines on the chart. A circular video overlay of the presenter is located in the bottom-right corner. The text density is light, prioritizing the visual data analysis.
- Example 3: The slide features a large, bold title 'Results - DFAUST' positioned at the top-left, separated from the main content by a thin horizontal line. The main body is organized into two columns. The left column contains a large table comparing various methods, such as PointNet and Set Transformer, against the proposed 'Ours' method. The table includes columns for 'Method', 'Frame acc. (top 1 and top 3)', and 'mAP', with the best results highlighted in bold and underlined. The right column contains a stacked bar chart showing the distribution of frames across different action categories (e.g., 'hips', 'knees', 'punching'). The chart uses a blue and orange color scheme to distinguish between 'train' and 'test' datasets. A footer at the bottom left provides the presentation context, including the event 'CVPR 2024 Highlight' and the presenter's name. The slide has a clean white background and moderate text density.
- Example 4: The slide features a large, bold title 'Scaling analysis' positioned in the top-left corner. The main content is a large line graph centered on the slide. The graph's y-axis is labeled 'Zero-shot mIoU' and the x-axis is labeled 'Training Object Categories'. The graph shows a blue line connecting several data points represented by circles. One data point at the lower end of the scale is highlighted in red with a corresponding red text label 'N Categories = Existing Datasets Combined'. The final data point at the highest end of the scale is highlighted in green with a green text label 'N Categories = Ours'. In the bottom-right corner, there is a circular inset video of the presenter. The slide has a clean white background with light text density, focusing entirely on the scaling trend shown in the chart.
- Example 5: The slide features a large, serif-font title 'Quantitative results' positioned at the top left. The main body of the slide is composed of two large, horizontally-oriented tables stacked vertically. The first table presents 'Reconstruction results on 7-Scenes dataset' (as indicated by the caption centered below it) and compares several methods across seven specific scenes, an average, and an FPS metric. The second table, titled 'Reconstruction results on Replica dataset' below it, follows a similar format, comparing methods across nine different rooms/offices. Both tables use a grid-like structure where rows represent different algorithms (e.g., DUSt3R, MAST3R, SLAM3R) and columns represent datasets or performance metrics. Numerical values for Accuracy and Completeness are shown in each cell, with the best results highlighted in bold. The 'FPS' column on the far right of both tables uses color-coded backgrounds—red for slow performance (\<1 FPS), light green for moderate (~24-25 FPS), and bright green for high performance (\>50 FPS). The slide has a clean white background and a high text density due to the extensive numerical data.

Duration statistics for this section (from references): min=1.0s, max=36.0s, avg=9.5s.

Your job is to decide the **visual layout** for this slide. Do NOT decide builds or animations — those will be planned later.

## CHOOSE THE BEST LAYOUT

Pick the layout template that best suits the content. Common templates include (but you are NOT limited to these):
- `two_col_fig_left` — Figure on left, bullets on right. Best for: method diagrams, architecture figures.
- `two_col_fig_right` — Bullets on left, figure on right. Best for: motivation slides with illustrative figures.
- `full_fig_with_callouts` — Large figure with small bullet callouts below. Best for: results, data visualizations.
- `one_col_bullets` — Full-width bullets, no figure. Best for: text-heavy overview or summary slides.

If none of these fit, invent a descriptive template name and define its regions.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "bullets": {"x": 0.55, "y": 0.25, "w": 0.4, "h": 0.6}
  },
  "has_figure": true,
  "style_rationale": "Two-column layout with figure on left is ideal for showing the architecture diagram alongside explanatory bullets."
}

## STRICT RULES:
1. **Region keys**: Only use `title`, `bullets`, `figure` as region keys. Do NOT invent keys like `callout_1`, `table`, etc.
2. **Coordinates**: All x/y/w/h values must be normalized (0.0 to 1.0). Regions must not overlap.
3. **has_figure**: Set to `true` only if the content summary has relevant figures. If no figure is available, omit `figure` from regions.
4. **No builds**: Do NOT include `build_skeleton`, `expected_build_steps`, or any animation information.
5. Output ONLY valid JSON, no markdown fences, no explanation.


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
  "style_rationale": "This layout places the core qualitative insights on the left, allowing the presenter to explain the decoupling of spatial and temporal power. The right side is dedicated to a visual comparison of the data from Tables 3 and 4 (Noun vs. Verb recognition), providing immediate quantitative evidence for the claim that verbs are harder to recognize and require temporal context."
}"""

Token usage so far: 223030 prompt tokens, 14834 completion tokens

Cost so far: $2.67532

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "The clustering experiment decouples spatial and temporal representation power by grouping the 56 atomic actions into 12 verb and 22 noun classes. A primary insight is that nouns are significantly easier to recognize than verbs across all architectures, as assembly components (nouns) can often be identified from static spatial geometry. In contrast, verbs (motions) are inherently more difficult to recognize because they require the accumulation of temporal sequence information. Per-frame methods show a notable performance boost in noun recognition, indicating they are adept at capturing global geometric representations even without temporal context. The results suggest that while spatial features are sufficient for identifying objects, temporal modeling is the critical driver for distinguishing between different assembly motions.",
  "key_figures": [
    {
      "ref": "Figure 5",
      "caption": "Duration statistics. Sequence (a) and action (b) duration distributions in the IKEA Ego 3D dataset.",
      "relevance": "Provides statistical context for the difficulty of verb recognition; the distribution of action durations (5b) supports the claim that verbs require accumulating sequence information over time."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 3",
      "caption": "Noun recognition results. We cluster the action classes by nouns and report the performance of state-of-the-art approaches. This experiment demonstrates the spatial quality of the methods (how well they capture objects).",
      "relevance": "Quantifies the models' spatial representation capabilities, showing that identifying the 'what' (object) is significantly easier than identifying the full atomic action."
    },
    {
      "ref": "Table 4",
      "caption": "Verb recognition results. We cluster the action classes by verbs and report the performance of state-of-the-art approaches. This experiment demonstrates the temporal quality of the methods (how well they distinguish motions).",
      "relevance": "Serves as the primary evidence for the temporal quality of the methods, highlighting that motion-based classes are the main bottleneck in action recognition performance."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "Section 4.3"
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
  "style_rationale": "This layout places the core qualitative insights on the left, allowing the presenter to explain the decoupling of spatial and temporal power. The right side is dedicated to a visual comparison of the data from Tables 3 and 4 (Noun vs. Verb recognition), providing immediate quantitative evidence for the claim that verbs are harder to recognize and require temporal context."
}

Scene context:
{
  "scene_id": 8,
  "title": "Noun and Verb Clustering Insights",
  "summary": "Presents findings from decoupling spatial and temporal power, revealing that verbs are inherently harder to recognize than nouns and rely more heavily on temporal sequence information.",
  "paper_section": "4.3 Noun and Verb clustering experiment",
  "narrative_role": "results",
  "duration_stat": {
    "min": 8.0,
    "max": 14.0,
    "avg": 10.0
  }
}

## Previous Content
The following content was drafted for the immediately preceding scenes.
You MUST NOT repeat the exact text content or claims from these previous scenes in your current draft.

{
  "bullets": [
    "Temporal smoothing (+TS) significantly boosts performance across all architectures",
    "PointNet++ with smoothing achieves the highest top-1 accuracy",
    "PSTNet outperforms 3DinAction on ego-view sensor motion challenges",
    "Results suggest a need for improved global representations in dynamic 3D scenes"
  ],
  "audio_content": "Benchmark results show that temporal smoothing significantly boosts performance, with PointNet plus plus emerging as a surprisingly strong baseline. While PSTNet performs well, 3DinAction struggles with the head motion inherent in ego-view data. This highlights the need for models that better handle dynamic, ego-centric perspectives."
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
  "source": ["Figure 1", "Section 3.1"],
  "prompt": "Visual description of the scene for generation"
}

## STRICT RULES:
1. **Number of bullets**: Write 2-4 concise, impactful bullets that cover the key points from the extracted content.
2. **Figure reference**: ONLY use figures listed in the content summary's `key_figures`. Do NOT invent figure references. If the style plan has `has_figure: false`, omit `figure` entirely.
3. **Bullet text**: Each bullet should be concise (under 15 words preferred), impactful, and directly derived from `extracted_content`. Not a copy — a focused summary.
4. **audio_content**: Natural narration covering all bullet points. 
5. **duration_sec**: First, draft the `audio_content`. Then, CALCULATE the duration: `duration_sec = word_count_of_audio / 2.5`. Do NOT guess. If the stats say 8s but you wrote 40 words, `duration_sec` MUST be 16.0.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""```json
{
  "title": "Noun and Verb Recognition Insights",
  "audio_content": "Clustering actions into nouns and verbs shows that objects are easier to recognize than motions. Nouns rely on static geometry, while verbs require temporal sequences. This confirms that temporal modeling is the essential factor for distinguishing complex assembly actions.",
  "duration_sec": 14.4,
  "bullets": [
    "Nouns are easily identified through static spatial geometry",
    "Verbs are inherently harder, requiring temporal sequence accumulation",
    "Temporal modeling is the critical driver for distinguishing assembly motions"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 5",
    "caption": "Duration statistics for sequences and actions in the IKEA Ego 3D dataset"
  },
  "source": [
    "Section 4.3",
    "Figure 5"
  ],
  "prompt": "A slide with the title 'Noun and Verb Recognition Insights'. On the left, three bullet points explain that nouns are easier to recognize than verbs due to static geometry versus temporal sequences. On the right, Figure 5 from the paper shows the duration distributions of sequences and actions, providing context for the temporal complexity of assembly tasks."
}
```"""

Token usage so far: 229812 prompt tokens, 15116 completion tokens

Cost so far: $2.75160

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "Noun and Verb Recognition Insights",
  "audio_content": "Clustering actions into nouns and verbs shows that objects are easier to recognize than motions. Nouns rely on static geometry, while verbs require temporal sequences. This confirms that temporal modeling is the essential factor for distinguishing complex assembly actions.",
  "duration_sec": 14.4,
  "bullets": [
    "Nouns are easily identified through static spatial geometry",
    "Verbs are inherently harder, requiring temporal sequence accumulation",
    "Temporal modeling is the critical driver for distinguishing assembly motions"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 5",
    "caption": "Duration statistics for sequences and actions in the IKEA Ego 3D dataset"
  },
  "source": [
    "Section 4.3",
    "Figure 5"
  ],
  "prompt": "A slide with the title 'Noun and Verb Recognition Insights'. On the left, three bullet points explain that nouns are easier to recognize than verbs due to static geometry versus temporal sequences. On the right, Figure 5 from the paper shows the duration distributions of sequences and actions, providing context for the temporal complexity of assembly tasks."
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
1. **Build count**: `expected_build_steps` = 1 + number_of_bullets. Build 0 shows title (and figure if present), then one build per bullet.
2. **One bullet per build**: After build 0, each build reveals exactly ONE bullet. `bullets[0]` in build 1, `bullets[1]` in build 2, etc.
3. **Build 0**: Always shows `title` (and `figure` if present). Never shows bullets in build 0.
4. **Audio segments**: Split the `audio_content` from the draft into segments. Each build's `audio_segment` must be non-empty and correspond to what that build reveals.
5. **Bullet ordering**: Assign bullets to builds in the order that creates the best storytelling flow for the audience.
6. **time_offset_sec**: Space evenly across the total time. For N builds over T seconds: offsets at 0, T/N, 2T/N, etc.
7. **visual_emphasis**: Always set to empty list `[]`.
8. **Action targets**: Only use targets that exist in `elements`: `title`, `figure`, `bullets[0]`, `bullets[1]`, etc.
9. **elements**: Copy the drafted title, figure, and bullets exactly — do not modify the text content.
10. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "style": "Slides",
  "expected_build_steps": 4,
  "elements": {
    "title": "Noun and Verb Recognition Insights",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 5",
      "caption": "Duration statistics for sequences and actions in the IKEA Ego 3D dataset"
    },
    "bullets": [
      "Nouns are easily identified through static spatial geometry",
      "Verbs are inherently harder, requiring temporal sequence accumulation",
      "Temporal modeling is the critical driver for distinguishing assembly motions"
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
      "audio_segment": "Clustering actions into nouns and verbs shows that objects are easier to recognize than motions.",
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
      "audio_segment": "Nouns rely on static geometry,",
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
      "audio_segment": "while verbs require temporal sequences.",
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
      "audio_segment": "This confirms that temporal modeling is the essential factor for distinguishing complex assembly actions.",
      "visual_emphasis": []
    }
  ]
}"""

Token usage so far: 236286 prompt tokens, 15658 completion tokens

Cost so far: $2.83260

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 9,
  "title": "Conclusion and Future Directions",
  "summary": "Summarizes the dataset's role as a challenging testbed for 3D computer vision and suggests future research in multi-modal fusion, action anticipation, and AR human assistive systems.",
  "paper_section": "6. Conclusions",
  "narrative_role": "results",
  "duration_stat": {
    "min": 6.0,
    "max": 10.0,
    "avg": 8.0
  }
}

## Previous Scenes Memory
The following content was extracted for the immediately preceding scenes. **This is provided as a memory of what the audience has JUST seen.**
You MUST NOT repeat the claims, figures, tables, or equations from these previous scenes in your current extraction, to ensure the presentation maintains forward momentum without redundant slides.
If you must reference the exactly same figure/table, the 'relevance' MUST be clearly unique to avoid narrative duplication.

{
  "extracted_content": "The benchmark results reveal that incorporating naive temporal smoothing (+TS) leads to a significant performance boost across all per-frame architectures, confirming that temporal information is essential for action inference in 3D point clouds. Surprisingly, PointNet++ with temporal smoothing emerges as the best-performing method in terms of top-1 accuracy, outperforming more complex spatio-temporal models. Among the specialized action recognition methods, PSTNet demonstrates superior performance compared to 3DinAction on this specific dataset. The authors attribute 3DinAction's relative underperformance to its t-patch construction method, which is prone to collapsing when faced with the large, non-action-related head and sensor motions inherent in ego-view data. This suggests that current specialized 3D action recognition methods may need to improve their global representation capabilities to better handle dynamic ego-centric perspectives.",
  "key_figures": [],
  "key_tables": [
    {
      "ref": "Table 2",
      "caption": "Action recognition results on IKEA Ego 3D. Comparing between recent state-of-the-art approaches using frame accuracy (top1 and top3), macro recall and mAP metrics.",
      "relevance": "Provides the quantitative basis for the analysis of the performance boost gained from temporal smoothing and the comparison between specialized spatio-temporal models like PSTNet and 3DinAction."
    }
  ],
  "key_equations": []
}
{
  "extracted_content": "The clustering experiment decouples spatial and temporal representation power by grouping the 56 atomic actions into 12 verb and 22 noun classes. A primary insight is that nouns are significantly easier to recognize than verbs across all architectures, as assembly components (nouns) can often be identified from static spatial geometry. In contrast, verbs (motions) are inherently more difficult to recognize because they require the accumulation of temporal sequence information. Per-frame methods show a notable performance boost in noun recognition, indicating they are adept at capturing global geometric representations even without temporal context. The results suggest that while spatial features are sufficient for identifying objects, temporal modeling is the critical driver for distinguishing between different assembly motions.",
  "key_figures": [
    {
      "ref": "Figure 5",
      "caption": "Duration statistics. Sequence (a) and action (b) duration distributions in the IKEA Ego 3D dataset.",
      "relevance": "Provides statistical context for the difficulty of verb recognition; the distribution of action durations (5b) supports the claim that verbs require accumulating sequence information over time."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 3",
      "caption": "Noun recognition results. We cluster the action classes by nouns and report the performance of state-of-the-art approaches. This experiment demonstrates the spatial quality of the methods (how well they capture objects).",
      "relevance": "Quantifies the models' spatial representation capabilities, showing that identifying the 'what' (object) is significantly easier than identifying the full atomic action."
    },
    {
      "ref": "Table 4",
      "caption": "Verb recognition results. We cluster the action classes by verbs and report the performance of state-of-the-art approaches. This experiment demonstrates the temporal quality of the methods (how well they distinguish motions).",
      "relevance": "Serves as the primary evidence for the temporal quality of the methods, highlighting that motion-based classes are the main bottleneck in action recognition performance."
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
  "extracted_content": "The IKEA Ego 3D dataset is established as a large-scale, annotated resource for fine-grained action recognition from ego-view 3D point clouds, specifically designed to challenge algorithms with simultaneous sensor and action motion. Future research directions enabled by this dataset include the exploration of multi-modal fusion between point clouds and RGB streams, as well as advanced temporal tasks like action anticipation and forecasting. Practical applications for this work focus on Augmented Reality (AR) human assistive systems that provide real-time instructional feedback and error prevention during complex assembly tasks in both industrial and domestic environments. Ultimately, the dataset provides a foundation for deeper perceptual understanding of human-object interactions and geometric consistency in lengthy, real-world activities.",
  "key_figures": [],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Section 5",
    "Section 6"
  ]
}"""

Token usage so far: 242975 prompt tokens, 15860 completion tokens

Cost so far: $2.90555

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "The IKEA Ego 3D dataset is established as a large-scale, annotated resource for fine-grained action recognition from ego-view 3D point clouds, specifically designed to challenge algorithms with simultaneous sensor and action motion. Future research directions enabled by this dataset include the exploration of multi-modal fusion between point clouds and RGB streams, as well as advanced temporal tasks like action anticipation and forecasting. Practical applications for this work focus on Augmented Reality (AR) human assistive systems that provide real-time instructional feedback and error prevention during complex assembly tasks in both industrial and domestic environments. Ultimately, the dataset provides a foundation for deeper perceptual understanding of human-object interactions and geometric consistency in lengthy, real-world activities.",
  "key_figures": [],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Section 5",
    "Section 6"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 9,
  "title": "Conclusion and Future Directions",
  "summary": "Summarizes the dataset's role as a challenging testbed for 3D computer vision and suggests future research in multi-modal fusion, action anticipation, and AR human assistive systems.",
  "paper_section": "6. Conclusions",
  "narrative_role": "results",
  "duration_stat": {
    "min": 6.0,
    "max": 10.0,
    "avg": 8.0
  }
}

Reference style advice:
Reference Layouts for 'results' section from similar papers:
- Example 1: The slide features a centered title at the top in a black serif font. The main content area is divided into ten distinct rectangular panels of varying sizes, separated by dashed gray lines. Each panel contains a set of images—including photographs, sketches, and line drawings—accompanied by small wireframe diagrams representing camera poses (frustums) and coordinate axes. Most panels show pairs of images (e.g., statues, monuments, or portraits) with their estimated relative poses. The largest panel, located in the bottom right, displays five different views of a Nike backpack arranged around a central 3D coordinate system and camera pose visualization. Images are typically outlined with thin green or orange borders. The background is plain white, and the text density is very light, emphasizing qualitative visual results.
- Example 2: The slide consists of a single, large 3D figure centered on a plain white background. There is no title, heading, or any text present on the slide. The figure is a point-cloud or voxel-based representation of a human body, constructed from many small spheres. The model is color-coded to show different segments: the head, torso, and limbs are primarily a tan/brown color. Specific parts are highlighted with distinct colors: a circular area on the abdomen is light pink, the right hand is purple, the left hand is magenta, the right foot is mint green, and the left foot is cyan. The layout is extremely minimalist with zero text density, focusing entirely on the visual data representation.
- Example 3: The slide follows a two-column structure beneath a large, bold title at the top left, which is separated from the main content by a full-width horizontal line. The left column is occupied by a large 3D point cloud visualization showing a person in a blue jacket assembling a white table in a room with a sofa and a patterned rug. The right column contains a quantitative results table. This table lists various methods in the first column and their performance across metrics like 'Frame acc.' (subdivided into top 1, top 3, and macro) and 'mAP'. The table uses horizontal rules to separate the header, baseline methods, and the proposed 'Ours' methods, with the best results highlighted in bold. A footer at the bottom left provides the paper's highlight status at CVPR 2024 and the author's name. The slide has a clean white background and moderate text density.
- Example 4: The slide features a large, serif-font title 'Visualization' positioned at the top left. The main body of the slide is organized into two side-by-side rectangular panels, each framed by a thin light-blue border, representing a comparison between two different scenarios. The left panel is captioned 'Synthetic indoor video' and contains three sub-elements: a small 'RGB input' image of a room, a small 'Local 3D points predicted by the I2P model' visualization (a colorful depth-like map), and a larger 'Global 3D points predicted by the L2W model' showing a 3D point cloud reconstruction. The right panel is captioned 'Self-captured outdoor video' and mirrors this structure with an outdoor building scene, including its corresponding RGB input, local 3D point map, and global 3D point cloud. The text density is light, with labels placed directly beneath their respective images. The background is a clean, solid white.
- Example 5: The slide features a large, bold title positioned at the top-left against a plain white background. Below the title, the main content is organized into three side-by-side columns, each containing a 3D visualization of a human body model. Each model is labeled with a centered heading directly above it: 'Jumping jacks' on the left, 'Knee' in the center, and 'Hips' on the right. The human figures are represented as point clouds or sphere-based meshes, colored with a GradCAM heatmap where red indicates high activation and blue indicates low activation. The 'Jumping jacks' figure shows red highlights on the hands; the 'Knee' figure shows a red highlight on a raised knee; and the 'Hips' figure shows red highlights around the pelvic region. The overall text density is light, prioritizing visual qualitative results over textual explanation.

Duration statistics for this section (from references): min=1.0s, max=36.0s, avg=9.5s.

Your job is to decide the **visual layout** for this slide. Do NOT decide builds or animations — those will be planned later.

## CHOOSE THE BEST LAYOUT

Pick the layout template that best suits the content. Common templates include (but you are NOT limited to these):
- `two_col_fig_left` — Figure on left, bullets on right. Best for: method diagrams, architecture figures.
- `two_col_fig_right` — Bullets on left, figure on right. Best for: motivation slides with illustrative figures.
- `full_fig_with_callouts` — Large figure with small bullet callouts below. Best for: results, data visualizations.
- `one_col_bullets` — Full-width bullets, no figure. Best for: text-heavy overview or summary slides.

If none of these fit, invent a descriptive template name and define its regions.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "bullets": {"x": 0.55, "y": 0.25, "w": 0.4, "h": 0.6}
  },
  "has_figure": true,
  "style_rationale": "Two-column layout with figure on left is ideal for showing the architecture diagram alongside explanatory bullets."
}

## STRICT RULES:
1. **Region keys**: Only use `title`, `bullets`, `figure` as region keys. Do NOT invent keys like `callout_1`, `table`, etc.
2. **Coordinates**: All x/y/w/h values must be normalized (0.0 to 1.0). Regions must not overlap.
3. **has_figure**: Set to `true` only if the content summary has relevant figures. If no figure is available, omit `figure` from regions.
4. **No builds**: Do NOT include `build_skeleton`, `expected_build_steps`, or any animation information.
5. Output ONLY valid JSON, no markdown fences, no explanation.


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
      "w": 0.45,
      "h": 0.7
    },
    "bullets": {
      "x": 0.55,
      "y": 0.2,
      "w": 0.4,
      "h": 0.7
    }
  },
  "has_figure": true,
  "style_rationale": "A two-column layout with the figure on the left is ideal for a concluding slide. It allows for a representative visualization of the IKEA Ego 3D dataset (such as the point cloud actions from Figure 3) to remain on screen while the right side summarizes the key takeaways and future research directions like multi-modal fusion and AR applications."
}"""

Token usage so far: 250046 prompt tokens, 16136 completion tokens

Cost so far: $2.98454

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "The IKEA Ego 3D dataset is established as a large-scale, annotated resource for fine-grained action recognition from ego-view 3D point clouds, specifically designed to challenge algorithms with simultaneous sensor and action motion. Future research directions enabled by this dataset include the exploration of multi-modal fusion between point clouds and RGB streams, as well as advanced temporal tasks like action anticipation and forecasting. Practical applications for this work focus on Augmented Reality (AR) human assistive systems that provide real-time instructional feedback and error prevention during complex assembly tasks in both industrial and domestic environments. Ultimately, the dataset provides a foundation for deeper perceptual understanding of human-object interactions and geometric consistency in lengthy, real-world activities.",
  "key_figures": [],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Section 5",
    "Section 6"
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
      "w": 0.45,
      "h": 0.7
    },
    "bullets": {
      "x": 0.55,
      "y": 0.2,
      "w": 0.4,
      "h": 0.7
    }
  },
  "has_figure": true,
  "style_rationale": "A two-column layout with the figure on the left is ideal for a concluding slide. It allows for a representative visualization of the IKEA Ego 3D dataset (such as the point cloud actions from Figure 3) to remain on screen while the right side summarizes the key takeaways and future research directions like multi-modal fusion and AR applications."
}

Scene context:
{
  "scene_id": 9,
  "title": "Conclusion and Future Directions",
  "summary": "Summarizes the dataset's role as a challenging testbed for 3D computer vision and suggests future research in multi-modal fusion, action anticipation, and AR human assistive systems.",
  "paper_section": "6. Conclusions",
  "narrative_role": "results",
  "duration_stat": {
    "min": 6.0,
    "max": 10.0,
    "avg": 8.0
  }
}

## Previous Content
The following content was drafted for the immediately preceding scenes.
You MUST NOT repeat the exact text content or claims from these previous scenes in your current draft.

{
  "bullets": [
    "Nouns are easily identified through static spatial geometry",
    "Verbs are inherently harder, requiring temporal sequence accumulation",
    "Temporal modeling is the critical driver for distinguishing assembly motions"
  ],
  "audio_content": "Clustering actions into nouns and verbs shows that objects are easier to recognize than motions. Nouns rely on static geometry, while verbs require temporal sequences. This confirms that temporal modeling is the essential factor for distinguishing complex assembly actions."
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
  "source": ["Figure 1", "Section 3.1"],
  "prompt": "Visual description of the scene for generation"
}

## STRICT RULES:
1. **Number of bullets**: Write 2-4 concise, impactful bullets that cover the key points from the extracted content.
2. **Figure reference**: ONLY use figures listed in the content summary's `key_figures`. Do NOT invent figure references. If the style plan has `has_figure: false`, omit `figure` entirely.
3. **Bullet text**: Each bullet should be concise (under 15 words preferred), impactful, and directly derived from `extracted_content`. Not a copy — a focused summary.
4. **audio_content**: Natural narration covering all bullet points. 
5. **duration_sec**: First, draft the `audio_content`. Then, CALCULATE the duration: `duration_sec = word_count_of_audio / 2.5`. Do NOT guess. If the stats say 8s but you wrote 40 words, `duration_sec` MUST be 16.0.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "title": "Conclusion and Future Directions",
  "audio_content": "The IKEA Ego 3D dataset establishes a challenging new benchmark for fine-grained action recognition. This resource paves the way for future research in multi-modal fusion and action forecasting, ultimately supporting AR assistive systems that provide real-time feedback and error prevention during complex assembly tasks.",
  "duration_sec": 11.2,
  "bullets": [
    "Challenging testbed for ego-view 3D action recognition",
    "Enables research in multi-modal fusion and action forecasting",
    "Foundation for AR assistive systems and real-time feedback"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 3",
    "caption": "Visualizing RGB, 3D point clouds, and action labels for assembly tasks"
  },
  "source": [
    "Section 5",
    "Section 6",
    "Figure 3"
  ],
  "prompt": "A concluding slide with a two-column layout. On the left, Figure 3 from the paper is displayed, showing the synchronization of RGB video, 3D point clouds, and action labels like 'spin screwdriver' and 'use drill'. On the right, bullet points summarize the dataset's role as a benchmark and its future applications in AR and multi-modal computer vision."
}"""

Token usage so far: 256508 prompt tokens, 16447 completion tokens

Cost so far: $3.05849

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "Conclusion and Future Directions",
  "audio_content": "The IKEA Ego 3D dataset establishes a challenging new benchmark for fine-grained action recognition. This resource paves the way for future research in multi-modal fusion and action forecasting, ultimately supporting AR assistive systems that provide real-time feedback and error prevention during complex assembly tasks.",
  "duration_sec": 11.2,
  "bullets": [
    "Challenging testbed for ego-view 3D action recognition",
    "Enables research in multi-modal fusion and action forecasting",
    "Foundation for AR assistive systems and real-time feedback"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 3",
    "caption": "Visualizing RGB, 3D point clouds, and action labels for assembly tasks"
  },
  "source": [
    "Section 5",
    "Section 6",
    "Figure 3"
  ],
  "prompt": "A concluding slide with a two-column layout. On the left, Figure 3 from the paper is displayed, showing the synchronization of RGB video, 3D point clouds, and action labels like 'spin screwdriver' and 'use drill'. On the right, bullet points summarize the dataset's role as a benchmark and its future applications in AR and multi-modal computer vision."
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
      "w": 0.45,
      "h": 0.7
    },
    "bullets": {
      "x": 0.55,
      "y": 0.2,
      "w": 0.4,
      "h": 0.7
    }
  },
  "has_figure": true,
  "total_time_sec": 11.2
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
1. **Build count**: `expected_build_steps` = 1 + number_of_bullets. Build 0 shows title (and figure if present), then one build per bullet.
2. **One bullet per build**: After build 0, each build reveals exactly ONE bullet. `bullets[0]` in build 1, `bullets[1]` in build 2, etc.
3. **Build 0**: Always shows `title` (and `figure` if present). Never shows bullets in build 0.
4. **Audio segments**: Split the `audio_content` from the draft into segments. Each build's `audio_segment` must be non-empty and correspond to what that build reveals.
5. **Bullet ordering**: Assign bullets to builds in the order that creates the best storytelling flow for the audience.
6. **time_offset_sec**: Space evenly across the total time. For N builds over T seconds: offsets at 0, T/N, 2T/N, etc.
7. **visual_emphasis**: Always set to empty list `[]`.
8. **Action targets**: Only use targets that exist in `elements`: `title`, `figure`, `bullets[0]`, `bullets[1]`, etc.
9. **elements**: Copy the drafted title, figure, and bullets exactly — do not modify the text content.
10. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "style": "Slides",
  "expected_build_steps": 4,
  "elements": {
    "title": "Conclusion and Future Directions",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 3",
      "caption": "Visualizing RGB, 3D point clouds, and action labels for assembly tasks"
    },
    "bullets": [
      "Challenging testbed for ego-view 3D action recognition",
      "Enables research in multi-modal fusion and action forecasting",
      "Foundation for AR assistive systems and real-time feedback"
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
      "audio_segment": "The IKEA Ego 3D dataset establishes a challenging new benchmark for fine-grained action recognition.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 2.8,
      "actions": [
        {"type": "fade_in", "target": "bullets[0]"}
      ],
      "audio_segment": "This resource paves the way for future research",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 5.6,
      "actions": [
        {"type": "fade_in", "target": "bullets[1]"}
      ],
      "audio_segment": "in multi-modal fusion and action forecasting,",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 8.4,
      "actions": [
        {"type": "fade_in", "target": "bullets[2]"}
      ],
      "audio_segment": "ultimately supporting AR assistive systems that provide real-time feedback and error prevention during complex assembly tasks.",
      "visual_emphasis": []
    }
  ]
}"""

Token usage so far: 263017 prompt tokens, 16970 completion tokens

Cost so far: $3.13927

