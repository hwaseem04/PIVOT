"""
utils/grid_image.py
───────────────────
Generates a slide-canvas grid overlay image used for coordinate grounding
in the style planner.

A 20×20 grid divides the normalized [0, 1] canvas into 5% cells:
  • Columns  A–U  →  x = 0.00, 0.05, …, 1.00  (21 vertical   gridlines)
  • Rows    00–20 →  y = 0.00, 0.05, …, 1.00  (21 horizontal gridlines)

Grid ID format: <col-letter><2-digit-row>  — always 3 characters.
Examples:
  "A00"  →  top-left  corner  (x=0.00, y=0.00)
  "B01"  →  (x=0.05, y=0.05)
  "K10"  →  centre           (x=0.50, y=0.50)
  "U20"  →  bottom-right     (x=1.00, y=1.00)

Gemini receives this image alongside the prompt and picks two intersection
IDs per element:  {"tl": "B01", "br": "K10"}
The engine converts those IDs to exact normalized coordinates — no
free-form float generation needed.
"""

from __future__ import annotations

from PIL import Image, ImageDraw, ImageFont

# ── Module-level singleton (generated once per process) ─────────────────────

_GRID_IMG: "Image.Image | None" = None

def _reset_grid_cache() -> None:
    """Reset the cached grid image (call after any parameter changes)."""
    global _GRID_IMG
    _GRID_IMG = None

# Grid parameters — changing these also changes the ID ↔ coordinate mapping,
# so keep them in sync with layout_spec.Box.from_dict().
GRID_COLS: int = 20   # number of cells; 21 gridlines  (A … U)
GRID_ROWS: int = 20   # number of cells; 21 gridlines  (00 … 20)

# Output image size (half-scale of 1920×1080 — crisp but token-efficient)
GRID_W: int = 960
GRID_H: int = 540


def make_grid_image(
    cols: int = GRID_COLS,
    rows: int = GRID_ROWS,
    W: int = GRID_W,
    H: int = GRID_H,
) -> "Image.Image":
    """Return (and cache) the grid overlay PIL Image.

    The image shows:
    - Light-gray gridlines every 5% of the canvas
    - Slightly darker major gridlines every 20% (every 4th cell)
    - Column letters (A–U) along the top edge
    - Row numbers (00–20) along the left edge
    """
    global _GRID_IMG
    if _GRID_IMG is not None:
        return _GRID_IMG

    img  = Image.new("RGB", (W, H), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # ── Fonts ─────────────────────────────────────────────────────────────────
    # Edge labels (col letters, row numbers): 11 pt — must be legible on edges
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 11)
    except OSError:
        try:
            font = ImageFont.truetype("arial.ttf", 11)
        except OSError:
            font = ImageFont.load_default()

    # Intersection labels (e.g. "B01"): 7 pt — small enough to fit in a 48×27 cell
    try:
        small_font = ImageFont.truetype("DejaVuSans.ttf", 7)
    except OSError:
        try:
            small_font = ImageFont.truetype("arial.ttf", 7)
        except OSError:
            small_font = font

    # ── Grid line colours ────────────────────────────────────────────────────
    MINOR_COLOR = (210, 210, 210)   # light grey  — every cell boundary
    MAJOR_COLOR = (160, 160, 160)   # medium grey — every 4th line (20% steps)
    LABEL_COLOR = (60,  60,  60)    # dark grey   — text labels

    # ── Draw vertical lines (columns) ────────────────────────────────────────
    for i in range(cols + 1):            # 0 … 20
        px = int(i * W / cols)
        color = MAJOR_COLOR if i % 4 == 0 else MINOR_COLOR
        draw.line([(px, 0), (px, H)], fill=color, width=1)

        # Column label (A … U) at the top
        letter = chr(ord('A') + i)
        try:
            bbox = font.getbbox(letter)
            lw   = bbox[2] - bbox[0]
        except AttributeError:
            lw = 7
        lx = px - lw // 2
        draw.text((lx, 2), letter, fill=LABEL_COLOR, font=font)

    # ── Draw horizontal lines (rows) ─────────────────────────────────────────
    for j in range(rows + 1):            # 0 … 20
        py = int(j * H / rows)
        color = MAJOR_COLOR if j % 4 == 0 else MINOR_COLOR
        draw.line([(0, py), (W, py)], fill=color, width=1)

        # Row label (00 … 20) on the left edge
        label = f"{j:02d}"
        try:
            bbox = font.getbbox(label)
            lh   = bbox[3] - bbox[1]
        except AttributeError:
            lh = 8
        ly = py - lh // 2
        draw.text((2, ly), label, fill=LABEL_COLOR, font=font)

    # ── Intersection ID labels (e.g. "B01" at the crossing of col B and row 01) ──
    # These let the LLM read the full ID directly from the image without having
    # to mentally combine the edge labels.  We skip the last col/row (U/20) to
    # avoid labels being clipped at the canvas boundary.
    INTERSECT_COLOR = (150, 150, 150)   # lighter grey — readable but unobtrusive
    for i in range(cols):               # 0 … 19  (A … T)
        for j in range(rows):           # 0 … 19  (00 … 19)
            px = int(i * W / cols)
            py = int(j * H / rows)
            label = f"{chr(ord('A') + i)}{j:02d}"
            draw.text((px + 2, py + 1), label, fill=INTERSECT_COLOR, font=small_font)

    _GRID_IMG = img
    return img


def grid_id_to_norm(grid_id: str) -> float:
    """Convert a single axis grid label to a normalized [0, 1] float.

    Examples:
        grid_id_to_norm("A")  →  0.00
        grid_id_to_norm("B")  →  0.05
        grid_id_to_norm("K")  →  0.50
        grid_id_to_norm("U")  →  1.00
        grid_id_to_norm("01") →  0.05
        grid_id_to_norm("10") →  0.50
    """
    s = grid_id.strip().upper()
    if s.isalpha():
        return (ord(s[0]) - ord('A')) / GRID_COLS
    return int(s) / GRID_ROWS


def parse_grid_box(tl: str, br: str) -> tuple[float, float, float, float]:
    """Parse two grid IDs to (x, y, w, h) normalized coordinates.

    Args:
        tl: top-left  intersection ID, e.g. "B01"
        br: bottom-right intersection ID, e.g. "K10"

    Returns:
        (x, y, w, h) — normalized floats in [0, 1].

    Raises:
        ValueError: if the IDs are malformed or br ≤ tl on any axis.
    """
    tl = tl.strip().upper()
    br = br.strip().upper()

    if len(tl) < 2 or len(br) < 2:
        raise ValueError(f"Grid IDs must be ≥2 chars: got '{tl}', '{br}'")

    tl_col = ord(tl[0]) - ord('A')
    tl_row = int(tl[1:])
    br_col = ord(br[0]) - ord('A')
    br_row = int(br[1:])

    x = tl_col / GRID_COLS
    y = tl_row / GRID_ROWS
    w = max(1 / GRID_COLS, (br_col - tl_col) / GRID_COLS)
    h = max(1 / GRID_ROWS, (br_row - tl_row) / GRID_ROWS)
    return float(x), float(y), float(w), float(h)
