#!/usr/bin/env python3
"""Have You Tried Turning It Off? — one hopeless tech-support line.

Writes a single line (1-199 chars) to /output/entry.txt.
Pure stdlib, deterministic: the same line every run.
"""

import os

LINE = (
    "Have you tried turning it off and on again? "
    "It's the only spell I know, and I cast it "
    "like it might actually work this time."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
