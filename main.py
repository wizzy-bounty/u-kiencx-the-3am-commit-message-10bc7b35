import os
from pathlib import Path

ENTRY = "One star: your inn has too many mirrors and the garlic bread is a war crime, but the blood-orange sorbet was to die for."


def write_entry(output_dir: Path) -> None:
    target = output_dir / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(ENTRY, encoding="utf-8")


def main() -> None:
    write_entry(Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")))


if __name__ == "__main__":
    main()
