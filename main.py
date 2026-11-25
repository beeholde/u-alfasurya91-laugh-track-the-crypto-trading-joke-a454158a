"""Save the one-line contest entry for grading."""

import os
from pathlib import Path


OPENING = "I sent my accountant 4,000 trades totaling -$18,412."
CLOSING = "He billed me $200 and wrote one word: condolences."
ENTRY = f"{OPENING} {CLOSING}"


def save_entry() -> None:
    output_directory = Path(os.getenv("MAKEFUN_OUTPUT_DIR", "/output"))
    output_directory.mkdir(parents=True, exist_ok=True)
    (output_directory / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    save_entry()
