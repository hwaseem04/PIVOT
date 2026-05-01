import json
import sys
from pathlib import Path

# Add parent directory to path to import modules
sys.path.insert(0, str(Path(__file__).parent.parent))
from llms.gemini import GEMINI

def repair_json(s):
    """Attempt to repair common JSON truncation issues."""
    s = s.strip()
    if not s:
        return s
    
    # Count braces and brackets
    open_braces = s.count('{')
    close_braces = s.count('}')
    open_brackets = s.count('[')
    close_brackets = s.count(']')
    
    # If it ends abruptly inside a string
    # Check if last unescaped quote is open
    import re
    quotes = re.findall(r'(?<!\\)"', s)
    if len(quotes) % 2 != 0:
        s += '"'
    
    # Add missing closing braces/brackets
    while s.count('}') < s.count('{'):
        s += '}'
    while s.count(']') < s.count('['):
        s += ']'
        
    return s

CATEGORIZATION_PROMPT_TEMPLATE = """You are analyzing a research paper that has been divided into sections with summaries. Your task is to reorganize these sections into a standard structure.

CURRENT SECTIONS:
{sections_json}

STANDARD CATEGORIES (in order):
1. abstract - Paper abstract/summary
2. introduction - Introduction, motivation, background
3. method - Methodology, approach, proposed method, related work if it's foundational to the method
4. experiments - Experimental setup, datasets, implementation details
5. results - Results, findings, analysis, discussion
6. conclusion - Conclusion, future work, limitations
7. supplementary - Supplementary material (if exists)

YOUR TASK:
1. Analyze each section's content and determine which standard category it belongs to
2. If multiple sections belong to the same category, MERGE them by combining their content
3. If a section contains both experiments AND results, SPLIT it into two separate entries
4. DO NOT modify the actual content/text - only reorganize and categorize
5. If a section doesn't fit any category, assign it to the most appropriate one

CONCISENESS & SAFETY:
- BE CONCISE. Summarize the content to be high-level while preserving ALL LaTeX equations.
- Target roughly 200-400 words per category maximum to avoid response truncation.
- Ensure the JSON is complete and valid. DO NOT cut off the output.

OUTPUT FORMAT:
Return ONLY a JSON object mapping standard categories to their content. Example:
{{
  "abstract": "concise summary...",
  "introduction": "concise summary...",
  "method": "concise summary with equations...",
  "experiments": "concise summary...",
  "results": "concise summary...",
  "conclusion": "concise summary...",
  "supplementary": "concise summary if exists"
}}

IMPORTANT:
- Only include categories that have content
- Preserve the exact LaTeX equations but summarize the surrounding text to be more compact.
- RETURN ONLY THE JSON OBJECT.
- NO MARKDOWN WRAPPING (No ```).
- Ensure every quote and brace is closed.
"""


def categorize_sections(paper_data, gemini_client, max_retries=2):
    """
    Use Gemini to categorize and reorganize sections into standard structure.

    Args:
        paper_data: Dictionary with paper sections
        gemini_client: GEMINI client instance
        max_retries: Maximum number of retry attempts

    Returns:
        Dictionary with categorized sections
    """
    paper_name = paper_data.get("paper_name", "Unknown")
    sections = paper_data.get("sections", {})

    if not sections:
        print(f"  WARNING: No sections found in paper")
        return {}

    # Format sections for the prompt
    sections_json = json.dumps(sections, indent=2)
    base_prompt = CATEGORIZATION_PROMPT_TEMPLATE.format(sections_json=sections_json)
    prompt = base_prompt

    print(f"  Categorizing {len(sections)} sections...")

    for attempt in range(max_retries + 1):
        if attempt > 0:
            print(f"  Retry attempt {attempt}/{max_retries}...")

        # Query Gemini
        _, response = gemini_client.query(
            prompt=prompt
        )

        # Parse response
        try:
            # Deep clean the response
            cleaned_response = response.strip()
            
            # Remove markdown code blocks
            if "```" in cleaned_response:
                import re
                json_match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', cleaned_response, re.DOTALL)
                if json_match:
                    cleaned_response = json_match.group(1)
                else:
                    # Fallback: just strip the blocks
                    cleaned_response = cleaned_response.strip("`").strip()
                    if cleaned_response.startswith("json"):
                        cleaned_response = cleaned_response[4:].strip()

            # Attempt repair before first parse
            try:
                categorized = json.loads(cleaned_response)
            except json.JSONDecodeError:
                print("  Attempting to repair truncated JSON...")
                repaired = repair_json(cleaned_response)
                categorized = json.loads(repaired)

            if not isinstance(categorized, dict):
                raise ValueError("Response is not a dictionary object")

            print(f"  ✓ Reorganized into {len(categorized)} standard categories:")
            for category in categorized.keys():
                print(f"    - {category}")

            return categorized

        except (json.JSONDecodeError, ValueError) as e:
            error_msg = str(e)
            print(f"  ERROR: {error_msg}")
            
            # Save failed response for debugging
            debug_file = Path(f"debug_failed_response_attempt_{attempt}.txt")
            with open(debug_file, "w") as f:
                f.write(response)
            print(f"  DEBUG: Saved failed response to {debug_file}")
            
            if attempt < max_retries:
                # Refine prompt with SPECIFIC error for retry as requested by user
                prompt = f"""{base_prompt}

CRITICAL: THE PREVIOUS ATTEMPT FAILED. 
ERROR: {error_msg}
RESPONSE FRAGMENT: {response[:2000]}... [truncated]

INSTRUCTIONS TO FIX THE ERROR:
1. Ensure the response is a SINGLE VALID JSON OBJECT.
2. DO NOT use markdown code blocks (no ```json).
3. Ensure all strings are properly terminated with double quotes.
4. ESCAPE all internal double quotes with a backslash (\\").
5. ENSURE the JSON is NOT truncated. If the content is too long, summarize it slightly while keeping key details.
6. The error '{error_msg}' suggests your JSON was malformed. Please double-check the closing quotes and braces."""
                continue
            else:
                print(f"  ✗ Failed after {max_retries} retries")
                return {}


def process_all_papers(input_dir, output_dir, target_files=None):
    """
    Process papers from input_dir (or specific target_files) and save categorized versions to output_dir.

    Args:
        input_dir: Directory containing paper JSONs with sections
        output_dir: Directory to save categorized JSONs
        target_files: Optional list of filenames to process. If None, process all in input_dir.
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)

    # Create output directory
    output_path.mkdir(parents=True, exist_ok=True)

    # Initialize Gemini client
    print("Initializing Gemini client...")
    gemini_client = GEMINI(config_path=Path("config.yml"))
    print(f"Using model: {gemini_client.model}\n")

    # Get JSON files
    if target_files:
        json_files = []
        for f in target_files:
            p = input_path / f
            if p.exists():
                json_files.append(p)
            else:
                print(f"Warning: File not found: {p}")
        json_files = sorted(json_files)
    else:
        json_files = sorted(list(input_path.glob('*.json')))

    # Filter out empty JSON files
    valid_files = []
    for json_file in json_files:
        try:
            with open(json_file) as f:
                data = json.load(f)
                if data and data != {}:  # Not empty
                    valid_files.append(json_file)
        except Exception as e:
            print(f"Warning: Could not read {json_file.name}: {e}")

    print(f"Found {len(valid_files)} non-empty JSON files to process")
    if not target_files:
        print(f"(Skipped {len(json_files) - len(valid_files)} empty files)\n")

    # Process each paper
    results = {}
    for i, json_file in enumerate(valid_files, 1):
        print(f"\n[{i}/{len(valid_files)}] Processing: {json_file.name}")
        print("-" * 80)

        try:
            # Read paper data
            with open(json_file) as f:
                paper_data = json.load(f)

            # Categorize sections
            categorized_sections = categorize_sections(paper_data, gemini_client)

            if not categorized_sections:
                print(f"  ✗ Skipping due to errors")
                results[json_file.name] = "ERROR: No categorized sections"
                continue

            # Create output data
            output_data = {
                "paper_name": paper_data.get("paper_name", json_file.stem),
                "num_sections": len(categorized_sections),
                "sections": categorized_sections,
                "method": "gemini_categorized"
            }

            # Save to output file
            output_file = output_path / json_file.name
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(output_data, f, indent=2, ensure_ascii=False)

            print(f"  ✓ Saved to: {output_file.name}")
            results[json_file.name] = len(categorized_sections)

        except Exception as e:
            print(f"  ✗ ERROR: {str(e)}")
            import traceback
            traceback.print_exc()
            results[json_file.name] = f"ERROR: {str(e)}"

    # Print summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    successful = 0
    for filename, result in results.items():
        if isinstance(result, int):
            print(f"✓ {filename}: {result} categories")
            successful += 1
        else:
            print(f"✗ {filename}: {result}")

    print(f"\nSuccessfully processed: {successful}/{len(valid_files)}")
    print(f"Output saved to: {output_path}")

    # Print token usage
    print("\n" + "=" * 80)
    print("TOKEN USAGE")
    print("=" * 80)
    gemini_client._post_process()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Categorize paper sections using Gemini")
    parser.add_argument("--input_dir", default="data_reference/section_summary_extraction_gemini", help="Directory containing paper JSONs")
    parser.add_argument("--output_dir", default="data_reference/categorised_section_summary_extraction_gemini", help="Directory to save categorized JSONs")
    parser.add_argument("--files", nargs="+", help="Specific JSON filenames to process")

    args = parser.parse_args()
    process_all_papers(args.input_dir, args.output_dir, args.files)
