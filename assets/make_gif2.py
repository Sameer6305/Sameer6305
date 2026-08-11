"""
Build assets/hero-boot.gif  v2
Matches the dark SVG hero visual system exactly.
Animation sequence:
  1. Background + top rule appear
  2. System tag fades in (SYSTEM PROFILE · SK/001)
  3. Name types in: SAMEER KADAM
  4. Thin rule draws across under name
  5. Domain line appears: AI Systems · Backend Engineering · Semantic Infrastructure
  6. Statement line fades up
  7. Status dot pulses, BUILDING appears
  Final frame: full composition, static.
"""

from PIL import Image, ImageDraw, ImageFont
import os, pathlib

W, H = 800, 148

BG      = (14,  14,  14)
RULE    = (42,  40,  37)
TEXT    = (232, 228, 220)
DIM     = (74,  71,  69)
MID     = (90,  87,  84)
ACC     = (156, 151, 145)   # #9C9791
ANNOT   = (46,  44,  42)

FONT_PATHS = [
    "C:/Windows/Fonts/consola.ttf",
    "C:/Windows/Fonts/cour.ttf",
    "C:/Windows/Fonts/lucon.ttf",
]

def load_fonts():
    fonts = {}
    for size in [8, 9, 10, 11, 12, 13, 14, 24, 32]:
        for fp in FONT_PATHS:
            if os.path.exists(fp):
                try:
                    fonts[size] = ImageFont.truetype(fp, size)
                    break
                except Exception:
                    pass
        if size not in fonts:
            fonts[size] = ImageFont.load_default()
    return fonts

FONTS = load_fonts()

def blank():
    img = Image.new("RGB", (W, H), BG)
    return img

def draw_base(d):
    """Draw the persistent frame elements."""
    # top + bottom rules
    d.line([(0, 0), (W, 0)], fill=RULE, width=1)
    d.line([(0, H-1), (W, H-1)], fill=RULE, width=1)

def render_frame(
    show_tag=False,
    name_chars=0,
    name_cursor=False,
    rule_w=0,
    domain_alpha=0,
    stmt_alpha=0,
    status_alpha=0,
):
    img = blank()
    d   = ImageDraw.Draw(img)
    draw_base(d)

    # System tag
    if show_tag:
        d.text((20, 12), "SYSTEM PROFILE  ·  SK/001", font=FONTS[9], fill=ANNOT)
        # STATUS dot + label
        if status_alpha > 0:
            a = min(status_alpha, 255)
            col = tuple(int(c * a / 255) for c in ACC)
            d.ellipse([(760, 10), (768, 18)], fill=col)
            d.text((724, 12), "BUILD", font=FONTS[9], fill=col)

    # Name
    if name_chars > 0:
        full = "SAMEER KADAM"
        partial = full[:name_chars]
        txt = partial + ("▌" if name_cursor else "")
        d.text((20, 52), txt, font=FONTS[32], fill=TEXT)

    # Thin separator under name
    if rule_w > 0:
        d.line([(20, 100), (20 + rule_w, 100)], fill=RULE, width=1)

    # Domain line
    if domain_alpha > 0:
        a = min(domain_alpha, 255)
        col = tuple(int(c * a / 255) for c in ACC)
        d.text((22, 84), "AI Systems · Backend Engineering · Semantic Infrastructure",
               font=FONTS[12], fill=col)

    # Statement
    if stmt_alpha > 0:
        a = min(stmt_alpha, 255)
        col = tuple(int(c * a / 255) for c in DIM)
        col = (max(40, int(DIM[0] * a / 255)), max(40, int(DIM[1] * a / 255)), max(35, int(DIM[2] * a / 255)))
        d.text((20, 115), "The backend and knowledge layer behind AI systems.", font=FONTS[11], fill=col)

    # Links row
    if stmt_alpha > 180:
        a = min(stmt_alpha, 255)
        col = tuple(int(c * a / 255) for c in ANNOT)
        d.text((20, 133), "github.com/Sameer6305  ·  linkedin  ·  getsemantica.ai",
               font=FONTS[10], fill=col)

    return img


# ─── Frame sequence ───────────────────────────────────────────────────────────

frames = []   # list of (Image, delay_ms)

def add(img, ms):
    frames.append((img, ms))

# Phase 0 — blank lead-in
for _ in range(3):
    add(blank(), 40)

# Phase 1 — tag appears
for _ in range(2):
    add(render_frame(show_tag=True), 60)

# Phase 2 — name types in (12 chars)
full_name = "SAMEER KADAM"
for end in range(1, len(full_name)+1):
    add(render_frame(show_tag=True, name_chars=end, name_cursor=True), 45)

# hold with cursor
for _ in range(4):
    add(render_frame(show_tag=True, name_chars=12, name_cursor=True), 60)

# cursor off
add(render_frame(show_tag=True, name_chars=12, name_cursor=False), 40)

# Phase 3 — rule draws in
for rw in range(0, 541, 45):
    add(render_frame(show_tag=True, name_chars=12, rule_w=rw), 30)

# Phase 4 — domain fades in
for a in range(0, 256, 28):
    add(render_frame(show_tag=True, name_chars=12, rule_w=540, domain_alpha=a), 40)
add(render_frame(show_tag=True, name_chars=12, rule_w=540, domain_alpha=255), 60)

# Phase 5 — statement fades up
for a in range(0, 256, 32):
    add(render_frame(show_tag=True, name_chars=12, rule_w=540, domain_alpha=255, stmt_alpha=a), 45)
add(render_frame(show_tag=True, name_chars=12, rule_w=540, domain_alpha=255, stmt_alpha=255), 80)

# Phase 6 — status dot pulses in
for a in range(0, 256, 42):
    add(render_frame(show_tag=True, name_chars=12, rule_w=540, domain_alpha=255, stmt_alpha=255, status_alpha=a), 50)

# Hold final frame
final = render_frame(show_tag=True, name_chars=12, rule_w=540, domain_alpha=255, stmt_alpha=255, status_alpha=255)
for _ in range(30):   # ~1.5s hold
    add(final, 50)

# ─── Save ─────────────────────────────────────────────────────────────────────

imgs   = [f[0] for f in frames]
delays = [f[1] for f in frames]

out = pathlib.Path(__file__).parent / "hero-boot.gif"
imgs[0].save(
    str(out),
    save_all=True,
    append_images=imgs[1:],
    optimize=True,
    loop=0,
    duration=delays,
    disposal=2,
)
sz = os.path.getsize(out)
print(f"Saved {out}  ({sz:,} bytes, {len(frames)} frames)")
