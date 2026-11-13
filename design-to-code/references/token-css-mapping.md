# Token → CSS mapping (v2)

Generate the stylesheets with:
```
node /home/youssef/tools/argon-ds-v2/argon-ds-plugin/tools/argon.mjs tokens-css > argon-tokens.css            # roles, dark mode, breakpoints, .type-* classes
node /home/youssef/tools/argon-ds-v2/argon-ds-plugin/tools/argon.mjs base-css --no-vars > argon-base.css      # every HTML element, using those roles
```
Every role's CSS name is shown by `get_tokens` (the `--…` column). `tokens-css --primitives` adds the raw kit values as well; leave them out unless you need a kit gradient.

## Naming
A role id becomes a CSS custom property by replacing dots with dashes and adding `--`:

| Role id | CSS | Light / dark |
|---|---|---|
| `color.bg.surface` | `var(--color-bg-surface)` | `#ffffff` / `#161d35` |
| `color.text.muted` | `var(--color-text-muted)` | `#525f7f` / `#a9b2d0` |
| `color.border.control` | `var(--color-border-control)` | `#8392ab` / `#7783ad` |
| `color.action.primary` | `var(--color-action-primary)` | `#3d55df` / `#8b9af5` |
| `color.status.danger.soft` / `.text` / `.solid` / `.on-solid` | `var(--color-status-danger-soft)` … | per mode |
| `elevation.card` | `var(--elevation-card)` | two-layer box-shadow, stronger in dark |
| `space.md` | `var(--space-md)` | `16px` (`space.gutter` is 24 at desktop and tablet, 16 at mobile) |
| `radius.sm` / `radius.pill` | `var(--radius-sm)` / `var(--radius-pill)` | `4px` / `9999px` |
| `motion.duration.base` | `var(--motion-duration-base)` | `200ms` |

Type roles become a size, a line height, a weight and a tracking variable, and a ready-made class:

```css
/* generated */
--type-h4-size: 1.5rem; --type-h4-line: 1.37; --type-h4-weight: 600; --type-h4-tracking: -0.0333em;
.type-h4 { font-family: var(--font-sans); font-size: var(--type-h4-size); line-height: var(--type-h4-line); font-weight: var(--type-h4-weight); letter-spacing: var(--type-h4-tracking); }
```

In components, use the class (or `composes:` in CSS Modules); inside a rule, set `font-size`, `line-height`, `font-weight` and `letter-spacing` from the four variables.

## Modes and breakpoints
- **Dark** is in the generated file: it follows the system setting (`prefers-color-scheme`), and `data-theme="dark"` or `"light"` on the root forces one. Use roles everywhere and nothing else changes. Dark values are designed here (the kits have none); every pair is checked (`argon.mjs pairs`).
- **Tablet** (768–1199px) and **mobile** (<768px) redefine `--space-gutter`, `--grid-columns`, `--touch-target` and the large type roles (display 1 and 2, h1 to h3). Write media queries at `max-width: 1199px` and `max-width: 767px` for layout; the variables take care of the rest.

## Which role to use where
| CSS property | Role family |
|---|---|
| `background` of a page, a card, a subtle area | `color.bg.page`, `color.bg.surface`, `color.bg.subtle` |
| `background` of a control | `color.action.primary`, `color.action.secondary` (+ `-hover`, `-pressed`) |
| status fills | `color.status.<success\|info\|warning\|danger>.soft` (with `.text`) or `.solid` (with `.on-solid`) |
| `color` (text, icons) | `color.text.default`, `.muted`, `.subtle`, `.link`, `.on-action`, `.inverse` |
| `border-color` | `color.border.default` (decorative), `color.border.control` (inputs, 3:1), `color.border.focus` |
| decoration only (large shapes, chart lines) | `color.accent` (the brand blue; not for small text) |
| `box-shadow` | `elevation.*` |
| `padding`, `margin`, `gap` | `space.*`: 4, 8, 16, 24, 40 (the kits also use 12, 20, 68) |
| `border-radius` | `radius.*` |
| `font` | `.type-*` classes or the four variables |
| `transition` | `motion.duration.*` with `motion.easing.*` |

Fixed component dimensions (`height: 43px`, `width: 20px`) are component geometry, not spacing; write them as plain values taken from `get_component` variant sizes.

## Rules
- **No raw values.** `lint` flags hex/rgb colors, off-scale padding/margin/gap, unknown radius and font sizes, misspelled `var(--…)` names, and raw kit variables (it names the role to use).
- A value with no role (e.g. a 1px hairline divider) uses the nearest role: `node /home/youssef/tools/argon-ds-v2/argon-ds-plugin/tools/argon.mjs nearest <hex> 3 border`.
- **Do not invent dark values** for something that has no role: add a role-based rule, or tell the user the role is missing.
- Hover and pressed states have their own roles (`-hover`, `-pressed`); use them instead of `filter: brightness()`.
- Focus ring: `outline: 2px solid var(--color-border-focus); outline-offset: 2px;` on `:focus-visible`.
- Touch: `min-height: var(--touch-target)` on controls (44px at tablet and mobile; the base stylesheet already does this).
