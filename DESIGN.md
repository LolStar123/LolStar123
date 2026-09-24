# A page from the same notebook

This profile follows Atul's existing personal site, not a dashboard template. The reference is the paper hillside, continuous pen drawing, handwritten name and meowl in `LolStar123/meowl-corner`. Keep GitHub navigation native; the README is the canvas.

## Visual rules

- Paper `#eeeae0`, ink `#3b3a36`, olive `#60715d`, clay `#936957`, ochre `#8b7248`. Dark paper `#20241f`, ink `#eeeae0`, secondary ink `#c3c4b7`. Text uses the high contrast ink pair; accents are illustrative.
- Nothing You Could Do for handwritten headings, Newsreader for short captions. Both are SIL OFL fonts copied from the personal site with their licenses. SVG text is outlined for consistent rendering without external font requests. Every linked illustration has descriptive HTML alt text.
- One hillside hero, then six linked sketches. No statistics badges, status claims, fake counters, charts of commits or decorative technology logos.
- Sketches are 390 CSS pixels wide on desktop and shrink to their container on phones. They wrap naturally into a single column. A separate mobile hero preserves legibility. Native text navigation remains outside the artwork.
- The meowl strains and the rock nudges on a slow cycle; eyes blink occasionally. Motion is decorative. The HTML picture selects an entirely static SVG for `prefers-reduced-motion`, avoiding inconsistent media-query propagation inside SVG images. Project drawings remain still. No hover or sound claims: GitHub sanitizes README markup.
- Original editable vector illustrations live in `scripts/draw_profile.py`. Fonts are the only borrowed assets. No external image service or workflow is required.

## Acceptance checklist

- GitHub profile renders all artwork and links after publication.
- Desktop and phone layouts have no horizontal overflow; captions remain legible.
- Light and dark artwork both retain contrast and a consistent character.
- Animated image frames differ; reduced-motion image frames stay still.
- Existing project shelf, demo links, scope notes and collaborative credit survive.
- Real links remain keyboard accessible, with meaningful alt text.

## Regenerate

Install `fonttools` and `brotli`, then run `python scripts/draw_profile.py`. Commit the generated SVGs with the source. No ongoing service is involved.
