"""Shared helpers for building Claude Design cards.

A Claude Design "card" is a self-contained HTML file whose FIRST LINE is a
marker comment:  <!-- @dsCard group="..." -->
The app indexes cards by that marker; everything else is normal HTML/CSS.
"""
import re
import pathlib

MONO = 'ui-monospace,"SF Mono",Menlo,Consolas,monospace'
SANS = 'ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif'


def dscard(group, title, head_css, body, root_css=""):
    """Wrap a body fragment into a complete, self-contained card document.
    `group` is the Design-System-pane section (e.g. Brand, Color, Type,
    Components). The returned string's first line is the @dsCard marker."""
    return f'''<!-- @dsCard group="{group}" -->
<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/><title>{title}</title>
<style>
{root_css}
  *{{box-sizing:border-box;}}
  body{{margin:0;padding:32px;font-family:{SANS};font-size:14px;line-height:1.5;}}
  h1{{font-size:18px;margin:0 0 4px;letter-spacing:-.01em;}}
  p.sub{{margin:0 0 24px;font-size:13px;opacity:.72;}}
  h2{{font-size:12px;text-transform:uppercase;letter-spacing:.06em;opacity:.72;
      margin:26px 0 12px;font-weight:600;}}
{head_css}
</style></head><body>{body}</body></html>'''


def namespace_svg(svg, prefix):
    """Rewrite a self-contained SVG's internal ids so several SVGs can be
    inlined in one document without colliding (gradients, clipPaths, filters,
    <use href>). Without this, duplicate ids resolve to the first definition
    and later logos can mis-paint."""
    ids = set(re.findall(r'id="([^"]+)"', svg))
    for i in sorted(ids, key=len, reverse=True):
        svg = svg.replace(f'id="{i}"', f'id="{prefix}-{i}"')
        svg = svg.replace(f'url(#{i})', f'url(#{prefix}-{i})')
        svg = svg.replace(f'href="#{i}"', f'href="#{prefix}-{i}"')
    return svg


def write(path, content):
    """Write a card and assert the @dsCard marker is the first line."""
    first = content.splitlines()[0]
    if not first.startswith("<!-- @dsCard"):
        raise ValueError(f"{path}: first line must be the @dsCard marker, got: {first!r}")
    p = pathlib.Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    return p
