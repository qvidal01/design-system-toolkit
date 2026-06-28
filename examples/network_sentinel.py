"""Example: the Network Sentinel — SOC Dashboard design system (a *product* of
AIQSO). Branded-house model: it reuses the AIQSO master logo + a product
signature line, and earns its own identity via a cyan highlight + dark SOC
surfaces. Logo SVGs come from the aiqso-brand repo; colors mirror the SOC tokens.
Run:  python examples/network_sentinel.py   → out/network-sentinel/
"""
import os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from dscards import color_card
from dscards.lib import dscard, write, namespace_svg

OUT = pathlib.Path(__file__).resolve().parent.parent / "out" / "network-sentinel"
LOGO_DIR = os.environ.get("AIQSO_LOGO_DIR", os.path.expanduser("~/projects/aiqso-brand/logo"))
AZURE, CYAN = "oklch(0.62 0.13 245)", "#46C8E6"

# --- Brand: AIQSO master lockup + "AIQSO // NETWORK SENTINEL" product signature ---
horiz_p, emblem_p = os.path.join(LOGO_DIR, "aiqso-logo-horizontal.svg"), os.path.join(LOGO_DIR, "aiqso-emblem.svg")
if os.path.exists(horiz_p) and os.path.exists(emblem_p):
    horiz = namespace_svg(open(horiz_p, encoding="utf-8").read().strip(), "hd")
    emblem = namespace_svg(open(emblem_p, encoding="utf-8").read().strip(), "em")
    css = '''  :root{ --bg:oklch(0.15 0.006 255); --card:oklch(0.185 0.007 255); --fg:oklch(0.96 0.004 255);
            --muted:oklch(0.68 0.008 255); --border:oklch(1 0 0 / 8%);
            --primary:oklch(0.62 0.13 245); --accent:#46C8E6; }
  body{background:var(--bg);color:var(--fg);}
  .frame{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:28px 32px;display:flex;align-items:center;gap:28px;flex-wrap:wrap;}
  .frame svg{display:block;} .lockup-h svg{height:52px;width:auto;}
  .product{display:flex;align-items:center;gap:18px;} .product .em svg{height:58px;width:auto;}
  .divider{width:1px;height:42px;background:var(--border);}
  .sig .org{font:600 12px/1 ui-sans-serif,system-ui;letter-spacing:.18em;color:var(--muted);}
  .sig .prod{font:700 20px/1 ui-monospace,"SF Mono",Menlo,monospace;letter-spacing:.04em;color:var(--fg);margin-top:7px;}
  .sig .prod b{color:var(--accent);font-weight:700;}
  .cap{color:var(--muted);font-size:12px;margin-top:10px;max-width:64ch;}'''
    body = f'''<h1>AIQSO &mdash; Network Sentinel &middot; Brand</h1>
  <p class="sub">A <em>product</em> of AIQSO &mdash; reuses the master logo; identity comes from the cyan highlight + dark SOC surfaces, not a new mark.</p>
  <h2>Master lockup &mdash; horizontal (white, for dark surfaces)</h2>
  <div class="frame lockup-h">{horiz}</div>
  <h2>Product lockup &mdash; AIQSO // Network Sentinel</h2>
  <div class="frame"><div class="product"><div class="em">{emblem}</div><div class="divider"></div>
    <div class="sig"><div class="org">AIQSO</div><div class="prod">NETWORK&nbsp;<b>SENTINEL</b></div></div></div></div>
  <p class="cap">Branded-house: master AIQSO mark + product signature. Azure stays the core UI accent; cyan <code>#46C8E6</code> is the product highlight.</p>'''
    write(OUT / "brand/logo.html", dscard("Brand", "AIQSO // Network Sentinel — Brand", css, body))
else:
    print(f"(skipping logo card — AIQSO logo SVGs not found under {LOGO_DIR}; set AIQSO_LOGO_DIR)")

# --- Color & severity (SOC dashboard) ---
color_card.build(OUT / "tokens/colors.html", title="Network Sentinel — Color & Severity",
    intro="Restrained enterprise. Charcoal surfaces, AIQSO azure for core UI, a cyan product-highlight, saturation otherwise reserved for severity.",
    bg="oklch(0.15 0.006 255)", fg="oklch(0.96 0.004 255)", groups=[
        {"heading": "Surfaces (dark)", "swatches": [
            {"name": "background", "value": "oklch(0.15 0.006 255)"}, {"name": "card +1", "value": "oklch(0.185 0.007 255)"},
            {"name": "popover +2", "value": "oklch(0.205 0.008 255)"}, {"name": "muted", "value": "oklch(0.225 0.007 255)"}]},
        {"heading": "Brand accent — AIQSO azure (primary)", "swatches": [{"name": "primary · azure", "value": AZURE}]},
        {"heading": "Product highlight — Network Sentinel cyan", "swatches": [{"name": "accent · cyan", "value": CYAN}]},
        {"heading": "Severity scale (the only saturated colors)", "swatches": [
            {"name": "critical", "value": "oklch(0.58 0.22 25)"}, {"name": "high", "value": "oklch(0.68 0.19 48)"},
            {"name": "medium", "value": "oklch(0.80 0.16 85)"}, {"name": "low", "value": "oklch(0.62 0.13 245)"},
            {"name": "info", "value": "oklch(0.68 0.012 255)"}, {"name": "resolved", "value": "oklch(0.65 0.15 155)"}]}])
print("built network-sentinel cards into", OUT)
