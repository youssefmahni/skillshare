# Layout patterns for Argon screens (v2)

Measured from the reference screens of the two kits. Use `get_pattern(id, include_image=true)` to see each one, and `get_pattern(kind="layout")` for how the screens change at tablet and mobile. Component ids are the v2 ids (old v1 ids still resolve in `get_component`).

## Two anatomies

### App screens (Dashboard patterns: `dashboards-*`, `applications-*`, `ecommerce-*`, `pages-*`, `authentication-*`)
Frames are 1920px wide. A fixed **sidebar** at the left, a **top bar** over the content, then cards on a 12-column grid.

| Part | Size (1920px frame) | Components |
|---|---|---|
| Sidebar | 250px wide expanded, 130px collapsed (the "Short" variant) | `sidebar` + `sidebar-item` (selected / not selected) |
| Top bar | 1303px wide, 46px tall | `top-bar` (breadcrumb, search `search-input`, account `avatar`, notifications `button-icon-round`) |
| Content | cards on `color.bg.surface` over `color.bg.page`; gutter 24 | `stat-card`, `card-widget`, `data-table`, `chart` |
| Footer | full content width | `footer` |

Tablet (768–1199): the sidebar becomes an icon rail and the grid has 8 columns. Mobile (<768): no sidebar, a menu button opens it as a drawer; the grid has 4 columns and 16px gutters. The sidebar and top bar `Responsive` lines say the same.

### Website screens (Design System patterns: `app-pages-*`, `example-pages-*`, `design-blocks-*`)
| Part | Size (1920px frame) | Notes |
|---|---|---|
| Navbar | full width, 85px tall | Over the hero. White `navbar-item` items on the dark hero; logo left, menu right. |
| Hero section | full width, ~680px | Photo + dark overlay; centered title group 337px wide at y≈205 (H1 white + lead text). |
| Main card | centered, overlaps the hero by ~200px (starts y≈483) | `color.bg.surface`, `radius.sm`, `elevation.card`. |
| Footer | full width, ~230px | Top row: "Thank you" text + `button-social` (icon circle); bottom row: copyright + `text-link-14`. |

Main card widths: **auth** (login, register, reset) 391px with 296px inner content; **settings-like** (two columns) 1040px = 260px menu + 693px content; content width for tables and alerts 1010px.

At 1440px keep the same card widths and centre them. Under 768px, cards go full width with 16px side padding (`space.md`); the navbar folds behind a menu button.

## Spacing rhythm
Use the space roles (`get_tokens("space")`: xs 4, sm 8, md 16, lg 24, xl 40, gutter 24; the kits also use 12, 20 and 68). Anything else is off-scale.
- Inside components and controls: 4–16. Between form fields: 16–24. Between groups of fields: 40.
- Card padding: 24 (dense) or 40 (auth and marketing). Between page sections: 68 or more.

## Screen recipes

"Pattern" is the reference to open first. All ids are v2 component ids.

### Login / Register / Reset password
Pattern: `app-pages-login-page`, `app-pages-register-page`, `app-pages-reset-page` (website kit); `authentication-*` (app kit, 17 variants).

| Region | Slots → components |
|---|---|
| Card top | caption ("Sign in with") `text-link-14`; social sign-in `button-icon-left` (brand: Github / Google) or `button-social` |
| Card body | email and password `text-input` (Regular with Left Icon Alternative on the gray card section); remember me `checkbox` |
| Card bottom | submit `button` (Primary, Regular); secondary links `text-link-14` or `button-link` |
| Errors | field error → `text-input` validation: Error Input; whole-form error → `alert` |

### Account settings / profile edit
Pattern: `app-pages-account-settings`.

| Region | Slots → components |
|---|---|
| Left column (260px) | section menu `navigation-pills` (Vertical Tabs with Icons) |
| Content column (693px) | fields `text-input`; choices `select`, `radio`; on/off preferences `switch`; avatar `file-upload` (Avatar) |
| Actions | Save `button` (Primary); Cancel `button-outline` or `button-link` |

### KPI dashboard / admin
Patterns: `dashboards-automotive`, `dashboards-default-menu-expand`, `dashboards-crm`, `dashboards-smart-home`.

| Region | Slots → components |
|---|---|
| Shell | `sidebar` + `top-bar` |
| KPI row | 3–4 × `stat-card` (value, label, change up/down); tablet 2×2, mobile one column |
| Charts | `chart` (line, line gradient, radar, polar) in `card-widget`; mobile: full width, 200px or taller |
| Data | `data-table` with `badge` for status, `progress-bar`, `avatar`, `table-action-button` for row actions; `pagination` below |
| Filters | date range `datepicker`; search `search-input` |
| Feedback | `toast` for background events; `modal` (Small) to confirm destructive actions |

### Kanban / task board
Pattern: `applications-kanban`. Columns of `kanban-card` (415×151), `avatar`, `tag` or `badge` for labels, `button` to add; views in `tabs`; new task in a `modal`; discussion in `comments`. Mobile: one column at a time, swipe.

### Data table page
Patterns: `applications-datatable`, `ecommerce-order-list`. `search-input` + `select` filters above `data-table`; `pagination` below. Mobile: filters in a sheet; rows scroll sideways or stack as cards.

### Store: orders, products, checkout
Patterns: `ecommerce-order-list`, `ecommerce-order-details`, `ecommerce-product-list`, `ecommerce-product-page`, `ecommerce-new-product*`, `app-pages-checkout-page`.
- Orders: `data-table` + `badge` status + `search-input` + `pagination`; details with `timeline` and `list-item`.
- Products: `card-product`; edit forms with `text-input`, `select`, `file-upload`.
- Checkout: cart lines `data-table` (Shopping Cart Table), address and payment `text-input` + `select`, pay `button` (Success or Primary).

### Calendar, wizard
Patterns: `applications-calendar` (`calendar-event`, `datepicker`), `applications-wizzard*` (`wizard`: steps collapse to "Step 2 of 4" on mobile).

### Chat / messaging
Pattern: `app-pages-chat-page`. Left: `chat` (Users List). Thread: `chat` (Conversations Messages). Composer: `text-input` + `button-icon-round`. Mobile: the thread takes the whole screen.

### Invoice
Patterns: `app-pages-invoice-page`, `pages-account-invoice`. `data-table` for lines, type roles for totals; Print/Download with `button-icon-left`. The email an invoice is sent as is not a screen of this system.

### Pricing
Patterns: `example-pages-pricing-page`, `design-blocks-pricing`. Monthly/yearly switch: `navigation-pills`; 2–4 plans: `card-pricing` (highlight the recommended plan; on mobile it comes first); FAQ: `accordion`; comparison: `data-table`.

### Landing / marketing
Patterns: `example-pages-landing-page`, plus Design Blocks. Order: header (`design-blocks-headers`) → features (`design-blocks-features`, `card-feature`) → social proof (`design-blocks-testimonials`) → pricing → contact (`design-blocks-contact-us`) → footer.

### Profile / team / blog / shop
Patterns: `example-pages-profile-page`, `design-blocks-teams`, `example-pages-blog-posts`, `example-pages-ecommerce-page`. People: `card-profile`, `avatar`. Articles: `card-article`, `card-image-story`. Products: `card-product`.

### Email client (inbox, reading pane, compose)
Patterns: `mail-inbox` (three panes), `mail-inbox-bulk`, `mail-thread`, `mail-compose`, `mail-search`, `mail-inbox-zero`, and on a phone `mail-inbox-mobile`, `mail-message-mobile`, `mail-compose-mobile`, `mail-folders-mobile`. An email client is an app, so it uses the App anatomy with a mail-specific left column.

| Part | Components |
|---|---|
| Folders and labels (16rem; a 4.5rem icon rail on a narrow window; a drawer on a phone) | `folder-nav` (Compose button, system folders with unread counts, labels) |
| List column | `message-list-toolbar` (select all, refresh, paging; bulk actions when messages are selected; filter chips in search) above `message-list-item` rows. Use the stacked row (class `ar-msg-row--mobile`) when the list sits beside a reading pane; use the single-line row for a full-width list |
| Reading pane or conversation | `message-header` (subject, sender, "to me" details, actions), then `thread-message` (collapsed earlier messages, the open one with `attachment-chip` files, an inline reply) |
| Composer | `compose-window` docked at the bottom right, minimized to a bar, full screen on a phone; `recipient-input` for To, Cc and Bcc |
| Feedback | `toast` with Undo after send, archive or delete; `empty-state` for inbox zero and no search results |
| Phone | `app-bar` (large title, search), stacked rows with swipe actions, `fab` for Compose, `bottom-sheet` for message actions |

Rules: unread is bold plus a dot plus a hidden word (never bold alone); the message list is one `ul`, the thread is `article`s; send, archive and delete always offer Undo; keep the compose window non-modal so the inbox stays usable. Install the mail styles with `argon.mjs components-css`.

### Immersive panel (large displays, headset-style)
Patterns: `vr-default`, `vr-info` (the two VR reference screens, built from our own components and tokens; open their HTML with `get_pattern`). A floating panel over a full-bleed background, an icon rail, and a widget grid of `card-widget`. Controls are 48px or larger; dark theme. On a phone or tablet this layout becomes a normal app screen (see `get_pattern(kind="layout")`, id `immersive-panel`).
