---
name: asset-generation
description: >
  Use to GENERATE raster graphic assets for a build — mosaics, textures, seamless/tileable patterns,
  hero images, backgrounds, illustrations, photographic elements. Claude art-directs; Codex renders with
  its own OpenAI key (no key ever touches Claude). Trigger on: "generate an image/texture/pattern/mosaic/
  background/illustration/hero", "make a graphic", "we need artwork", or any build needing real graphics.
  For UI SYSTEM (tokens/components) use design-system-sync; for real references use mobbin-research.
---

# Asset Generation (Claude art-directs → Codex renders)

The kit's "graphic designer." Claude writes a precise brief and reviews the output; **Codex** (the local
coding agent, which holds the OpenAI key) generates the image and saves it to disk. This keeps credentials
with Codex, reuses what the operator already pays for, and gives real graphics instead of hand-coded CSS.

## Engine: GPT-Image-2 via Codex `$imagegen` (upgraded 2026)
Codex ships an **`$imagegen`** skill driving **gpt-image-2** — a real step up over gpt-image-1. Prefer it:
- **Reasoning mode** — it plans composition and self-checks before rendering (fewer artifact re-rolls).
- **>99% text accuracy** — reliable for wordmarks, labels, UI text baked into art, diagram callouts.
- **Resolution**: 2K stable, 4K beta. **Aspect** 3:1 → 1:3. **Batch up to 10 images in one call.**
- **Invoke** by ending a Codex prompt with `$imagegen`, or `codex exec "Generate … save to ./<name>.png"`.
- **Transparency is NOT native** → use the **chroma-key workflow** below (fixes edge speckle on loaders/medallions).
- **Cost** ≈ $0.006–0.211/image on Codex's OWN OpenAI account; ~250 img/min cap. For BATCH pipelines have Codex
  set `OPENAI_API_KEY` so it doesn't burn the plan allowance. Claude still never touches the key.
- **Verify loop**: after render, upload to Figma via the `figma` MCP `upload_assets` and/or screenshot-check.

## Transparency (chroma-key) — the clean-alpha fix
gpt-image-2 can't emit true alpha, so a "transparent" ask leaves a muddy/speckled edge. Instead:
1. Brief it to render the subject **on a solid `#00ff00` (pure green) background, subject fully inside frame**.
2. Have Codex key out the green → alpha (Pillow/ImageMagick), e.g. remove pixels near `#00ff00`, feather 1px.
3. Result: crisp transparent PNG. Use this for the **mosaic loading ring, medallion, laurel, any overlay art**.
(For a subject that legitimately contains green, key on `#ff00ff` magenta instead.)

## Beat AI slop (the highest-leverage levers)
Slop = everything rendered from the generic default. Two cheap fixes move quality the most:
- **Fonts are the #1 tell.** Never ship the default UI font. Pick a specific, characterful face and commit.
  Free sources: Google Fonts, Font Share, Open Foundry, Typewolf, fonts.inuse.com (browse real-world uses).
  To match a reference brand, scrape its site's typography/branding (e.g. Firecrawl "branding" extract — cheap,
  strips HTML) and use that font or the closest free equivalent.
- **Real generated/library assets, not hand-coded CSS art** — icons, textures, hero art, illustrations,
  animated marks (see Sources).
- **One consistent style per project.** Every asset pulls from ONE system (`/BRAND.md`): one icon
  style, one type system, one palette. Consistency across web/menu/social/slides IS the anti-slop.

## Sources & tools (pick the right generator)
- **Raster illustration / photoreal / graphics**: **Codex `$imagegen` (gpt-image-2)** — the kit's asset
  generator; use it for ALL pictures and graphics (holds its own OpenAI key; Claude never touches it).
  *(Parked — NOT wired: Nano Banana (Gemini) Pro and Higgsfield for image+video. Don't reach for these; add
  later only if a project actually needs video or heavier photoreal.)*
- **Icon sets**: a single cohesive pack (Flaticon / Icons8 / Streamline) — ONE style per project (attribution
  if free). Or generate + slice a set (batch `$imagegen`) then chroma-key to transparency.
- **Animated icons / motion marks**: Lordicon + Lottie — export the Lottie JSON, keep a small repo, reference
  it. For loaders, micro-motion, reels/carousels. Check the license (many free under CC).
- **Premium components / shaders ("UI sniping")**: 21st.dev, aceternity, reactbits.dev — grab the component
  code or screenshot for inspiration, then adapt to the brand. One showstopper **"moving piece"** per page
  beats many scattered effects.
- **Data as motion**: animate real numbers (bar/line charts) and **codify the style as a reusable asset**
  ("use this exact chart style for all future charts") so every deliverable matches.

## When NOT to use gpt-image-2
- **Crisp production vectors / brand-critical logos** → generate raster then vectorize, or draw as SVG/Figma vectors.
- **Pixel-accurate visual grounding** (placing hotspots exactly on a screenshot) → gpt-image / Opus vision is
  weak here; **Gemini Pro "Nano Banana"** is stronger for photo-real edits + spatial grounding. Note as an option;
  Codex/gpt-image-2 remains the default for original art/textures.

## The loop
1. **Art-direct** — write a precise brief: subject · style · palette (hex) · composition · seamless/tileable? ·
   transparent? · size · "no text, no outer frame".
2. **Delegate to Codex** via the kit wrapper (run in BACKGROUND — image gen takes ~1–3 min):
   ```bash
   ~/brand-kit/bin/gen-asset.sh <output_dir> <name>.png "<BRIEF>" [ref1.png ref2.png ...]
   ```
   Trailing args = reference images (registry assets / BRAND.md refs) — copied to `.refs/` and named in
   the prompt as style anchors. Codex side has an `asset-render` skill (~/.codex/skills/asset-render)
   with the standing render rules (hex fidelity, chroma-key alpha, sizing, single-file, self-check) —
   briefs no longer need to repeat those mechanics, only the art direction.
   The wrapper appends the save+single-file instruction and runs `codex exec -s workspace-write` in the dir.
   For transparency say "FULLY TRANSPARENT background (PNG alpha), no background fill" explicitly.
   Codex handles generation + resizing (Pillow / ImageMagick / sips, whichever the machine has). Cost ≈ 25–45k tokens on Codex's OWN account per image.
   Launch several in parallel as separate background tasks (NOT nested in one heredoc script — that hung once).
3. **Review (art director)** — when the file lands, VIEW it (Read the .png) or screenshot. Check against
   web-design-principles + the brief: palette right? seamless? legible behind UI? no slop/artifacts?
4. **Iterate** — if off, refine the brief (more specific palette/composition) and re-run. Don't accept "close enough."
5. **Integrate** — place in the app's assets, reference it, keep the original in research/assets.

## Brief template (fill every slot)
> Generate ONE <seamless tileable / standalone> <type> image: <subject + motifs>. Palette: <2–4 hex + roles>.
> <composition/mood, e.g. flat, low-contrast, sits behind UI>. <edges must tile / centered subject>.
> No text, no outer frame. <WxH>. Save as <name>.png in the current directory. Only produce that one file.

## Rules & limits
- **Raster only** (gpt-image-2): great for textures/backgrounds/hero/illustration/loading art. **No true vector/SVG** —
  for a crisp scalable icon/pattern, generate raster then vectorize, or flag for a vector tool later.
- **Batch icon/asset sets** in ONE `$imagegen` call (≤10) with a shared style template so the set stays consistent —
  cheaper and more coherent than one-at-a-time. Save each to its own role-named file.
- **Security:** never ask Codex for secrets; Codex keeps its own OpenAI key — Claude never handles it. Treat that as a hard rule.
- **Determinism:** always pass `-C "$PWD"` pointed at the assets dir + a fixed filename so pickup is predictable.
- **Reference first:** the palette, type, material and light rules all come from `/BRAND.md` — never from
  adjectives in the request. Asset-generation fills the gap a design system does not: bespoke artwork and textures.

## Known-good (mechanism verified end to end)
- A 1024×1024 seamless tileable texture from a single briefed call, palette-exact, no re-roll needed.
- ~28 assets across one identity (hero art, icon sheet, loaders, wordmarks) staying visually in-family,
  because each was generated from the previously approved ones via the registry's `refs used` column.
- Transparent overlays: always route through the chroma-key workflow above. Asking the model directly for a
  transparent background gives a speckled edge every time.
