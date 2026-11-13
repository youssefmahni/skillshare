# Self-check before handing over a screen (v2)

Run the automated checks first, then go through the list. Every "no" needs a fix or an explicit, explained exception in the report.

```bash
node /home/youssef/tools/argon-ds-v2/argon-ds-plugin/tools/argon.mjs lint <your .html/.css/.tsx files>             # must print "no token issues found"
node /home/youssef/tools/argon-ds-v2/argon-ds-plugin/tools/argon.mjs lint --mode dark <files>                      # the same, with dark-mode suggestions
node /home/youssef/tools/argon-ds-v2/argon-ds-plugin/tools/argon.mjs contrast color.text.muted color.bg.surface --mode dark
node /home/youssef/tools/argon-ds-v2/argon-ds-plugin/tools/argon.mjs pairs                                         # the role pairs the system promises, both modes
```

## Components and elements
- [ ] Every slot uses an Argon component from the slot table, or is marked "built from tokens" with a reason.
- [ ] No `avoid_when` rule of a chosen component applies to its slot.
- [ ] At most one primary (solid) button per region; secondary actions use `button-outline` or `button-link`.
- [ ] Siblings match: same button size in a row, same input style in a form, same card style in a grid.
- [ ] No `[internal part]` component used on its own.
- [ ] Plain parts use the real HTML element from `get_element` (details for a disclosure, dialog for a native modal, meter and progress for gauges, dl for definitions), not a styled `div`.
- [ ] Every gap a tool reported is listed in the report, not silently filled.

## Tokens and modes
- [ ] Colors, text and shadows all come from **roles** (`var(--color-…)`, `.type-*`, `var(--elevation-…)`); `lint` reports nothing.
- [ ] No raw kit variable (`--color-primary-default`): it ignores the mode and some of them fail contrast.
- [ ] Spacing uses the space roles (4 / 8 / 16 / 24 / 40) or the kit steps (12, 20, 68); radius only the radius roles.
- [ ] Dark mode: `data-theme="dark"` shows no light patches and no unreadable text; every pair you added passes in both modes.

## Responsive
- [ ] Tablet (768–1199) and mobile (<768) follow each component's `Responsive` line and the layout from `get_pattern(kind="layout")`.
- [ ] No horizontal page scroll at 360px; a wide table scrolls inside its own card.
- [ ] Every control has a 44×44px hit area at tablet and mobile (a smaller drawn control keeps its look and grows its hit area, never its size).
- [ ] Type at tablet and mobile uses the breakpoint overrides (large headings shrink); body text stays at 16px, and nothing is under 12px.

## Accessibility
- [ ] Body text contrast ≥ 4.5:1; large text (≥ 24px, or ≥ 18.66px bold) and UI parts ≥ 3:1, in both modes.
- [ ] The role colors already pass. Raw kit colors do not always: white on the brand blue #5e72e4 is 4.20:1, so primary buttons use `color.action.primary`, and the brand blue is `color.accent` for decoration only.
- [ ] Every input has a visible label or an accessible name; icon-only buttons have an accessible name; images have alt text; decorative icons are `aria-hidden`.
- [ ] Focus is visible on interactive elements (`color.border.focus` outline).
- [ ] Status never relies on color alone: add text or an icon.

## Content
- [ ] No placeholder copy left from the kits (lorem ipsum, "Creative Tim", sample prices, sample names).
- [ ] The primary action label says what happens ("Create account", not "Submit").
- [ ] Brand icons (Google, GitHub…) are used only for that brand, unaltered.
