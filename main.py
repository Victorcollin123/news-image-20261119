#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261119.

Writes the front-page image for Thursday 19 November 2026 to
``/output/entry.png``.

The image is fixed: this program copies the ``entry.png`` stored in the
repository, byte for byte. It needs no network, uses no randomness and
does not depend on the time of day, so every run writes identical bytes.
"""
import shutil
from pathlib import Path

REPO_DIR = Path(__file__).resolve().parent
IMAGE_IN_REPO = REPO_DIR / "entry.png"
IMAGE_OUT = Path("/output/entry.png")


def write_entry_image() -> Path:
    """Copy the stored front page to the output path, making it first."""
    IMAGE_OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(IMAGE_IN_REPO, IMAGE_OUT)
    return IMAGE_OUT


if __name__ == "__main__":
    written = write_entry_image()
    print(f"wrote {written}")
