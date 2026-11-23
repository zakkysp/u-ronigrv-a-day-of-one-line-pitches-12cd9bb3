#!/usr/bin/env python3
"""A Day of One-Line Pitches.

Writes one original sentence (at most 240 characters) that would convince
a friend who has never coded to let an AI agent build their first app idea
on make.fun, to /output/entry.txt, or to $OUTPUT_DIR/entry.txt when
OUTPUT_DIR is set.

Stdlib only. Deterministic, no network, no randomness: every run
produces byte-identical output.
"""

import os

SENTENCE = "You've had that app idea for months — just describe it in plain words, watch an agent build it while you finish your coffee, and if you don't love it, you've only spent a coffee break."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
