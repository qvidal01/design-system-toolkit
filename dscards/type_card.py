"""Build a Typography specimen card.

specimens: [{"label":..,"text":..,"size":<px>,"weight":<opt>,"mono":<opt bool>}]
"""
from .lib import dscard, MONO, write


def build(out, *, specimens, title="Typography", intro="", bg="#0b1622", fg="#e8eef5", group="Type"):
    css = f'''  body{{background:{bg};color:{fg};}}
  .spec{{border-top:1px solid rgba(255,255,255,.12);padding:14px 0;display:grid;
         grid-template-columns:140px 1fr;gap:16px;align-items:baseline;}}
  .lab{{opacity:.6;font-size:11px;font-family:{MONO};}}'''
    body = f'<h1>{title}</h1><p class="sub">{intro}</p>'
    for s in specimens:
        style = f'font-size:{s["size"]}px'
        if s.get("weight"):
            style += f';font-weight:{s["weight"]}'
        if s.get("mono"):
            style += f';font-family:{MONO}'
        body += (f'<div class="spec"><div class="lab">{s["label"]}</div>'
                 f'<div style="{style}">{s["text"]}</div></div>')
    return write(out, dscard(group, title, css, body))
