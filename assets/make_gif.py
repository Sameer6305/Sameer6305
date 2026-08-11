"""
Build assets/hero-boot.gif
Concept: minimal engineering system initialization
- near-black background (#141414)
- warm off-white text (#E8E4DC)
- muted graphite accent (#9C9791)
- No neon, no glow, no cyberpunk
"""

from PIL import Image, ImageDraw, ImageFont
import os, math

W, H = 560, 120
BG      = (20, 20, 20)
WHITE   = (232, 228, 220)   # warm off-white
GRAY    = (156, 151, 145)   # #9C9791
DIM     = (80, 76, 72)      # dimmer graphite
DARK    = (40, 38, 36)      # slightly lifted bg for rule

def make_base():
    img = Image.new("RGB", (W, H), BG)
    return img

def draw_frame(text_rows, cursor_row=-1, rule_width=0, status_text="", status_visible=False):
    """
    text_rows: list of (text, color, x, y, font_size)
    cursor_row: which row gets a blinking cursor appended (-1 = none)
    rule_width: 0..W, draws a thin horizontal rule at y=74
    status_text/visible: bottom-right status pill
    """
    img = make_base()
    d = ImageDraw.Draw(img)

    # Try to load a monospace font; fall back to default
    font_paths = [
        "C:/Windows/Fonts/consola.ttf",   # Consolas
        "C:/Windows/Fonts/cour.ttf",       # Courier New
        "C:/Windows/Fonts/lucon.ttf",      # Lucida Console
    ]
    fonts = {}
    for size in [10, 12, 14, 16, 18]:
        for fp in font_paths:
            if os.path.exists(fp):
                try:
                    fonts[size] = ImageFont.truetype(fp, size)
                    break
                except Exception:
                    pass
        if size not in fonts:
            fonts[size] = ImageFont.load_default()

    for i, row in enumerate(text_rows):
        text, color, x, y, sz = row
        fnt = fonts.get(sz, fonts.get(12))
        display = text + ("▌" if i == cursor_row else "")
        d.text((x, y), display, fill=color, font=fnt)

    # thin rule
    if rule_width > 0:
        d.line([(16, 76), (16 + rule_width, 76)], fill=DIM, width=1)

    # status pill bottom-right
    if status_visible and status_text:
        fnt_s = fonts.get(10)
        bbox = d.textbbox((0, 0), status_text, font=fnt_s)
        tw = bbox[2] - bbox[0]
        sx = W - tw - 18
        sy = H - 18
        d.text((sx, sy), status_text, fill=GRAY, font=fnt_s)

    return img


# ── Define frame sequence ──────────────────────────────────────────────────

def build_frames():
    frames = []

    ROW_NAME   = ("SAMEER KADAM",                        WHITE, 16, 14, 16)
    ROW_DOMAIN = ("AI Systems · Backend Engineering · Semantic Infrastructure", GRAY, 16, 38, 12)
    ROW_TAG    = ("The backend and knowledge layer behind AI systems.", DIM,  16, 58, 10)
    ROW_RULE   = None  # handled via rule_width

    # ── Phase 0: blank hold (2 frames = ~100ms lead-in)
    for _ in range(2):
        frames.append((make_base(), 6))   # 6 = 60ms per frame

    # ── Phase 1: cursor pulse, name types in (simulated — show partial name)
    name_full = "SAMEER KADAM"
    for end in [3, 6, 9, 12]:
        partial = name_full[:end]
        row = (partial, WHITE, 16, 14, 16)
        frames.append((draw_frame([row], cursor_row=0), 5))

    # hold full name + cursor
    for _ in range(3):
        frames.append((draw_frame([ROW_NAME], cursor_row=0), 6))

    # ── Phase 2: domain appears, cursor moves down
    for _ in range(3):
        frames.append((draw_frame([ROW_NAME, ROW_DOMAIN], cursor_row=1), 6))

    # ── Phase 3: rule draws in
    for width in [60, 140, 220, 320, 420, 520, 540]:
        img = draw_frame([ROW_NAME, ROW_DOMAIN], cursor_row=-1, rule_width=width)
        frames.append((img, 4))

    # ── Phase 4: tagline fades in (simulate via color stepping)
    tag_steps = [
        (40, 38, 36), (58, 55, 52), (80, 76, 72), (108, 103, 98),
        (156, 151, 145), (180, 176, 170), (200, 196, 190)
    ]
    for col in tag_steps:
        row_tag = ("The backend and knowledge layer behind AI systems.", col, 16, 58, 10)
        img = draw_frame([ROW_NAME, ROW_DOMAIN, row_tag], rule_width=540)
        frames.append((img, 4))

    # ── Phase 5: status appears bottom-right
    for visible in [False, True, True, True]:
        img = draw_frame([ROW_NAME, ROW_DOMAIN, ROW_TAG], rule_width=540,
                         status_text="● BUILDING", status_visible=visible)
        frames.append((img, 6))

    # ── Hold final frame
    final = draw_frame([ROW_NAME, ROW_DOMAIN, ROW_TAG], rule_width=540,
                       status_text="● BUILDING", status_visible=True)
    for _ in range(24):   # ~1.4s hold at end before loop
        frames.append((final, 6))

    return frames


frames = build_frames()
imgs   = [f[0] for f in frames]
delays = [f[1] * 10 for f in frames]   # Pillow duration is in ms

out = os.path.join(os.path.dirname(__file__), "hero-boot.gif")
imgs[0].save(
    out,
    save_all=True,
    append_images=imgs[1:],
    optimize=True,
    loop=0,
    duration=delays,
    disposal=2,
)
print(f"Saved {out}  ({os.path.getsize(out):,} bytes)")
