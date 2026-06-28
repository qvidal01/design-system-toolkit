"""Example: the Color + Type token cards added to the (design-sync-managed)
Touchstone Construction design system. Values mirror
touchstone-construction-website/app/globals.css (post zac-feedback rebrand).
Run:  python examples/touchstone.py   → out/touchstone/
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from dscards import color_card, type_card

OUT = pathlib.Path(__file__).resolve().parent.parent / "out" / "touchstone"
INK, PAPER = "#11141A", "#FAFAF7"
FRAUNCES, INTER = 'Fraunces,Georgia,"Times New Roman",serif', "Inter,system-ui,sans-serif"

color_card.build(OUT/"tokens/colors.html", title="Touchstone Construction — Color",
  intro="Light-first brand. Graphite + alabaster ground the UI; silver-slate is primary, forest the accent; bronze / gold / sand are warm metallics.",
  bg=PAPER, fg=INK, groups=[
    {"heading":"Foundation","swatches":[
      {"name":"graphite","value":"#0E1623"},{"name":"graphite-700","value":"#182336"},
      {"name":"alabaster","value":"#FAFAF7"},{"name":"alabaster-200","value":"#F2EFE7"}]},
    {"heading":"Primary — silver / slate","swatches":[
      {"name":"primary","value":"#7A8698"},{"name":"amber (base)","value":"#7E8896"},{"name":"amber-300","value":"#c2cad3"}]},
    {"heading":"Accent — forest","swatches":[
      {"name":"accent / forest","value":"#1F4732"},{"name":"forest-600","value":"#163525"}]},
    {"heading":"Warm metallics","swatches":[
      {"name":"bronze","value":"#8A6B3D"},{"name":"bronze-300","value":"#bf9c5a"},
      {"name":"gold","value":"#C9A24E"},{"name":"sand","value":"#D9D2C0"},{"name":"sand-200","value":"#e3ddc8"}]}])

type_card.build(OUT/"tokens/typography.html", title="Touchstone Construction — Typography",
  intro="Display: Fraunces (serif). UI / body: Inter. Loaded via Google Fonts in the app.",
  bg=PAPER, fg=INK, specimens=[
    {"label":"Display · Fraunces","text":"Built on trust","size":40,"weight":600,"font":FRAUNCES},
    {"label":"Headline · Inter","text":"Roofing & exteriors","size":24,"weight":600,"font":INTER},
    {"label":"Body · Inter","text":"The quick brown fox jumps over the lazy dog.","size":16,"font":INTER},
    {"label":"Small · Inter","text":"Licensed & insured · GAF certified","size":13,"font":INTER},
    {"label":"Mono","text":"estimate #2026-0142","size":13,"mono":True}])
print("built touchstone cards into", OUT)
