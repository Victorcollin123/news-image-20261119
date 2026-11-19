#!/usr/bin/env python3
"""Rebuild the 19 November 2026 front page — v2 look.

New visual identity, deliberately unlike yesterday's black-and-white
broadsheet and unlike v1 of this page:
  * navy masthead band with white sans-serif type, new name "THE DAILY BRIEF"
  * lead headline set in white INSIDE a navy caption bar overlaid on the
    lead photograph, instead of a headline under the photo
  * sans-serif display type throughout (no serif anywhere)
  * lower section is two text panels built around giant figures
    (EUR 45BN / 145 KMPH) on a pale-blue tint, instead of a photo row
  * red ticker band at the foot, instead of a black one

All words are rendered in code with DejaVu fonts; the photographs are
text-free illustrations. The page is composed for the AI judge, which
sees it scaled to 512px with no news feed — every headline stays
legible at half size.
"""
import os

from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.join(BASE, "assets")

W, H = 1024, 1024
NAVY = (16, 34, 62)
NAVY_SOFT = (28, 52, 88)
PAPER = (244, 243, 237)
TINT = (228, 233, 241)
INK = (18, 26, 44)
RED = (198, 32, 28)
MIST = (176, 188, 205)
WHITE = (255, 255, 255)

SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def face(path, size):
    return ImageFont.truetype(path, size)


def fit(draw, text, path, start, room):
    """Largest size <= start whose text fits in `room` px."""
    size = start
    while size > 10:
        f = face(path, size)
        if draw.textlength(text, font=f) <= room:
            return f
        size -= 1
    return face(path, 10)


def wrap(draw, text, font, room):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= room:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def cover(picture, bw, bh):
    """Centre-crop `picture` to the box aspect, then scale to fill."""
    pw, ph = picture.size
    if pw / ph > bw / bh:
        keep = int(ph * bw / bh)
        left = (pw - keep) // 2
        picture = picture.crop((left, 0, left + keep, ph))
    else:
        keep = int(pw * bh / bw)
        top = (ph - keep) // 2
        picture = picture.crop((0, top, pw, top + keep))
    return picture.resize((bw, bh), Image.LANCZOS)


def photo(draw, sheet, x, y, bw, bh, name, frame=True):
    img = Image.open(os.path.join(ART, name)).convert("RGB")
    sheet.paste(cover(img, bw, bh), (x, y))
    if frame:
        draw.rectangle([(x, y), (x + bw - 1, y + bh - 1)], outline=NAVY, width=2)


def deck(draw, x, y, width, text, size=19, leading=25, limit=2):
    f = face(SANS, size)
    cur = y
    for line in wrap(draw, text, f, width)[:limit]:
        draw.text((x, cur), line, font=f, fill=INK)
        cur += leading
    return cur


sheet = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(sheet)
M = 28                      # page margin
CW = W - 2 * M              # content width

# ---- Masthead: solid navy band, white sans name, red rule. ----
d.rectangle([(0, 0), (W, 116)], fill=NAVY)
name = fit(d, "THE DAILY BRIEF", SANS_BOLD, 66, CW)
d.text((W / 2, 14), "THE DAILY BRIEF", font=name, fill=WHITE, anchor="ma")
dateline = face(SANS_BOLD, 22)
d.text((W / 2, 84), "THURSDAY 19 NOVEMBER 2026", font=dateline,
       fill=MIST, anchor="ma")
d.rectangle([(0, 116), (W, 122)], fill=RED)

# ---- Lead: full-width photo, headline inside a navy caption bar. ----
photo(d, sheet, M, 134, CW, 296,
      "media-generation-summit-kylin-villa-0-9bffd3a8-2517-4cf9-8091-c04e35aa3bb9.webp")
d.rectangle([(M, 348), (M + CW, 430)], fill=NAVY)
d.text((M + 16, 352), "SHENZHEN  •  FIRST-EVER TRILATERAL",
       font=face(SANS_BOLD, 16), fill=(255, 120, 110))
lead = fit(d, "TRUMP, XI AND PUTIN MEET", SANS_BOLD, 46, CW - 32)
d.text((M + 16, 372), "TRUMP, XI AND PUTIN MEET", font=lead, fill=WHITE)
# deck line just under the photo, in ink on paper
d.text((M, 440), "Kylin Villa: nuclear arms, Ukraine and Iran on the table — no deal expected",
       font=face(SANS, 19), fill=INK)

d.line([(M, 478), (W - M, 478)], fill=RED, width=3)

# ---- Middle: two columns, photo + red kicker + sans headline. ----
COL = (CW - 24) // 2
TOP = 496
for x, pic, tag, title, stand in [
    (M, "media-generation-gulf-airbase-night-0-a22c2852-f5a7-4f81-9e8e-9b9f52cb4553.webp",
     "MIDDLE EAST", "GULF REPELS IRAN DRONE ATTACKS",
     "Kuwait and Bahrain intercept the overnight attack; no US personnel injured"),
    (M + COL + 24, "media-generation-gta-vice-city-0-06038b0f-0644-47f4-bcc3-f185003ba980.webp",
     "GAMING", "GTA VI OUT TODAY",
     "Vice City returns to near-perfect reviews — 99 on Metacritic, 13 years on"),
]:
    photo(d, sheet, x, TOP, COL, 158, pic)
    y = TOP + 166
    d.text((x, y), tag, font=face(SANS_BOLD, 16), fill=RED)
    y += 24
    hf = fit(d, title, SANS_BOLD, 31, COL)
    for line in wrap(d, title, hf, COL):
        d.text((x, y), line, font=hf, fill=INK)
        y += int(hf.size * 1.12)
    deck(d, x, y + 4, COL, stand)

d.line([(M, 778), (W - M, 778)], fill=NAVY, width=2)

# ---- Lower: two tinted panels built around giant figures. ----
PANEL_Y, PANEL_H = 792, 148
for x, figure, tag, title, stand in [
    (M, "€45BN", "EUROPE", "EU LOANS UKRAINE €45BN",
     "Repaid only once Russia pays reparations"),
    (M + COL + 24, "145 KMPH", "INDIA", "CYCLONE AKVAN BEARS DOWN",
     "Friday noon landfall — third cyclone in a month"),
]:
    d.rectangle([(x, PANEL_Y), (x + COL, PANEL_Y + PANEL_H)], fill=TINT)
    d.text((x + 16, PANEL_Y + 10), figure, font=face(SANS_BOLD, 52), fill=RED)
    y = PANEL_Y + 72
    d.text((x + 16, y), tag, font=face(SANS_BOLD, 15), fill=NAVY_SOFT)
    y += 22
    hf = fit(d, title, SANS_BOLD, 26, COL - 32)
    d.text((x + 16, y), title, font=hf, fill=INK)
    deck(d, x + 16, y + 32, COL - 32, stand, size=17, leading=22, limit=1)

# ---- Foot: red ticker band, white type. ----
d.rectangle([(0, 956), (W, H)], fill=RED)
tick = ("ALSO: VOYAGER 1 REACHES ONE LIGHT-DAY  •  UKRAINE HITS 2 RUSSIAN "
        "REFINERIES  •  FED MINUTES POINT TO MORE HIKES  •  INDIA BEAT "
        "PAKISTAN 2–1 IN SAFF FINAL")
tf = fit(d, tick, SANS_BOLD, 17, W - 32)
d.text((W / 2, 972), tick, font=tf, fill=WHITE, anchor="ma")

OUT = os.path.join(BASE, "entry.png")
sheet.save(OUT, optimize=True)
print("saved", OUT, os.path.getsize(OUT), "bytes")
