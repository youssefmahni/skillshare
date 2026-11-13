# Building in Figma with `use_figma` (paid seats only, v2)

`use_figma` runs Figma Plugin API code in a file. Figma documents it as needing a **Professional, Education, Organization or Enterprise plan** and **edit access** to the file. On Starter, or with a View/Collab seat, skip this file and use the code-preview path.

> This procedure hasn't been run on the plugin author's account (Starter plan). Verify the first build visually and adjust the code if the API rejects a call.

## What can be placed
Component variants have ids like `ds:0:21248` or `dashboard:29:7860`: the part before the first colon is the **kit**, the rest is the Figma node id.
- **`ds:` variants** live in your own copy of the Argon Design System PRO file (the zip includes no link to it). Their node ids resolve only inside that file. Create or reuse a page named **Screens** there.
- **`dashboard:` variants** live in `Argon Dashboard Pro 2.fig`, a file this plugin has only as a local copy (no share link). A node of that kit cannot be placed from the Design System file. If the user has the Dashboard file in their Figma account with edit access, build there instead; otherwise build those slots from tokens (frames, auto-layout, local styles) and say so.
- Components are local to their file (not a published library), so a third file cannot use them without publishing, which needs a paid plan.
- **Light mode only.** Neither Figma file has a dark theme or variables. For dark, build the light frame and hand over the `tokens-css` stylesheet; do not invent dark fills in Figma.

## Budget
- Do all creation in **one** `use_figma` call: frame, auto-layout, instances, text overrides, styles.
- Verify with **one** `get_screenshot` of the new frame.
- Fix with at most one more `use_figma` call. Don't loop.

## Finding the style for a role
Roles are the vocabulary (`color.bg.surface`), the Figma file has styles. `get_tokens("color", query="bg.surface")` prints `[kit: color.white]` for a role that comes from a kit value; `get_tokens("primitive:color", query="color.white")` then prints `Figma style "Color/White"`. Use that name below. A role without a `[kit: …]` (a designed dark value, for example) has no Figma style: use the nearest one and note it.

## Code template
Fill the arrays from the slot table: variant node ids (the part after `ds:`) from `get_component`, and Figma style names from `get_tokens`.

```js
const page = figma.root.children.find(p => p.name === "Screens") ?? (() => { const p = figma.createPage(); p.name = "Screens"; return p; })();
await figma.setCurrentPageAsync(page);

// Local styles by name (the primitives' "Figma style" names)
const paint = Object.fromEntries((await figma.getLocalPaintStylesAsync()).map(s => [s.name, s]));
const text  = Object.fromEntries((await figma.getLocalTextStylesAsync()).map(s => [s.name, s]));
const fx    = Object.fromEntries((await figma.getLocalEffectStylesAsync()).map(s => [s.name, s]));

const screen = figma.createFrame();
screen.name = "Login — composed";
screen.layoutMode = "VERTICAL";
screen.primaryAxisSizingMode = "AUTO";
screen.counterAxisSizingMode = "FIXED";
screen.resize(1440, 900);
screen.itemSpacing = 24;                       // space.lg
screen.paddingTop = screen.paddingBottom = 40; // space.xl
screen.counterAxisAlignItems = "CENTER";
await screen.setFillStyleIdAsync(paint["Color/Secondary/Default"].id);   // role color.bg.page

const card = figma.createFrame();
card.name = "Card";
card.layoutMode = "VERTICAL";
card.itemSpacing = 16;                         // space.md
card.paddingLeft = card.paddingRight = card.paddingTop = card.paddingBottom = 40;
card.cornerRadius = 4;                         // radius.sm
card.resize(391, 10); card.primaryAxisSizingMode = "AUTO";
await card.setFillStyleIdAsync(paint["Color/White"].id);   // role color.bg.surface
await card.setEffectStyleIdAsync(fx["Shadow/Card"].id);    // role elevation.card
screen.appendChild(card);

// Insert component instances by node id (from the slot table)
async function place(nodeId, parent, overrides = {}) {
  const comp = await figma.getNodeByIdAsync(nodeId);
  if (!comp || comp.type !== "COMPONENT") throw new Error(`Not a component: ${nodeId}`);
  const inst = comp.createInstance();
  parent.appendChild(inst);
  for (const [layerName, chars] of Object.entries(overrides)) {
    const t = inst.findOne(n => n.type === "TEXT" && (n.name === layerName || layerName === "*"));
    if (!t) continue;
    const fonts = t.getRangeAllFontNames(0, t.characters.length);
    await Promise.all(fonts.map(f => figma.loadFontAsync(f)));
    t.characters = chars;
  }
  return inst;
}

await place("0:21248", card, { "*": "Email" });       // text-input, Regular with Left Icon
await place("0:21248", card, { "*": "Password" });
await place("0:25149", card, { "*": "SIGN IN" });     // button, Primary Regular

figma.viewport.scrollAndZoomIntoView([screen]);
return { frameId: screen.id };
```

## Rules
- Use **instances**: never detach them, and never redraw a component that exists in Argon.
- Apply colors, text and shadows **only through local styles** (`setFillStyleIdAsync`, `setTextStyleIdAsync`, `setEffectStyleIdAsync`). Spacing and radius come from the role scale.
- Overridden text keeps the instance's text style. Change copy, not style.
- Open Sans is available in Figma by default. Load fonts before editing text.
- Images: `use_figma` can't add new images. Keep the component's sample image, or use `upload_assets` / `generate_image` if available.
- Icons are Font Awesome Free in v2; the Figma files still carry the old Argon icons. Place the old ones for the Figma frame and note the Font Awesome name from `get_icon` in the slot table, which is what the code uses.
