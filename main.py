#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes.

Writes one one-line joke about office life to entry.txt in the
output directory given by MAKEFUN_OUTPUT_DIR (default /output).
"""
import os

JOKE = (
    "The office birthday card has been circulating for signatures "
    "so long that the birthday person has had another birthday."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    # The file itself (not the /output dir, which the harness owns)
    # must be readable by every user: see makefun-submit E3.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
