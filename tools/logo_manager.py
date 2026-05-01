"""
Logo manager for title page generation.

3-tier fallback:
  1. Per-paper directory: <pdf_dir>/<pdf_stem>_logos/
  2. Online retrieval (Clearbit Logo API / Google Favicon)
  3. Placeholder (gray rounded rect with text)
"""

import logging
import requests
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

logger = logging.getLogger(__name__)


def resolve_logos(pdf_path: Path, affiliations: list, venue: str = "") -> dict:
    """
    Resolve logos for the title page.
    
    Args:
        pdf_path: Path to the input PDF
        affiliations: List of dicts with 'id', 'name', 'email_domain'
        venue: Conference/journal name (e.g. "CVPR 2025")
    
    Returns:
        {
            "conference": Path or None,
            "affiliations": [Path or None, ...]
        }
    """
    logos_dir = pdf_path.parent / f"{pdf_path.stem}_logos"
    result = {
        "conference": None,
        "affiliations": [],
    }
    
    # --- Conference logo ---
    result["conference"] = _resolve_single_logo(
        name="conference",
        logos_dir=logos_dir,
        filename="conference.png",
        domain=_venue_to_domain(venue),
        label=venue,
    )
    
    # --- Affiliation logos ---
    for aff in affiliations:
        aff_id = aff.get("id", 0)
        aff_name = aff.get("name", "")
        domain = aff.get("email_domain", "")
        
        logo_path = _resolve_single_logo(
            name=f"affiliation_{aff_id}",
            logos_dir=logos_dir,
            filename=f"affiliation_{aff_id}.png",
            domain=domain,
            label=aff_name,
        )
        result["affiliations"].append(logo_path)
    
    return result


def _resolve_single_logo(
    name: str,
    logos_dir: Path,
    filename: str,
    domain: str,
    label: str,
) -> Path | None:
    """Resolve a single logo with 3-tier fallback."""
    
    # Tier 1: Per-paper directory
    if logos_dir.exists():
        # Try exact filename and common variants
        for candidate in [filename, filename.replace(".png", ".jpg"), filename.replace(".png", ".jpeg")]:
            local_path = logos_dir / candidate
            if local_path.exists():
                logger.info(f"  Logo '{name}': found locally at {local_path}")
                return local_path
    
    # Tier 2: Online retrieval
    if domain:
        online_path = _fetch_logo_online(domain, logos_dir, filename)
        if online_path:
            logger.info(f"  Logo '{name}': fetched online for domain '{domain}'")
            return online_path
    
    # Tier 3: Placeholder
    placeholder_path = _generate_placeholder(label or name, logos_dir, filename)
    if placeholder_path:
        logger.info(f"  Logo '{name}': generated placeholder")
        return placeholder_path
    
    return None


def _fetch_logo_online(domain: str, save_dir: Path, filename: str) -> Path | None:
    """Try to fetch a logo from Clearbit or Google Favicon API."""
    if not domain:
        return None
    
    # Clean domain
    domain = domain.strip().lower()
    if domain.startswith("www."):
        domain = domain[4:]
    
    save_dir.mkdir(parents=True, exist_ok=True)
    save_path = save_dir / filename
    
    # Try Clearbit Logo API (higher quality)
    urls = [
        f"https://logo.clearbit.com/{domain}",
        f"https://www.google.com/s2/favicons?domain={domain}&sz=128",
    ]
    
    for url in urls:
        try:
            resp = requests.get(url, timeout=5)
            if resp.status_code == 200 and len(resp.content) > 100:
                # Verify it's a valid image
                save_path.write_bytes(resp.content)
                # Quick validation
                img = Image.open(save_path)
                img.verify()
                logger.info(f"  Fetched logo from {url}")
                return save_path
        except Exception as e:
            logger.debug(f"  Failed to fetch logo from {url}: {e}")
            if save_path.exists():
                save_path.unlink()
            continue
    
    return None


def _generate_placeholder(label: str, save_dir: Path, filename: str) -> Path | None:
    """Generate a placeholder logo: gray rounded rect with text."""
    if not label:
        return None
    
    save_dir.mkdir(parents=True, exist_ok=True)
    save_path = save_dir / filename
    
    # Create placeholder image
    w, h = 200, 80
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Rounded rectangle background
    draw.rounded_rectangle(
        [0, 0, w - 1, h - 1],
        radius=12,
        fill=(220, 220, 220, 255),
        outline=(180, 180, 180, 255),
        width=1,
    )
    
    # Text — truncate if too long
    display_text = label if len(label) <= 20 else label[:17] + "..."
    
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 14)
    except Exception:
        font = ImageFont.load_default()
    
    bbox = draw.textbbox((0, 0), display_text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    tx = (w - tw) // 2
    ty = (h - th) // 2
    draw.text((tx, ty), display_text, fill=(80, 80, 80, 255), font=font)
    
    img.save(save_path, "PNG")
    return save_path


def _venue_to_domain(venue: str) -> str:
    """Map common conference names to domains for logo retrieval."""
    if not venue:
        return ""
    
    venue_lower = venue.lower()
    mapping = {
        "cvpr": "cvpr.thecvf.com",
        "iccv": "iccv.thecvf.com",
        "eccv": "eccv.ecva.net",
        "neurips": "neurips.cc",
        "icml": "icml.cc",
        "iclr": "iclr.cc",
        "aaai": "aaai.org",
        "acl": "aclanthology.org",
        "emnlp": "emnlp.org",
        "sigir": "sigir.org",
    }
    
    for key, domain in mapping.items():
        if key in venue_lower:
            return domain
    
    return ""


def format_authors_display(authors: list, max_display: int = 8) -> str:
    """
    Format author list for display. Truncates if >max_display authors.
    Returns: "Author1, Author2, Author3, ..., Last Author"
    """
    if not authors:
        return ""
    
    names = [a.get("name", "") for a in authors if a.get("name")]
    
    if len(names) <= max_display:
        return ", ".join(names)
    
    # First 3 + ... + last
    display = names[:3] + ["..."] + [names[-1]]
    return ", ".join(display)


def format_affiliations_display(authors: list, affiliations: list) -> str:
    """
    Format affiliations for display with superscript numbers.
    Returns: "¹University A  ²Company B"
    """
    if not affiliations:
        return ""
    
    superscripts = "⁰¹²³⁴⁵⁶⁷⁸⁹"
    
    def to_superscript(n: int) -> str:
        return "".join(superscripts[int(d)] for d in str(n))
    
    parts = []
    for aff in affiliations:
        aff_id = aff.get("id", 0)
        name = aff.get("name", "")
        if name:
            parts.append(f"{to_superscript(aff_id)}{name}")
    
    return "  ".join(parts)


def format_authors_with_superscripts(authors: list, max_display: int = 8) -> str:
    """
    Format author names with affiliation superscripts.
    Returns: "Author1¹, Author2², Author3¹"
    """
    if not authors:
        return ""
    
    superscripts = "⁰¹²³⁴⁵⁶⁷⁸⁹"
    
    def to_superscript(n: int) -> str:
        return "".join(superscripts[int(d)] for d in str(n))
    
    # Build display list
    entries = []
    for a in authors:
        name = a.get("name", "")
        aff_id = a.get("affiliation_id", 0)
        if name:
            entries.append(f"{name}{to_superscript(aff_id)}")
    
    if len(entries) <= max_display:
        return ", ".join(entries)
    
    # Truncate: first 3 + ... + last
    display = entries[:3] + ["..."] + [entries[-1]]
    return ", ".join(display)
