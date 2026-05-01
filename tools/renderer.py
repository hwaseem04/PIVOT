import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import fitz # PyMuPDF
import textwrap
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips, CompositeVideoClip, VideoFileClip
import json
import logging

class SlideRenderer:
    def __init__(self, output_dir: Path, pdf_path: Path, tts_engine=None, planner_func=None):
        self.output_dir = output_dir
        self.pdf_path = pdf_path
        self.tts_engine = tts_engine
        self.planner_func = planner_func   # optional LLM for Gemini-based figure extraction
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.logger = logging.getLogger("SlideRenderer")

        # Layout constants
        self.W = 1920
        self.H = 1080
        self.MARGIN = 60
        self.TITLE_FONT_SIZE = 80
        self.BODY_FONT_SIZE = 48
        
        # Load fonts (fallback to default if necessary)
        self.title_font = self._load_font("Arial Bold.ttf", self.TITLE_FONT_SIZE)
        self.body_font = self._load_font("Arial.ttf", self.BODY_FONT_SIZE)
        # Title page fonts
        self.title_page_font = self._load_font("Arial Bold.ttf", 64)
        self.author_font = self._load_font("Arial.ttf", 36)
        self.affiliation_font = self._load_font("Arial.ttf", 28)
        self.venue_font = self._load_font("Arial Bold.ttf", 32)

    def _load_font(self, name, size):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            try:
                # macOS specific
                return ImageFont.truetype(f"/System/Library/Fonts/Supplemental/{name}", size)
            except OSError:
                return ImageFont.load_default()

    def _make_font(self, size: int):
        """Return a truetype body font at the requested size (falls back gracefully)."""
        return self._load_font("Arial.ttf", size)

    def render_scene(self, scene_plan: dict, scene_idx: int) -> str:
        """
        Render a full scene video based on the plan.
        Returns the path to the generated video file.
        """
        scene_dir = self.output_dir / f"scene_{scene_idx}"
        scene_dir.mkdir(exist_ok=True)

        layout = scene_plan.get("layout", {})
        elements = scene_plan.get("elements", {})
        builds = scene_plan.get("builds", [])

        # ── LayoutSpec v1: validate, repair, and extract regions ─────────────
        spec_dict = layout.get("spec")
        if spec_dict and isinstance(spec_dict, dict) and spec_dict.get("version") == 1:
            try:
                from pipeline.layout.layout_spec import LayoutSpec
                from pipeline.layout import layout_validate
                from pipeline.layout.layout_compile import compile_spec

                spec = LayoutSpec.from_dict(spec_dict)
                result = compile_spec(spec, scene_plan, self, run_repair=True)

                # Merge repaired regions back into layout (backward-compatible)
                layout = dict(layout)  # shallow copy so we don't mutate scene_plan
                layout["regions"] = result["regions"]
                # Preserve background_color from spec
                if "background_color" not in layout:
                    layout["background_color"] = spec_dict.get("background_color", "#FFFFFF")

                # ── Add standard target aliases ──────────────────────────────
                # Build actions use canonical targets ("figure", "bullets",
                # "title", "video"). If the LLM chose non-standard element IDs
                # (e.g. "architecture_diagram" instead of "figure"), we inject
                # aliases so _apply_build_actions can find them by type.
                from pipeline.layout.layout_spec import RENDER_GROUP
                _regions = dict(layout["regions"])
                _orig    = dict(_regions)   # immutable snapshot — always read elem boxes from here
                _added: set = set()
                _figure_count = 0
                for _elem in spec.elements:
                    _std = RENDER_GROUP.get(_elem.type)
                    if _std == "figure":
                        # Map 1st F/D/CH/TAB element → "figure",
                        #     2nd → "figure_2", 3rd → "figure_3", …
                        # Read from _orig (not _regions) so that earlier writes
                        # (e.g. _regions["figure"] = LEFT) don't corrupt later
                        # lookups for elements whose id happens to be "figure".
                        alias = "figure" if _figure_count == 0 else f"figure_{_figure_count + 1}"
                        if _elem.id in _orig:
                            _regions[alias] = _orig[_elem.id]
                            self.logger.debug(
                                f"Scene {scene_idx}: aliased region '{_elem.id}' → '{alias}'"
                            )
                        _figure_count += 1
                    elif (
                        _std in ("bullets", "title", "video", "equation")
                        and _std not in _regions
                        and _elem.id in _orig
                        and _std not in _added
                    ):
                        _regions[_std] = _orig[_elem.id]
                        _added.add(_std)
                        self.logger.debug(
                            f"Scene {scene_idx}: aliased region '{_elem.id}' → '{_std}'"
                        )
                layout["regions"] = _regions

                if result["flags"].get("needs_split_slide"):
                    self.logger.warning(
                        f"Scene {scene_idx}: layout validator flagged needs_split_slide. "
                        "Consider splitting content across two slides."
                    )
            except Exception as e:
                self.logger.warning(
                    f"Scene {scene_idx}: LayoutSpec v1 compile failed ({e}). "
                    "Falling back to layout.regions."
                )

        clips = []
        
        # Check if this is a title page
        template = layout.get("template", "")
        if template == "title_page":
            current_img = self._render_title_page(elements, layout)
        else:
            # Base image state
            current_img = self._create_base_slide(layout, elements)
        
        # Track all visible bullets across builds to prevent overlap
        all_visible_bullets = set()

        for i, build in enumerate(builds):
            # Apply build actions to current image
            current_img, all_visible_bullets = self._apply_build_actions(
                current_img, build.get("actions", []), elements, layout, all_visible_bullets
            )
            
            # Save frame for debugging
            frame_path = scene_dir / f"build_{i}.png"
            current_img.save(frame_path)
            
            # Generate audio for this build step
            audio_text = build.get("audio_segment", "")
            audio_path = self._generate_audio(audio_text, scene_dir / f"audio_{i}.mp3")
            
            audio_clip = None
            if audio_path and Path(audio_path).exists():
                audio_clip = AudioFileClip(str(audio_path))
                # Audio drives the duration — no truncation
                duration = audio_clip.duration
            else:
                # Fallback: use time_offset_sec to calculate duration
                current_start = build.get("time_offset_sec", 0.0)
                if i < len(builds) - 1:
                    next_start = builds[i+1].get("time_offset_sec", current_start + 2.0)
                    duration = max(0.5, next_start - current_start)
                else:
                    total_time = scene_plan.get("time_allocation_sec", 7.0)
                    duration = max(0.5, total_time - current_start)
            
            video_clip = ImageClip(str(frame_path)).set_duration(duration)
            
            # --- OVERLAY Custom Asset Videos if present in this build ---
            # If the base elements have a 'video' block and an action says 'show video'
            # we need to composite it over the static slide.
            # video_overlays = []
            # for action in build.get("actions", []):
            #     atype = action.get("type")
            #     target = action.get("target")
            #     if (atype == "show" or atype == "fade_in") and target == "video" and "video" in elements:
            #         vid_info = elements["video"]
            #         vid_region = layout.get("regions", {}).get("video")
            #         if vid_info and vid_region:
            #             vid_path = self.pdf_path.parent / f"{self.pdf_path.stem} assets" / vid_info.get("path", "")
            #             if vid_path.exists():
            #                 # Load the video snippet
            #                 vx, vy, vw, vh = self._to_px(vid_region)
            #                 try:
            #                     # We loop the snippet if it's shorter than the duration,
            #                     # or cut it if it's longer to fit the build duration.
            #                     sub_clip = VideoFileClip(str(vid_path)).resize((vw, vh)).set_position((vx, vy))
            #                     if sub_clip.duration < duration:
            #                         import moviepy.video.fx.all as vfx
            #                         sub_clip = sub_clip.fx(vfx.loop, duration=duration)
            #                     else:
            #                         sub_clip = sub_clip.subclip(0, duration)
            #                     
            #                     video_overlays.append(sub_clip)
            #                 except Exception as e:
            #                     self.logger.error(f"Failed to overlay video {vid_path}: {e}")

            # if video_overlays:
            #     video_clip = CompositeVideoClip([video_clip] + video_overlays).set_duration(duration)

            if audio_clip:
                video_clip = video_clip.set_audio(audio_clip)
                
            clips.append(video_clip)
            
        # Concatenate
        final_clip = concatenate_videoclips(clips)
        output_path = scene_dir / f"scene{scene_idx}.mp4"
        final_clip.write_videofile(str(output_path), fps=24, logger=None)
        
        return str(output_path)

    def _create_base_slide(self, layout, elements):
        img = Image.new('RGB', (self.W, self.H), (255, 255, 255)) # White background
        draw = ImageDraw.Draw(img)
        
        # Check template/regions
        regions = layout.get("regions", {})
        
        # ALWAYS draw title first if it exists
        if "title" in elements:
             title_region = regions.get("title", {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1})
             self._date_text(draw, elements["title"], title_region, self.title_font, align="center")
             
        # Other elements are drawn by _apply_build_actions dynamically?
        # OR we draw the "background" elements here?
        # The prompt says "actions: show title", "show figure". 
        # So we start blank (except maybe background color) and let builds add things.
        # But `_create_base_slide` implies the starting state.
        # Let's verify start state. Usually step 0 action is "show title".
        # So base slide is just background.
        
        return img

    def _render_title_page(self, elements, layout):
        """Render a title page with paper title, authors, affiliations, venue, and logos."""
        bg_color = layout.get("background_color", "#FFFFFF")
        img = Image.new('RGB', (self.W, self.H), bg_color)
        draw = ImageDraw.Draw(img)
        regions = layout.get("regions", {})
        
        # --- Draw paper title (with text wrapping) ---
        title_text = elements.get("title", "")
        if title_text and "title" in regions:
            title_region = regions["title"]
            tx, ty, tw, th = self._to_px(title_region)
            
            # Wrap title text to fit region width
            lines = self._wrap_text(title_text, tw, self.title_page_font)
            line_height = self.title_page_font.getbbox("Ay")[3] + 8
            
            # Center vertically within region
            total_text_height = len(lines) * line_height
            start_y = ty + max(0, (th - total_text_height) // 2)
            
            for line in lines:
                line_bbox = self.title_page_font.getbbox(line)
                line_w = line_bbox[2] - line_bbox[0]
                line_x = tx + (tw - line_w) // 2  # Center each line
                draw.text((line_x, start_y), line, fill="black", font=self.title_page_font)
                start_y += line_height
        
        # --- Draw authors ---
        authors_text = elements.get("authors", "")
        if authors_text and "authors" in regions:
            authors_region = regions["authors"]
            ax, ay, aw, ah = self._to_px(authors_region)
            
            # Wrap if too wide
            lines = self._wrap_text(authors_text, aw, self.author_font)
            line_height = self.author_font.getbbox("Ay")[3] + 6
            total_h = len(lines) * line_height
            start_y = ay + max(0, (ah - total_h) // 2)
            
            for line in lines:
                line_bbox = self.author_font.getbbox(line)
                line_w = line_bbox[2] - line_bbox[0]
                line_x = ax + (aw - line_w) // 2
                draw.text((line_x, start_y), line, fill=(60, 60, 60), font=self.author_font)
                start_y += line_height
        
        # --- Draw affiliations ---
        aff_text = elements.get("affiliations", "")
        if aff_text and "affiliations" in regions:
            aff_region = regions["affiliations"]
            fx, fy, fw, fh = self._to_px(aff_region)
            
            aff_bbox = self.affiliation_font.getbbox(aff_text)
            aff_w = aff_bbox[2] - aff_bbox[0]
            aff_x = fx + (fw - aff_w) // 2
            aff_y = fy + (fh - (aff_bbox[3] - aff_bbox[1])) // 2
            draw.text((aff_x, aff_y), aff_text, fill=(100, 100, 100), font=self.affiliation_font)
        
        # --- Draw venue ---
        venue_text = elements.get("venue", "")
        if venue_text and "venue" in regions:
            venue_region = regions["venue"]
            vx, vy, vw, vh = self._to_px(venue_region)
            
            venue_bbox = self.venue_font.getbbox(venue_text)
            venue_w = venue_bbox[2] - venue_bbox[0]
            venue_x = vx + (vw - venue_w) // 2
            venue_y = vy + (vh - (venue_bbox[3] - venue_bbox[1])) // 2
            draw.text((venue_x, venue_y), venue_text, fill=(40, 40, 40), font=self.venue_font)
        
        # --- Place conference logo ---
        conf_logo = elements.get("conference_logo")
        if conf_logo and isinstance(conf_logo, dict) and "conference_logo" in regions:
            self._place_logo(img, conf_logo.get("path", ""), regions["conference_logo"])
        
        # --- Place affiliation logos ---
        aff_logos = elements.get("affiliation_logos", [])
        if aff_logos and isinstance(aff_logos, list) and "affiliation_logos" in regions:
            aff_region = regions["affiliation_logos"]
            rx, ry, rw, rh = self._to_px(aff_region)
            
            # Space logos evenly across the region
            n_logos = len(aff_logos)
            if n_logos > 0:
                slot_w = rw // n_logos
                for i, logo_info in enumerate(aff_logos):
                    if isinstance(logo_info, dict):
                        logo_path = logo_info.get("path", "")
                    else:
                        logo_path = str(logo_info)
                    
                    # Create a sub-region for this logo
                    sub_region = {
                        "x": aff_region["x"] + (i * aff_region["w"] / n_logos),
                        "y": aff_region["y"],
                        "w": aff_region["w"] / n_logos,
                        "h": aff_region["h"],
                    }
                    self._place_logo(img, logo_path, sub_region)
        
        return img
    
    def _place_logo(self, img, logo_path, region):
        """Place a logo image into the given region, preserving aspect ratio."""
        if not logo_path or not Path(logo_path).exists():
            return
        
        try:
            logo = Image.open(logo_path)
            # Convert to RGBA if needed
            if logo.mode != 'RGBA':
                logo = logo.convert('RGBA')
            
            rx, ry, rw, rh = self._to_px(region)
            
            # Scale logo to fit region while preserving aspect ratio
            logo_ratio = logo.width / logo.height
            region_ratio = rw / rh
            
            if logo_ratio > region_ratio:
                new_w = int(rw * 0.9)  # 90% of region width
                new_h = int(new_w / logo_ratio)
            else:
                new_h = int(rh * 0.9)
                new_w = int(new_h * logo_ratio)
            
            if new_w < 1 or new_h < 1:
                return
            
            logo = logo.resize((new_w, new_h), Image.LANCZOS)
            
            # Center in region
            paste_x = rx + (rw - new_w) // 2
            paste_y = ry + (rh - new_h) // 2
            
            # Paste with transparency
            img.paste(logo, (paste_x, paste_y), logo if logo.mode == 'RGBA' else None)
            
        except Exception as e:
            self.logger.warning(f"Failed to place logo {logo_path}: {e}")

    def _apply_build_actions(self, img, actions, elements, layout, cumulative_visible_bullets=None):
        new_img = img.copy()
        draw = ImageDraw.Draw(new_img)
        regions = layout.get("regions", {})

        # Track cumulative visible bullets across all builds
        if cumulative_visible_bullets is None:
            cumulative_visible_bullets = set()

        # Collect new bullet indices from this build's actions
        for action in actions:
            atype = action.get("type")
            target = action.get("target")

            if (atype == "show" or atype == "fade_in") and target and target.startswith("bullets"):
                try:
                    idx = int(target.split("[")[1].strip("]"))
                    cumulative_visible_bullets.add(idx)
                except:
                    pass

        # Render non-bullet actions
        for action in actions:
            atype = action.get("type")
            target = action.get("target")

            # Skip bullet actions (handled separately below)
            if target and target.startswith("bullets"):
                continue

            if atype == "show" or atype == "fade_in":
                content = None
                region = None

                if target == "title":
                    content = elements.get("title")
                    region = regions.get("title")
                    if content and region:
                        self._date_text(draw, content, region, self.title_font, align="center")

                elif target == "subtitle":
                    content = elements.get("subtitle")
                    region = regions.get("subtitle")
                    if content and region:
                        subtitle_font = self._make_font(28)
                        self._date_text(draw, content, region, subtitle_font, align="center")

                elif target == "figure":
                    fig_info = elements.get("figure")
                    region = regions.get("figure")
                    if fig_info and region:
                        self._draw_figure(new_img, fig_info, region)

                elif target and target.startswith("figure_") and target[7:].isdigit():
                    # Handle indexed figures: figure_2, figure_3, etc.
                    fig_info = elements.get(target)
                    region = regions.get(target)
                    if fig_info and region:
                        self._draw_figure(new_img, fig_info, region)

                elif (
                    target == "equation"
                    or target == "equations"
                    or (target and (
                        target.startswith("equation[")
                        or target.startswith("equations[")
                    ))
                ):
                    # Covers: "equation", "equations", "equation[0]", "equations[0]"
                    eq_content = elements.get("equations") or elements.get("equation")
                    region = (
                        regions.get("equations")
                        or regions.get("equation")
                        or regions.get("polynomial_equations")
                    )
                    if eq_content and region:
                        self._draw_equations(new_img, draw, eq_content, region, layout)

                elif target == "video":
                    pass  # disabled — compositing handled by moviepy

                else:
                    # Generic handling for any other target
                    # Check if this target corresponds to an EQ element via spec
                    spec_dict = layout.get("spec")
                    is_eq_target = False
                    if spec_dict and isinstance(spec_dict, dict):
                        from pipeline.layout.layout_spec import RENDER_GROUP
                        for elem in spec_dict.get("elements", []):
                            if elem.get("id") == target and RENDER_GROUP.get(elem.get("type", "")) == "equation":
                                is_eq_target = True
                                break

                    if is_eq_target:
                        eq_content = elements.get("equations") or elements.get("equation") or elements.get(target)
                        region = regions.get(target)
                        if eq_content and region:
                            self._draw_equations(new_img, draw, eq_content, region, layout)
                    else:
                        element_key = action.get("content_ref", target)
                        if element_key in elements:
                            content = elements[element_key]
                            region = regions.get(target)
                            if region:
                                if isinstance(content, str):
                                    font = self.title_font if "title" in target.lower() else self.body_font
                                    self._date_text(draw, content, region, font, align="center" if "title" in target.lower() else "left")
                                elif isinstance(content, dict) and content.get("type") == "paper_figure":
                                    self._draw_figure(new_img, content, region)

            elif atype == "highlight":
                 bbox = action.get("target_bbox")
                 if bbox:
                     self._draw_highlight(draw, bbox)

        # Redraw ALL visible bullets in correct stacked positions
        # This clears and redraws the bullet region to prevent overlap
        if cumulative_visible_bullets:
            bullets = elements.get("bullets", [])
            bullet_region = regions.get("bullets")

            if bullet_region and bullets:
                # Clear the bullet region first (fill with background color)
                bx, by, bw, bh = self._to_px(bullet_region)
                bg_color = layout.get("background_color", "#FFFFFF")
                draw.rectangle([bx, by, bx + bw, by + bh], fill=bg_color)

                # ── Fixed bullet font size (36px) ────────────────────────────
                # We use a fixed readable size rather than shrinking.
                # The low-level planner is responsible for not generating too
                # many / too verbose bullets (enforced via Canvas Constraints).
                BULLET_FONT_SIZE = 36
                BULLET_INDENT = 30
                LINE_SPACING = 1.15
                BULLET_GAP = 10

                bullet_font = self._make_font(BULLET_FONT_SIZE)
                bullet_y_offset = 0

                for idx in sorted(cumulative_visible_bullets):
                    if idx < len(bullets):
                        # Stop drawing if we've exhausted the region height
                        if bullet_y_offset >= bh:
                            self.logger.debug(
                                f"Bullet region full at offset {bullet_y_offset}px "
                                f"(region h={bh}px); remaining bullets clipped."
                            )
                            break
                        content = bullets[idx]
                        height_used = self._draw_bullet(draw, content, bullet_region, bullet_y_offset, font=bullet_font)
                        bullet_y_offset += height_used + BULLET_GAP

        return new_img, cumulative_visible_bullets

    def _draw_figure(self, img, fig_info, region):
        # Extract figure from PDF
        try:
            ref_text = fig_info.get('ref', '')
            caption_text = fig_info.get('caption', '')
            
            # Determine type
            etype = 'image'
            if 'table' in ref_text.lower():
                etype = 'table'
            
            # Use a filename based on the reference label to avoid ordinal collisions
            safe_ref = ref_text.replace(" ", "_").replace(".", "").lower()
            temp_fig_path = self.output_dir / f"extracted_{safe_ref}.png"
            
            # --- Extraction: try Gemini vision first, then Docling fallback ---
            extracted = ""
            if self.planner_func is not None:
                from utils.slides import get_figure_via_gemini
                extracted = get_figure_via_gemini(
                    str(self.pdf_path), ref_text, caption_text,
                    str(temp_fig_path), self.planner_func,
                )

            if not (extracted and Path(extracted).exists() and Path(extracted).stat().st_size > 0):
                # Fallback: Docling caption-matching
                from utils.slides import get_specific_element
                extracted = get_specific_element(
                    str(self.pdf_path), etype, ref_text, caption_text, str(temp_fig_path)
                )

            x, y, w, h = self._to_px(region)
            if Path(extracted).exists() and Path(extracted).stat().st_size > 0:
                # Load and draw
                fig_img = Image.open(extracted)
                
                # Scale to fill the region as much as possible while preserving
                # aspect ratio.  Unlike thumbnail(), this ALSO upscales figures
                # whose extracted PNG is smaller than the assigned box (e.g. a
                # 300×300 px diagram in a 700×750 px region).
                scale = min(w / fig_img.width, h / fig_img.height)
                new_w = max(1, round(fig_img.width  * scale))
                new_h = max(1, round(fig_img.height * scale))
                fig_img = fig_img.resize((new_w, new_h), Image.Resampling.LANCZOS)

                # Center in region
                draw_x = x + (w - fig_img.width) // 2
                draw_y = y + (h - fig_img.height) // 2
                
                img.paste(fig_img, (draw_x, draw_y))
                return

            # Fallback if extraction fails
            draw = ImageDraw.Draw(img)
            draw.rectangle([x, y, x+w, y+h], outline="blue", width=5)
            draw.text((x+50, y+50), f"FIGURE: {ref_text} (Extraction Failed)", fill="blue", font=self.body_font)
            
        except Exception as e:
            self.logger.error(f"Figure extraction failed: {e}")
            # Draw error placeholder
            x, y, w, h = self._to_px(region)
            draw = ImageDraw.Draw(img)
            draw.rectangle([x, y, x+w, y+h], outline="red", width=5)

        return None

    def _generate_audio(self, text, output_path):
        if not text:
             return None
        
        if self.tts_engine:
            try:
                if hasattr(self.tts_engine, 'return_audio'):
                     audio_url = self.tts_engine.return_audio(text)
                     import requests
                     resp = requests.get(audio_url)
                     if resp.status_code == 200:
                         with open(output_path, "wb") as f:
                             f.write(resp.content)
                         return str(output_path)
            except Exception as e:
                self.logger.error(f"TTS failed: {e}")
        return None

    def _draw_bullet(self, draw, text, region, bullet_y_offset=0, font=None):
        """
        Draw a bullet point with automatic text wrapping.

        Args:
            draw: PIL ImageDraw object
            text: Bullet text content
            region: Region dictionary with normalized coordinates
            bullet_y_offset: Y offset in pixels from region top (for dynamic positioning)
            font: PIL ImageFont to use (defaults to self.body_font)

        Returns:
            Height in pixels consumed by this bullet (including wrapping)
        """
        if not region:
            return 0

        if font is None:
            font = self.body_font

        x, y, w, h = self._to_px(region)

        # Constants for bullet formatting
        BULLET_CHAR = "• "
        BULLET_INDENT = 30  # Pixels for bullet character
        LINE_SPACING = 1.15  # Standard line spacing (like Google Slides default)

        # Calculate available width for text (excluding bullet character)
        available_width = w - BULLET_INDENT - 20  # 20px right margin

        # Get font metrics for proper line height calculation
        try:
            ascent, descent = font.getmetrics()
            font_height = ascent + descent
        except AttributeError:
            bbox = font.getbbox("Ay")
            font_height = bbox[3] - bbox[1]

        # Apply standard line spacing (1.15x like Google Slides)
        line_height = int(font_height * LINE_SPACING)

        # Word-wrap the text
        wrapped_lines = self._wrap_text(text, available_width, font)

        # Calculate starting position
        current_y = y + bullet_y_offset

        # Draw bullet character on first line
        draw.text((x, current_y), BULLET_CHAR, fill="black", font=font)

        # Region bottom boundary in absolute pixels
        region_bottom = y + int(region["h"] * self.H)

        # Draw text lines with proper indentation
        lines_drawn = 0
        for i, line in enumerate(wrapped_lines):
            # Clip: stop drawing if line would exceed the region bottom
            if current_y >= region_bottom:
                break
            text_x = x + BULLET_INDENT
            draw.text((text_x, current_y), line, fill="black", font=font)
            current_y += line_height
            lines_drawn += 1

        # Return total height consumed (only drawn lines)
        total_height = lines_drawn * line_height
        return total_height

    @staticmethod
    def _repair_equation_escapes(text: str) -> str:
        """Repair common JSON-mangled LaTeX backslash sequences.

        LLMs sometimes emit single-backslash LaTeX commands in JSON strings.
        Python's eval() (used to parse LLM responses) then interprets the
        escape sequences as control characters, e.g.:
          - \\a  → BEL  (0x07) — intended: \\alpha, \\approx
          - \\b  → BS   (0x08) — intended: \\beta,  \\bar, \\begin
          - \\t  → HT   (0x09) — intended: \\theta, \\tau
          - \\v  → VT   (0x0B) — intended: \\vdots, \\vee
          - \\f  → FF   (0x0C) — intended: \\frac,  \\forall
          - \\r  → CR   (0x0D) — intended: \\right, \\rho

        This method maps those control characters back to their LaTeX equivalents.
        """
        _CONTROL_TO_LATEX = {
            '\x07': '\\a',   # BEL       → \a  (e.g. \alpha, \approx)
            '\x08': '\\b',   # backspace → \b  (e.g. \beta, \bar, \begin)
            '\x09': '\\t',   # tab       → \t  (e.g. \theta, \tau)
            '\x0b': '\\v',   # vert-tab  → \v  (e.g. \vdots, \vee)
            '\x0c': '\\f',   # form-feed → \f  (e.g. \frac, \forall)
            '\x0d': '\\r',   # CR        → \r  (e.g. \right, \rho)
        }
        for ctrl, repl in _CONTROL_TO_LATEX.items():
            text = text.replace(ctrl, repl)
        return text

    @staticmethod
    def _to_latex_math(text: str) -> str:
        """
        Convert a plain-text / pseudo-LaTeX equation string to a matplotlib
        mathtext-compatible LaTeX math string.  Only safe, unambiguous
        substitutions are made.
        """
        import re
        t = text.strip()

        # Greek letters (lower then upper, longest names first to avoid
        # partial matches, e.g. 'epsilon' before 'psi')
        _GREEK_LOWER = [
            'epsilon', 'theta', 'lambda', 'sigma', 'omega',
            'alpha', 'beta', 'gamma', 'delta', 'kappa', 'mu', 'nu',
            'xi', 'pi', 'rho', 'tau', 'phi', 'chi', 'psi', 'eta',
        ]
        _GREEK_UPPER = [
            'Epsilon', 'Theta', 'Lambda', 'Sigma', 'Omega',
            'Gamma', 'Delta', 'Xi', 'Pi', 'Phi', 'Psi',
        ]
        for name in _GREEK_LOWER + _GREEK_UPPER:
            t = re.sub(rf'\b{name}\b', rf'\\{name}', t)

        # Named ML/DL functions → \mathrm{}
        for fn in ['GELU', 'ReLU', 'SiLU', 'softmax', 'sigmoid', 'Softmax']:
            t = re.sub(rf'\b{fn}\b', rf'\\mathrm{{{fn}}}', t)

        # Standard math functions → LaTeX built-ins
        for fn in ['tanh', 'exp', 'log', 'sin', 'cos', 'max', 'min',
                   'inf', 'sup', 'det', 'dim']:
            t = re.sub(rf'\b{fn}\b', rf'\\{fn}', t)

        return t

    def _render_equation_image(self, eq_text: str, max_width: int,
                               font_size: int = 34) -> 'Image.Image | None':
        """
        Render a single equation string as a PIL RGBA Image using
        matplotlib's mathtext renderer (LaTeX-quality, no external LaTeX
        installation required).  Returns None on any failure.
        """
        try:
            import re
            import io
            import matplotlib
            matplotlib.use('Agg')            # non-interactive backend
            import matplotlib.pyplot as plt

            # ── Repair JSON-mangled LaTeX escape sequences ───────────────────
            # e.g. LLM wrote "\frac" in JSON → parsed as form-feed + "rac"
            eq_text = self._repair_equation_escapes(eq_text)

            # ── Strip common label prefixes: "Eq. 6:", "(6)", etc. ──────────
            clean = re.sub(
                r'^(?:Eq(?:uation)?\.?\s*\d+\s*[:\.)]\s*|\(\d+\)\s*)',
                '', eq_text.strip(), flags=re.IGNORECASE
            ).strip()

            # ── Convert to LaTeX math ────────────────────────────────────────
            # If the LLM already emitted LaTeX commands (backslash present),
            # skip auto-substitution to avoid double-escaping.
            if '\\' in clean:
                latex_body = clean
            else:
                latex_body = self._to_latex_math(clean)
            math_str = f'${latex_body}$'

            # ── Render via matplotlib ────────────────────────────────────────
            DPI = 150
            # Generous initial size; we crop tightly after rendering.
            fig_w_in = max(2.0, max_width / DPI)
            fig, ax = plt.subplots(figsize=(fig_w_in, 1.6))
            ax.set_axis_off()
            fig.patch.set_alpha(0.0)    # transparent background
            ax.patch.set_alpha(0.0)

            ax.text(
                0.5, 0.5, math_str,
                ha='center', va='center',
                fontsize=font_size,
                color='#1E2878',        # dark navy blue
                transform=ax.transAxes,
            )

            buf = io.BytesIO()
            fig.savefig(
                buf, format='png', dpi=DPI,
                bbox_inches='tight', transparent=True,
                pad_inches=0.08,
            )
            plt.close(fig)
            buf.seek(0)

            eq_img = Image.open(buf).convert('RGBA')

            # ── Scale down if wider than the available region ───────────────
            if eq_img.width > max_width:
                scale  = max_width / eq_img.width
                eq_img = eq_img.resize(
                    (max_width, int(eq_img.height * scale)),
                    Image.LANCZOS,
                )

            return eq_img

        except Exception as e:
            self.logger.debug(
                f"Equation matplotlib render failed for '{eq_text[:60]}': {e}"
            )
            return None

    def _draw_equations(self, img_canvas, draw, equations, region, layout):
        """
        Render equations into a slide region.

        Attempts LaTeX-quality typesetting via matplotlib mathtext for each
        equation, pasting the resulting image onto *img_canvas*.  Any equation
        whose render fails falls back to plain styled text via *draw*.

        Args:
            img_canvas: PIL Image — the slide image to paste equation images onto
            draw:        PIL ImageDraw — used for text fallback and background fill
            equations:   str or list[str] — the equation content(s)
            region:      Region dict with normalized coordinates
            layout:      full layout dict (for background_color)
        """
        if not region or not equations:
            return

        # ── Normalise to list ────────────────────────────────────────────────
        if isinstance(equations, str):
            eq_list = [equations]
        elif isinstance(equations, list):
            eq_list = [str(e) for e in equations if e]
        else:
            eq_list = [str(equations)]

        x, y, w, h = self._to_px(region)

        # ── Clear region background ──────────────────────────────────────────
        bg_color = layout.get("background_color", "#FFFFFF")
        draw.rectangle([x, y, x + w, y + h], fill=bg_color)

        # ── Attempt to render each equation as a matplotlib image ────────────
        FALLBACK_FONT_SIZE = max(22, self.BODY_FONT_SIZE - 6)
        fallback_font      = self._make_font(FALLBACK_FONT_SIZE)
        ITEM_GAP           = 14   # px between stacked equations

        items = []  # list of ('image', PIL.Image) | ('text', str)
        for eq in eq_list:
            rendered = self._render_equation_image(eq, w - 20)
            if rendered is not None:
                items.append(('image', rendered))
            else:
                items.append(('text', eq))

        # ── Calculate total height needed ────────────────────────────────────
        def _item_height(kind, item):
            if kind == 'image':
                return item.height
            # text fallback: measure wrapped lines
            try:
                ascent, descent = fallback_font.getmetrics()
                line_h = int((ascent + descent) * 1.35)
            except AttributeError:
                bb = fallback_font.getbbox("Ay")
                line_h = int((bb[3] - bb[1]) * 1.35)
            lines = self._wrap_text(item, w - 20, fallback_font)
            return line_h * len(lines)

        total_h_needed = sum(_item_height(k, v) for k, v in items)
        total_h_needed += ITEM_GAP * max(0, len(items) - 1)

        # ── Pre-scale ALL image items uniformly if the stack overflows ───────
        # This ensures every equation gets a proportional share of the region
        # rather than the first one consuming all available space.
        if total_h_needed > h and h > 0:
            scale = h / total_h_needed
            scaled_items = []
            for kind, item in items:
                if kind == 'image':
                    new_w = max(1, int(item.width * scale))
                    new_h = max(1, int(item.height * scale))
                    scaled_items.append(('image', item.resize((new_w, new_h), Image.LANCZOS)))
                else:
                    scaled_items.append((kind, item))
            items = scaled_items
            # Recompute total height after scaling
            total_h_needed = sum(_item_height(k, v) for k, v in items)
            total_h_needed += ITEM_GAP * max(0, len(items) - 1)

        # ── Vertically center the stack in the region ────────────────────────
        current_y    = y + max(0, (h - total_h_needed) // 2)
        region_bottom = y + h

        for kind, item in items:
            if current_y >= region_bottom:
                break

            if kind == 'image':
                # Centre horizontally; guard against residual overflow
                avail_h = region_bottom - current_y
                if avail_h <= 4:
                    break  # Not enough space for any more items
                if item.height > avail_h:
                    scale = avail_h / item.height
                    new_w = max(1, int(item.width * scale))
                    item = item.resize((new_w, avail_h), Image.LANCZOS)
                paste_x = x + max(0, (w - item.width) // 2)
                img_canvas.paste(item, (paste_x, current_y), item)
                current_y += item.height + ITEM_GAP

            else:
                # Fallback: plain dark-blue centered text
                try:
                    ascent, descent = fallback_font.getmetrics()
                    line_h = int((ascent + descent) * 1.35)
                except AttributeError:
                    bb = fallback_font.getbbox("Ay")
                    line_h = int((bb[3] - bb[1]) * 1.35)

                for line in self._wrap_text(item, w - 20, fallback_font):
                    if current_y >= region_bottom:
                        break
                    lbbox = fallback_font.getbbox(line)
                    lw    = lbbox[2] - lbbox[0]
                    draw_x = x + max(0, (w - lw) // 2)
                    draw.text((draw_x, current_y), line,
                              fill=(30, 30, 120), font=fallback_font)
                    current_y += line_h
                current_y += ITEM_GAP

    def _wrap_text(self, text, max_width, font):
        """
        Wrap text to fit within max_width using the given font.

        Args:
            text: Text to wrap
            max_width: Maximum width in pixels
            font: PIL ImageFont object

        Returns:
            List of wrapped text lines
        """
        words = text.split()
        lines = []
        current_line = []

        for word in words:
            # Test if adding this word exceeds max width
            test_line = ' '.join(current_line + [word])
            bbox = font.getbbox(test_line)
            text_width = bbox[2] - bbox[0]

            if text_width <= max_width:
                current_line.append(word)
            else:
                # Current line is full, start new line
                if current_line:
                    lines.append(' '.join(current_line))
                    current_line = [word]
                else:
                    # Single word is too long, force it on its own line
                    lines.append(word)
                    current_line = []

        # Add remaining words
        if current_line:
            lines.append(' '.join(current_line))

        return lines if lines else [text]

    def _date_text(self, draw, text, region, font, align="left"):
        """Draw text with automatic word-wrapping clipped to the region box."""
        if not region: return
        x, y, w, h = self._to_px(region)

        lines = self._wrap_text(text, w, font)

        # Compute line height from font metrics
        try:
            ascent, descent = font.getmetrics()
            line_height = ascent + descent + 4
        except AttributeError:
            bbox = font.getbbox("Ay")
            line_height = (bbox[3] - bbox[1]) + 4

        # Vertically center the text block within the region
        total_text_h = len(lines) * line_height
        current_y = y + max(0, (h - total_text_h) // 2)

        for line in lines:
            # Clip: stop if we're past the bottom of the region
            if current_y >= y + h:
                break
            if align == "center":
                lbbox = font.getbbox(line)
                lw = lbbox[2] - lbbox[0]
                draw_x = x + max(0, (w - lw) // 2)
            else:
                draw_x = x
            draw.text((draw_x, current_y), line, fill="black", font=font)
            current_y += line_height

    def _draw_highlight(self, draw, bbox):
        # bbox can be raw pixel coords [x1, y1, x2, y2] or normalized
        # Check if values are > 1 to determine format
        if all(v <= 1.0 for v in bbox):
            # Normalized format
            x, y, w, h = self._to_px({"x": bbox[0], "y": bbox[1], "w": bbox[2], "h": bbox[3]})
            draw.rectangle([x, y, x+w, y+h], outline="red", width=8)
        else:
            # Raw pixel coords [x1, y1, x2, y2]
            x1, y1, x2, y2 = [int(v) for v in bbox]
            draw.rectangle([x1, y1, x2, y2], outline="red", width=8)

    def _to_px(self, region):
        return (
            int(region["x"] * self.W),
            int(region["y"] * self.H),
            int(region["w"] * self.W),
            int(region["h"] * self.H)
        )
