#!/usr/bin/env python3
"""Describe Your Ex in One Word: make.fun entry.

Writes one word to /output/entry.txt. Deterministic: the same word every
run, no input, no network, no environment secrets. The word is a
self-contained one-word verdict on an ex: the joke arrives with the word
itself.

The word: Freemium.
  The ex treated affection like a freemium service: the basics were free,
  but the good stuff -- attention, honesty, commitment -- sat behind a
  paywall. A precise absurdity (a SaaS pricing model applied to a person),
  instantly readable as a verdict, surprising, correctly spelled, and
  universally recognizable in the app era.
"""

import os
import sys

# The entry: exactly one word, 1-111 characters, nothing else attached.
WORD = "Freemium"

MAX_CHARS = 111


def validate_word(word: str) -> None:
    """Gate: the entry must be one non-blank word of 1-111 characters.

    Fails loudly (non-zero exit) so a bad word never ships silently.
    """
    if not word or not word.strip():
        print("ERROR: entry word is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if len(word) != len(word.strip()) or any(ch.isspace() for ch in word):
        print("ERROR: entry must be exactly one word (no spaces)", file=sys.stderr)
        sys.exit(1)
    if len(word) > MAX_CHARS:
        print(
            f"ERROR: entry is {len(word)} chars, over the {MAX_CHARS}-char limit",
            file=sys.stderr,
        )
        sys.exit(1)


def main() -> None:
    validate_word(WORD)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
