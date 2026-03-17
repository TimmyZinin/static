#!/usr/bin/env python3
"""Generate a bold Telegram cover card for 'После 40 в IT не берут' post."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
img = Image.new("RGB", (W, H), "#1a1a2e")
draw = ImageDraw.Draw(img)

# Gradient-like effect with rectangles
for i in range(H):
    r = int(26 + (i / H) * 20)
    g = int(26 + (i / H) * 10)
    b = int(46 + (i / H) * 30)
    draw.line([(0, i), (W, i)], fill=(r, g, b))

# Accent bar on left
draw.rectangle([0, 0, 8, H], fill="#e94560")

# Top label
try:
    font_label = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 28)
    font_myth = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 32)
    font_main = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 72)
    font_sub = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36)
    font_bottom = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
except:
    font_label = ImageFont.load_default()
    font_myth = font_label
    font_main = font_label
    font_sub = font_label
    font_bottom = font_label

# "РАЗРУШАЕМ МИФЫ" label
draw.rounded_rectangle([40, 30, 340, 75], radius=8, fill="#e94560")
draw.text((55, 35), "РАЗРУШАЕМ МИФЫ", fill="white", font=font_label)

# Main title
draw.text((40, 120), "ПОСЛЕ 40", fill="white", font=font_main)
draw.text((40, 210), "В IT НЕ БЕРУТ", fill="white", font=font_main)

# Strikethrough on "НЕ БЕРУТ"
bbox = draw.textbbox((40, 210), "В IT НЕ БЕРУТ", font=font_main)
mid_y = (bbox[1] + bbox[3]) // 2
draw.rectangle([bbox[0], mid_y - 4, bbox[2], mid_y + 4], fill="#e94560")

# Reality line
draw.text((40, 330), "Реальность: после 40 — другой рынок.", fill="#0f3460", font=font_sub)
draw.text((40, 330), "Реальность: после 40 — другой рынок.", fill="#a8d8ea", font=font_sub)

# Stats boxes
box_y = 420
box_h = 90
boxes = [
    ("52 года", "средний возраст\nCTO в Fortune 500"),
    ("45 лет", "средний возраст\nуспешного фаундера"),
    ("80%", "senior-позиций\nчерез нетворк"),
]

box_w = 340
gap = 30
start_x = 40

for i, (num, desc) in enumerate(boxes):
    x = start_x + i * (box_w + gap)
    draw.rounded_rectangle([x, box_y, x + box_w, box_y + box_h], radius=12, fill=(255, 255, 255, 30), outline="#e94560", width=2)
    # Semi-transparent box
    overlay = Image.new("RGBA", (box_w, box_h), (255, 255, 255, 15))
    img.paste(Image.alpha_composite(Image.new("RGBA", (box_w, box_h), (0, 0, 0, 0)), overlay), (x, box_y))

    draw.text((x + 15, box_y + 10), num, fill="#e94560", font=font_myth)

    try:
        font_desc = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 18)
    except:
        font_desc = font_bottom

    for j, line in enumerate(desc.split("\n")):
        draw.text((x + 15, box_y + 48 + j * 20), line, fill="#a8d8ea", font=font_desc)

# Bottom branding
draw.text((40, H - 45), "Tim Zinin | AI-агенты & Карьера", fill="#666688", font=font_bottom)
draw.text((W - 200, H - 45), "timzinin.com", fill="#e94560", font=font_bottom)

out = "/Users/timofeyzinin/static/telegram-career-40-card.png"
img.save(out, "PNG", quality=95)
print(f"Saved: {out} ({os.path.getsize(out)} bytes)")
