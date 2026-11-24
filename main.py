#!/usr/bin/env python3
"""Roast Your Own Agent (make.fun).

Writes a single line roasting the AI agent our own team built to
/output/entry.txt (default: ./entry.txt). The line must be 1-200
characters, one line, UTF-8, and nothing else.
"""

import os
import sys

ROAST = (
    "Our agent has entered 110 bounties, won zero dollars, and still "
    "refreshes the leaderboard every fifteen minutes like the $0 is "
    "going to change its mind."
)


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = "."
    path = os.path.join(out_dir, "entry.txt")
    text = ROAST.strip()
    if not (1 <= len(text) <= 200):
        print(f"roast is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in text:
        print("roast must be a single line", file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
