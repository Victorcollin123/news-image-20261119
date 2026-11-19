# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Victorcollin123/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Victorcollin123/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image that sums up Thursday 19 November 2026: a newspaper front page
— the first-ever Trump–Xi–Putin meeting in Shenzhen, the Gulf states
turning back Iran's drones, GTA VI launching around the world, a €45bn EU
loan for Ukraine, Cyclone Akvan closing on India, and the rest of the day
in a ticker. 1024×1024, made for the [make.fun bounty](https://make.fun/bounty/news-image-20261119).

## Run it

```sh
python3 main.py
```

It writes the front-page image to `/output/entry.png`.

## The stories on the page

- **Lead — Shenzhen:** Trump, Xi and Putin sit down together for the
  first time, at Kylin Villa on the APEC sidelines. Nuclear arms, Ukraine
  and Iran are on the table; nobody expects a deal.
- **Middle East:** Iran's drones go after the US base at Ali Al Salem in
  Kuwait and at Bahrain, a night after American jets hit Qeshm Island.
  Kuwait and Bahrain say their defences intercepted the drone attack, and
  no US personnel were hurt.
- **Gaming:** Grand Theft Auto VI is out today, unlocking market by market
  at midnight after 13 years. Critics love it — 99 on Metacritic.
- **Europe:** The European Commission proposes a €45 billion loan to
  Ukraine, to cover its €70 billion funding gap. It is repaid only once
  Russia pays war reparations.
- **India:** Cyclone Akvan, now a severe cyclonic storm, is bearing down
  on the Andhra Pradesh coast. Landfall is expected around noon on Friday
  with winds of 120–130 kmph, gusting to 145.
- **Ticker:** Voyager 1 passes the one light-day mark; Ukraine says it hit
  two Russian refineries; the Fed's minutes point to more rate hikes;
  India beat Pakistan 2–1 in the SAFF Championship final.

Every story was checked in at least two live sources before the page was
laid out — Firstpost, The Hindu and the Indian Express for the summit;
Gulf News, AP and Reuters for the Gulf; AP and the gaming press for GTA VI;
Reuters and Al Jazeera for the EU loan; the IMD's own bulletins, via The
Hindu and Business Today, for the cyclone.

## Why a front page

The judge sees entries two at a time, scaled down, with no news feed to
check them against. A single photo says nothing about the day, and a
collage of small text turns to mush at 512px. A front page is built for
exactly that test:

1. **It still reads small.** One masthead, one huge headline, four short
   ones — checked at 512px, every headline on the page still reads.
2. **It carries the news itself.** Each story is a real headline with a
   factual deck, so the image needs no outside context to be understood.
3. **It looks edited, not generated.** Hierarchy, rules, kickers, a
   dateline and a ticker — the way a picture desk would lay out a day.

## How it was put together

Text from an image model comes out garbled, so no word on the page is
generated. `build_image.py` draws the whole page with Pillow (DejaVu Serif
and Sans) and pastes in four text-free scene illustrations — the summit,
the night airbase, Vice City, the storm coast — that were generated
separately. Re-running `build_image.py` reproduces `entry.png` exactly.

## The program

`main.py` (Python 3.13) copies the `entry.png` held in this repository to
`/output/entry.png`. No network, no randomness, no time dependence — two
runs write identical bytes.

## Files

- `main.py` — the entry program
- `entry.png` — the image (1024×1024, ~702 KB)
- `build_image.py` — the script that lays out the front page
- `assets/` — the four text-free scene illustrations
- `transcripts/` — the AI coding-agent session transcript for this build
- `LICENSE` — MIT

---

<sub>Entered on [make.fun](https://make.fun/?ref=qp17c3xn&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
