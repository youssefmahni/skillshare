---
name: design-review
description: Review a screen or frame against the Argon design system (v2). Checks token use (roles, light and dark modes), spacing and radius against the scale, component and HTML element fit, responsive behavior at tablet and mobile, accessibility (WCAG contrast in both modes, 44px touch targets, labels). Reports issues with concrete fixes (role, component, variant, element). Use when asked to review, audit, critique, QA or check a Figma frame, selection, screenshot, HTML/React screen, or Argon pattern.
---

# Design review against Argon (v2)

**Tools:** argon-ds MCP (`get_component`, `get_tokens`, `search_components`, `get_pattern`, `get_element`, `get_icon`); Figma MCP (optional); `node /home/youssef/tools/argon-ds-v2/argon-ds-plugin/tools/argon.mjs` (`contrast`, `nearest`, `lint`, `pairs`).

## 1. Get the frame (pick the cheapest source available)
1. **Code** (HTML/CSS/TSX): read the files and run `node /home/youssef/tools/argon-ds-v2/argon-ds-plugin/tools/argon.mjs lint <files>`.
2. **Argon pattern or compose-screen output**: `get_pattern(id, include_image=true)` or the slot table.
3. **Screenshot** from the user: inspect it visually; ask for exact values only when a finding depends on them.
4. **Figma frame** (link or selection): first call `whoami` (free).
   - On Starter or a View/Collab seat (about 6 to 20 calls a month), use at most **2 calls**: `get_design_context` for values and structure, and `get_screenshot` only if you need the visuals.
   - On Full/Dev seats, also call `get_metadata` (layer sizes) and `get_variable_defs` (styles used).

Say which source you used, which **platform and mode** it shows (web light by default; a screenshot shows one mode and one width only), and what it can't show.

## 2. Map what's there
List the elements as Argon components: match layer or instance names like `Buttons/Default/…` to ids via `get_component` (old v1 ids resolve), or use `search_components` for unnamed elements. Match plain markup to elements with `get_element`. Note anything that is **not** an Argon component.

## 3. Run the checks
Follow [checks.md](references/checks.md) in order:
1. **Tokens**: colors, text, shadows are **roles**. Map every raw value with `nearest` (it answers with a role in the chosen mode).
2. **Spacing and radius** against the scale.
3. **Consistency**: variants, sizes, one primary action per region.
4. **Components and elements used correctly**: check each against its `avoid_when` rules, and plain markup against `get_element`.
5. **Responsive**: the `Responsive` line of each component, the layout from `get_pattern(kind="layout")`, 44px targets at tablet and mobile.
6. **Accessibility**:
   - contrast with `contrast <fg> <bg> --mode light` and `--mode dark` for every text/background pair;
   - touch targets;
   - labels, alt text and focus.
7. **Platform and screen fit**: is each component available on the target platform (`get_component(id, platform=…)`)? A component the platform does not have is a finding. For a mail app screen, check it against the mail components (message row, toolbar, folder navigation, header, thread, recipients, attachments, composer).

Compute contrast with the tool. Never estimate it by eye.

## 4. Report
Use the report format in checks.md:
- a summary line (counts by severity);
- then one row per issue with **where / what's wrong / evidence / fix**, where every fix names a role, component, variant or element;
- system-level issues (inherited from the kits themselves) in a separate short list, so they aren't blamed on this screen.

Offer to apply the fixes (in code, or in Figma with `use_figma` on paid seats).
