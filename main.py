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


def validate(text: str) -> str | None:
    """Return an error message if *text* breaks the brief, else None.

    Brief constraints: 1-200 characters, exactly one line, no leading
    or trailing whitespace, and encodable as UTF-8.
    """
    if text != text.strip():
        return "roast must not have leading/trailing whitespace"
    if not (1 <= len(text) <= 200):
        return f"roast is {len(text)} chars, must be 1-200"
    if "\n" in text or "\r" in text:
        return "roast must be a single line"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        return f"roast must be UTF-8 encodable: {exc}"
    return None


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = "."
    path = os.path.join(out_dir, "entry.txt")
    text = ROAST.strip()
    error = validate(text)
    if error is not None:
        print(error, file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
