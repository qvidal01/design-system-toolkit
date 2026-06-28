"""Build a Color card from swatch groups.

groups: [{"heading": <str>, "swatches": [{"name":..,"value":<css color>}]}]
`value` is any CSS color (hex, oklch(...), rgb(...)) and is used both as the
chip background and the printed token value.
"""
from .lib import dscard, MONO, write


def build(out, *, groups, title="Color", intro="", bg="#0b1622", fg="#e8eef5", group="Color"):
    css = f'''  body{{background:{bg};color:{fg};}}
  .row{{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px;}}
  .sw{{border:1px solid rgba(255,255,255,.12);border-radius:10px;overflow:hidden;}}
  .chip{{height:56px;}} .m{{padding:7px 9px;}} .n{{font-weight:600;font-size:12px;}}
  .v{{font-family:{MONO};font-size:10px;opacity:.7;}}'''

    def sw(s):
        return (f'<div class="sw"><div class="chip" style="background:{s["value"]}"></div>'
                f'<div class="m"><div class="n">{s["name"]}</div>'
                f'<div class="v">{s["value"]}</div></div></div>')

    body = f'<h1>{title}</h1><p class="sub">{intro}</p>'
    for g in groups:
        body += f'<h2>{g["heading"]}</h2><div class="row">' + "".join(sw(s) for s in g["swatches"]) + '</div>'
    return write(out, dscard(group, title, css, body))
