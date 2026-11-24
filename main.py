"""The One-Line Exit — a one-line resignation letter writer.

Writes exactly one funny one-line resignation letter to /output/entry.txt.

The letter is fixed text: the same line on every run, so the program is
fully deterministic (no randomness, no network, no clock, no input).
"""

import os
import sys

# The resignation letter: one line, one joke, one very tired IT guy.
# The twist reuses the oldest IT support line in the book — "have you
# tried turning it off and on again?" — and turns it on the writer
# himself: this time the thing being switched off for good is him.
LETTER = (
    "I hereby resign as the office's only IT guy, effective Friday, "
    "because I have tried turning it off and on again, and this time it is me."
)

MAX_CHARS = 140


def build_letter() -> str:
    """Return the resignation letter, enforcing the competition's gate."""
    line = LETTER.strip()
    if not line:
        raise ValueError("letter must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("letter must be exactly one line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"letter is {len(line)} chars, over the {MAX_CHARS} limit")
    return line


def main(argv: list[str]) -> int:
    out_path = argv[1] if len(argv) > 1 else os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    letter = build_letter()
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    # newline="" keeps the bytes identical on every platform: no trailing
    # newline is added and no line ending is translated.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(letter)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
