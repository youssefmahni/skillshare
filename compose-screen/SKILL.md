---
name: compose-screen
description: "Compose a new screen with the Argon design system (v2: Design System PRO and Dashboard PRO 2 merged into one library, with light and dark modes). Brief → platform and mode → layout → pick components, HTML elements and icons with the argon-ds tools → build (in Figma on paid seats, otherwise a token-only HTML preview plus a build spec) → self-check against tokens, both modes, and tablet and mobile. For web apps, dashboards, websites, the immersive panel layout and an email client (inbox, reading pane, compose). Use when asked to design, mock up, lay out or build a screen, page, view or flow (login, dashboard, kanban, orders, settings, pricing, checkout…) with Argon."
---

# Compose a screen with Argon

**Tools:** argon-ds MCP (`search_components`, `get_component`, `get_tokens`, `get_pattern`, `get_element`, `get_icon`); Figma MCP (optional); the helper CLI `node /home/youssef/tools/argon-ds-v2/argon-ds-plugin/tools/argon.mjs`.

## 1. Brief
Restate in at most 5 lines: goal, primary user action, content and data, **platform**, **mode**, constraints. Ask one question only if the primary action is unclear; otherwise state your assumptions and continue.

- **Platform.** Web is the default: desktop (≥1200px, design at 1440), tablet (768–1199) and mobile (<768). An email client is an app: its screens are App screens built with the mail components (see the Email client recipe in [layout-patterns.md](references/layout-patterns.md)). Android is planned (nothing built) and the Apple platforms are blocked by license: say so and offer the web design as the starting point; do not invent native components.
- **Mode.** Design in light and keep every color a role, so dark works without changes. Show dark only when asked, and still check both (step 7).
- **Kind.** App screens (dashboards, tables, boards) follow the Dashboard patterns; website screens (landing, pricing, blog) follow the Design System patterns. Both draw on the same components.

## 2. Check the Figma budget (once per session)
Call the Figma MCP `whoami`; it doesn't count against rate limits.
- **Full or Dev seat on a Professional+ plan, with edit access to the Argon Design System file** → build path A is available, for Design System components only (see figma-build.md).
- **Starter plan or View/Collab seat** → only about 6 to 20 Figma calls a month and no `use_figma`. Use path B and don't spend Figma calls unless the user asks.
- **Figma MCP not connected** → path B.

## 3. Reference and layout
1. `get_pattern()` lists the kinds: app (74 screens, including the two VR screens and the 10 email client screens), website (29), layout (7). Pick the closest reference with [layout-patterns.md](references/layout-patterns.md) and view it with `get_pattern(id, include_image=true)`.
2. `get_pattern(kind="layout")` says how the app shell, KPI row, table with filters, sign-in, kanban and website page change at tablet and mobile. Use it for the responsive plan.
3. Write the layout as **regions → slots**. Each slot is one need in plain words ("primary action: sign in", "status of each order").

## 4. Pick components, elements and icons per slot
For each slot: `search_components(need)` → `get_component(id, filter=…)` → choose one variant.
- Read the `Platforms` and `Responsive` lines of the component: they say how it behaves at tablet and mobile and whether its smallest variant needs a larger touch area.
- Follow `avoid_when`; if a rule points elsewhere (→ id), switch.
- One primary (solid) button per region. Siblings use the same variant family and size.
- Skip results marked `[internal part]`.
- **Plain HTML parts** (headings, lists, quotes, details, dialogs, meters, definition lists, form groups): `get_element(tag or need)` says which element, how Argon styles it and the accessibility notes. Use the real element, not a styled `div`.
- **Icons:** `get_icon(meaning)` (Font Awesome Free). Decorative icons get `aria-hidden`; icon-only controls get an accessible name. Brand icons only for that brand.
- If nothing fits, say so and build that slot from tokens. Never invent an Argon component. When a tool reports a gap, report it; do not fill it silently.

Record the **slot table**; it is the build spec:

| Region | Slot | Component id or element | Variant (uid, values) | Key tokens | Tablet / mobile | Notes |
|---|---|---|---|---|---|---|

## 5. Tokens
Use **roles**, not raw kit values: `get_tokens("color", mode="both")`, `get_tokens("type")`, `get_tokens("space")`, `get_tokens("breakpoints")`. A role (`color.text.muted`) changes with the mode and the breakpoint; a raw kit color (`color.primary.default`) does not, and some fail contrast. `get_tokens(query="#5e72e4")` maps a color you have to its role.

## 6. Build
- **A. In Figma** (paid seat only): follow [figma-build.md](references/figma-build.md). One batched `use_figma` call in the Design System file, on a page named "Screens".
- **B. Code preview** (default):
  1. `node /home/youssef/tools/argon-ds-v2/argon-ds-plugin/tools/argon.mjs tokens-css > argon-tokens.css` (roles, dark mode, tablet and mobile overrides, `.type-*` classes) and `node /home/youssef/tools/argon-ds-v2/argon-ds-plugin/tools/argon.mjs base-css --no-vars > argon-base.css` (every HTML element styled). If a slot uses a component marked "Designed in Argon v2" (skeleton, empty state, form field, drawer, bottom sheet, app bar…), also run `node /home/youssef/tools/argon-ds-v2/argon-ds-plugin/tools/argon.mjs components-css > argon-components.css`, link it after the base styles and paste the markup that `get_component` prints. Link the files and load Open Sans.
  2. Write `<screen>.html` with semantic elements. Rebuild each component from its tokens (see design-to-code's component-mapping.md) and tag it `data-argon="<component id>:<variant uid>"`.
  3. Make it responsive with the breakpoints from `get_tokens("breakpoints")` (`max-width: 1199px` tablet, `max-width: 767px` mobile), following each component's `Responsive` line.
  4. Put `data-theme="dark"` on `<html>` to see dark mode.

## 7. Self-check
Work through [slot-checklist.md](references/slot-checklist.md):
- `node /home/youssef/tools/argon-ds-v2/argon-ds-plugin/tools/argon.mjs lint <files>` must report no issues (add `--mode dark` to see dark-mode suggestions).
- Check every text and background pair in both modes: `node /home/youssef/tools/argon-ds-v2/argon-ds-plugin/tools/argon.mjs contrast <fg role> <bg role> --mode light` and `--mode dark`. Roles are already checked (`pairs`); a pair you invented is not.
- If a browser is available, screenshot at 1440, 768 and 390px wide, light and dark, and look at them.
- Fix and re-run until clean. List accepted exceptions explicitly.

## 8. Report
Give the slot table, file paths or the Figma link, the platform gaps you hit, open issues, and the next step (`design-review`, or `design-to-code` for production code).
