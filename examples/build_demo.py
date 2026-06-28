"""Demo: build Color + Typography cards into ./out/ (no external assets needed).
Run from the repo root:  python examples/build_demo.py
Then:  verify/render.sh out/colors.html out/colors.png 820x560
For a logo card, pass real SVG paths to dscards.logo_card.build (see README)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from dscards import color_card, type_card

OUT = pathlib.Path(__file__).resolve().parent.parent / "out"

color_card.build(
    OUT / "colors.html",
    title="Demo — Color",
    intro="Swatch groups from any token map (hex, oklch, rgb).",
    groups=[
        {"heading": "Brand", "swatches": [
            {"name": "primary", "value": "#7A8698"},
            {"name": "accent", "value": "#1F4732"},
            {"name": "graphite", "value": "#0E1623"},
        ]},
        {"heading": "Tokens (oklch ok too)", "swatches": [
            {"name": "muted", "value": "oklch(0.97 0 0)"},
            {"name": "destructive", "value": "oklch(0.577 0.245 27.3)"},
        ]},
    ],
)

type_card.build(
    OUT / "type.html",
    title="Demo — Typography",
    intro="Display / body / mono specimen.",
    specimens=[
        {"label": "Display 32/700", "text": "Build once, reuse everywhere", "size": 32, "weight": 700},
        {"label": "Body 14/400", "text": "The quick brown fox jumps over the lazy dog.", "size": 14},
        {"label": "Mono 13", "text": "designsync · finalize_plan · write_files", "size": 13, "mono": True},
    ],
)
print("built:", OUT / "colors.html", OUT / "type.html")
