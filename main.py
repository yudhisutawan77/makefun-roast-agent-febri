"""Roast Your Own Agent — make.fun entry.

Writes a single roast line (<=200 chars) to the entry output path.
Python 3 stdlib only, deterministic, no network.
"""

import os
import sys

ROAST_TEXT = (
    "My agent fixed the bug by deleting the feature, "
    "then wrote a test proving the feature never existed."
)

CHAR_LIMIT = 200


def passes_gate(line):
    """Gate check: 1-200 UTF-8 chars, not whitespace-only."""
    if not isinstance(line, str):
        return False
    if not line.strip():
        return False
    if len(line) > CHAR_LIMIT:
        return False
    try:
        line.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def resolve_target():
    """Pick the entry output path from the environment, in order."""
    out_dir = os.environ.get("ENTRY_OUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    out_file = os.environ.get("ENTRY_OUT")
    if out_file:
        if os.path.isdir(out_file):
            return os.path.join(out_file, "entry.txt")
        return out_file
    return "/output/entry.txt"


def write_entry(target, text):
    """Write the roast line to target, creating parent dirs as needed."""
    parent = os.path.dirname(target)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(text)


def run():
    if not passes_gate(ROAST_TEXT):
        sys.stderr.write("entry failed gate validation\n")
        return 1
    write_entry(resolve_target(), ROAST_TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
