# A page from the same notebook

This profile follows Atul's existing personal site, not a dashboard template. The reference is the paper hillside, continuous pen drawing, handwritten name and meowl in `LolStar123/just-a-little-further`. Keep GitHub navigation native; the README is the canvas.

## Visual rules

- Paper `#eeeae0`, ink `#3b3a36`, olive `#60715d`, clay `#936957`, ochre `#8b7248`. Dark paper `#20241f`, ink `#eeeae0`, secondary ink `#c3c4b7`. Text uses the high contrast ink pair; accents are illustrative.
- Nothing You Could Do for handwritten headings, Newsreader for short captions. Both are SIL OFL fonts copied from the personal site with their licenses. SVG text is outlined for consistent rendering without external font requests. Every linked illustration has descriptive HTML alt text.
- One hillside hero, then six linked sketches. No statistics badges, status claims, fake counters, charts of commits or decorative technology logos.
- Every project row and the hero share the full content width. Desktop rows use a 960px drawing grid: 44px title inset, 326px caption start, a sketch centred at 820px, and a 903px arrow centre. All rows are 132px high. Below a 1011px viewport, projects use a 520 by 188 layout with 32px text insets to stay readable alongside GitHub's sidebar or on phones. A separate mobile hero preserves legibility. Native text navigation remains outside the artwork.
- Each image link occupies its own paragraph for consistent native GitHub spacing. Anchor markup has no interior whitespace that could create stray underlined text. Borders retain a slight pen wobble; text baselines, sketch centres and arrows use shared coordinates.
- The meowl strains and the rock nudges on a slow cycle; eyes blink occasionally. Motion is decorative. The HTML picture selects an entirely static SVG for `prefers-reduced-motion`, avoiding inconsistent media-query propagation inside SVG images. Project drawings remain still. No hover or sound claims: GitHub sanitizes README markup.
- Original editable vector illustrations live in `scripts/draw_profile.py`. Fonts are the only borrowed assets. No external image service or workflow is required.
- The HALO row keeps the meeting purpose and personal context; its browser link remains a meeting-notes demo. When an SVG changes, version only that asset's README URL to avoid an old GitHub image-cache response. The four HALO variants use `?v=20261002-context`.
- One short native text line connects games, commuting and research to the work. The profile offers six ways in; `PROJECTS.md` links all 17 public repositories, marks the two earlier sources as combined, and keeps the current workbench/catalogue links beside them. Do not reintroduce deprecated repository names or private source links.

## Acceptance checklist

- GitHub profile renders all artwork and links after publication.
- Desktop and phone layouts have no horizontal overflow; captions remain legible.
- Light and dark artwork both retain contrast and a consistent character.
- Animated image frames differ; reduced-motion image frames stay still.
- Existing project shelf, demo links, scope notes and collaborative credit survive.
- All 17 public repositories appear in the shelf, including profile source and the two explicitly labelled earlier repositories.
- Real links remain keyboard accessible, with meaningful alt text.

## Regenerate

Install `fonttools` and `brotli`, then run `python scripts/draw_profile.py`. Commit the generated SVGs with the source. No ongoing service is involved.

## Local review, 2 October 2026

The generated light/dark desktop and phone art was rendered in headless Chrome. All 32 referenced SVG variants parsed and loaded; picture sources selected mobile artwork at the expected breakpoints and still headers under reduced motion. Local previews are layout evidence, not a claim about GitHub's sanitizer or image cache. Verify the published README after release, including the versioned HALO image URLs.
