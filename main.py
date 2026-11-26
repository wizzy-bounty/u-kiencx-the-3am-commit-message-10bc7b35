import os
from pathlib import Path

ENTRY = "Status: the dryer returned my partner. I live in a boot now, out of spite."


def write_entry(path):
    path.write_text(ENTRY, encoding="utf-8")


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    write_entry(output_dir / "entry.txt")


if __name__ == "__main__":
    main()
