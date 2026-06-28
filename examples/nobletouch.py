"""Real-world example: a FULL design system (logo + color + type + components)
seeded from the Noble Touch Painting repo (Next.js + shadcn).

Run from the repo root:  python examples/nobletouch.py
Outputs into ./out/nobletouch/ ; verify with verify/render.sh.

Values mirror nobletouch/app/globals.css and public/logo.svg — the pattern is:
pull real tokens + the logo from the product repo, never invent them. Push the
built cards into the design system with DesignSync (see the README sequence).
"""
import os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from dscards import logo_card, color_card, type_card
from dscards.lib import dscard, write

OUT = pathlib.Path(__file__).resolve().parent.parent / "out" / "nobletouch"

CREAM, INK, NAVY, GOLD, TAUPE = "#fbf8f2", "#14203c", "#1e2d52", "#c2a14e", "#5f5749"
FRAUNCES = 'Fraunces,Georgia,"Times New Roman",serif'
INTER = 'Inter,system-ui,sans-serif'
# Point this at the product repo's clean vector logo (no embedded raster):
LOGO = os.environ.get("NT_LOGO", os.path.expanduser("~/projects/nobletouch/public/logo.svg"))

# --- Brand / Logo (skipped gracefully if the source SVG isn't present) ---
if os.path.exists(LOGO):
    logo_card.build(OUT / "brand/logo.html",
        title="Noble Touch Painting — Logo",
        intro="Crest + NT monogram + paintbrush, navy & gold on warm cream. "
              "Self-contained vector. Mono variants exist in public/ for single-color use.",
        ink=NAVY, fg=CREAM, lightbg=CREAM,
        variants=[{"svg": LOGO, "label": "Primary logo — on cream", "bg": "light", "h": 220}],
        usage=["Primary lockup on cream/white; on navy use logo-mono-white.png.",
               "Don't recolor the crest or rainbow bristles; scale uniformly.",
               "Clear space ≈ the crown height on all sides."])
else:
    print(f"(skipping logo card — {LOGO} not found; set NT_LOGO to the logo.svg path)")

# --- Color ---
color_card.build(OUT / "tokens/colors.html",
    title="Noble Touch Painting — Color",
    intro="Warm, premium, trustworthy. Cream ground · navy authority · gold for CTAs & accents.",
    bg=CREAM, fg=INK,
    groups=[
        {"heading": "Brand", "swatches": [
            {"name": "navy (primary)", "value": NAVY}, {"name": "gold (accent / CTA)", "value": GOLD},
            {"name": "cream (background)", "value": CREAM}, {"name": "ink (headings)", "value": INK},
            {"name": "taupe (muted / borders)", "value": TAUPE}]},
        {"heading": "Dark mode", "swatches": [
            {"name": "background", "value": INK}, {"name": "foreground", "value": CREAM},
            {"name": "gold", "value": GOLD}]},
    ])

# --- Typography ---
type_card.build(OUT / "tokens/typography.html",
    title="Noble Touch Painting — Typography",
    intro="Display: Fraunces (serif). UI / body: Inter. Loaded via next/font.",
    bg=CREAM, fg=INK,
    specimens=[
        {"label": "Display · Fraunces", "text": "A noble touch of color", "size": 40, "weight": 600, "font": FRAUNCES},
        {"label": "Headline · Fraunces", "text": "Interior & exterior painting", "size": 24, "weight": 600, "font": FRAUNCES},
        {"label": "Body · Inter", "text": "Expert color matching, undertones, sheen & surface guidance.", "size": 16, "font": INTER},
        {"label": "Small · Inter", "text": "Residential & commercial · free estimates", "size": 13, "font": INTER},
        {"label": "Mono", "text": "lead #NTP-2026-0042", "size": 13, "mono": True},
    ])

# --- Components (custom card via dscard + write — buttons + estimate form) ---
css = f'''  body{{background:{CREAM};color:{INK};}}
  .btn{{display:inline-flex;align-items:center;gap:8px;height:42px;padding:0 22px;border-radius:8px;
        font-size:15px;font-weight:600;border:1.5px solid transparent;cursor:default;font-family:{INTER};}}
  .primary{{background:{NAVY};color:{CREAM};}} .cta{{background:{GOLD};color:{INK};}}
  .outline{{background:transparent;color:{NAVY};border-color:{NAVY};}} .ghost{{background:transparent;color:{NAVY};}}
  .grp{{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:20px;}}
  .card{{background:#fff;border:1px solid rgba(20,32,60,.12);border-radius:14px;padding:24px;max-width:420px;
         box-shadow:0 6px 24px rgba(20,32,60,.06);}}
  .card h3{{font-family:{FRAUNCES};font-size:20px;margin:0 0 6px;color:{INK};}}
  .card p{{margin:0 0 14px;color:{TAUPE};font-size:14px;}}
  .inp{{width:100%;height:42px;padding:0 14px;border:1.5px solid rgba(95,87,73,.4);border-radius:8px;
        background:{CREAM};color:{INK};font-size:15px;font-family:{INTER};}}
  label{{display:block;font-size:13px;font-weight:600;margin:0 0 6px;}}'''
body = f'''<h1>Noble Touch Painting — Components</h1>
<p class="sub">shadcn/ui (new-york, slate base) styled with the brand tokens. Navy is primary; gold is the CTA.</p>
<h2>Buttons</h2>
<div class="grp"><button class="btn primary">Get a free estimate</button>
<button class="btn cta">Book now</button><button class="btn outline">Our work</button>
<button class="btn ghost">Learn more</button></div>
<h2>Card + form</h2>
<div class="card"><h3>Request an estimate</h3><p>Interior, exterior, or commercial — we'll match your color.</p>
<label>Name</label><input class="inp" value="Quinn Vidal">
<div style="height:12px"></div><label>Project</label><input class="inp" value="Repaint living room + trim">
<div style="height:16px"></div><button class="btn cta">Send request</button></div>'''
write(OUT / "components/buttons.html", dscard("Components", "Noble Touch — Components", css, body))

print("built nobletouch cards into", OUT)
