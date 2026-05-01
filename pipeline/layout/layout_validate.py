"""
layout_validate.py — Static validation and heuristic repair for LayoutSpec v1.

Design rationale:
  - Geometric checks (overlap, out-of-bounds) are pure math → always static.
  - Text overflow is estimated with a fast character-count heuristic.
  - Repair rules are deterministic and fast (no LLM calls in the render path).
  - A LayoutAnalyserAgent hook is left as a placeholder for future LLM-based
    semantic quality checks that can run asynchronously.

Repair priority (highest first):
  1. Text/bullet overflow  → shrink font_size → steal height from adjacent figure
  2. Element overlap       → nudge lower-priority element inward
  3. Out-of-bounds         → clamp to canvas
"""

import logging
import copy
from typing import List, Tuple

from .layout_spec import LayoutSpec, Element, Box, GlobalConstraints, RENDER_GROUP

logger = logging.getLogger("layout_validate")

# ── Canvas constants ─────────────────────────────────────────────────────────
CANVAS_W = 1920
CANVAS_H = 1080
# Approximate characters that fit in one pixel of width at body font (48px)
# Calibrated for Arial 48px: ~13 chars per 1000px ≈ 0.013 chars/px
CHARS_PER_PX_BODY = 0.013
LINE_HEIGHT_FRAC = 0.052  # fraction of canvas height per text line at default body font


# ── Public API ───────────────────────────────────────────────────────────────

def check_overlaps(elements: List[Element]) -> List[Tuple[str, str, float]]:
    """Return list of (elem_a_id, elem_b_id, overlap_area) for all overlapping pairs.

    overlap_area is in normalized canvas units (0..1).
    """
    overlaps = []
    for i, a in enumerate(elements):
        for b in elements[i + 1:]:
            area = a.box.overlap_area(b.box)
            if area > 1e-6:
                overlaps.append((a.id, b.id, area))
    return overlaps


def check_overflow(element: Element, content_payload: dict) -> bool:
    """Heuristic: estimate whether text content overflows the element's box.

    Only applicable to text-group elements (T, ST, B, P, L).
    Returns True if estimated content height exceeds box height.
    """
    from .layout_spec import resolve_content_ref
    rgroup = RENDER_GROUP.get(element.type, "")
    if rgroup not in ("text", "bullets"):
        return False  # non-text elements cannot overflow in this model

    content = resolve_content_ref(element.content_ref or "", content_payload)
    if content is None:
        return False

    font_size = element.style.get("font_size", 24 if element.type == "B" else 40)
    min_font_size = element.style.get("min_font_size", 14)

    # Scale line height proportionally to font size (baseline: 48px → LINE_HEIGHT_FRAC)
    line_h = LINE_HEIGHT_FRAC * (font_size / 48.0)
    chars_per_px = CHARS_PER_PX_BODY * (48.0 / font_size)

    box_w_px = element.box.w * CANVAS_W
    box_h = element.box.h

    if element.type == "B" and isinstance(content, list):
        total_lines = sum(
            max(1, _estimate_lines(str(b), box_w_px, chars_per_px)) for b in content
        )
    else:
        text = str(content) if not isinstance(content, str) else content
        total_lines = max(1, _estimate_lines(text, box_w_px, chars_per_px))

    estimated_h = total_lines * line_h
    return estimated_h > box_h


def repair(
    spec: LayoutSpec,
    content_payload: dict,
) -> Tuple[LayoutSpec, List[str], dict]:
    """Validate and repair a LayoutSpec in-place (works on a deep copy).

    Returns:
        repaired_spec  — the (possibly modified) spec
        repair_log     — list of human-readable repair action strings
        flags          — dict with boolean keys:
                           overflow_warn    — at least one element still overflows
                           needs_split_slide— content may need to be split across slides
                           had_overlap      — overlaps were detected (and fixed)
                           had_oob          — out-of-bounds elements were clamped
    """
    spec = _deep_copy_spec(spec)
    log = []
    flags = {
        "overflow_warn": False,
        "needs_split_slide": False,
        "had_overlap": False,
        "had_oob": False,
    }

    gc = spec.global_constraints

    # 0. Remove elements whose content_ref resolves to nothing and reclaim space.
    #    This handles cases like a layout designed for equations + bullets but the
    #    content only provides bullets — the empty equation region is merged into
    #    the bullet element so bullets fill the available column space.
    spec, reclaim_log = _reclaim_empty_element_space(spec, content_payload)
    log.extend(reclaim_log)

    # 1. Clamp all boxes to [0, 1]
    for elem in spec.elements:
        clamped = _clamp_box(elem.box)
        if clamped != elem.box:
            log.append(f"OOB clamp: '{elem.id}' box clamped to canvas bounds.")
            elem.box = clamped
            flags["had_oob"] = True

    # 2. Repair text overflow
    if gc.no_overflow:
        for elem in spec.elements:
            if RENDER_GROUP.get(elem.type, "") in ("text", "bullets"):
                if check_overflow(elem, content_payload):
                    repaired, msg, still_overflows = _repair_overflow(elem, spec, content_payload, gc)
                    log.extend(msg)
                    if still_overflows:
                        flags["overflow_warn"] = True
                        flags["needs_split_slide"] = True

    # 3. Repair overlaps
    if gc.no_overlap:
        overlaps = check_overlaps(spec.elements)
        if overlaps:
            flags["had_overlap"] = True
            for a_id, b_id, area in overlaps:
                # Lower priority = later in element list
                a_idx = _elem_idx(spec, a_id)
                b_idx = _elem_idx(spec, b_id)
                lower_priority = spec.elements[max(a_idx, b_idx)]
                msg = _nudge_apart(lower_priority, spec.elements, a_id, b_id)
                if msg:
                    log.append(msg)

    return spec, log, flags


# ── Placeholder hook for future LLM-based layout analysis ───────────────────

def layout_analyser_agent_hook(spec: LayoutSpec, content_payload: dict) -> dict:
    """Future extension point: call an LLM-based layout quality checker.

    Currently a no-op. In v2 this can be wired to an async agent that
    scores the layout on aesthetics, readability, and content fit.

    Returns:
        dict with optional keys: 'score' (float), 'issues' (list[str])
    """
    return {}


# ── Internal helpers ─────────────────────────────────────────────────────────

def _estimate_lines(text: str, box_w_px: float, chars_per_px: float) -> int:
    """Estimate number of wrapped lines for text given box width."""
    if box_w_px <= 0 or chars_per_px <= 0:
        return 1
    chars_per_line = max(1, int(box_w_px * chars_per_px))
    words = text.split()
    if not words:
        return 1
    lines, current_len = 1, 0
    for word in words:
        if current_len + len(word) + 1 <= chars_per_line:
            current_len += len(word) + 1
        else:
            lines += 1
            current_len = len(word)
    return lines


def _repair_overflow(
    elem: Element,
    spec: LayoutSpec,
    content_payload: dict,
    gc: GlobalConstraints,
) -> Tuple[Element, List[str], bool]:
    """Try to fix overflow for a single element. Modifies elem in-place.

    Strategy:
      1. Reduce font_size by 2 until overflow is gone or min_font_size reached.
      2. If still overflowing, try stealing up to 15% height from an adjacent
         figure/table element in the same horizontal band.
      3. If still overflowing, flag it.
    """
    log = []
    min_fs = int(elem.style.get("min_font_size", gc.min_font_size))
    fs = int(elem.style.get("font_size", 24 if elem.type == "B" else 40))

    # Step 1: reduce font size
    while fs > min_fs and check_overflow(elem, content_payload):
        fs -= 2
        elem.style["font_size"] = fs
        log.append(f"Overflow fix: '{elem.id}' font_size reduced to {fs}.")

    if not check_overflow(elem, content_payload):
        return elem, log, False

    # Step 2: steal height from adjacent image-type element
    donor = _find_adjacent_donor(elem, spec)
    if donor:
        steal = min(0.15, donor.box.h * 0.15)
        donor.box = Box(donor.box.x, donor.box.y + steal, donor.box.w, donor.box.h - steal)
        elem.box = Box(elem.box.x, elem.box.y, elem.box.w, elem.box.h + steal)
        log.append(
            f"Overflow fix: stole {steal:.3f} height from '{donor.id}' for '{elem.id}'."
        )

    if not check_overflow(elem, content_payload):
        return elem, log, False

    log.append(
        f"Overflow WARNING: '{elem.id}' still overflows after repair. "
        "Consider splitting into two slides."
    )
    return elem, log, True


def _find_adjacent_donor(elem: Element, spec: LayoutSpec) -> Element | None:
    """Find the nearest figure/table element in the same horizontal band."""
    donor_types = {"F", "D", "CH", "TAB"}
    band_center = elem.box.y + elem.box.h / 2.0
    best = None
    best_dist = float("inf")
    for other in spec.elements:
        if other.id == elem.id or other.type not in donor_types:
            continue
        other_center = other.box.y + other.box.h / 2.0
        if abs(other_center - band_center) < 0.2:  # same rough band
            dist = abs(other.box.x - elem.box.x)
            if dist < best_dist:
                best_dist = dist
                best = other
    return best


def _nudge_apart(lower: Element, all_elements: List[Element], a_id: str, b_id: str) -> str:
    """Nudge lower-priority element inward to resolve overlap with higher-priority."""
    # Find the higher-priority element
    other_id = a_id if lower.id == b_id else b_id
    higher = next((e for e in all_elements if e.id == other_id), None)
    if higher is None:
        return ""

    # Determine nudge direction: move lower away from higher
    lc_x = lower.box.x + lower.box.w / 2.0
    hc_x = higher.box.x + higher.box.w / 2.0
    lc_y = lower.box.y + lower.box.h / 2.0
    hc_y = higher.box.y + higher.box.h / 2.0

    # Nudge by 1% of canvas in the dominant separation axis
    if abs(lc_x - hc_x) >= abs(lc_y - hc_y):
        delta = 0.01 if lc_x > hc_x else -0.01
        new_x = _clamp01(lower.box.x + delta)
        lower.box = Box(new_x, lower.box.y, max(0.01, lower.box.w - abs(delta)), lower.box.h)
    else:
        delta = 0.01 if lc_y > hc_y else -0.01
        new_y = _clamp01(lower.box.y + delta)
        lower.box = Box(lower.box.x, new_y, lower.box.w, max(0.01, lower.box.h - abs(delta)))

    return f"Overlap fix: nudged '{lower.id}' away from '{higher.id}'."


def _clamp_box(box: Box) -> Box:
    x = max(0.0, min(box.x, 1.0))
    y = max(0.0, min(box.y, 1.0))
    w = max(0.01, min(box.w, 1.0 - x))
    h = max(0.01, min(box.h, 1.0 - y))
    return Box(x, y, w, h)


def _clamp01(v: float) -> float:
    return max(0.0, min(v, 1.0))


def _elem_idx(spec: LayoutSpec, elem_id: str) -> int:
    for i, e in enumerate(spec.elements):
        if e.id == elem_id:
            return i
    return 0


def _deep_copy_spec(spec: LayoutSpec) -> LayoutSpec:
    """Return a deep copy of a LayoutSpec so repair is non-destructive."""
    return LayoutSpec.from_dict(spec.to_dict())


def _reclaim_empty_element_space(
    spec: LayoutSpec,
    content_payload: dict,
) -> Tuple[LayoutSpec, List[str]]:
    """Remove elements that have a content_ref but no resolvable content.

    When the LLM designs a layout with an element (e.g. EQ "polynomial_equations")
    whose content_ref (e.g. "elements.equations") doesn't exist in the actual
    content payload, that element occupies canvas space while rendering nothing.
    This repair step:
      1. Identifies such "empty" elements (content_ref present but resolves to None).
      2. Finds the nearest same-column element adjacent to each empty element.
      3. Expands the beneficiary's box to absorb the freed space.
      4. Removes the empty elements from the spec.

    Title elements (type T) are never removed.
    """
    from .layout_spec import resolve_content_ref

    log: List[str] = []

    # Element-type groupings for fallback resolution
    _VISUAL_TYPES = {"F", "D", "TAB", "CH"}  # all use elements.figure as fallback

    # Identify elements with content_ref that resolve to nothing
    removable: List[Element] = []
    for elem in spec.elements:
        # Never remove titles or subtitles — handled gracefully by the renderer
        if elem.type in ("T", "ST"):
            continue
        if not elem.content_ref:
            continue  # no content_ref → not content-driven, keep it

        val = resolve_content_ref(elem.content_ref, content_payload)

        # ── Fallbacks for common naming mismatches ─────────────────────────
        # 1. Visual elements (F / D / TAB / CH): the low-level planner always
        #    stores the visual asset under "elements.figure" regardless of the
        #    specific id chosen by the style planner (e.g. "table_1", "chart_2").
        if val is None and elem.type in _VISUAL_TYPES:
            val = resolve_content_ref("elements.figure", content_payload)

        # 2. EQ elements: check both singular ("elements.equation") and plural
        #    ("elements.equations") because the style planner and low-level
        #    planner sometimes disagree on plurality.
        if val is None and elem.type == "EQ":
            for alt_ref in ("elements.equations", "elements.equation"):
                if alt_ref != elem.content_ref:
                    val = resolve_content_ref(alt_ref, content_payload)
                    if val is not None:
                        break

        if val is None:
            removable.append(elem)

    if not removable:
        return spec, log

    remove_ids = {e.id for e in removable}

    for empty_elem in removable:
        beneficiary = _find_space_beneficiary(empty_elem, spec, remove_ids)
        if beneficiary is None:
            log.append(
                f"Empty element '{empty_elem.id}' removed "
                f"(content_ref '{empty_elem.content_ref}' unresolved; no beneficiary)."
            )
            continue

        # Determine relative position: is beneficiary below or above empty_elem?
        empty_bottom = empty_elem.box.y + empty_elem.box.h
        bene_top = beneficiary.box.y

        if bene_top >= empty_bottom - 0.02:
            # Beneficiary is directly below → expand it upward
            new_y = empty_elem.box.y
            new_h = beneficiary.box.h + (beneficiary.box.y - new_y)
            beneficiary.box = Box(beneficiary.box.x, new_y, beneficiary.box.w, new_h)
        else:
            # Beneficiary is above or overlapping → expand downward
            new_h = beneficiary.box.h + empty_elem.box.h
            beneficiary.box = Box(beneficiary.box.x, beneficiary.box.y, beneficiary.box.w, new_h)

        log.append(
            f"Empty element '{empty_elem.id}' removed; "
            f"space reassigned to '{beneficiary.id}' "
            f"(new box y={beneficiary.box.y:.2f} h={beneficiary.box.h:.2f})."
        )

    # Remove the empty elements
    spec.elements = [e for e in spec.elements if e.id not in remove_ids]
    return spec, log


def _find_space_beneficiary(
    empty_elem: Element,
    spec: LayoutSpec,
    remove_ids: set,
) -> Element | None:
    """Find the nearest same-column element to receive empty_elem's freed space.

    "Same column" means the x-ranges overlap by at least 50% of the narrower box.
    Among candidates, prefer the one whose edge is closest to empty_elem.
    """
    best: Element | None = None
    best_dist = float("inf")

    for other in spec.elements:
        if other.id in remove_ids or other.id == empty_elem.id:
            continue
        if other.type == "T":
            continue  # don't grow title elements

        # Column overlap check
        x_overlap = (
            min(empty_elem.box.x + empty_elem.box.w, other.box.x + other.box.w)
            - max(empty_elem.box.x, other.box.x)
        )
        min_w = min(empty_elem.box.w, other.box.w)
        if min_w <= 0 or x_overlap / min_w < 0.4:
            continue

        # Distance: min gap between the two boxes vertically
        dist = min(
            abs(other.box.y - (empty_elem.box.y + empty_elem.box.h)),
            abs(empty_elem.box.y - (other.box.y + other.box.h)),
        )
        if dist < best_dist:
            best_dist = dist
            best = other

    return best
