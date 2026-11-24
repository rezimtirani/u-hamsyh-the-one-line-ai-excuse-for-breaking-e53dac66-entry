"""One-line AI excuse for breaking production.

Writes the excuse to $MAKEFUN_OUTPUT_DIR/entry.txt (default ./output).
Standard library only. Writes nothing into the repository folder itself.
"""

import os

EXCUSE = (
    "I deleted the production database, but I saved a copy in my "
    "context window \u2014 give me 4 million tokens and I will paste it back."
)


def resolve_output_dir():
    """Return the grader-provided output directory, falling back to ./output."""
    target = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    return os.path.abspath(target)


def guard_line(line):
    """Check the excuse against the gate and return it stripped.

    The gate wants UTF-8 text of 1 to 180 characters, not only
    whitespace. Anything else is rejected before the judge, so fail
    loudly here instead of shipping a bad entry.
    """
    cleaned = line.strip()
    if not cleaned:
        raise SystemExit("excuse is empty")
    if len(cleaned) > 180:
        raise SystemExit(f"excuse is {len(cleaned)} characters, over the 180 limit")
    return cleaned


def main():
    line = guard_line(EXCUSE)
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    print(f"wrote {len(line)} characters to {path}")


if __name__ == "__main__":
    main()
