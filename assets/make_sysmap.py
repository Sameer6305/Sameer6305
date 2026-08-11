"""
Generate assets/dark/system-map.svg and assets/light/system-map.svg
Architecture: AI Systems bifurcates into Knowledge Graphs and Retrieval,
both feed into Data/Ingestion, then Backend Infrastructure,
then converges to Developer Tooling (MCP·CLI·APIs).
Visual: thin-line engineering schematic, monospace labels, layer numbers,
small technical annotations.
"""

import pathlib

W, H = 800, 320

DARK_BG    = "#0E0E0E"
DARK_RULE  = "#2A2825"
DARK_BOX   = "#161412"
DARK_STROKE= "#3A3835"
DARK_TEXT  = "#E8E4DC"
DARK_DIM   = "#4A4745"
DARK_ANNOT = "#2E2C2A"
DARK_ACC   = "#9C9791"   # accent: warm graphite

LIGHT_BG    = "#F6F6F4"
LIGHT_RULE  = "#DEDAD5"
LIGHT_BOX   = "#EEECEA"
LIGHT_STROKE= "#C8C4C0"
LIGHT_TEXT  = "#1A1816"
LIGHT_DIM   = "#7A7673"
LIGHT_ANNOT = "#C0BCB8"
LIGHT_ACC   = "#7A7673"

MONO = "'Courier New', Courier, monospace"

def svg(bg, rule, box, stroke, text, dim, annot, acc):
    # Box positions (cx, cy, w, h, label, sublabel)
    boxes = [
        (400, 28,  300, 32, "AI SYSTEMS",               "inference · generation · reasoning"),
        (220, 110, 220, 30, "KNOWLEDGE GRAPHS",          "GraphRAG · Neo4j · SPARQL"),
        (580, 110, 200, 30, "RETRIEVAL",                 "vector · hybrid · BM25"),
        (400, 190, 260, 30, "DATA / INGESTION",          "pipelines · ETL · batch"),
        (400, 254, 300, 30, "BACKEND INFRASTRUCTURE",    "APIs · services · distributed"),
        (400, 312, 280, 32, "DEVELOPER TOOLING",         "MCP · CLI · APIs · SDKs"),
    ]

    lines = []
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 344" width="{W}" height="344">')
    lines.append(f'  <rect width="{W}" height="344" fill="{bg}"/>')

    # Layer labels on left
    layer_y = [44, 125, 205, 269, 328]
    layer_labels = ["L01", "L02", "L03", "L04", "L05"]
    for i, (ly, ll) in enumerate(zip(layer_y, layer_labels)):
        lines.append(f'  <text x="10" y="{ly}" font-family="{MONO}" font-size="8" letter-spacing="1" fill="{annot}">{ll}</text>')

    # Draw boxes
    for (cx, cy, bw, bh, label, sublabel) in boxes:
        x = cx - bw // 2
        y = cy - bh // 2
        # highlight Developer Tooling with accent stroke
        s = acc if label == "DEVELOPER TOOLING" else stroke
        lw = "1.5" if label == "DEVELOPER TOOLING" else "1"
        lines.append(f'  <rect x="{x}" y="{y}" width="{bw}" height="{bh}" fill="{box}" stroke="{s}" stroke-width="{lw}"/>')
        lines.append(f'  <text x="{cx}" y="{cy + 5}" font-family="{MONO}" font-size="11" letter-spacing="2" text-anchor="middle" fill="{text}">{label}</text>')
        # sublabel annotation — right of box
        lines.append(f'  <text x="{x + bw + 8}" y="{cy + 4}" font-family="{MONO}" font-size="8" letter-spacing="0.5" fill="{annot}">{sublabel}</text>')

    # Connectors — AI SYSTEMS → KG (left) and RETRIEVAL (right)
    # AI bottom center → split
    ax, ay = 400, 44  # AI center-bottom
    lines.append(f'  <line x1="{ax}" y1="{ay}" x2="{ax}" y2="70" stroke="{dim}" stroke-width="1"/>')
    # horizontal branch
    lines.append(f'  <line x1="220" y1="70" x2="580" y2="70" stroke="{dim}" stroke-width="1"/>')
    # down to KG
    lines.append(f'  <line x1="220" y1="70" x2="220" y2="95" stroke="{dim}" stroke-width="1"/>')
    lines.append(f'  <polygon points="216,92 224,92 220,96" fill="{dim}"/>')
    # down to Retrieval
    lines.append(f'  <line x1="580" y1="70" x2="580" y2="95" stroke="{dim}" stroke-width="1"/>')
    lines.append(f'  <polygon points="576,92 584,92 580,96" fill="{dim}"/>')

    # KG + Retrieval → converge to Data/Ingestion
    lines.append(f'  <line x1="220" y1="125" x2="220" y2="160" stroke="{dim}" stroke-width="1"/>')
    lines.append(f'  <line x1="580" y1="125" x2="580" y2="160" stroke="{dim}" stroke-width="1"/>')
    lines.append(f'  <line x1="220" y1="160" x2="580" y2="160" stroke="{dim}" stroke-width="1"/>')
    lines.append(f'  <line x1="400" y1="160" x2="400" y2="175" stroke="{dim}" stroke-width="1"/>')
    lines.append(f'  <polygon points="396,173 404,173 400,177" fill="{dim}"/>')

    # Data → Backend
    lines.append(f'  <line x1="400" y1="205" x2="400" y2="239" stroke="{dim}" stroke-width="1"/>')
    lines.append(f'  <polygon points="396,237 404,237 400,241" fill="{dim}"/>')

    # Backend → Developer Tooling (accent colored)
    lines.append(f'  <line x1="400" y1="269" x2="400" y2="296" stroke="{acc}" stroke-width="1"/>')
    lines.append(f'  <polygon points="396,294 404,294 400,298" fill="{acc}"/>')

    # Bottom rule
    lines.append(f'  <line x1="30" y1="340" x2="770" y2="340" stroke="{rule}" stroke-width="1"/>')
    lines.append(f'  <text x="30" y="344" font-family="{MONO}" font-size="8" letter-spacing="1" fill="{annot}">SAMEER KADAM · ENGINEERING SYSTEM · SK/001</text>')

    lines.append('</svg>')
    return '\n'.join(lines)


base = pathlib.Path(__file__).parent

dark_svg  = svg(DARK_BG,  DARK_RULE,  DARK_BOX,  DARK_STROKE,  DARK_TEXT,  DARK_DIM,  DARK_ANNOT,  DARK_ACC)
light_svg = svg(LIGHT_BG, LIGHT_RULE, LIGHT_BOX, LIGHT_STROKE, LIGHT_TEXT, LIGHT_DIM, LIGHT_ANNOT, LIGHT_ACC)

(base / "dark"  / "system-map.svg").write_text(dark_svg,  encoding="utf-8")
(base / "light" / "system-map.svg").write_text(light_svg, encoding="utf-8")

import os
for p in ["dark/system-map.svg", "light/system-map.svg"]:
    full = base / p
    print(f"{p}: {os.path.getsize(full):,} bytes")
print("Done.")
