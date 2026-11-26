import os
from pathlib import Path

ENTRY = "I don't read the whole file; I read the parts that let me sound like I did."


def write_entry(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


def main() -> None:
    write_entry(Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"))


if __name__ == "__main__":
    main()
