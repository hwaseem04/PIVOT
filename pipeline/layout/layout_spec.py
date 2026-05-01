"""
LayoutSpec v1 — standardized, open-ended slide layout representation.

A LayoutSpec describes WHERE elements live on the slide canvas using
normalized coordinates (0.0–1.0). It does NOT hold the actual content —
content is resolved at render time via content_ref dot-paths.

Element types:
  T   — Primary title
  ST  — Subtitle
  B   — Bullet list
  P   — Body paragraph
  EQ  — LaTeX equation
  L   — Sub-figure label (small, centered above/below a figure)
  META— Author names / logos / affiliations composite row
  F   — Paper figure / image asset
  D   — Architecture / flow diagram (image asset)
  CH  — Chart (bar, line, scatter, etc.) image
  TAB — Table image
  QR  — QR code (generated from a URL)
"""

from dataclasses import dataclass, field
from typing import Optional
import math

# ── Element type constants ──────────────────────────────────────────────────

ELEMENT_TYPES = {"T", "ST", "B", "P", "EQ", "L", "META", "F", "D", "CH", "TAB", "QR"}

# Maps element type → rendering group used by layout_compile
RENDER_GROUP = {
    "F":   "figure",
    "D":   "figure",
    "CH":  "figure",
    "TAB": "figure",
    "T":   "text",
    "ST":  "text",
    "B":   "bullets",
    "P":   "text",
    "L":   "text",
    "EQ":  "equation",
    "META":"meta",
    "QR":  "qr",
}

# ── Dataclasses ─────────────────────────────────────────────────────────────

@dataclass
class Box:
    """Normalized bounding box. All values in [0.0, 1.0]."""
    x: float
    y: float
    w: float
    h: float

    def overlaps(self, other: "Box", tolerance: float = 0.0) -> bool:
        """Return True if this box overlaps other (with optional tolerance gap)."""
        ax1, ay1 = self.x - tolerance, self.y - tolerance
        ax2, ay2 = self.x + self.w + tolerance, self.y + self.h + tolerance
        bx1, by1 = other.x, other.y
        bx2, by2 = other.x + other.w, other.y + other.h
        return ax1 < bx2 and ax2 > bx1 and ay1 < by2 and ay2 > by1

    def overlap_area(self, other: "Box") -> float:
        """Return normalized overlap area between the two boxes."""
        ix = max(0.0, min(self.x + self.w, other.x + other.w) - max(self.x, other.x))
        iy = max(0.0, min(self.y + self.h, other.y + other.h) - max(self.y, other.y))
        return ix * iy

    def to_dict(self) -> dict:
        return {"x": self.x, "y": self.y, "w": self.w, "h": self.h}

    @classmethod
    def from_dict(cls, d: dict) -> "Box":
        # ── Grid-ID format: {"tl": "B01", "br": "K10"} ──────────────────────
        # Columns A–U = x 0.00–1.00 (step 0.05); Rows 00–20 = y 0.00–1.00.
        if "tl" in d and "br" in d:
            from utils.grid_image import parse_grid_box
            x, y, w, h = parse_grid_box(d["tl"], d["br"])
            return cls(x=x, y=y, w=w, h=h)
        # ── Legacy normalized-float format: {"x": …, "y": …, "w": …, "h": …}
        return cls(x=float(d["x"]), y=float(d["y"]), w=float(d["w"]), h=float(d["h"]))

    def to_px(self, W: int = 1920, H: int = 1080) -> tuple:
        """Return (x_px, y_px, w_px, h_px) pixel rectangle."""
        return (
            int(self.x * W),
            int(self.y * H),
            int(self.w * W),
            int(self.h * H),
        )


@dataclass
class GlobalConstraints:
    no_overlap: bool = True
    no_overflow: bool = True
    min_font_size: int = 14

    def to_dict(self) -> dict:
        return {
            "no_overlap": self.no_overlap,
            "no_overflow": self.no_overflow,
            "min_font_size": self.min_font_size,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "GlobalConstraints":
        return cls(
            no_overlap=d.get("no_overlap", True),
            no_overflow=d.get("no_overflow", True),
            min_font_size=int(d.get("min_font_size", 14)),
        )


@dataclass
class Element:
    id: str
    type: str                          # one of ELEMENT_TYPES
    box: Box
    content_ref: Optional[str] = None # dot-path into content_payload (e.g. "elements.title")
    style: dict = field(default_factory=dict)
    constraints: dict = field(default_factory=dict)

    def __post_init__(self):
        if self.type not in ELEMENT_TYPES:
            raise ValueError(f"Unknown element type '{self.type}'. Must be one of {ELEMENT_TYPES}.")

    def to_dict(self) -> dict:
        d = {
            "id": self.id,
            "type": self.type,
            "box": self.box.to_dict(),
        }
        if self.content_ref is not None:
            d["content_ref"] = self.content_ref
        if self.style:
            d["style"] = self.style
        if self.constraints:
            d["constraints"] = self.constraints
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "Element":
        return cls(
            id=d["id"],
            type=d["type"],
            box=Box.from_dict(d["box"]),
            content_ref=d.get("content_ref"),
            style=d.get("style", {}),
            constraints=d.get("constraints", {}),
        )


@dataclass
class LayoutSpec:
    version: int
    elements: list  # list[Element]
    layout_type: str = ""
    layout_tags: list = field(default_factory=list)
    layout_signature: str = ""
    background_color: str = "#FFFFFF"
    global_constraints: GlobalConstraints = field(default_factory=GlobalConstraints)

    def to_dict(self) -> dict:
        return {
            "version": self.version,
            "layout_type": self.layout_type,
            "layout_tags": self.layout_tags,
            "layout_signature": self.layout_signature,
            "background_color": self.background_color,
            "elements": [e.to_dict() for e in self.elements],
            "global_constraints": self.global_constraints.to_dict(),
        }

    @classmethod
    def from_dict(cls, d: dict) -> "LayoutSpec":
        if d.get("version") != 1:
            raise ValueError(f"Unsupported LayoutSpec version: {d.get('version')}. Expected 1.")
        elements = [Element.from_dict(e) for e in d.get("elements", [])]
        return cls(
            version=1,
            elements=elements,
            layout_type=d.get("layout_type", ""),
            layout_tags=d.get("layout_tags", []),
            layout_signature=d.get("layout_signature", ""),
            background_color=d.get("background_color", "#FFFFFF"),
            global_constraints=GlobalConstraints.from_dict(d.get("global_constraints", {})),
        )

    def to_regions(self) -> dict:
        """Convert elements to old-style regions dict keyed by element id.
        Enables backward-compatible use with the existing renderer."""
        return {elem.id: elem.box.to_dict() for elem in self.elements}

    def get_element(self, elem_id: str) -> Optional[Element]:
        for e in self.elements:
            if e.id == elem_id:
                return e
        return None

    def get_font_size(self, elem_id: str, default: int = 24) -> int:
        elem = self.get_element(elem_id)
        if elem:
            return int(elem.style.get("font_size", default))
        return default


# ── Helpers ──────────────────────────────────────────────────────────────────

def sig_from_elements(elements: list) -> str:
    """Auto-generate a layout_signature string from an element list.

    Algorithm:
    1. Group elements into horizontal bands (rows) based on y-midpoint.
    2. Within each band, sort elements left-to-right.
    3. Represent each band as 'TYPE-TYPE-...' and join bands with '|'.

    Example: title at top, figure+bullets below → 'T|F-B'
    """
    if not elements:
        return ""

    # Compute midpoint for each element
    items = [(e.box.y + e.box.h / 2.0, e.box.x, e.type) for e in elements]

    # Cluster into bands using a simple 0.08 tolerance gap
    items_sorted = sorted(items, key=lambda t: t[0])
    bands = []
    current_band = [items_sorted[0]]
    for item in items_sorted[1:]:
        if abs(item[0] - current_band[-1][0]) < 0.08:
            current_band.append(item)
        else:
            bands.append(current_band)
            current_band = [item]
    bands.append(current_band)

    row_strs = []
    for band in bands:
        band_sorted = sorted(band, key=lambda t: t[1])  # sort by x
        row_strs.append("-".join(t[2] for t in band_sorted))

    return "|".join(row_strs)


def resolve_content_ref(content_ref: str, content_payload: dict):
    """Resolve a dot-path content_ref against content_payload.

    Example: "elements.figure" → content_payload["elements"]["figure"]
    Returns None if the path does not exist.
    """
    if not content_ref:
        return None
    parts = content_ref.split(".")
    obj = content_payload
    for part in parts:
        if isinstance(obj, dict):
            obj = obj.get(part)
        else:
            return None
        if obj is None:
            return None
    return obj
