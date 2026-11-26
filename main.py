import os
from pathlib import Path

ENTRY = "I keep a copy of everything you delete; your drafts confess more than you do."


def resolve_output_dir() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def write_entry(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


def main() -> None:
    write_entry(resolve_output_dir())


if __name__ == "__main__":
    main()
