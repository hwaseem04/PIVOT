"""
layout_compile.py — Compile a LayoutSpec v1 into renderer calls.

The compiler bridges LayoutSpec v1 (WHERE things go + WHAT type they are)
with a content_payload (the actual content) and a renderer (HOW to draw).

Usage:
    from pipeline.layout.layout_compile import compile_spec

    compile_spec(spec, scene_plan, renderer)

The renderer is expected to expose the following methods (all existing in
tools/renderer.py):
    _draw_figure(img, fig_info, region_dict)
    _draw_bullet(draw, text, region_dict, y_offset) → height
    _date_text(draw, text, region_dict, font, align)
    _to_px(region_dict) → (x, y, w, h)

The compiler does NOT handle builds/animations — those are still managed by
the existing `_apply_build_actions` path in the renderer. Its role is to
validate + translate LayoutSpec into the old regions dict format so the
existing renderer can work unchanged.
"""

import logging
from typing import Optional

from .layout_spec import LayoutSpec, Element, RENDER_GROUP, resolve_content_ref
from . import layout_validate

logger = logging.getLogger("layout_compile")


def compile_spec(
    spec: LayoutSpec,
    scene_plan: dict,
    renderer,
    *,
    run_repair: bool = True,
) -> dict:
    """Validate, repair, and extract a regions dict from a LayoutSpec.

    This is the main entry point called by the renderer. It:
      1. (Optionally) repairs the spec via layout_validate.repair().
      2. Derives a backward-compatible ``regions`` dict from element ids/boxes.
      3. Returns the (possibly repaired) regions dict and the repaired spec.

    Args:
        spec: A LayoutSpec v1 instance.
        scene_plan: The full scene_plan dict (used as content_payload for validation).
        renderer: The SlideRenderer instance (used for logging only here).
        run_repair: Whether to run validation/repair before compiling.

    Returns:
        dict with keys:
            "regions" — element_id → box dict (backward-compatible format)
            "spec"    — the repaired LayoutSpec dict
            "flags"   — repair flags dict
    """
    if run_repair:
        spec, repair_log, flags = layout_validate.repair(spec, scene_plan)
        for msg in repair_log:
            logger.info(f"[layout_compile] {msg}")
        if flags.get("needs_split_slide"):
            logger.warning(
                "[layout_compile] One or more elements may need a split slide (needs_split_slide=True)."
            )
    else:
        flags = {}

    # Build backward-compatible regions dict: element id → box dict
    regions = {elem.id: elem.box.to_dict() for elem in spec.elements}

    return {
        "regions": regions,
        "spec": spec.to_dict(),
        "flags": flags,
    }


def resolve_element_content(element: Element, scene_plan: dict):
    """Resolve the content for a LayoutSpec element from the scene plan.

    Handles the common content_refs used by the pipeline:
      "elements.title"   → scene_plan["elements"]["title"]
      "elements.figure"  → scene_plan["elements"]["figure"]
      "elements.bullets" → scene_plan["elements"]["bullets"]
      "elements.video"   → scene_plan["elements"]["video"]

    Returns None if the ref cannot be resolved.
    """
    if not element.content_ref:
        # Fall back to looking up by element id in elements dict
        return scene_plan.get("elements", {}).get(element.id)

    return resolve_content_ref(element.content_ref, scene_plan)


def get_element_style(element: Element, key: str, default=None):
    """Convenience accessor for element style properties."""
    return element.style.get(key, default)


def spec_to_layout_dict(spec: LayoutSpec) -> dict:
    """Convert a LayoutSpec to the merged_plan['layout'] dict format used by preacher.py.

    This is the canonical conversion point called in the merge step.
    """
    return {
        "template": spec.layout_type or "custom",
        "background_color": spec.background_color,
        "regions": spec.to_regions(),  # element id → box dict
        "spec": spec.to_dict(),        # full spec preserved for the renderer
    }
