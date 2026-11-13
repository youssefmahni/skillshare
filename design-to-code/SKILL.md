---
name: design-to-code
description: Turn an Argon design (v2) frame or screen into React/TSX code that uses Argon components, HTML elements and design tokens (CSS custom properties with light and dark modes and tablet and mobile breakpoints), with no raw colors or off-scale spacing. Works from a Figma frame (Figma MCP), a compose-screen slot table or HTML preview, or an Argon reference pattern. Use when asked to implement, code, build, convert or hand off a design or screen to React/Next.js.
---

# Design to code with Argon tokens (v2)

**Tools:** argon-ds MCP (`get_component`, `get_tokens`, `get_pattern`, `search_components`, `get_element`, `get_icon`); Figma MCP (optional); `node /home/youssef/tools/argon-ds-v2/argon-ds-plugin/tools/argon.mjs` (`tokens-css`, `base-css`, `lint`, `contrast`).

## 1. Get the design (cheapest source first)
- **compose-screen slot table or HTML preview**: use it directly.
- **Argon pattern**: `get_pattern(id, include_image=true)`. The two VR patterns also give a finished HTML file to read.
- **Figma frame**: call `whoami` (free). On Starter or a View/Collab seat (about 6 to 20 calls a month), make **one** `get_design_context` call for the frame and treat its generated code as a structure hint only. On Full/Dev seats you may add `get_screenshot`.

## 2. Look at the target codebase first
Find the framework, the styling approach (CSS Modules, global CSS, Tailwind…) and existing UI components (`Button`, `Input`, `Card`…).
- Reuse and extend existing components rather than duplicating them.
- Default when nothing exists: React/TSX function components with CSS Modules (Next.js friendly).

## 3. Install the tokens and the base styles once
- `node /home/youssef/tools/argon-ds-v2/argon-ds-plugin/tools/argon.mjs tokens-css > <styles dir>/argon-tokens.css`: the roles for light and dark (system setting, or `data-theme` on the root), the tablet and mobile overrides, and one `.type-*` class per type role.
- `node /home/youssef/tools/argon-ds-v2/argon-ds-plugin/tools/argon.mjs base-css --no-vars > <styles dir>/argon-base.css`: styles for **every HTML element** (buttons, inputs, tables, details, dialog, progress…), so plain semantic markup already looks like Argon.
- `node /home/youssef/tools/argon-ds-v2/argon-ds-plugin/tools/argon.mjs components-css > <styles dir>/argon-components.css`: styles for the components Argon v2 designed (skeleton, empty state, form field, menus, drawer, bottom sheet, app bar…), `ar-*` classes on plain markup. Only needed when the screen uses one; `get_component` says so ("Designed in Argon v2") and prints the markup to copy. See [designed-components.md](references/designed-components.md).
- Import them globally (e.g. in `app/layout.tsx`) and load Open Sans (e.g. `next/font/google`). Naming rules are in [token-css-mapping.md](references/token-css-mapping.md). Never hand-edit the generated files; regenerate after a data update.

## 4. Map every element to an HTML element, a component and its props
A component marked "Designed in Argon v2" has no Figma node: copy its markup from `get_component` (classes, states, accessibility attributes) and add the script its `Behavior` line names (open and close, keyboard, focus); the CSS is visual only.
For each instance or slot: Argon component id → code component → props from its variant values (`get_component(id)` for the axes and properties). Follow [component-mapping.md](references/component-mapping.md). Where the base styles already cover the element (button, input, select, textarea, details, dialog, progress, meter, table), write the plain element with the right `data-variant` / `data-size`; build a component only for what needs structure (cards, stat cards, sidebar, wizard…). If something isn't in Argon, build it from tokens and note it.

## 5. Write the code
- Colors, shadows and sizes come only from `var(--…)` roles; text uses the `.type-*` classes. No raw kit variables (`--color-primary-default`): `lint` names the role to use.
- Spacing comes from the space roles (`var(--space-md)`), radius from the radius roles.
- Use semantic HTML (`get_element` says which): `<button type>`, `<label htmlFor>`, `<nav>`, `<main>`, lists, tables, `<details>`, `<dialog>`. Give icon-only buttons an `aria-label` and decorative icons `aria-hidden`.
- Icons are Font Awesome Free: `get_icon(meaning, include_svg=true)` for inline SVG, or the package; keep the attribution from NOTICE.md.
- Responsive: follow each component's `Responsive` line with media queries at the token breakpoints (`max-width: 1199px`, `max-width: 767px`); controls get a 44px hit area there.
- Include states: `:hover`, `:focus-visible` (visible ring), `:disabled`, plus validation states for inputs.
- Replace the kits' sample copy with real or clearly marked placeholder content.

## 6. Verify
1. `node /home/youssef/tools/argon-ds-v2/argon-ds-plugin/tools/argon.mjs lint <changed files>` must report nothing; run it with `--mode dark` too.
2. Run the project's typecheck, lint and tests if it has them.
3. If the app can run, compare a screenshot with the design at 1440, 768 and 390px, light and dark.

## 7. Hand off
List files created or changed, the component-to-Argon mapping table, deviations from the design (with reasons), platform gaps you met, and what's left (data wiring, routes).
