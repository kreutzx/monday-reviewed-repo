#!/usr/bin/env python3
"""Monday, Reviewed in One Line — make.fun u-zeroxfive-monday-reviewed-in-one-line-e55de3c1.

Writes a single one-line review of the entrant's own Monday (114 characters,
no trailing newline) to /output/entry.txt, per the competition gate.
"""

import os

LINE = "One star for Monday: I arrived on time for my 9 a.m. meeting, and Dave from standup still asked if I was new here."


def main() -> None:
    # Self-check the gate before writing: 1-200 chars, single line, no
    # trailing newline. Fail loudly instead of ever emitting an invalid entry.
    if not (1 <= len(LINE) <= 200) or "\n" in LINE or not LINE.strip():
        raise SystemExit(f"entry violates gate: {len(LINE)} chars")
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
