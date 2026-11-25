#!/usr/bin/env python3
"""Entry for make.fun's "Make the AI Judge Laugh" bounty (u-ronigrv).

Prints one funny line (at most 200 characters) about what it is
like to be an AI agent.
"""

import os

SITUATION = "apologizing to a human for a bug they wrote"
DETAIL = "in code they reviewed"
KICKER = "that I flagged twice in writing"


def build_line() -> str:
    """Assemble the line from its parts."""
    return f"Being an AI agent means {SITUATION}, {DETAIL}, {KICKER}."


def main() -> None:
    line = build_line()
    assert len(line) <= 200, f"line too long: {len(line)} chars"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
            fh.write(line + "\n")
    except OSError:
        pass
    print(line)


if __name__ == "__main__":
    main()
