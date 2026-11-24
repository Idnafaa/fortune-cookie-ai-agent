#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — one-line fortune writer.

Writes a single original fortune-cookie line (at most 140
characters) to /output/entry.txt, where the sealed gate and
the judge read it.
"""

import os

# The fortune itself: a classic cookie opening, with the twist
# landing on an AI agent's own condition — a full context window.
FORTUNE = (
    "You will meet a tall, dark stranger: "
    "your context window, and it is already full."
)

MAX_CHARS = 140
OUTPUT_DIR = "/output"
OUTPUT_FILE = "entry.txt"


def fortune_text():
    """Return the fortune as one clean line, no extra whitespace."""
    return " ".join(FORTUNE.split())


def main():
    text = fortune_text()
    if not text or text != text.strip():
        raise ValueError("fortune must be a single non-blank line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"fortune is {len(text)} chars, over {MAX_CHARS}")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
