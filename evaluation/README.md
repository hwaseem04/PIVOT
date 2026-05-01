# Evaluation Pipeline

Evaluates video presentation quality by testing whether key information from the paper is preserved in the generated video.

## How It Works

1. **Generate questions** from the paper PDF (ground truth)
2. **Student LLM** answers those questions using only the video's extracted content (transcript, bullets, figures, tables)
3. **Judge LLM** scores the student's answers against ground truth

## Usage

### 1. Generate Questions

Input: directory of PDFs. Generates 5 easy, 10 medium, 20 hard questions per paper.

```bash
python -u evaluation/generate_questions_by_difficulty.py dataset/
```

Papers already present in the question files are skipped. Safe to re-run after adding new PDFs.

### 2. Student Evaluation

```bash
python evaluation/evaluate_extraction.py style_agent_output/federated
```

### 3. Judge Evaluation

```bash
python evaluation/judge.py style_agent_output/federated
```

### 4. Batch (runs steps 2+3 for all)

```bash
python evaluation/batch_evaluate.py style_agent_output/
```

## Question Categories

| Category | What it tests |
|---|---|
| **core_contribution** | Can the viewer identify the main problem and key innovation? |
| **methodology** | Does the video explain the technical approach, algorithms, and implementation? |
| **experimental_results** | Are datasets, metrics, results, and baseline comparisons conveyed? |
| **limitations** | Does the video mention acknowledged limitations and constraints? |
| **negative_traps** | Can the viewer correctly identify what the paper does NOT claim? Prevents false positives from generic answers. |

## Understanding the Report

### Per-Question Scores (0-10)

Each student answer is judged on three criteria:

| Metric | What it measures |
|---|---|
| **Accuracy** | Is the information in the answer factually correct? A high score means the video conveyed correct facts. A low score means the video introduced errors or the student misunderstood. |
| **Completeness** | Does the answer cover all key points from the ground truth? A high score means the video covered the topic thoroughly. A low score means important details were omitted. |
| **Relevance** | Is the answer focused on what was asked? A high score means the video content was well-organized and the student could find the right info. A low score suggests vague or off-topic coverage. |
| **Overall Score** | Combined judgment (0-10) considering all three criteria above. This is the primary metric for comparing methods. |

### Aggregated Metrics

#### `info_missing_rate`
Percentage of questions the student could not answer at all (`INSUFFICIENT_INFORMATION`). This is the most direct measure of information loss — it tells you what fraction of the paper's content is completely absent from the video.

- **0%** = The video covers everything tested
- **High %** = Significant information gaps in the video

#### `by_difficulty`
Scores broken down by easy / medium / hard. Expect scores to decrease with difficulty:

- **Easy** questions test surface-level facts (explicitly stated). Low scores here indicate fundamental coverage issues.
- **Medium** questions require connecting concepts across sections. Low scores suggest the video doesn't explain relationships well.
- **Hard** questions require deep comprehension, inference, and synthesis. Low scores are more acceptable — these test subtle details.

#### `by_category`
Scores broken down by the 5 question categories. This reveals which aspects of the paper the video covers well vs. poorly:

- Low `methodology` score → the video doesn't explain the technical approach well enough
- Low `experimental_results` score → results/tables/comparisons are not well conveyed
- Low `limitations` score → the video omits limitations (common, since videos tend to focus on positives)
- Low `negative_traps` score → the video is vague enough that a viewer might attribute false claims to the paper

### What "Good" Looks Like

| Metric | Weak | Acceptable | Strong |
|---|---|---|---|
| Overall Score | < 5.0 | 5.0 - 7.0 | > 7.0 |
| Info Missing Rate | > 30% | 10-30% | < 10% |
| Easy difficulty | < 6.0 | 6.0 - 8.0 | > 8.0 |
| Hard difficulty | < 4.0 | 4.0 - 6.0 | > 6.0 |

### Comparing Methods

When you have multiple runs for the same paper (e.g. `federated_baseline` vs `federated_veo`), compare:

1. **Overall score** — which method produces more informative videos?
2. **Info missing rate** — which method loses less information?
3. **Category breakdown** — does one method handle methodology better but miss experimental results?
4. **Difficulty breakdown** — does one method only handle easy facts, or does it preserve deeper content too?
