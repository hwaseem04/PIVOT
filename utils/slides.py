import fitz  # PyMuPDF
import logging
from PIL import Image
import io
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions, AcceleratorDevice, AcceleratorOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
from .textwork import _CONVERTER, _CONVERSION_CACHE

_log = logging.getLogger(__name__)

def get_specific_element(pdf_path, element_type, element_label, target_caption, image_path):
    """
    :param element_type: 'table' or 'picture'
    :param element_label: The label string (e.g., "Figure 10", "Table 2")
    :param target_caption: The descriptive caption text from the planner
    :param image_path: Path to save the extracted image
    """
    if Path(image_path).exists() and Path(image_path).stat().st_size > 0:
        return image_path

    global _CONVERTER
    pdf_key = str(pdf_path)
    
    if pdf_key in _CONVERSION_CACHE:
        raw_result = _CONVERSION_CACHE[pdf_key]
    else:
        pipeline_options = PdfPipelineOptions()
        pipeline_options.accelerator_options.device = AcceleratorDevice.CPU
        pipeline_options.do_ocr = False
        pipeline_options.images_scale = 5.0
        pipeline_options.generate_page_images = True
        pipeline_options.generate_picture_images = True

        import utils.textwork as tw
        if tw._CONVERTER is None:
            tw._CONVERTER = DocumentConverter(
                format_options={
                    InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
                }
            )
        
        raw_result = tw._CONVERTER.convert(pdf_path)
        tw._CONVERSION_CACHE[pdf_key] = raw_result

    import re as _re

    best_match = None
    max_score = -1

    # Normalize label for matching (e.g., "Figure 10" -> "figure 10")
    norm_label = element_label.lower().strip()
    # Build several label variants to maximize caption matching chances:
    #   "figure 10" → "fig. 10", "fig 10", "figure10"
    alt_variants = [norm_label]
    if "figure" in norm_label:
        alt_variants.append(norm_label.replace("figure", "fig."))
        alt_variants.append(norm_label.replace("figure", "fig"))
        alt_variants.append(norm_label.replace("figure ", "fig. "))
        alt_variants.append(norm_label.replace(" ", ""))      # "figure10"
    elif "fig." in norm_label:
        alt_variants.append(norm_label.replace("fig.", "figure"))
        alt_variants.append(norm_label.replace("fig.", "fig"))
    elif "table" in norm_label:
        alt_variants.append(norm_label.replace("table", "tab."))
        alt_variants.append(norm_label.replace("table ", "tab. "))
        alt_variants.append(norm_label.replace(" ", ""))

    # Parse the ordinal number from the label (e.g. "Figure 1" → 0-based index 0)
    _num_match = _re.search(r'(\d+)', norm_label)
    ordinal_idx = int(_num_match.group(1)) - 1 if _num_match else None

    doc_elements = []
    if "table" in element_type.lower():
        doc_elements = raw_result.document.tables
    else:
        doc_elements = raw_result.document.pictures

    for element in doc_elements:
        caption_text = element.caption_text(raw_result.document).lower()
        # NOTE: do NOT skip elements with empty captions — they remain as candidates
        # for the ordinal fallback even if they score 0 in caption matching.

        score = 0
        if caption_text:
            # 1. Label match against all variant forms (highest priority)
            for variant in alt_variants:
                if variant in caption_text:
                    score += 100
                    if caption_text.startswith(variant):
                        score += 50
                    break  # one match is enough

            # 2. Content overlap with provided caption
            if target_caption:
                target_words = set(target_caption.lower().split())
                caption_words = set(caption_text.split())
                score += len(target_words.intersection(caption_words))

        if score > max_score:
            max_score = score
            best_match = element

    # ── Primary path: caption-based match ───────────────────────────────────
    if best_match and max_score > 0:
        with Path(image_path).open("wb") as fp:
            best_match.get_image(raw_result.document).save(fp, "PNG")
        return image_path

    # ── Fallback: ordinal index among CAPTIONED elements only ────────────────
    # Logos, header icons, and decorative images are almost always uncaptioned.
    # Real paper figures/tables have captions.  By indexing into the captioned
    # subset we skip non-figure images so "Figure 1" → 1st captioned picture,
    # not the 1st image Docling found (which is often a logo).
    captioned = [e for e in doc_elements
                 if e.caption_text(raw_result.document).strip()]
    fallback_list = captioned if captioned else doc_elements  # last resort: use all

    _log.warning(
        "Caption-based match failed for '%s' (max_score=%d); "
        "falling back to ordinal index %s "
        "(captioned candidates: %d, total elements: %d).",
        element_label, max_score, ordinal_idx,
        len(captioned), len(doc_elements),
    )

    if ordinal_idx is not None and 0 <= ordinal_idx < len(fallback_list):
        fallback_elem = fallback_list[ordinal_idx]
        try:
            with Path(image_path).open("wb") as fp:
                fallback_elem.get_image(raw_result.document).save(fp, "PNG")
        except Exception:
            pass  # if this also fails, return image_path as-is (placeholder)

    return image_path


def get_figure_via_gemini(
    pdf_path: str,
    element_label: str,
    target_caption: str,
    image_path: str,
    planner_func,
    dpi: int = 300,
) -> str:
    """Hybrid extraction: Gemini identifies the page, Docling crops cleanly.

    Each tool does what it's good at:
    - Gemini: reads the whole PDF and reliably identifies WHICH page a figure is on.
    - Docling: its layout model extracts ONLY the figure graphic region via
      element.get_image() — no caption text, no body-text bleed, pixel-perfect crop.

    Algorithm:
    1. Ask Gemini for the 1-indexed page number where element_label appears.
    2. Filter Docling's already-converted picture/table list to that page.
    3. Score elements on that page by caption label match (same as get_specific_element).
    4. Call element.get_image() for a clean, caption-free crop.

    Returns image_path on success, "" on failure (caller falls back to Docling alone).
    """
    import utils.textwork as tw
    from utils.textwork import _load_json_dict
    from docling.datamodel.base_models import InputFormat
    from docling.datamodel.pipeline_options import PdfPipelineOptions, AcceleratorDevice
    from docling.document_converter import DocumentConverter, PdfFormatOption

    if Path(image_path).exists() and Path(image_path).stat().st_size > 0:
        return image_path

    # ── Step 1: Ask Gemini for the page number only ───────────────────────────
    # We ask only for the page — NOT a bbox.  Docling handles the precise crop
    # so we never need to worry about caption-text or column bleed.
    base_prompt = (
        f'Find "{element_label}" in the attached PDF.\n'
        f"Return ONLY a JSON object with exactly one field:\n"
        f'  "page": integer — 1-indexed page number where {element_label} appears\n\n'
        f'Example: {{"page": 4}}\n'
        f"Output ONLY the JSON object, no markdown fences, no extra text."
    )
    prompt = base_prompt
    target_page = None  # 1-indexed

    max_retries = 3
    for attempt in range(max_retries):
        try:
            raw_response = planner_func(prompt=prompt, pdf_path=Path(pdf_path))
            # Strip triple-quote wrappers Gemini sometimes adds
            raw_stripped = raw_response.strip()
            for _triple in ('"""', "'''"):
                if raw_stripped.startswith(_triple) and raw_stripped.endswith(_triple):
                    raw_stripped = raw_stripped[3:-3].strip()
                    break
            loc = _load_json_dict(raw_stripped)

            if not isinstance(loc, dict) or "page" not in loc:
                _log.warning(
                    "get_figure_via_gemini attempt %d: no 'page' field for %s: %s",
                    attempt + 1, element_label, raw_stripped[:200],
                )
                prompt = base_prompt + (
                    f'\n\nERROR: Previous response did not contain "page". '
                    f'Return only: {{"page": N}}'
                )
                continue

            target_page = int(loc["page"])  # 1-indexed
            _log.info(
                "get_figure_via_gemini: Gemini says %s is on page %d",
                element_label, target_page,
            )
            break

        except Exception as e:
            _log.warning(
                "get_figure_via_gemini attempt %d failed for %s: %s",
                attempt + 1, element_label, e,
            )

    if target_page is None:
        return ""  # Gemini couldn't identify the page

    # ── Step 2: Get (or reuse) Docling conversion ─────────────────────────────
    pdf_key = str(pdf_path)
    if pdf_key in tw._CONVERSION_CACHE:
        raw_result = tw._CONVERSION_CACHE[pdf_key]
    else:
        pipeline_options = PdfPipelineOptions()
        pipeline_options.accelerator_options.device = AcceleratorDevice.CPU
        pipeline_options.do_ocr = False
        pipeline_options.images_scale = 5.0
        pipeline_options.generate_page_images = True
        pipeline_options.generate_picture_images = True
        if tw._CONVERTER is None:
            tw._CONVERTER = DocumentConverter(
                format_options={
                    InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
                }
            )
        raw_result = tw._CONVERTER.convert(pdf_path)
        tw._CONVERSION_CACHE[pdf_key] = raw_result

    # ── Step 3: Filter Docling elements to target_page ────────────────────────
    is_table = "table" in element_label.lower()
    all_elements = (
        raw_result.document.tables if is_table else raw_result.document.pictures
    )

    page_elements = []
    for elem in all_elements:
        if hasattr(elem, "prov") and elem.prov:
            for prov_item in elem.prov:
                if hasattr(prov_item, "page_no") and prov_item.page_no == target_page:
                    page_elements.append(elem)
                    break

    if not page_elements:
        _log.warning(
            "get_figure_via_gemini: no Docling elements on page %d for %s "
            "(total elements: %d) — will fallback",
            target_page, element_label, len(all_elements),
        )
        return ""

    # ── Step 4: Score elements on that page by label match ───────────────────
    norm_label = element_label.lower().strip()
    alt_variants = [norm_label]
    if "figure" in norm_label:
        alt_variants += [
            norm_label.replace("figure", "fig."),
            norm_label.replace("figure", "fig"),
            norm_label.replace(" ", ""),
        ]
    elif "table" in norm_label:
        alt_variants += [
            norm_label.replace("table", "tab."),
            norm_label.replace(" ", ""),
        ]

    best_elem = None
    max_score = -1
    for elem in page_elements:
        caption_text = elem.caption_text(raw_result.document).lower()
        score = 0
        if caption_text:
            for variant in alt_variants:
                if variant in caption_text:
                    score += 100
                    if caption_text.startswith(variant):
                        score += 50
                    break
        if score > max_score:
            max_score = score
            best_elem = elem

    # No caption matched — Gemini confirmed the page, so just use the first
    # element on that page (almost certainly the right one).
    if best_elem is None:
        best_elem = page_elements[0]
        _log.warning(
            "get_figure_via_gemini: no caption match on page %d for %s; "
            "using first element on that page (%d candidates)",
            target_page, element_label, len(page_elements),
        )

    # ── Step 5: Clean crop via Docling ────────────────────────────────────────
    # element.get_image() returns ONLY the figure graphic region as detected
    # by Docling's layout model — no caption text, no body-text bleed.
    try:
        pil_img = best_elem.get_image(raw_result.document)
        Path(image_path).parent.mkdir(parents=True, exist_ok=True)
        with Path(image_path).open("wb") as fp:
            pil_img.save(fp, "PNG")
        _log.info(
            "get_figure_via_gemini (hybrid): extracted %s from page %d via Docling crop",
            element_label, target_page,
        )
        return str(image_path)
    except Exception as e:
        _log.warning(
            "get_figure_via_gemini: Docling get_image failed for %s on page %d: %s",
            element_label, target_page, e,
        )
        return ""


def create_ppt_style_image( image_path, description, output_path,  width=800):
    temp_img = Image.new('RGB', (width, 10), (255, 255, 255))
    temp_draw = ImageDraw.Draw(temp_img)
    
    try:
        title_font = ImageFont.truetype("arial.ttf", 40)
        desc_font = ImageFont.truetype("arial.ttf", 24)
    except:
        # 备用默认字体
        title_font = ImageFont.load_default()
        title_font.size = 40
        desc_font = ImageFont.load_default()
        desc_font.size = 24
    
    
    # title_bbox = temp_draw.textbbox((0, 0), title, font=title_font)
    # title_height = title_bbox[3] - title_bbox[1]
    
    
    content_img = Image.open(image_path)
    content_img.thumbnail((width-100, width-100))  # 限制图片大小
    
    
    char_width = desc_font.getlength("A")  # 获取字符平均宽度
    max_chars_per_line = int((width * 0.9) // char_width)  # 每行最多字符数
    wrapped_lines = textwrap.wrap(description, width=max_chars_per_line)
    
    
    line_height = int(desc_font.size * 1.2)
    desc_height = len(wrapped_lines) * line_height
    
    
    top_margin = 50
    spacing = 30
    total_height = (top_margin + spacing + 
                   content_img.height + spacing + 
                   desc_height + top_margin)
    width = int(total_height*16/9)
    
    image = Image.new('RGB', (width, total_height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    
    #choosable with title
    #title_x = (width - (title_bbox[2] - title_bbox[0])) // 2
    #draw.text((title_x, top_margin), title, fill="black", font=title_font)
    
    img_y = top_margin  + spacing
    img_x = (width - content_img.width) // 2
    image.paste(content_img, (img_x, img_y))
    
    
    desc_y = img_y + content_img.height + spacing
    for i, line in enumerate(wrapped_lines):
        line_bbox = draw.textbbox((0, 0), line, font=desc_font)
        line_width = line_bbox[2] - line_bbox[0]
        line_x = (width - line_width) // 2
        draw.text((line_x, desc_y + i * line_height), 
                 line, fill="black", font=desc_font)
    
    image.save(output_path)
    return output_path

def crop_pdf_page(pdf_path, page_num, crop_coords, output_path=None, dpi=72):
    """
    crop_coords: [x_min, y_min, x_max, y_max] in pixels at given dpi
    """
    doc = fitz.open(pdf_path)
    page = doc[page_num]

    scale = 72.0 / dpi
    x0, y0, x1, y1 = [c * scale for c in crop_coords]

    clip = fitz.Rect(x0, y0, x1, y1)
    page_rect = page.rect

    clip = clip & page_rect  # 交集
    if clip.is_empty:
        raise ValueError(f"Crop box {crop_coords} is outside page {page_num}")

    mat = fitz.Matrix(dpi / 72.0, dpi / 72.0)
    pix = page.get_pixmap(matrix=mat, clip=clip)

    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    if output_path:
        img.save(str(output_path))

    doc.close()
    return img if output_path is None else output_path


# pdf_path = "C:\\Users\\87719\\Desktop\\AgenticIR-main\\dataset\\ControlNet.pdf"
# page_index = 3  # 假设 FIGURE 3 在第 4 页（索引从 0 开始）
# coords = [(332.11, 81.50), (347.82, 81.50), (347.82, 97.22), (332.11, 97.22)]


# cropped_image = crop_pdf_page(pdf_path, page_index, coords)
# cropped_image.save("C:\\Users\\87719\\Desktop\\AgenticIR-main\\output\\output.png")

# cropped_image.show()




