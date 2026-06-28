"""Build a Brand logo card from one or more self-contained SVG files.

Each variant is a dict:
  {"svg": <path>, "label": <str>, "bg": "dark"|"light", "h": <px height>}
Multiple SVGs are id-namespaced so their gradients/clips don't collide.
"""
import pathlib
from .lib import dscard, namespace_svg, write


def build(out, *, variants, title="Brand — Logo", intro="", usage=None,
          ink="#0b1622", fg="#e8eef5", lightbg="#f4f7fb", group="Brand"):
    css = f'''  body{{background:{ink};color:{fg};}}
  .grid{{display:grid;grid-template-columns:1fr 1fr;gap:16px;}}
  .frame{{border:1px solid rgba(255,255,255,.10);border-radius:12px;padding:28px;
          display:flex;align-items:center;justify-content:center;min-height:110px;}}
  .frame svg{{display:block;}}
  .cap{{font-size:11px;opacity:.7;margin:8px 2px 0;}}
  ul.rules{{font-size:12.5px;line-height:1.7;opacity:.8;padding-left:18px;margin:6px 0 0;}}'''
    cells = []
    for n, v in enumerate(variants):
        svg = namespace_svg(pathlib.Path(v["svg"]).read_text(encoding="utf-8").strip(), f"v{n}")
        bg = lightbg if v.get("bg") == "light" else ink
        h = v.get("h", 64)
        cells.append(
            f'<div><div class="frame" style="background:{bg}">'
            f'<div style="height:{h}px;display:flex" class="ns{n}">{svg}</div></div>'
            f'<p class="cap">{v.get("label","")}</p></div>'
        )
    # constrain each inlined svg to its cell height
    css += "".join(f"\n  .ns{n} svg{{height:{v.get('h',64)}px;width:auto;}}"
                   for n, v in enumerate(variants))
    body = f'<h1>{title}</h1><p class="sub">{intro}</p><div class="grid">' + "".join(cells) + '</div>'
    if usage:
        body += '<h2>Usage</h2><ul class="rules">' + "".join(f"<li>{u}</li>" for u in usage) + '</ul>'
    return write(out, dscard(group, title, css, body))
