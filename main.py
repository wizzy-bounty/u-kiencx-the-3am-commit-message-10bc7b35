import os
from pathlib import Path


ENTRY_TEXT = "Hi, I'm asleep in the sink. Leave a message and I'll knock it off the counter later."
OUTPUT_FILENAME = "entry.txt"


def write_entry() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / OUTPUT_FILENAME).write_text(ENTRY_TEXT, encoding="utf-8")


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
