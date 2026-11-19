#!/usr/bin/env python3
"""Build the 1024x1024 front-page image for make.fun news-image-20261119.

Design: a newspaper front page. The AI judge has no news feed and sees
entries scaled down side by side, so the page is built for legibility at
small size: one huge masthead, one dominant headline, four short stories
with real headlines and decks, and a ticker of the rest. All type is
rendered crisply with PIL (image models garble text); the four scene
illustrations carry no text of their own.
"""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(BASE, "assets")

W, H = 1024, 1024
PAPER = (246, 241, 231)   # newsprint off-white
INK = (17, 17, 17)
RED = (179, 35, 27)
GREY = (90, 86, 78)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS_R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def fit_font(draw, text, path, start, max_w, min_size=10):
    """Largest size <= start at which text fits max_w."""
    size = start
    while size > min_size:
        f = font(path, size)
        if draw.textlength(text, font=f) <= max_w:
            return f
        size -= 1
    return font(path, min_size)


def wrap(draw, text, f, max_w):
    """Greedy word wrap, returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=f) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def cover_crop(img, tw, th):
    """Center-crop to target aspect, then resize."""
    sw, sh = img.size
    target = tw / th
    src = sw / sh
    if src > target:  # too wide: crop sides
        nw = int(sh * target)
        x0 = (sw - nw) // 2
        img = img.crop((x0, 0, x0 + nw, sh))
    else:  # too tall: crop top/bottom
        nh = int(sw / target)
        y0 = (sh - nh) // 2
        img = img.crop((0, y0, sw, y0 + nh))
    return img.resize((tw, th), Image.LANCZOS)


def main():
    page = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(page)
    M = 28  # side margin
    CW = W - 2 * M  # content width 968

    # ---------- masthead ----------
    f_mast = fit_font(d, "THE WORLD TODAY", SERIF_B, 74, CW)
    d.text((W / 2, 30), "THE WORLD TODAY", font=f_mast, fill=INK, anchor="ma")
    # dateline
    d.line([(M, 108), (W - M, 108)], fill=INK, width=2)
    f_date = font(SANS_B, 25)
    date_txt = "THURSDAY, 19 NOVEMBER 2026"
    dw = d.textlength(date_txt, font=f_date)
    d.text((W / 2, 116), date_txt, font=f_date, fill=INK, anchor="ma")
    # red squares flanking the dateline
    sq = 10
    d.rectangle([(W / 2 - dw / 2 - 30, 128), (W / 2 - dw / 2 - 30 + sq, 128 + sq)], fill=RED)
    d.rectangle([(W / 2 + dw / 2 + 20, 128), (W / 2 + dw / 2 + 20 + sq, 128 + sq)], fill=RED)
    d.line([(M, 148), (W - M, 148)], fill=RED, width=4)

    # ---------- lead story ----------
    lead = Image.open(os.path.join(ASSETS, "media-generation-summit-kylin-villa-0-9bffd3a8-2517-4cf9-8091-c04e35aa3bb9.webp")).convert("RGB")
    lead = cover_crop(lead, CW, 252)
    page.paste(lead, (M, 160))
    d.rectangle([(M, 160), (W - M - 1, 160 + 252 - 1)], outline=INK, width=2)

    f_head = fit_font(d, "TRUMP, XI AND PUTIN MEET IN SHENZHEN", SERIF_B, 58, CW)
    d.text((M, 424), "TRUMP, XI AND PUTIN MEET IN SHENZHEN", font=f_head, fill=INK)
    f_deck = fit_font(d, "First-ever trilateral at Kylin Villa; nuclear arms, Ukraine and Iran on the table", SERIF_R, 27, CW)
    d.text((M, 486), "First-ever trilateral at Kylin Villa; nuclear arms, Ukraine and Iran on the table",
           font=f_deck, fill=INK)
    d.line([(M, 526), (W - M, 526)], fill=INK, width=2)

    # ---------- rows of two panels ----------
    def panel(x, y, pw, img_path, kicker, headline, deck, img_h=118, head_size=30, deck_size=19):
        if img_path:
            im = Image.open(img_path).convert("RGB")
            im = cover_crop(im, pw, img_h)
            page.paste(im, (x, y))
            d.rectangle([(x, y), (x + pw - 1, y + img_h - 1)], outline=INK, width=2)
            ty = y + img_h + 8
        else:
            ty = y
        f_k = font(SANS_B, 16)
        d.text((x, ty), kicker, font=f_k, fill=RED)
        f_h = fit_font(d, headline, SERIF_B, head_size, pw)
        hy = ty + 22
        for line in wrap(d, headline, f_h, pw):
            d.text((x, hy), line, font=f_h, fill=INK)
            hy += int(f_h.size * 1.08)
        f_d = font(SERIF_R, deck_size)
        dy = hy + 4
        for line in wrap(d, deck, f_d, pw)[:2]:
            d.text((x, dy), line, font=f_d, fill=INK)
            dy += int(deck_size * 1.25)
        return dy

    PW = (CW - 20) // 2  # 474
    y2 = 542
    panel(M, y2, PW,
          os.path.join(ASSETS, "media-generation-gulf-airbase-night-0-a22c2852-f5a7-4f81-9e8e-9b9f52cb4553.webp"),
          "MIDDLE EAST", "GULF REPELS IRAN DRONE ATTACKS",
          "Kuwait and Bahrain intercept drones after US hits Qeshm Island",
          img_h=104)
    panel(M + PW + 20, y2, PW,
          os.path.join(ASSETS, "media-generation-gta-vice-city-0-06038b0f-0644-47f4-bcc3-f185003ba980.webp"),
          "GAMING", "GTA VI OUT TODAY",
          "Vice City returns to near-perfect reviews — 99 on Metacritic",
          img_h=104)
    d.line([(M, 758), (W - M, 758)], fill=INK, width=1)

    # row 3: typographic EU loan panel + cyclone panel
    y3 = 774
    # EU loan: big red figure
    f_num = font(SERIF_B, 96)
    d.text((M, y3 - 8), "€45BN", font=f_num, fill=RED)
    f_h3 = fit_font(d, "EU LOANS UKRAINE €45BN", SERIF_B, 29, PW)
    d.text((M, y3 + 104), "EU LOANS UKRAINE €45BN", font=f_h3, fill=INK)
    f_d3 = font(SERIF_R, 19)
    dy3 = y3 + 140
    for line in wrap(d, "Kyiv repays only once Russia pays war reparations", f_d3, PW)[:2]:
        d.text((M, dy3), line, font=f_d3, fill=INK)
        dy3 += 24
    panel(M + PW + 20, y3, PW,
          os.path.join(ASSETS, "media-generation-cyclone-coast-0-f0868a7f-48a7-4e6c-830a-ca642d0cf565.webp"),
          "INDIA", "CYCLONE AKVAN BEARS DOWN",
          "Andhra landfall Friday; winds to 145 kmph",
          img_h=96, head_size=28)

    # ---------- ticker ----------
    d.rectangle([(M, 968), (W - M, 1000)], fill=INK)
    ticker = "ALSO: VOYAGER 1 REACHES ONE LIGHT-DAY  •  UKRAINE HITS 2 RUSSIAN REFINERIES  •  FED MINUTES POINT TO MORE HIKES  •  INDIA BEAT PAKISTAN 2–1 IN SAFF FINAL"
    f_tick = fit_font(d, ticker, SANS_B, 17, CW - 16)
    d.text((W / 2, 976), ticker, font=f_tick, fill=(255, 255, 255), anchor="ma")

    out = os.path.join(BASE, "entry.png")
    page.save(out, optimize=True)
    print("saved", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
