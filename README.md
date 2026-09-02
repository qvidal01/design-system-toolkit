# design-system-toolkit

Build self-contained **Claude Design** design-system cards (`@dsCard` HTML)
from a repo's brand assets and design tokens, render-verify them, then push
them into a claude.ai/design **design system** with the DesignSync MCP tool.

Distilled from seeding the AIQSO Foundations, Network Sentinel, and Subjectly
design systems by hand — so the next product (e.g. LearnMyWay) is a config,
not a rebuild.

## When to use this (vs `/design-sync`)

| Situation | Use |
|---|---|
| Product **has a real web component library** (React/shadcn + Tailwind tokens) | the official **`design-sync` CLI** (`.design-sync/` + `resync.mjs`) — it compiles real components into cards |
| Product is **brand-only** (logo + palette + type), or a token set with no component build | **this toolkit** — hand-author Brand / Color / Type (and simple Component) cards |

## The card model

A card is one self-contained HTML file whose **first line** is the marker:

```html
<!-- @dsCard group="Brand" -->
```

The Design-System pane indexes cards by that marker and groups them by
`group` (Brand, Color, Type, Components, …). Everything else is plain HTML/CSS;
inline your SVGs and `<style>` so the card renders standalone.

## Quickstart

```bash
python3 examples/build_demo.py                 # builds out/colors.html, out/type.html
verify/render.sh out/colors.html out/c.png 820x560   # screenshot to eyeball it
```

## Builders (`dscards/`)

```python
from dscards import logo_card, color_card, type_card

# Brand logo card — inline SVGs, light/dark panels, usage rules.
# Multiple SVGs are id-namespaced automatically so gradients don't collide.
logo_card.build("out/brand/logo.html",
    title="AIQSO — Logo",
    intro="Master mark; products ride on it.",
    variants=[
        {"svg": "/path/aiqso-emblem-text.svg", "label": "Primary (any bg)", "bg": "dark", "h": 130},
        {"svg": "/path/aiqso-logo-horizontal.svg",       "label": "Dark bg (white)",  "bg": "dark",  "h": 52},
        {"svg": "/path/aiqso-logo-horizontal-light.svg", "label": "Light bg (navy)",  "bg": "light", "h": 52},
    ],
    usage=["Dark → white lockup; light → navy lockup.",
           "Clear space ≈ emblem height.", "Don't recolor or distort."])

# Color card — swatch groups; value is any CSS color (hex, oklch, rgb).
color_card.build("out/tokens/colors.html",
    title="Subjectly — Color",
    groups=[{"heading": "Brand", "swatches": [{"name": "primary", "value": "#7A8698"}]}])

# Typography card — specimen rows.
type_card.build("out/tokens/typography.html",
    specimens=[{"label": "Display", "text": "Headline", "size": 32, "weight": 700},
               {"label": "Mono", "text": "code", "size": 13, "mono": True}])
```

Pull token values straight from the product's source of truth — `globals.css`
`@theme`/`:root` for web apps, the brand repo's logo SVGs + token doc for
brand kits — never invent them.

## Push to a design system (DesignSync MCP)

Hand-authored cards are written via the raw API, which **bypasses the app's
self-check**, so you must also **register** them or the pane shows "No cards yet".

1. `DesignSync(list_projects)` → find the design system's `projectId`
   (`get_project` to confirm `type: PROJECT_TYPE_DESIGN_SYSTEM`).
2. `finalize_plan(projectId, writes=[...card paths], deletes=[], localDir=<out dir>)`
3. `write_files(planId, files=[{path, localPath}, ...])`
4. `register_assets(planId, assets=[{name, path, group, subtitle, viewport}, ...])`
   — this writes the card index the gallery reads.
5. `list_files(projectId)` to confirm.
6. In the app: **refresh / reopen** the design system to see the cards, and
   check the **Published** (and **Default**, if org-wide) toggle on its page.

> Note: this lightweight push is for hand-authored cards. The official
> `design-sync` CLI uses a stricter atomic upload (sentinel → content →
> `_ds_sync.json` last) for component-managed systems — don't mix the two on
> the same project.

## Layout

```
dscards/        logo_card · color_card · type_card · lib (dscard wrapper, SVG id-namespacer)
verify/         render.sh — headless-Chrome screenshot of a card
examples/       worked configs — one per design system: build_demo (minimal) · subjectly · network_sentinel
```
