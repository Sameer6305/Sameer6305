"""
Generate section header SVGs for dark and light themes.
Each section: number + label + thin full-width rule + small annotation.
"""

SECTIONS = [
    ("01", "ENGINEERING IDENTITY",   "~/identity"),
    ("02", "CURRENT WORK",           "~/semantica — building now"),
    ("03", "SYSTEM MAP",             "~/architecture"),
    ("04", "ENGINEERING PRINCIPLES", "~/specification"),
]

DARK = {
    "bg":       "#0E0E0E",
    "rule":     "#2A2825",
    "num":      "#9C9791",
    "label":    "#E8E4DC",
    "annot":    "#3A3835",
}

LIGHT = {
    "bg":       "#F6F6F4",
    "rule":     "#DEDAD5",
    "num":      "#7A7673",
    "label":    "#1A1816",
    "annot":    "#C0BCB8",
}

TEMPLATE = """\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 48" width="800" height="48">
  <rect width="800" height="48" fill="{bg}"/>
  <text x="20" y="28"
        font-family="'Courier New', Courier, monospace"
        font-size="22" font-weight="700" letter-spacing="1"
        fill="{num}">{num_text}</text>
  <text x="70" y="28"
        font-family="'Courier New', Courier, monospace"
        font-size="13" letter-spacing="3"
        fill="{label}">{label_text}</text>
  <line x1="20" y1="36" x2="780" y2="36" stroke="{rule}" stroke-width="1"/>
  <text x="20" y="46"
        font-family="'Courier New', Courier, monospace"
        font-size="9" letter-spacing="1"
        fill="{annot}">{annot_text}</text>
</svg>"""

import os, pathlib

for theme_name, c in [("dark", DARK), ("light", LIGHT)]:
    out_dir = pathlib.Path(__file__).parent / theme_name
    out_dir.mkdir(exist_ok=True)
    for num, label, annot in SECTIONS:
        slug = f"s{num}"
        svg = TEMPLATE.format(
            bg=c["bg"], rule=c["rule"],
            num=c["num"], label=c["label"], annot=c["annot"],
            num_text=num, label_text=label, annot_text=annot,
        )
        out_path = out_dir / f"{slug}.svg"
        out_path.write_text(svg, encoding="utf-8")
        print(f"  {out_path}")

print("Done.")
