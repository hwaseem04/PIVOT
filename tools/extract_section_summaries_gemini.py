"""
Extract section-wise summaries from research papers using Gemini.
Reads PDFs from data_reference/final/ and outputs to section_summary_extraction_gemini/
"""

import json
import sys
from pathlib import Path

# Add parent directory to path to import modules
sys.path.insert(0, str(Path(__file__).parent.parent))
from llms.gemini import GEMINI


SECTION_SUMMARY_PROMPT = """You are analyzing a research paper PDF. Your task is to extract and summarize the content section by section.

INSTRUCTIONS:
1. BEFORE conclusion section:
   - Extract all main sections with their original names (e.g., abstract, introduction, related work, method, experiments, results, etc.)
   - Remove number prefixes and convert to lowercase
   - Merge subsections into their parent section

2. AFTER conclusion section:
   - SKIP: Acknowledgements, Acknowledgments, Funding, Author Contributions, References, Bibliography
   - Everything else (appendices, supplementary materials, etc.): merge into ONE section called "supplementary"
   - Within "supplementary", you can include subsection names/headings in the summary text

3. For each section, provide a comprehensive summary that:
   - Captures ALL key points and details
   - Preserves ALL mathematical equations in LaTeX format
   - Does NOT lose any important information or meaning
   - Is detailed and thorough, not superficial

OUTPUT FORMAT:
Return ONLY a JSON object with section names as keys and comprehensive summaries as values. Example:
{{
  "abstract": "Detailed summary...",
  "introduction": "Comprehensive summary including subsections...",
  "related work": "Summary...",
  "method": "Detailed summary with equations...",
  "experiments": "Summary...",
  "results": "Summary...",
  "conclusion": "Summary...",
  "supplementary": "Appendix A: ... Appendix B: ... (can include subsection headings in text)"
}}

IMPORTANT:
- Retain actual section names BEFORE conclusion
- After conclusion: skip acknowledgments/funding/contributions/references, put everything else in "supplementary"
- Supplementary can have subsection names within its content

CRITICAL REQUIREMENTS:
- Preserve ALL LaTeX equations but DOUBLE-ESCAPE backslashes for valid JSON (e.g., $E=mc^2$, $$\\\\frac{{a}}{{b}}$$)
- In JSON strings, use \\\\ instead of \\ for LaTeX commands
- Be thorough and detailed - capture ALL important content
- Merge subsection content into parent sections
- Do NOT modify, omit, or simplify equations
- Return ONLY valid JSON - all backslashes in LaTeX must be doubled (\\\\)
- Return ONLY the JSON object, no explanations or markdown formatting"""


def extract_section_summaries(pdf_path, gemini_client, max_retries=2):
    """
    Extract and summarize sections from a PDF using Gemini.

    Args:
        pdf_path: Path to the PDF file
        gemini_client: GEMINI client instance
        max_retries: Maximum number of retry attempts

    Returns:
        Dictionary with section summaries
    """
    print(f"Processing: {pdf_path.name}")

    prompt = SECTION_SUMMARY_PROMPT

    for attempt in range(max_retries + 1):
        if attempt > 0:
            print(f"  Retry attempt {attempt}/{max_retries}...")
        else:
            print("  Sending PDF to Gemini for section extraction and summarization...")

        # Query Gemini with the PDF
        _, response = gemini_client.query(
            pdf_path=str(pdf_path),
            prompt=prompt
        )

        # Parse response
        try:
            # Remove markdown code blocks if present
            cleaned_response = response.strip()
            if cleaned_response.startswith("```"):
                # Remove opening ```json or ```
                cleaned_response = cleaned_response.split('\n', 1)[1] if '\n' in cleaned_response else cleaned_response
                # Remove closing ```
                if cleaned_response.endswith("```"):
                    cleaned_response = cleaned_response.rsplit('\n```', 1)[0]

            # Try to parse as-is first
            try:
                sections = json.loads(cleaned_response)
            except json.JSONDecodeError as parse_error:
                # If parsing fails due to escape sequences, try to fix common LaTeX issues
                import re
                # Fix single backslashes in LaTeX that should be double-escaped
                # This is a fallback - ideally Gemini should return proper JSON
                fixed_response = re.sub(r'\\(?!["\\/bfnrtu])', r'\\\\', cleaned_response)
                sections = json.loads(fixed_response)

            if not isinstance(sections, dict):
                raise ValueError("Response is not a dictionary")

            print(f"  ✓ Extracted and summarized {len(sections)} sections:")
            for section_name in sections.keys():
                print(f"    - {section_name}")

            return sections

        except (json.JSONDecodeError, ValueError) as e:
            error_msg = str(e)
            print(f"  ERROR: {error_msg}")
            print(f"  Response preview: {response[:300]}...")

            # If we have retries left, refine the prompt with the error
            if attempt < max_retries:
                prompt = f"""{SECTION_SUMMARY_PROMPT}

PREVIOUS ATTEMPT FAILED WITH ERROR: {error_msg}
Response preview that caused error: {response[:500]}

Please fix the issue and return valid JSON. Common issues:
- Ensure all backslashes in LaTeX are doubled (use \\\\ not \\)
- Ensure the response is a valid JSON object, not an array
- Don't wrap in markdown code blocks
- Ensure all quotes are properly escaped"""
                continue
            else:
                print(f"  ✗ Failed after {max_retries} retries")
                return {}


def process_all_pdfs(input_dir, output_dir, target_files=None):
    """
    Process all PDFs in input_dir (or specific target_files) and save section summaries to output_dir.

    Args:
        input_dir: Directory containing PDF files
        output_dir: Directory to save JSON output files
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

    # Get PDF files
    if target_files:
        pdf_files = []
        for f in target_files:
            p = input_path / f
            if p.exists():
                pdf_files.append(p)
            else:
                print(f"Warning: File not found: {p}")
        pdf_files = sorted(pdf_files)
    else:
        pdf_files = sorted(list(input_path.glob('*.pdf')))

    print(f"Found {len(pdf_files)} PDF files to process\n")

    # Process each PDF
    results = {}
    for i, pdf_file in enumerate(pdf_files, 1):
        print(f"\n[{i}/{len(pdf_files)}] {pdf_file.name}")
        print("-" * 80)

        try:
            # Extract section summaries
            section_summaries = extract_section_summaries(pdf_file, gemini_client)

            if not section_summaries:
                print(f"  ✗ Skipping due to errors")
                results[pdf_file.name] = "ERROR: No sections extracted"
                continue

            # Create output data
            output_data = {
                "paper_name": pdf_file.stem,
                "num_sections": len(section_summaries),
                "sections": section_summaries,
                "method": "gemini_summary"
            }

            # Save to output file
            output_filename = pdf_file.stem + '.json'
            output_file = output_path / output_filename

            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(output_data, f, indent=2, ensure_ascii=False)

            print(f"  ✓ Saved {len(section_summaries)} section summaries to: {output_filename}")
            results[pdf_file.name] = len(section_summaries)

        except Exception as e:
            print(f"  ✗ ERROR: {str(e)}")
            import traceback
            traceback.print_exc()
            results[pdf_file.name] = f"ERROR: {str(e)}"

    # Print summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    successful = 0
    for pdf_name, section_count in results.items():
        if isinstance(section_count, int):
            print(f"✓ {pdf_name}: {section_count} sections")
            successful += 1
        else:
            print(f"✗ {pdf_name}: {section_count}")

    print(f"\nSuccessfully processed: {successful}/{len(pdf_files)}")
    print(f"Output saved to: {output_path}")

    # Print token usage
    print("\n" + "=" * 80)
    print("TOKEN USAGE")
    print("=" * 80)
    gemini_client._post_process()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Extract section summaries using Gemini")
    parser.add_argument("--input_dir", default="data_reference/final", help="Directory containing PDF files")
    parser.add_argument("--output_dir", default="data_reference/section_summary_extraction_gemini", help="Directory to save JSON output")
    parser.add_argument("--files", nargs="+", help="Specific PDF filenames to process")

    args = parser.parse_args()
    process_all_pdfs(args.input_dir, args.output_dir, args.files)
