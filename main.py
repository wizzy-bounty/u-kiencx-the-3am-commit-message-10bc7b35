import os
from pathlib import Path

ENTRY = "One star: your oceans are undrinkable and your locals queue for bottled water, but the soup made my crew cancel the abduction."


def write_entry(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


def main() -> None:
    write_entry(Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")))


if __name__ == "__main__":
    main()
