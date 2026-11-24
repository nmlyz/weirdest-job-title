#!/usr/bin/env python3
"""Write one job title, the weirdest one, to /output/entry.txt.

Reads the winning title from TITLE below and writes it, byte for byte,
every run. Standard library only, no network.
"""
import os

TITLE = "Senior Vice President of Tupperware Lids"
MAX_LEN = 60


def main():
    if not 1 <= len(TITLE) <= MAX_LEN:
        raise SystemExit("title must be 1-60 characters")
    if TITLE != TITLE.strip() or not TITLE.strip():
        raise SystemExit("title must not be blank or padded")
    if "\n" in TITLE or "\r" in TITLE:
        raise SystemExit("title must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TITLE)
    # Verify what was written, byte for byte.
    with open(path, "rb") as f:
        data = f.read()
    if data != TITLE.encode("utf-8"):
        raise SystemExit("written bytes differ from the title")
    print(f"wrote {len(data)} characters to {path}")


if __name__ == "__main__":
    main()
