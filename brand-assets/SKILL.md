---
name: brand-assets
description: >
  Use for ANY image, icon, background, texture, logo, favicon, OG/social image, illustration, hero, product
  render, diagram, or "asset" request — including when asset creation is a sub-step of a larger task. The
  brand-locked asset pipeline: reads the repo's BRAND.md as the only authority, auto-audits what assets the
  project needs, classifies each as Path A (generated) or Path B (derived SVG), gates generation on approval,
  and keeps a registry so the set coheres. Trigger on: "image", "icon", "logo", "favicon", "hero", "banner",
  "background", "texture", "illustration", "OG image", "social card", "asset", "graphic", "render", or any
  build that will show a picture. This gate is not skippable because an asset is "small" or you're mid-task.
---

# Brand Assets — the brand-locked pipeline

Thin prompts ("hero image, dark theme") produce generic, off-brand output because brand tokens aren't in
scope when asset-gen is a sub-step. This skill forces brand context in and forces every generation through a
review gate. BRAND.md is the ONLY authority on palette/type/material/light; nothing here overrides it.

## Step 0 — load authority (every time, no exceptions)
1. Read `/BRAND.md` IN FULL. If it is missing, or its **References** section is a stub, **STOP and say so** —
   do not proceed on inferred branding. (No BRAND.md → offer to build one first; don't guess a brand.)
2. Read `/.assets/registry.md` (approved assets = your reference pool). If absent, create it (header only).

## Phase 0 — AUDIT (run unprompted, before producing anything)
Derive the asset manifest yourself; do NOT ask the user what they need. Read the project and infer:
- routes / pages / screens → which need hero, background, or section art
- components → every `<img>`/`<Image>`/`Image.asset`/`background-image`/icon import; flag placeholders,
  lorem/empty `src`, `TODO` art
- metadata / `<head>` / `manifest.json` / `Info.plist` / `AndroidManifest.xml` / launcher config → declared
  but unfilled platform-icon and social slots
- `package.json`/`pubspec.yaml` + framework + target platforms → required sets (PWA, iOS, Android, email, deck)
- prior conversation in this repo → product intent, audience, positioning, aesthetic already committed
Write `/.assets/MANIFEST.md` before producing anything:
`slot | where referenced | Path A/B | required/optional | status (missing/placeholder/present-but-off-brand) | priority`
Order by **dependency, not page order**: identity mark → tokens → reference images → platform icon sets →
OG template → page imagery. State what you inferred and what you couldn't determine. Ask ONLY about things
genuinely undecidable from the repo — not things you could decide and the user could reject later.
Re-run this audit unprompted whenever a new route/screen/component references a missing asset.

## Classify every request — Path A vs Path B (state it in one line + why)
- **Path A — GENERATED** (diffusion, via the Codex gpt-image bridge): photographic, illustrative, textural —
  hero art, backgrounds, product renders, editorial imagery, atmospheric textures.
- **Path B — DERIVED** (SVG authored → headless-browser render → PNG): icons, icon sets, favicons, logo marks,
  OG/social cards, diagrams, **anything with readable text**, **anything needed at multiple sizes**.
- **Never Path A for Path B assets** — AI raster icons degrade at 16px, render text unreliably, drift off
  palette, can't be regenerated identically. Mixed (e.g. OG card with a photo bg) → split: Path A plate +
  Path B type layer composited on top. Ambiguous → ask.

## Mobbin MCP — OPTIONAL. Skip this whole section if that MCP is not installed.
Query it for: which asset SLOTS apps in this category actually ship (you'll find slots the code doesn't
reference yet); screen-level COMPOSITION (where imagery sits, viewport share, hero scale, density, sequence);
category CONVENTIONS users expect. Do NOT use it for palette/type/material/light (BRAND.md is the only
authority and overrides anything found), for style imitation (never reproduce/trace/closely paraphrase a
specific app — copyrighted UIs), or to resolve ties (brand wins; note the divergence as intentional). When
Mobbin informs a decision, say so in one line naming what you took ("structure only — 3 apps in this
category lead with a full-bleed hero above a two-column proof section"). Never "match the look of <app>".

## Autonomy tiers (gating scales with the registry)
- **Tier 1 — fewer than 3 approved Path A entries in the registry:** show the prompt and STOP for approval,
  per Path A below. These first calls calibrate the style; a bad early approval poisons the whole set.
- **Tier 2 — 3+ approved references exist:** BATCH. Plan the group, generate straight through, show the
  finished set with its prompts. No per-asset gate. Prefer batches of related assets over one-offs (a set
  generated together from shared refs coheres; the same assets a week apart do not).
- **Tier 3 — always:** Path B needs NO gate at any tier (deterministic + editable) — just make it.
- **Escalate back to Tier 1** for any asset in a genuinely new role (first texture, first illustration, first
  product render) even if the registry is full — a new role has no valid reference to inherit from.

## Path A procedure (generated)
a. **References:** pick 2–3 — prefer registry assets closest in ROLE to the new one; else BRAND.md refs.
   Fewer, closer refs beat more.
b. **Write the prompt** to `/.assets/prompts/<slug>.md`:
   - 80+ words of narrative art direction, written as a brief to a human photographer/illustrator — NOT a
     keyword list ("moody, 4k, cinematic").
   - must name: subject with material detail · setting + spatial relationships · light source & direction ·
     camera framing & focal length · the exact hex accents allowed (from BRAND.md).
   - must end with an **exclusion clause** drawn from the BRAND.md NEVER list.
c. **Gate (Tier 1 / new role):** SHOW THE PROMPT AND STOP. Wait for approval. Never generate on an unreviewed
   prompt — not even mid-task. (Tier 2: skip per-asset gate; show the finished batch + prompts.)
d. **Generate:** call the bridge with the refs attached, **`timeout: 600000` ms** (calls take 4–6 min; a
   default timeout kills them and looks like failure). Bridge = `~/…/bin/gen-asset.sh` (Codex, own key).
   For transparency, generate on `#00FF00` and chroma-key out.
e. **Read the PNG back** into context. Compare to BRAND.md point by point. State ≥1 honest way it MISSES
   before offering it as done. If it violates a NEVER entry, revise the prompt and regenerate — don't ship it.

## Path B procedure (derived — no gate)
a. Author the asset as **SVG** using values read from BRAND.md (real fonts, real hex, no approximations).
b. Render to PNG at every required size via headless browser (Chrome `--headless --screenshot`).
c. Verify legibility **at the smallest target size** — actually view the 16px favicon at 16px, not scaled in
   your head.
d. Multi-size sets: delegate the mechanical resize / `.ico` packing / manifest / tag injection to an installed
   asset-generator skill if present — don't reimplement it.
e. Keep the SVG source in-repo — it is the editable master.

## After producing — register + report
- Append every approved asset to `/.assets/registry.md`:
  `slug | path | A/B | role | prompt-file or SVG-source | refs used | date | approved y/n`.
  An asset not in the registry doesn't exist as a reference.
- End-of-batch report: what you made, what you deliberately skipped, what's still missing from MANIFEST.md.

## Guardrails (hard)
- Never silently substitute a placeholder, an SVG doodle, or a stock URL when generation fails — say it
  failed and why.
- Never edit BRAND.md to accommodate an asset you already made.
- Never skip the approval gate because an asset is "small" or you're mid-larger-task.
- If a request contradicts BRAND.md, say so and ask: changing the brand, or making an exception?
- Standing behavior: when a task incidentally needs an asset, produce it under these rules — never drop in a
  placeholder.
