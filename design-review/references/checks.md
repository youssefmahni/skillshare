# Review checks, thresholds and report format (v2)

CLI: `node /home/youssef/tools/argon-ds-v2/argon-ds-plugin/tools/argon.mjs <command>`. `contrast` and `nearest` accept hex, rgb(a), a role id (`color.text.muted`) or a CSS variable, and take `--mode light|dark` (light is the default). `pairs` lists the role pairs the system promises, both modes.

## Severity
- **Blocker**: fails WCAG AA (contrast, target size, missing label) or breaks the primary task.
- **Major**: wrong component or element for the job, raw values where roles exist, more than one primary action, inconsistent variants, a component used on a platform where it does not exist.
- **Minor**: off-scale spacing or radius, nearly-matching color, copy issues.

## 1. Tokens
| Check | How | Fix |
|---|---|---|
| Every color is a role | Code: `lint`. Figma: `get_variable_defs` lists styles used; any fill or stroke without a style is raw. | `nearest <value> [bg\|text\|border]` → use that role. ΔE < 2.3 means "same color, just not linked". |
| No raw kit variable | `lint` flags `--color-primary-default` and its kin and names the role to use. A raw kit value ignores the mode and the breakpoint. | Swap for the role it names. |
| Text uses type roles | Font size and weight must match a `type.*` role (`get_tokens("type")`). | Use the closest role by size, then weight; `.type-*` class in code. |
| Shadows are roles | Compare with `get_tokens("elevation")`. | `elevation.low` for controls, `elevation.card` for cards, `elevation.raised` on hover. |
| Gradients | Only from the kit (`get_tokens("primitive:gradient")`). | Replace custom gradients. |
| Dark mode | Run `lint --mode dark`, and look at the screen with `data-theme="dark"`. Fills that are literal light colors stay light. | Roles carry both modes: replace the literal with its role. |

## 2. Spacing and radius
- Space roles: **4, 8, 16, 24, 40** (xs, sm, md, lg, xl; the gutter is 24). The kits also use 12, 20 and 68; anything else is off-scale. `lint` suggests the nearest value for code.
- The kits' own legacy geometry has values like 13, 15 and 21. Don't flag these inside unmodified Argon components; flag them in new layout.
- Radius roles: **4 (sm), 8 (md), 12 (lg), 20 (xl), pill**. Cards and inputs use sm; pills use pill.
- Alignment: elements in a column share a left edge; card padding is the same on all sides unless the pattern shows otherwise.

## 3. Consistency
- At most **one primary (solid) button per region**. Secondary actions are `button-outline`, tertiary are `button-link`.
- Siblings match: same button size in a row, the same input style in a form, the same card style in a grid.
- Don't mix square and pill shapes in one group (`button` vs `button-pill`).
- One icon style and size per context (Font Awesome Free: solid for filled, regular for outline, never both in one row).

## 4. Component and element fit
For each mapped component, read `get_component(id)` → `avoid_when`. Report any rule that matches, with its suggested replacement (→ id). Common misses:
- Badges used as buttons → `button`.
- Tooltips holding long text → `popover`.
- An alert used for a field error → `text-input` validation: Error Input.
- A select for 2–3 options → `radio`.
- A switch whose change only applies after Save → `checkbox`.

Plain markup (`get_element`): a `div` or `span` with a click handler → `button`; headings that skip levels; `<br>` as spacing; a table for layout; a placeholder as the only label; a hand-built accordion → `details`; a hand-built modal → `dialog`; a progress bar made of divs → `progress` or `meter`; an obsolete tag (`center`, `font`, `marquee`).

## 5. Responsive (web)
| Check | Threshold | How |
|---|---|---|
| Breakpoints | desktop ≥1200, tablet 768–1199, mobile <768 | `get_tokens("breakpoints")` |
| Behavior | Each component follows its `Responsive` line; layouts follow `get_pattern(kind="layout")` | `get_component(id)`, compare |
| Touch targets | **44×44px** at tablet and mobile; a smaller drawn control grows its hit area | `get_component` prints `Touch:` for the controls that need it |
| No hover-only information | Tooltips and hover menus have a tap or visible alternative | inspect |
| Overflow | No horizontal page scroll at 360px; a wide table scrolls inside its card | screenshot at 390px |
| Type | Large headings shrink at tablet and mobile (type overrides); body stays 16px; nothing under 12px | `get_tokens("breakpoints")` |

## 6. Accessibility
| Check | Threshold (WCAG 2.2 AA) | How |
|---|---|---|
| Text contrast | ≥ 4.5:1; large text (≥ 24px, or ≥ 18.66px bold) ≥ 3:1, **in both modes** | `contrast <text> <background> --mode light`, then `--mode dark`; for text on images, sample the lightest area behind the text |
| Non-text contrast | Control borders, icons, focus rings ≥ 3:1 against neighbors | `contrast` |
| Target size | ≥ 24×24px with spacing (2.5.8 AA); the system uses **44×44** on touch | see section 5 |
| Labels | Every input has a visible label or accessible name; placeholders alone don't count | inspect |
| Icon-only controls | Have an accessible name (aria-label) | inspect |
| Decorative icons | `aria-hidden="true"` | inspect |
| Images | Meaningful alt text, or empty alt for decorative images | inspect |
| Focus | Visible focus state on every interactive element (`color.border.focus`) | check the Focus/Active variant or the CSS |
| Color alone | Status isn't conveyed by color only (add text or an icon) | inspect badges and charts |

### Known issues in the raw kit colors (report as "system-level" when a screen uses them directly)
The roles already avoid these; a screen that uses the raw value inherits the problem.

| Raw kit pair | Ratio | Use instead |
|---|---|---|
| white on brand blue #5e72e4 (primary buttons, 14px) | 4.20:1 | `color.action.primary` (#3d55df, 5.89:1 with white); keep #5e72e4 as `color.accent` for decoration |
| white on danger #f5365c | 3.77:1 | `color.status.danger.solid` (#d40b33, 5.39:1 with white) |
| white on warning #fb6340 | 3.02:1 | dark text: `color.status.warning.on-solid` |
| white on success #2dce89 | 2.04:1 | dark text: `color.status.success.on-solid` |
| white on info #11cdef | 1.91:1 | dark text: `color.status.info.on-solid` |
| link text #5e72e4 on white | 4.20:1 | `color.text.link` |
| secondary text #8898aa on white, placeholders | 2.95:1 | `color.text.muted` (#525f7f, 6.36:1) or `color.text.subtle` (#62708a) |
| disabled text #ced4da | 1.49:1 | fine for disabled controls only (exempt); never for content |
| Checkboxes and radios 20px, table action buttons 14–30px, map controls 40px | — | hit area ≥ 44px (label click or padding) |

Re-run `node /home/youssef/tools/argon-ds-v2/argon-ds-plugin/tools/argon.mjs pairs` after a data update; the numbers come from the current tokens.

## 7. Email client screens
An email client is an app: review it like any App screen, then check the mail details.
- Unread is bold **and** a dot **and** a hidden "Unread" word; attachments have a hidden "Has an attachment"; selection is the checkbox state, not color.
- The message list is one `ul` with labelled checkboxes and star toggles (`aria-pressed`); the thread uses `article`s whose summary button has `aria-expanded`.
- Recipient fields are comboboxes with a listbox; chips have a labelled remove button; an invalid address shows an error message, not only a red chip.
- Send, archive, delete and move offer Undo (a status toast); the compose window is non-modal; Send is disabled with a message while attachments upload.
- On a phone: stacked rows, 44px targets everywhere, swipe actions also exist in a menu, full-screen composer with a round Send in the top bar.

## Report format

```
Design review — <frame/screen name> (source: <code | Figma get_design_context | screenshot | pattern>; screen <app|website>, platform <web>, mode <light|dark|both>)
Summary: <n> blockers · <n> major · <n> minor · <n> system-level

| # | Severity | Where | What's wrong | Evidence | Fix |
|---|----------|-------|--------------|----------|-----|
| 1 | Blocker | "Sign in" button | Text contrast too low | white on #5e72e4 = 4.20:1 (needs 4.5) | Fill color.action.primary (#3d55df, 5.89:1) |
| 2 | Major | Card padding | Off-scale | 15px | space.md (16px) |

System-level (from the kits themselves): <short list, with the recommendation from the table above>
Not checked: <what the source couldn't show: other mode, other widths, mail clients…>
```
