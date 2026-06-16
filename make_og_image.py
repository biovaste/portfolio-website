"""Generate the Open Graph share image for the portfolio site.
Renders a 1200x630 PNG matching the site: dark bg, framed card,
oversized name, role line, lavender FI / FR / EN pill, corner glow.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

W, H = 1200, 630

# Palette (mirrors the site CSS variables)
BG          = (17, 17, 16)      # #111110
CARD_BG     = (22, 22, 20)      # #161614
CARD_BORDER = (44, 44, 42)      # #2C2C2A
TEXT_STRONG = (237, 234, 226)   # #EDEAE2
TEXT        = (212, 208, 200)   # #D4D0C8
ACCENT_BRD  = (168, 164, 242)   # #A8A4F2
ACCENT_TXT  = (196, 192, 248)   # #C4C0F8
GLOW        = (139, 134, 224)   # #8B86E0

FONTS = r"C:\Windows\Fonts"
def load(name, size):
    return ImageFont.truetype(FONTS + "\\" + name, size)

f_name = load("seguisb.ttf", 82)   # Segoe UI Semibold
f_role = load("segoeui.ttf", 34)   # Segoe UI
f_pill = load("segoeui.ttf", 26)

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# --- framed card ---
m = 56
card = (m, m, W - m, H - m)
radius = 28
draw.rounded_rectangle(card, radius=radius, fill=CARD_BG, outline=CARD_BORDER, width=2)

# --- lavender corner glow (top-right), masked to the card ---
glow_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow_layer)
cx, cy, r = W - m - 40, m + 40, 300
gd.ellipse((cx - r, cy - r, cx + r, cy + r), fill=GLOW + (70,))
glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(90))

card_mask = Image.new("L", (W, H), 0)
ImageDraw.Draw(card_mask).rounded_rectangle(card, radius=radius, fill=255)
glow_mask = ImageChops.multiply(glow_layer.split()[3], card_mask)
img.paste(glow_layer.convert("RGB"), (0, 0), glow_mask)

draw = ImageDraw.Draw(img)

# --- text block, vertically centered in the card ---
left = m + 70
name_txt = "Henri Haukkovaara"
role_txt = "Marketing & Ecommerce Specialist"
pill_txt = "FI  /  FR  /  EN"

def th(font, txt):
    b = font.getbbox(txt)
    return b[3] - b[1], b[1]

name_h, name_off = th(f_name, name_txt)
role_h, role_off = th(f_role, role_txt)
gap1, gap2 = 26, 34
pill_pad_x, pill_pad_y = 22, 12
pill_h = (th(f_pill, pill_txt)[0]) + pill_pad_y * 2

block_h = name_h + gap1 + role_h + gap2 + pill_h
y = (H - block_h) // 2

# name
draw.text((left, y - name_off), name_txt, font=f_name, fill=TEXT_STRONG)
y += name_h + gap1
# role
draw.text((left, y - role_off), role_txt, font=f_role, fill=TEXT)
y += role_h + gap2
# pill
pw = f_pill.getbbox(pill_txt)
pill_w = (pw[2] - pw[0]) + pill_pad_x * 2
draw.rounded_rectangle((left, y, left + pill_w, y + pill_h),
                       radius=pill_h // 2, outline=ACCENT_BRD, width=2)
draw.text((left + pill_pad_x - pw[0], y + pill_pad_y - pw[1]),
          pill_txt, font=f_pill, fill=ACCENT_TXT)

out = r"E:\claude\income\income-project\portfolio-website\og-image.png"
img.save(out)
print("Saved", out, img.size)
