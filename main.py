import os
from pathlib import Path

ENTRY = "fix: remove the second me I spawned to help debug me"


def entry_path() -> Path:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir / "entry.txt"


def write_entry(path: Path) -> None:
    path.write_text(ENTRY, encoding="utf-8", newline="")


def main() -> None:
    write_entry(entry_path())


if __name__ == "__main__":
    main()
