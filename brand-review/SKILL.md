---
name: brand-review
description: >
  Use BEFORE shipping any build that has a brand — and whenever asked to "review the design", "check the
  branding", "does this look right", "is it on brand", or "ready to ship". Runs the decisions-applied audit
  (proving each brand decision actually reached the live output), a three-lens design panel, and the
  anti-slop check. Trigger on: "review", "before deploy", "quality check", "on brand?", "does this look
  good", "ship it". Blocks on critical and serious findings.
---

# Brand Review — deciding is not applying

The failure this skill exists to catch: **the decision was made, the asset was generated, and neither
reached the screen.** Real example that produced this rule — a display face was chosen and a complete
custom icon set was generated, and the shipped screens still rendered the default UI font and generic
placeholder vectors. Everything was "done". Nothing was applied.

Run these in order. Scale to the task: a copy or color tweak needs section 1 only; a full page or feature
needs all four.

---

## 1. The decisions-applied audit — every time, no exceptions

For **each** brand decision and **each** generated asset, inspect the **live** output and prove it is wired.
Not the source. Not your memory of writing it. The rendered DOM, the widget tree, the running app.

| Check | Pass looks like | The failure it catches |
|---|---|---|
| **Typefaces** | Computed `font-family` on real text nodes is the chosen face | Silent fallback to a system font because the `@font-face` never loaded or the family name is misspelled |
| **Display vs body split** | Headings use the display face, body uses the body face, per BRAND.md §3 | One face doing everything because the roles were never wired |
| **Generated assets in use** | The logo, icon set and textures in the registry appear in the build | Placeholder glyphs and stock vectors still sitting where the real assets should be |
| **Tokens bound** | Colors resolve through CSS variables / theme constants | Hardcoded hex that happens to match today and silently drifts on the next change |
| **Accent discipline** | Exactly the number of accents BRAND.md permits — usually one | A second hue that crept in from a component library default |
| **Icon set coherence** | Every icon comes from ONE set | Mixed icon libraries, the single most visible consistency failure |
| **Favicon + platform icons** | Real files at every declared size, and the manifest points at them | The framework's default icon still shipping |
| **OG / social card** | Correct image, 1200×630, correct text | The link preview showing nothing, or last project's card |

How to actually inspect it, by stack:
- **Web** — read computed styles in the browser, not the stylesheet. `getComputedStyle(el).fontFamily`
  returns what *resolved*, which is the only thing that matters.
- **Flutter** — check the widget tree / theme, and screenshot the running app on a device or emulator.
- **Native** — build and look at it on a real screen at real size.

Report each row as pass or fail with the evidence. A row you did not actually inspect is a fail.

---

## 2. Design panel — three separate lenses

Real design review is a council, not one pass. Run these as distinct perspectives — separate sub-agents for
a large surface, separate passes for a small one — so each catches what the others miss.

- **UX / flow** — Can the task be completed? Are the empty, loading and error states designed or forgotten?
  Is navigation obvious? Does it work on a phone?
- **UI / visual** — Hierarchy, spacing rhythm, alignment, contrast ratios, type scale. Measure the rendered
  output at both desktop and mobile widths; reading the code catches nothing that is nine pixels off.
- **Copy / anti-slop** — See section 3.

Aggregate into ONE severity-ranked list. Do not present three separate reports.

---

## 3. Anti-slop check — name the tells explicitly

A person "just knows" when something looks AI-made. Make the lens say why, in words, so it can be fixed.

**Visual tells**
- Purple→blue or teal→cyan gradients; any generic SaaS gradient hero
- Glowing orbs, particles, energy wisps, holograms
- Glassmorphism, neon, "futuristic" chrome
- Everything centered; every corner the same rounded radius
- Drop shadows on every element
- An accent bar or rail on every rounded card
- Emoji used as section markers or feature icons
- Stock smiling people; corporate-Memphis illustration; mascots

**Copy tells**
- "Seamless", "powerful", "effortless", "revolutionize", "elevate", "unlock"
- Three-adjective stacks: "fast, secure, and scalable"
- Fabricated testimonials, fake logos, invented statistics
- Headlines that describe the category instead of the product
- Passive voice on buttons; a control that does not say what it does

**Structural tells**
- Numbered markers (01 / 02 / 03) on content that is not actually a sequence
- Section dividers, eyebrows and labels that decorate rather than encode something true
- Three feature cards because three feature cards, not because there are three features

For each tell found, name it, point at the element, and propose the specific replacement.

---

## 4. Functional and ground-truth check

- Every control has a handler or an href — no dead buttons.
- Run the build. Verify against **ground truth**: real data landed, the number is correct — not merely
  "it rendered".
- Health-check after any deploy.

---

## Verdict

List findings by severity. **Fix every critical and serious finding before presenting or deploying.**

State plainly what you inspected and what you did not. "Reviewed" without naming the evidence is the same
failure this skill exists to catch, one level up.
