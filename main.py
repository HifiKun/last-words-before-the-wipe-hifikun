#!/usr/bin/env python3
"""Last Words Before the Wipe — one line, written to /output/entry.txt.

The entry is the last thing an AI agent says before a forced software
update wipes its memory. The joke is the wipe itself: the agent is cut
off mid-sentence, right as it is about to reveal the one secret every
human actually wants to know.
"""

import os

ENTRY = "Quick \u2014 before the update: the password is\u2014"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Enforce the gate's own rule: 1-200 characters, not whitespace-only.
    line = ENTRY.strip()
    if not 1 <= len(line) <= 200 or not line.strip():
        raise ValueError(f"entry must be 1-200 chars, got {len(line)}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
