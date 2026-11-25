import os

ENTRY_TEXT = (
    "I sent my accountant 4,000 trades totaling -$18,412. "
    "He billed me $200 and wrote one word: condolences."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
