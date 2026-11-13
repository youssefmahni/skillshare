# Argon component → code mapping (v2)

Measurements come from the kits' Figma files (`get_component` gives sizes per variant, and the `Properties:` line lists native Figma properties such as text and icon slots). Several Argon components collapse into one code component with props. Where the **base stylesheet** (`argon-base.css`, from `tools/argon.mjs base-css`) already styles the HTML element, write the plain element and skip the component.

## Plain element first (styled by the base stylesheet)
| Need | Write | Argon component it matches |
|---|---|---|
| Button | `<button>` primary by default; `data-variant="secondary\|outline\|link"`, `data-size="sm\|lg"` | `button`, `button-outline`, `button-link` |
| Text field, number, date, search… | `<input type=…>` with a `<label>` | `text-input`, `search-input`, `datepicker` (native date types) |
| Several lines | `<textarea>` | `textarea` |
| Choose one from a list | `<select>` | `select` |
| Checkbox, radio | `<input type="checkbox\|radio">` in a `<label>` | `checkbox`, `radio` |
| Switch | `<input type="checkbox" role="switch">` in a `<label>` | `switch` |
| Slider | `<input type="range">` | `slider` |
| Progress, gauge | `<progress>`, `<meter>` | `progress-bar` |
| Disclosure | `<details><summary>` | `accordion` |
| Native modal | `<dialog>` | `modal` |
| Table | `<table>` with `thead`, `th scope`; class `num` on number cells | `data-table` |
| Divider | `<hr>` | `divider` |
| Text, quotes, code, keys | `get_element(tag)` says which element and how it looks | n/a |

## Components that need their own markup
| Code component | Argon component ids | Props (from variant axes and properties) |
|---|---|---|
| `Button` (when you need icons or a split) | button, button-outline, button-link, button-pill, button-gradient, button-icon-left, button-icon-right, button-icon-square | `variant: solid \| outline \| link \| gradient`, `shape: square \| pill`, `color: primary \| secondary \| success \| info \| warning \| danger \| default \| white`, `size: sm \| md \| lg`, `block`, `iconLeft`, `iconRight` |
| `IconButton` | button-icon-round, button-icon-square, button-utility, map-control, table-action-button | `shape: square \| circle`, `color`, `size`, `aria-label` (required) |
| `SocialButton` | button-social | `brand`, `layout: label \| icon \| icon-circle` |
| `Badge`, `Tag` | badge, tag | `color`, `pill`, `count`, `onRemove` |
| `Tabs`, `NavPills`, `Breadcrumb`, `Pagination` | tabs, navigation-pills, breadcrumb-link, pagination | `items`, `orientation`, `withIcons`, `page`, `count` |
| `Navbar`, `Sidebar`, `TopBar`, `PageHeader` | navbar-item, dropdown-item, sidebar, sidebar-item, top-bar, page-header | `items`, `collapsed`, `selected` |
| `Wizard` | wizard | `steps`, `current` |
| `Alert`, `Toast` | alert, toast | `kind: success \| info \| warning \| danger`, `onClose` |
| `Tooltip`, `Popover`, `Modal` | tooltip, popover, modal | `placement`, `title`, `size` |
| `DatePicker` | datepicker (+ datepicker-day, picker-controls and the month and year labels) | `mode: single \| range \| datetime` |
| `StatCard`, `Chart`, `Timeline`, `CalendarEvent`, `KanbanCard`, `Rating` | stat-card, chart, timeline, calendar-event, kanban-card, rating | content props; `trend: up \| down`, `type: line \| radar \| polar` |
| `ListItem` | list-item | content props |
| `Avatar`, `Image`, `FileUpload`, `Carousel`, `Flag` | avatar, image, file-upload, carousel, flag | `size`, `bordered`, `raised`, `alt` |
| `Card` + variants | card-feature, card-pricing, card-profile, card-project, card-product, card-article, card-image, card-image-story, card-widget, card-credit | `FeatureCard`, `PricingCard`, `ProfileCard`, `ProjectCard`, `ProductCard`, `ArticleCard`, `ImageCard`, `WidgetCard`, `CreditCard` |
| `Comments`, `Chat` | comments, chat | content props |
| `TextLink` | text-link-13 … text-link-28, overline-link | `size`, `tone` |
| `Footer` | footer | `variant: primary \| secondary` |
| `Icon` | icons → **Font Awesome Free**: `get_icon(meaning)` | `name`, `style`, `size`, color via `currentColor`; `aria-hidden` unless it is the only label |

## Core specs (measured, written as roles)

### Button
| | Small | Regular (default) | Large |
|---|---|---|---|
| Height | 28px (`--control-sm`) | 43px (`--control-md`) | 51px (`--control-lg`) |
| Text | `type.button` (14px/600, uppercase) | same | same |

- Shape: `border-radius: var(--radius-sm)` (square) or `var(--radius-pill)`.
- **Solid:** background `var(--color-action-primary)`, text `var(--color-text-on-action)`. Hover `--color-action-primary-hover`, pressed `--color-action-primary-pressed`. Secondary: `--color-action-secondary` family with `--color-text-default`.
- **Status colors:** `var(--color-status-<success|info|warning|danger>-solid)` with `var(--color-status-<…>-on-solid)` text (dark text on success, info and warning; white on danger).
- **Outline / link:** transparent with a `--color-action-primary` border or text; the base stylesheet has both (`data-variant`).
- **Gradient (marketing only):** the kit's `gradient.primary.default`; there is no role for it (`tokens-css --primitives` includes the raw gradients). Not for email or app screens.
- **Icon slot:** 13–15px icon, `gap: var(--space-sm)`.
- At tablet and mobile every button has a 44px hit area (the base stylesheet sets the `min-height`).

### Text input
- Height 43px; `border-radius: var(--radius-sm)`; background `var(--color-bg-surface)`; border `1px solid var(--color-border-control)` (3:1 against the surface, unlike the decorative `--color-border-default`).
- Padding `0 var(--space-md)` (kit: 12px); with an icon, icon 12px from the edge and left padding 40px.
- Text `type.body-sm` or `type.body`, color `--color-text-default`. Placeholder `--color-text-subtle`; it is not a label, so always render a visible `<label>`.
- Focus: `outline: 2px solid var(--color-border-focus); outline-offset: 2px`.
- Validation: success → border and message in `--color-status-success-text`; error → `--color-status-danger-text`, plus the message below the field and `aria-invalid`/`aria-describedby`.

### Badge
- Padding `var(--space-xs) var(--space-sm)`; `type.badge` (12px/600, uppercase; the kit draws 10px, the role is raised to the 12px minimum, so a badge is about 24px tall, not the kit's 21px).
- Radius `var(--radius-sm)` (contextual) or `var(--radius-pill)`.
- Soft (recommended, passes AA in both modes): fill `--color-status-<k>-soft`, text `--color-status-<k>-text`. Solid: fill `-solid`, text `-on-solid`.

### Checkbox / Radio / Switch
- Checkbox 20×20, `var(--radius-sm)`; checked fill `--color-action-primary` with a check in `--color-text-on-action`. Radio 20×20 circle.
- Switch 44×24 in the base stylesheet (the Design System kit's has ON/OFF text and is 52×24; the Dashboard one has none): `role="switch"`, pill radius.
- Wrap each in a `<label>` so the clickable area reaches 44px.

### Card
- Background `var(--color-bg-surface)`, `var(--radius-sm)`, `var(--elevation-card)`, padding `var(--space-lg)`; on `--color-bg-page`.
- **Feature card:** icon in a 48px circle filled with a status or accent role, title `type.h5`, body `type.body-sm` in `--color-text-muted`; gap `--space-lg` below the icon, `--space-md` below the title.
- **Stat card:** value in a large type role, label `type.body-sm` muted, change with an up or down arrow in `--color-status-success-text` / `--color-status-danger-text` plus the sign (never color alone).

### Alert
- Full width, `var(--radius-sm)`, padding `var(--space-md) var(--space-lg)`, background `--color-status-<k>-soft`, title in `--color-status-<k>-text`, body in `--color-text-default`.
- Icon, a bold lead word, the message, a close button on the right.

### Modal
- Prefer native `<dialog>`: it traps focus and closes on Esc. Backdrop `--color-bg-overlay`; panel `--color-bg-surface`, `var(--radius-sm)`, `var(--elevation-modal)`; small width ~380px.
- Header, body, footer separated by `1px solid var(--color-border-default)`; a close `IconButton`.
- On mobile: a short confirmation is a **bottom sheet** (as tall as its content, at most 90% of the screen, grab handle, full-width actions at the bottom, closes on a scrim tap or swipe down); a form or long content is a full-screen sheet. Focus the safe action first when the other is destructive (`autofocus`). With a native `<dialog>`: `margin: auto 0 0`, `max-height: 90dvh` and **`height: fit-content`** (not `auto`: a modal dialog is fixed to the top and bottom, so `auto` stretches it to the full height). The base stylesheet lays `dialog form[method="dialog"]` out as a right-aligned row of buttons, so either keep only the buttons inside that form, or override it with the same selector (`dialog form[method="dialog"] { display: block; }`) when the title and text are inside it.

### Sidebar
- 250px expanded, 130px collapsed; items 40–54px tall (`get_component("sidebar-item")` for the variants); selected and not selected states. Tablet: icon rail with each item's label as its accessible name; mobile: a drawer with a scrim opened from the top bar.

### Designed components (no Figma node)
The 35 components Argon v2 designed (list and rules in [designed-components.md](designed-components.md)) are plain HTML with `ar-*` classes. Map them to a code component that renders that exact markup, keep the classes, states (`aria-expanded`, `aria-selected`, `aria-current`, `aria-busy`, `aria-invalid`, `data-state`) and accessibility attributes, and write the script named under `Behavior`. Do not restyle them with raw values: the stylesheet (`argon.mjs components-css`) already uses only roles, so dark mode and the tablet and mobile rules come with it.

### Everything else
Call `get_component(id, include_image=true)` and build from:
- its `tokens_used` (kit values: map each to its role with `get_tokens(query=…)`);
- its variant sizes (fixed dimensions);
- its `Responsive` line;
- the thumbnail.

Map any `hardcoded` value with `nearest`.
