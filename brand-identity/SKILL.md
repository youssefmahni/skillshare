---
name: brand-identity
description: >
  Use at the START of any branding or identity work — naming, logo, wordmark, mark exploration, choosing a
  visual direction, or writing the brand constitution. Owns the front half of the identity pipeline: brief →
  direction exploration → operator selection → BRAND.md. Trigger on: "brand", "branding", "identity", "logo",
  "wordmark", "name it", "visual direction", "brand kit", "design a mark", "what should it look like",
  "rebrand", "BRAND.md", or any project that will need a coherent look. Run this BEFORE brand-assets —
  brand-assets refuses to generate anything until BRAND.md exists, and this skill is what writes it.
---

# Brand Identity — the front half of the pipeline

Four stages, in order. Each consumes the previous one's output. Skipping ahead is how identities drift into
generic AI-looking output, because there is nothing concrete for later work to be checked against.

```
1 INTERROGATE  →  2 EXPLORE  →  3 SELECT  →  4 CONSTITUTE
   (brief)         (variants)    (operator)   (BRAND.md)
```

The output of this skill is **`/BRAND.md`** at the repo root. Until that file exists and its References
section is filled, no image generation may happen. That is a hard stop, not a preference.

---

## Stage 1 — Interrogate (no visuals yet)

Do NOT open an image generator. Do NOT propose colors. Ask until you can answer all of these in the
operator's own words, then write them down:

- **What is the product, in one sentence a customer would use?** (Not how it is built.)
- **Who buys it, and what are they anxious about?** Anxiety shapes tone more than demographics do.
- **What must the mark communicate?** Name the single idea. "Photograph becomes sculpture." "Receipts become
  a ledger." If you can't state it in five words, keep asking.
- **What is this NOT allowed to look like?** Push for specifics. Competitors they hate. Categories they refuse
  to be mistaken for. This becomes the seed of the NEVER list and it is the single most useful answer.
- **Where will it live?** App icon at 48px? Printed on a box? Embroidered? Each one rules something out.
- **Is there any existing equity?** An old logo, a color customers recognize, a name already on invoices.

Write the answers to `BRIEF.md`. If a companion `grill-me` skill is installed, use it for this stage — it goes
deeper. Otherwise do it here, and do not move on until the brief is written.

**Anti-pattern:** producing a moodboard to "get the conversation started". It anchors everyone on the first
arbitrary thing they saw and the real questions never get asked.

---

## Stage 2 — Explore directions (breadth, in one batch)

Generate a spread of genuinely **different ideas** — not one idea rendered eight times. Aim for 8–10.

Cover distinct mark TYPES so the operator is choosing between real alternatives:

| Type | What it is | Good when |
|---|---|---|
| **Wordmark** | The name, typeset and customized | The name is distinctive and short |
| **Lettermark / monogram** | One or two letters | The name is long or hard to say |
| **Pictorial** | A recognizable object | There is a concrete thing the product is about |
| **Abstract** | A constructed form | Nothing concrete represents it, or the category is crowded |
| **Emblem** | Mark contained inside a shape/badge | Heritage, craft, officialdom |
| **Combination** | Symbol + wordmark locked together | Default choice for most products — flexible, splits apart when needed |

**Rules for this stage**

- **Batch them in ONE generation call** (up to 10 per `$imagegen` call). A set generated together shares a
  style baseline and is genuinely comparable; the same eight generated one at a time are not.
- **Flat, vector-feeling, meaningful.** Prompt for *"minimal flat vector logo mark, single color, geometric,
  simple, no gradients, no photorealism, no 3D render."* This is not a stylistic preference — photoreal
  AI-rendered marks read as AI-made to everyone who sees them, and get rejected late and expensively.
- **Design in black and white first.** Color is a later decision and it hides weak forms.
- **The symbol should say what the product does.** A pretty abstract swoosh communicates nothing and is the
  most common failure mode of AI-assisted logo work.
- Name each variant by its IDEA, not by number: `v3-monogram-f.png`, `v7-fingerprint-profile.png`. You will
  need to talk about them, and "variant 7" is unusable in a conversation.
- Save them all under `design/logo/` in the project. Keep the rejects — they are the record of what was
  considered, and they are the reference pool for a later round.

**Use AI for ideation, not for finishing.** The generated variant is a *concept*, not a deliverable. Once one
is chosen, it gets rebuilt as clean SVG in Stage 4 — fewest possible nodes, real typeset font (never traced
lettering), flat colors, reflected for symmetry where the form allows.

---

## Stage 3 — Select (the operator picks, in a browser)

Never wire a mark into a build before it has been chosen.

1. Build a **contact sheet** — one HTML page showing every variant, on both a light and a dark ground, at
   large size and at 24px, in color and in pure black-and-white. Open it in a browser.
2. Present 3–5 you would defend, and say WHY for each in one line. Show the rest below as also-rans. An
   operator handed 10 equal options picks nothing.
3. **Stop and wait.** The operator picks. Do not proceed on your own favorite.
4. Run the survival tests on the chosen one before finishing it:
   - Legible at **24px** — actually look at it at 24px, not scaled down in your head.
   - Works in **pure black and pure white**, no gradients needed.
   - Distinguishable from the top three competitors at a glance.
   - Survives being **one color on one background** — embroidery, a stamp, a favicon.
   - Does not depend on fine interior detail that will disappear when printed small.

If it fails a test, say which one and go back to Stage 2 with that constraint added — do not "fix it in
post" with a thicker outline.

---

## Stage 4 — Write the constitution

`BRAND.md` at the repo root. Copy `templates/BRAND.template.md` and fill every section.

**The one rule that governs this file:** every line is a hard constraint, not a suggestion. The test is —
*two different people following this file must produce near-identical output.* If a line could be read two
ways, it is not finished.

Extract values from **what the build actually uses** — the theme file, the CSS custom properties, the fonts
actually loaded — not from an aspirational deck. A constitution that disagrees with the code is worse than
none, because now nobody knows which one is real.

The seven sections, and what makes each binding:

1. **Name & mark** — exact spelling and casing, the one permitted typeface, letter-spacing, and every file
   that is a legitimate version of the mark. State the misspellings and mis-settings that are forbidden.
2. **Palette** — every hex gets **one job**. Say which colors may appear in imagery versus which are UI-only.
   State how many accents exist (the answer should usually be **one**). Ban pure `#000` and pure `#FFF` as
   grounds and name the warm/cool near-black and off-white that replace them.
3. **Typography** — each face gets a role **and a forbidden list**. "Display only; forbidden in body,
   captions, anything small" is binding. "Elegant serif for headings" is not.
4. **Shape, shadow, motion** — named radii per component class, one shadow recipe, motion durations and one
   easing curve. Rule out scrolljacking, parallax gimmicks, bounce.
5. **Material & light doctrine** — the section that makes imagery reproducible. Material and finish, metal or
   surface treatment with a hex range, the ground, **the light source and its direction**, composition rules
   and a minimum negative-space share. Write it so a photographer could shoot it.
6. **NEVER list** — ten or more entries. **Must include the generic-AI tells**, because those are what you
   will actually be fighting: glowing orbs and particles, purple→blue or teal→cyan tech gradients,
   glassmorphism, neon, lens flare and bloom, stock smiling people, corporate-Memphis illustration, mascots,
   melted AI faces and hands, pure black or white grounds, a second accent hue. Then add the ones specific to
   this brand, drawn from the operator's Stage 1 answer about what it must not look like.
7. **Voice** — two good example lines and two bad ones. Cheap to write; stops the copy drifting when the
   visuals hold.

Plus a **References** section: 3–5 approved assets that new work inherits from. Until this is filled it is a
**stub**, and a stub blocks all generated-asset work downstream.

---

## Hand-off

When `BRAND.md` is written and References is filled, this skill is done. Hand to:

- **`brand-assets`** — audits what the project needs, classifies each slot, gates generation, keeps the registry.
- **`asset-generation`** — the engine layer underneath it.
- **`brand-review`** — proves the decisions actually reached the live build.

## Guardrails

- Never generate imagery in Stages 1–3 beyond the logo exploration itself.
- Never pick the mark yourself. Present and stop.
- Never edit `BRAND.md` later to accommodate an asset you already made — regenerate the asset, or make the
  brand change deliberately and say you are doing it.
- If the operator asks for something that contradicts the constitution, say so plainly and ask which it is:
  changing the brand, or making a one-time exception.
