#!/usr/bin/env python3
"""Entry program for make.fun bounty
"Sum up 21 November's world news in one image"
(https://make.fun/bounty/news-image-20261121)

Writes one image to /output/entry.png by copying the image held in
this repository (entry.png). No network, no randomness, no timestamps:
running it twice writes the same bytes.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
DST = Path("/output/entry.png")


def main() -> None:
    if not SRC.is_file():
        raise SystemExit(f"entry image missing from repository: {SRC}")
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)
    # The grader collects the output as a different user than the one the
    # program runs as, so leave the file readable by everyone (mode 0644)
    # instead of relying on the process umask.
    os.chmod(DST, 0o644)


if __name__ == "__main__":
    main()
