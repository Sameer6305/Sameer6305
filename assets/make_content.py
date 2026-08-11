"""
Generate content block SVGs:
  dark/identity.svg   light/identity.svg   — Engineering Identity text block
  dark/semantica.svg  light/semantica.svg  — Semantica current work block
  dark/principles.svg light/principles.svg — Engineering Principles + Technical Direction
  dark/footer.svg     light/footer.svg     — Footer status
"""

import pathlib, textwrap

MONO  = "'Courier New', Courier, monospace"
SANS  = "-apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"

# ─── Colour palettes ──────────────────────────────────────────────────────────

D = dict(
    bg="#0E0E0E", rule="#2A2825", box="#161412", stroke="#3A3835",
    text="#E8E4DC", dim="#4A4745", annot="#2E2C2A", acc="#9C9791",
    mid="#6A6560", label="#9C9791",
)
L = dict(
    bg="#F6F6F4", rule="#DEDAD5", box="#EEECEA", stroke="#C8C4C0",
    text="#1A1816", dim="#B0ACA8", annot="#C0BCB8", acc="#7A7673",
    mid="#8A8480", label="#7A7673",
)

base = pathlib.Path(__file__).parent

# ─── Helper ───────────────────────────────────────────────────────────────────

def write(path, content):
    pathlib.Path(path).write_text(content, encoding="utf-8")


# ═══════════════════════════════════════════════════════════════════════════════
# 1. ENGINEERING IDENTITY
# ═══════════════════════════════════════════════════════════════════════════════

def identity_svg(c):
    lines_text = [
        "My engineering work started in backend systems — services, APIs,",
        "and data pipelines — and has moved steadily toward AI infrastructure:",
        "retrieval pipelines, knowledge graphs, and semantic layers that let AI",
        "systems reason over structured knowledge rather than generating",
        "plausible text. Most of that work now happens in the open,",
        "on infrastructure other engineers rely on.",
    ]
    lh = 20
    W, H = 800, 30 + len(lines_text)*lh + 16
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
        f'  <rect width="{W}" height="{H}" fill="{c["bg"]}"/>',
    ]
    # left accent bar
    bar_h = len(lines_text)*lh + 4
    parts.append(f'  <rect x="20" y="14" width="2" height="{bar_h}" fill="{c["acc"]}" opacity="0.5"/>')
    # label
    parts.append(f'  <text x="32" y="26" font-family="{MONO}" font-size="9" letter-spacing="2" fill="{c["label"]}">PROGRESSION · BACKEND → AI INFRASTRUCTURE → OPEN SOURCE</text>')
    for i, line in enumerate(lines_text):
        y = 42 + i*lh
        parts.append(f'  <text x="32" y="{y}" font-family="{MONO}" font-size="13" fill="{c["text"]}">{line}</text>')
    # bottom rule
    parts.append(f'  <line x1="20" y1="{H-2}" x2="780" y2="{H-2}" stroke="{c["rule"]}" stroke-width="1"/>')
    parts.append('</svg>')
    return '\n'.join(parts)


write(base/"dark"/"identity.svg",  identity_svg(D))
write(base/"light"/"identity.svg", identity_svg(L))
print("identity.svg done")


# ═══════════════════════════════════════════════════════════════════════════════
# 2. SEMANTICA
# ═══════════════════════════════════════════════════════════════════════════════

def semantica_svg(c):
    W, H = 800, 230
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
        f'  <rect width="{W}" height="{H}" fill="{c["bg"]}"/>',
        # outer box
        f'  <rect x="20" y="10" width="760" height="210" fill="{c["box"]}" stroke="{c["stroke"]}" stroke-width="1"/>',
        # accent top edge
        f'  <line x1="20" y1="10" x2="780" y2="10" stroke="{c["acc"]}" stroke-width="1.5"/>',
        # SEMANTICA header inside box
        f'  <text x="36" y="36" font-family="{MONO}" font-size="16" letter-spacing="4" font-weight="700" fill="{c["text"]}">SEMANTICA</text>',
        # BUILDING NOW chip
        f'  <rect x="166" y="22" width="116" height="16" fill="{c["bg"]}" stroke="{c["acc"]}" stroke-width="1" rx="2"/>',
        f'  <text x="174" y="33" font-family="{MONO}" font-size="9" letter-spacing="2" fill="{c["acc"]}">BUILDING NOW</text>',
        # role line
        f'  <text x="36" y="54" font-family="{MONO}" font-size="10" letter-spacing="1" fill="{c["mid"]}">AI Systems &amp; Backend Engineering</text>',
        # thin inner rule
        f'  <line x1="36" y1="62" x2="764" y2="62" stroke="{c["rule"]}" stroke-width="1"/>',
        # description
        f'  <text x="36" y="80" font-family="{MONO}" font-size="11" fill="{c["text"]}">Semantic data and knowledge infrastructure for AI systems that need to be</text>',
        f'  <text x="36" y="96" font-family="{MONO}" font-size="11" fill="{c["text"]}">explainable and auditable — not just fluent. A knowledge graph engine,</text>',
        f'  <text x="36" y="112" font-family="{MONO}" font-size="11" fill="{c["text"]}">retrieval framework, and semantic layer built to close the gap between</text>',
        f'  <text x="36" y="128" font-family="{MONO}" font-size="11" fill="{c["text"]}">language models and structured, verifiable knowledge.</text>',
        # work scope label
        f'  <text x="36" y="150" font-family="{MONO}" font-size="9" letter-spacing="2" fill="{c["label"]}">SCOPE OF WORK</text>',
        # scope items — two columns
        f'  <text x="36" y="166" font-family="{MONO}" font-size="10" fill="{c["dim"]}">Backend infrastructure</text>',
        f'  <text x="220" y="166" font-family="{MONO}" font-size="10" fill="{c["dim"]}">Data ingestion / retrieval</text>',
        f'  <text x="420" y="166" font-family="{MONO}" font-size="10" fill="{c["dim"]}">Knowledge graph architecture</text>',
        f'  <text x="36" y="182" font-family="{MONO}" font-size="10" fill="{c["dim"]}">MCP server / CLI tooling</text>',
        f'  <text x="220" y="182" font-family="{MONO}" font-size="10" fill="{c["dim"]}">Integrations / developer tooling</text>',
        f'  <text x="420" y="182" font-family="{MONO}" font-size="10" fill="{c["dim"]}">Testing · code review · production</text>',
        # links
        f'  <text x="36" y="206" font-family="{MONO}" font-size="10" letter-spacing="1" fill="{c["acc"]}">semantica-agi/semantica</text>',
        f'  <text x="218" y="206" font-family="{MONO}" font-size="10" fill="{c["mid"]}">·</text>',
        f'  <text x="228" y="206" font-family="{MONO}" font-size="10" letter-spacing="1" fill="{c["acc"]}">getsemantica.ai</text>',
        '</svg>',
    ]
    return '\n'.join(parts)


write(base/"dark"/"semantica.svg",  semantica_svg(D))
write(base/"light"/"semantica.svg", semantica_svg(L))
print("semantica.svg done")


# ═══════════════════════════════════════════════════════════════════════════════
# 3. ENGINEERING PRINCIPLES + TECHNICAL DIRECTION
# ═══════════════════════════════════════════════════════════════════════════════

def principles_svg(c):
    W, H = 800, 310

    principles = [
        ("01 / GROUND TRUTH",
         "AI systems lean on retrieval and knowledge graphs —",
         "not blind trust in model output."),
        ("02 / FAILURE CASES",
         "The backend and data layer are designed around",
         "what happens when things break."),
        ("03 / INTERFACES",
         "APIs, CLIs, and MCP tools are part of the product —",
         "not secondary to the core logic."),
        ("04 / DELIVERY",
         "Tests and documentation ship with the feature.",
         "They are part of what  \"done\"  means."),
    ]

    domains = [
        ("AI &amp; SEMANTIC SYSTEMS",     "LLMs · GraphRAG · Knowledge Graphs · Retrieval · NLP"),
        ("BACKEND &amp; INFRASTRUCTURE",  "Python · Java · APIs · Distributed Systems · Docker · AWS · Redis"),
        ("DATA &amp; DISTRIBUTED SYSTEMS","Kafka · Spark · ETL · SQL · Data Quality"),
    ]

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
        f'  <rect width="{W}" height="{H}" fill="{c["bg"]}"/>',
        # PRINCIPLES label
        f'  <text x="20" y="16" font-family="{MONO}" font-size="9" letter-spacing="2" fill="{c["label"]}">ENGINEERING PRINCIPLES</text>',
        f'  <line x1="20" y1="22" x2="780" y2="22" stroke="{c["rule"]}" stroke-width="1"/>',
    ]

    # 2x2 principle grid
    cols = [20, 410]
    rows = [40, 128]
    pi = 0
    for ry in rows:
        for cx in cols:
            num_label, line1, line2 = principles[pi]
            pi += 1
            # box
            bw, bh = 370, 78
            parts.append(f'  <rect x="{cx}" y="{ry}" width="{bw}" height="{bh}" fill="{c["box"]}" stroke="{c["stroke"]}" stroke-width="1"/>')
            parts.append(f'  <text x="{cx+12}" y="{ry+18}" font-family="{MONO}" font-size="10" letter-spacing="2" fill="{c["acc"]}">{num_label}</text>')
            parts.append(f'  <line x1="{cx+12}" y1="{ry+24}" x2="{cx+bw-12}" y2="{ry+24}" stroke="{c["rule"]}" stroke-width="1"/>')
            parts.append(f'  <text x="{cx+12}" y="{ry+42}" font-family="{MONO}" font-size="11" fill="{c["text"]}">{line1}</text>')
            parts.append(f'  <text x="{cx+12}" y="{ry+58}" font-family="{MONO}" font-size="11" fill="{c["dim"]}">{line2}</text>')

    # TECHNICAL DIRECTION
    ty = 224
    parts.append(f'  <line x1="20" y1="{ty}" x2="780" y2="{ty}" stroke="{c["rule"]}" stroke-width="1"/>')
    parts.append(f'  <text x="20" y="{ty+14}" font-family="{MONO}" font-size="9" letter-spacing="2" fill="{c["label"]}">TECHNICAL DIRECTION</text>')
    dy = ty + 30
    for dom_label, dom_items in domains:
        parts.append(f'  <text x="20" y="{dy}" font-family="{MONO}" font-size="10" letter-spacing="2" fill="{c["text"]}" font-weight="700">{dom_label}</text>')
        lw = len(dom_label) * 7.4 + 20
        parts.append(f'  <text x="{lw + 10}" y="{dy}" font-family="{MONO}" font-size="10" fill="{c["mid"]}">— {dom_items}</text>')
        dy += 20

    parts.append(f'  <line x1="20" y1="{H-2}" x2="780" y2="{H-2}" stroke="{c["rule"]}" stroke-width="1"/>')
    parts.append('</svg>')
    return '\n'.join(parts)


write(base/"dark"/"principles.svg",  principles_svg(D))
write(base/"light"/"principles.svg", principles_svg(L))
print("principles.svg done")


# ═══════════════════════════════════════════════════════════════════════════════
# 4. FOOTER
# ═══════════════════════════════════════════════════════════════════════════════

def footer_svg(c):
    W, H = 800, 56
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
        f'  <rect width="{W}" height="{H}" fill="{c["bg"]}"/>',
        f'  <line x1="0" y1="0" x2="{W}" y2="0" stroke="{c["rule"]}" stroke-width="1"/>',
        # Status dot + label
        f'  <circle cx="26" cy="20" r="3" fill="{c["acc"]}" opacity="0.8"/>',
        f'  <text x="36" y="24" font-family="{MONO}" font-size="10" letter-spacing="2" fill="{c["acc"]}">BUILDING</text>',
        f'  <text x="104" y="24" font-family="{MONO}" font-size="10" fill="{c["rule"]}">·</text>',
        f'  <text x="114" y="24" font-family="{MONO}" font-size="10" letter-spacing="1" fill="{c["mid"]}">AI SYSTEMS · SEMANTIC INFRASTRUCTURE · OPEN SOURCE</text>',
        # Links row
        f'  <text x="26" y="44" font-family="{MONO}" font-size="9" letter-spacing="1" fill="{c["dim"]}">github.com/Sameer6305</text>',
        f'  <text x="176" y="44" font-family="{MONO}" font-size="9" fill="{c["annot"]}">·</text>',
        f'  <text x="186" y="44" font-family="{MONO}" font-size="9" letter-spacing="1" fill="{c["dim"]}">linkedin.com/in/sameerkadam6305</text>',
        f'  <text x="386" y="44" font-family="{MONO}" font-size="9" fill="{c["annot"]}">·</text>',
        f'  <text x="396" y="44" font-family="{MONO}" font-size="9" letter-spacing="1" fill="{c["dim"]}">getsemantica.ai</text>',
        f'  <text x="490" y="44" font-family="{MONO}" font-size="9" fill="{c["annot"]}">·</text>',
        f'  <text x="500" y="44" font-family="{MONO}" font-size="9" letter-spacing="1" fill="{c["dim"]}">sskadam6305@gmail.com</text>',
        f'  <line x1="0" y1="{H-1}" x2="{W}" y2="{H-1}" stroke="{c["rule"]}" stroke-width="1"/>',
        '</svg>',
    ]
    return '\n'.join(parts)


write(base/"dark"/"footer.svg",  footer_svg(D))
write(base/"light"/"footer.svg", footer_svg(L))
print("footer.svg done")

import os
total = 0
for theme in ["dark","light"]:
    for f in (base/theme).iterdir():
        sz = os.path.getsize(f)
        total += sz
        print(f"  {theme}/{f.name}: {sz:,} bytes")
print(f"Total: {total:,} bytes")
