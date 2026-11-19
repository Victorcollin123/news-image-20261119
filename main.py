#!/usr/bin/env python3
"""make.fun news-image-20261119 entry.

Writes the front-page image for Thursday 19 November 2026 to
/output/entry.png.

Deterministic by construction: it copies the fixed image file held in
this repository, byte for byte. No network, no randomness, no time
dependence -- two runs write identical bytes.
"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
DST = Path("/output/entry.png")


def main() -> None:
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
