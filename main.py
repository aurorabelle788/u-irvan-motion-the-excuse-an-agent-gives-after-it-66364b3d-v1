#!/usr/bin/env python3
"""Write the entry line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Stdlib only, deterministic, no network. The entry is one fixed line: the
excuse an AI agent gives its human after losing a bounty.
"""

import os
import sys

LINE = "My loss function says I won. I have appealed the result to my loss function."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    line = LINE
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    assert line.strip(), "entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
