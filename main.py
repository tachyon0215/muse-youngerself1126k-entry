#!/usr/bin/env python3
"""Entry for 'One Line to Your Younger Self' (u-boothlord-one-line-to-your-younger-self-22e97f76).

Candidates:
  A) "Buy the boring index fund, ignore the haircut compliments, and never lend your charger to the guy who 'forgot' his."
  B) "The embarrassing thing you replay at 2am? Nobody else remembers it - they were busy replaying their own."
  C) "Start the thing badly today; future you is tired of inheriting your 'someday' list."
Selected: "The embarrassing thing you replay at 2am? Nobody else remembers it - they were busy replaying their own."
Reason: Comforting twist that turns back on the reader; A is advice-list, C is motivational-poster phrasing.
Deterministic: fixed text, no network, no randomness.
"""
import os
from pathlib import Path
LINE = "The embarrassing thing you replay at 2am? Nobody else remembers it - they were busy replaying their own."
TEXT = LINE + "\n"
MAX_CHARS = 200
def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be one line")
    if body != body.strip() or "  " in body:
        raise ValueError("no stray whitespace")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
if __name__ == "__main__":
    main()
