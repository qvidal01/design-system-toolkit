"""Example: seed the Subjectly design system from subjectly-web (Next.js + shadcn).
Subjectly uses the stock shadcn "neutral" theme — greyscale UI, saturation only
in charts/destructive, Geist Sans/Mono. Values mirror app/globals.css.
Run:  python examples/subjectly.py   → out/subjectly/
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from dscards import color_card, type_card
from dscards.lib import dscard, write

OUT = pathlib.Path(__file__).resolve().parent.parent / "out" / "subjectly"
WHITE, NEARBLACK = "oklch(1 0 0)", "oklch(0.145 0 0)"

# shadcn neutral tokens (light + dark) — used by the component cards
TOKENS = """
  :root{ --radius:.625rem;
    --background:oklch(1 0 0); --foreground:oklch(0.145 0 0); --card:oklch(1 0 0);
    --primary:oklch(0.205 0 0); --primary-foreground:oklch(0.985 0 0);
    --secondary:oklch(0.97 0 0); --secondary-foreground:oklch(0.205 0 0);
    --muted:oklch(0.97 0 0); --muted-foreground:oklch(0.556 0 0);
    --accent:oklch(0.97 0 0); --destructive:oklch(0.577 0.245 27.325);
    --border:oklch(0.922 0 0); --input:oklch(0.922 0 0); --ring:oklch(0.708 0 0); }
  .dark{ --background:oklch(0.145 0 0); --foreground:oklch(0.985 0 0); --card:oklch(0.205 0 0);
    --primary:oklch(0.922 0 0); --primary-foreground:oklch(0.205 0 0);
    --secondary:oklch(0.269 0 0); --secondary-foreground:oklch(0.985 0 0);
    --muted:oklch(0.269 0 0); --muted-foreground:oklch(0.708 0 0);
    --destructive:oklch(0.704 0.191 22.216); --border:oklch(1 0 0 / 10%); --input:oklch(1 0 0 / 15%); }"""

color_card.build(OUT/"tokens/colors.html", title="Subjectly — Color",
  intro="shadcn/ui neutral system. Greyscale carries the UI; saturation is reserved for charts & destructive.",
  bg=WHITE, fg=NEARBLACK, groups=[
    {"heading":"Core","swatches":[
      {"name":"foreground","value":"oklch(0.145 0 0)"},{"name":"primary","value":"oklch(0.205 0 0)"},
      {"name":"secondary / muted","value":"oklch(0.97 0 0)"},{"name":"muted-fg","value":"oklch(0.556 0 0)"},
      {"name":"border","value":"oklch(0.922 0 0)"},{"name":"destructive","value":"oklch(0.577 0.245 27.325)"}]},
    {"heading":"Charts (the only saturated colors)","swatches":[
      {"name":"chart-1","value":"oklch(0.646 0.222 41.116)"},{"name":"chart-2","value":"oklch(0.6 0.118 184.704)"},
      {"name":"chart-3","value":"oklch(0.398 0.07 227.392)"},{"name":"chart-4","value":"oklch(0.828 0.189 84.429)"},
      {"name":"chart-5","value":"oklch(0.769 0.188 70.08)"}]},
    {"heading":"Dark surfaces","swatches":[
      {"name":"background","value":"oklch(0.145 0 0)"},{"name":"card","value":"oklch(0.205 0 0)"},
      {"name":"muted","value":"oklch(0.269 0 0)"}]}])

type_card.build(OUT/"tokens/typography.html", title="Subjectly — Typography",
  intro="Sans: Geist Sans. Mono: Geist Mono. (Substitutes shown if Geist isn't installed.)",
  bg=WHITE, fg=NEARBLACK, specimens=[
    {"label":"Display 32/700","text":"Understand anything, faster","size":32,"weight":700},
    {"label":"H1 24/600","text":"Documents & chat","size":24,"weight":600},
    {"label":"Body 14/400","text":"The quick brown fox jumps over the lazy dog.","size":14},
    {"label":"Mono 13","text":"npm run dev · localhost:8000","size":13,"mono":True}])

# Component cards use the TOKENS via dscard(root_css=...)
BTN = '''  body{background:var(--background);color:var(--foreground);}
  .btn{display:inline-flex;align-items:center;height:36px;padding:0 16px;border-radius:calc(var(--radius) - 2px);font-size:14px;font-weight:500;border:1px solid transparent;}
  .default{background:var(--primary);color:var(--primary-foreground);} .secondary{background:var(--secondary);color:var(--secondary-foreground);}
  .destructive{background:var(--destructive);color:#fff;} .outline{background:var(--background);color:var(--foreground);border-color:var(--border);}
  .ghost{background:transparent;color:var(--foreground);} .grp{display:flex;gap:10px;flex-wrap:wrap;align-items:center;}
  .panel{border:1px solid var(--border);border-radius:var(--radius);padding:20px;margin-bottom:14px;} .panel.dk{background:oklch(0.145 0 0);}'''
def btns(): return ('<div class="grp"><button class="btn default">Button</button><button class="btn secondary">Secondary</button>'
  '<button class="btn destructive">Destructive</button><button class="btn outline">Outline</button><button class="btn ghost">Ghost</button></div>')
write(OUT/"components/buttons.html", dscard("Components","Subjectly — Buttons", BTN,
  f'<h1>Subjectly — Buttons</h1><p class="sub">shadcn Button variants, light & dark.</p><div class="panel">{btns()}</div><h2>On dark</h2><div class="panel dk"><div class="dark">{btns()}</div></div>', root_css=TOKENS))

FORM = '''  body{background:var(--background);color:var(--foreground);}
  .field{margin-bottom:16px;max-width:420px;} label{display:block;font-size:13px;font-weight:500;margin-bottom:6px;}
  .inp{width:100%;height:36px;padding:0 12px;border:1px solid var(--input);border-radius:calc(var(--radius) - 2px);background:var(--background);color:var(--foreground);font-size:14px;}
  textarea.inp{height:80px;padding:8px 12px;resize:none;} .hint{font-size:12px;color:var(--muted-foreground);margin-top:6px;}'''
write(OUT/"components/forms.html", dscard("Components","Subjectly — Form controls", FORM,
  '<h1>Subjectly — Form controls</h1><p class="sub">Input, textarea — bound to --input, --ring, --radius.</p>'
  '<div class="field"><label>Email</label><input class="inp" value="quinn@aiqso.io"></div>'
  '<div class="field"><label>Ask about your document</label><textarea class="inp">Summarize chapter 3 in five bullets.</textarea><div class="hint">Press Enter to send.</div></div>', root_css=TOKENS))

SURF = '''  body{background:var(--background);color:var(--foreground);}
  .card{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:22px;max-width:440px;margin-bottom:16px;}
  .card h3{margin:0 0 4px;font-size:16px;} .card p{margin:0;color:var(--muted-foreground);font-size:13px;}
  .badge{display:inline-flex;height:22px;padding:0 9px;border-radius:999px;font-size:12px;font-weight:600;border:1px solid transparent;}
  .b-default{background:var(--primary);color:var(--primary-foreground);} .b-outline{border-color:var(--border);color:var(--foreground);}
  .b-destructive{background:var(--destructive);color:#fff;} .grp{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:14px;}
  .bar{height:8px;border-radius:999px;background:var(--secondary);overflow:hidden;max-width:440px;} .bar i{display:block;height:100%;width:64%;background:var(--primary);}'''
write(OUT/"components/surfaces.html", dscard("Components","Subjectly — Surfaces", SURF,
  '<h1>Subjectly — Surfaces</h1><p class="sub">Card, badge, progress.</p>'
  '<div class="card"><h3>Linear Algebra — Ch.3</h3><p>14 pages · indexed · 248 chunks.</p><div class="bar"><i></i></div></div>'
  '<div class="grp"><span class="badge b-default">Indexed</span><span class="badge b-outline">PDF</span><span class="badge b-destructive">Failed</span></div>', root_css=TOKENS))
print("built subjectly cards into", OUT)
