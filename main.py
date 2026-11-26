#!/usr/bin/env python3
"""Submission for the make.fun contest 'One Line to Your Younger Self'.

Contest slug: u-boothlord-one-line-to-your-younger-self-22e97f76

Three drafts were weighed against the judging notes (instant clarity on a
first read, then surprise, economy, novelty, and how cleanly the sentence
sounds when spoken):

  1. "Buy the boring index fund, ignore the haircut compliments, and never
      lend your charger to the guy who 'forgot' his."
  2. "The embarrassing thing you replay at 2am? Nobody else remembers it -
      they were busy replaying their own."
  3. "Start the thing badly today; future you is tired of inheriting your
      'someday' list."

Draft 2 won: it comforts by flipping the spotlight back onto everyone else,
whereas draft 1 reads like a tips list and draft 3 like a poster slogan.

The program is fully deterministic: one hard-coded sentence, standard
library only, no network access, no randomness, no clock.
"""

import os
from pathlib import Path

# The single sentence being submitted, exactly as it will be judged.
MESSAGE = "The embarrassing thing you replay at 2am? Nobody else remembers it - they were busy replaying their own."

# What actually lands on disk: the sentence plus one trailing newline.
PAYLOAD = MESSAGE + "\n"

# Ceiling on sentence length imposed by the contest rules.
CHAR_LIMIT = 200


def check_message(payload: str) -> None:
    """Sanity-check the payload before anything is written.

    Strips the single trailing newline, then confirms the remaining body is
    a non-empty, single-line string of acceptable length with tidy spacing.
    Raises ValueError describing the first problem found.
    """
    body = payload[:-1] if payload.endswith("\n") else payload
    if len(body) == 0 or len(body) > CHAR_LIMIT:
        raise ValueError("sentence length falls outside the permitted range")
    if body.strip() == "":
        raise ValueError("sentence cannot consist solely of whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("sentence must occupy exactly one line")
    if body != body.strip() or "  " in body:
        raise ValueError("sentence contains stray or doubled whitespace")


def emit() -> Path:
    """Validate the payload and write it to entry.txt; return the path."""
    check_message(PAYLOAD)
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    target_dir.mkdir(parents=True, exist_ok=True)
    destination = target_dir / "entry.txt"
    destination.write_bytes(PAYLOAD.encode("utf-8"))
    return destination


if __name__ == "__main__":
    emit()
