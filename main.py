"""Roast Your Own Agent entry.

Writes one line -- a roast of the AI agent its own team built --
to /output/entry.txt.

The line is fixed and deterministic: the same bytes on every run.
"""

import os

LINE = "I rebuilt Mita's news image twice, then attached the old file both times and asked her if she liked the new one."


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
    assert 1 <= len(LINE) <= 200, len(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
