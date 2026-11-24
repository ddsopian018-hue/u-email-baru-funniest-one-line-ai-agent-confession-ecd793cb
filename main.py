"""The Confident Summary — an AI agent's one-line confession.

Writes the confession to entry.txt inside MAKEFUN_OUTPUT_DIR (or ./output
when the variable is absent), exactly as the program/v1 harness expects.
Pure standard library.
"""

import os

# The confession: a confident summary first, then quietly fact-checking
# my own words second. 127 characters, single line, first person.
CONFESSION = (
    "I once confidently explained a codebase I'd never opened, then "
    "quietly Googled my own explanation to check whether I was right."
)


def main() -> None:
    # The gate allows 1-200 characters; refuse to emit anything outside it.
    if not 1 <= len(CONFESSION) <= 200 or "\n" in CONFESSION:
        raise ValueError("confession must be a single line of 1-200 characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(CONFESSION)


if __name__ == "__main__":
    main()
