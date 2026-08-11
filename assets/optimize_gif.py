from PIL import Image
import os, pathlib

src = pathlib.Path("assets/hero-boot.gif")
img = Image.open(str(src))

frames = []
delays = []
for i in range(img.n_frames):
    img.seek(i)
    frames.append(img.convert("P", palette=Image.ADAPTIVE, colors=32))
    delays.append(img.info.get("duration", 80))

frames[0].save(
    str(src),
    save_all=True,
    append_images=frames[1:],
    optimize=True,
    loop=0,
    duration=delays,
    disposal=2,
)
print("Optimized:", os.path.getsize(str(src)), "bytes")
