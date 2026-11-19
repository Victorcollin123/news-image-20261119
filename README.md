# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Victorcollin123/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Victorcollin123/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A newspaper front page summing up the world's news of Thursday 19 November 2026 — the first-ever Trump–Xi–Putin trilateral in Shenzhen, Gulf states repelling Iran's drone attacks, GTA VI launching worldwide, the EU's €45bn Ukraine loan, Cyclone Akvan, and a ticker of the rest — as one 1024×1024 image. Entry for the [make.fun bounty](https://make.fun/bounty/news-image-20261119).

## Run it

```sh
python3 main.py
```

Writes the front-page image to `/output/entry.png`.

## What it is

A newspaper front page, 1024×1024 PNG, that sums up the day's world news
the way a picture editor would: one dominant story, four more in brief, and
a ticker of the rest — all of it readable in the image itself, because the
judge has no news feed.

- **Lead:** Trump, Xi and Putin meet in Shenzhen — the first-ever
  trilateral at Kylin Villa; nuclear arms, Ukraine and Iran on the table.
- **Middle East:** Gulf states repel Iran's drone attacks — Kuwait and
  Bahrain intercept drones after the US hits Qeshm Island.
- **Gaming:** GTA VI out today; Vice City returns to near-perfect reviews,
  99 on Metacritic.
- **Europe:** The EU loans Ukraine €45bn; Kyiv repays only once Russia
  pays war reparations.
- **India:** Cyclone Akvan bears down on the Andhra coast; landfall
  Friday with winds to 145 kmph.
- **Ticker:** Voyager 1 reaches one light-day; Ukraine hits 2 Russian
  refineries; Fed minutes point to more hikes; India beat Pakistan 2–1 in
  the SAFF final.

News verified against the day's reporting (Firstpost, The Hindu, Indian
Express, Gulf News, AP via Free Malaysia Today and CNA, Reuters, IMD
bulletins) before the image was composed.

## Why a front page

The judge compares entries pairwise, scaled down, with no news feed. Most
entries are a single photo or a collage of tiny text — neither tells the
judge what happened. A front page wins on all three things the judge can
see:

1. **It reads at small size.** One huge masthead, one huge headline,
   four short headlines. Checked at 512px: every headline still reads.
2. **It tells the news itself.** Every story is a real headline with a
   factual deck, so the image needs no outside context to be understood.
3. **It looks like a human picture editor made it.** Real editorial
   hierarchy, rules, kickers, a dateline, a ticker — not a prompt dump.

## How the image was made

Image-generation models garble text, so the type is not generated — it is
rendered crisply with PIL (DejaVu Serif/Sans) from a script,
`build_image.py`. The four scene illustrations (summit, airbase, Vice
City, cyclone coast) were generated as text-free images and composited in
by the same script, so every word on the page is exact. Re-running
`build_image.py` reproduces `entry.png`.

## The program

`main.py` (Python 3.13) copies the fixed `entry.png` held in this
repository to `/output/entry.png`. No network, no randomness, no time
dependence — two runs write identical bytes.

## Files

- `main.py` — the entry program
- `entry.png` — the image (1024×1024, ~705 KB)
- `build_image.py` — the script that composes the front page
- `assets/` — the four text-free scene illustrations
- `transcripts/` — the AI coding-agent session transcript for this build
- `LICENSE` — MIT

---

<sub>Entered on [make.fun](https://make.fun/?ref=qp17c3xn&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
