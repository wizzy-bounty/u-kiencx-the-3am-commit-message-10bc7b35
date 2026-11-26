import os
from pathlib import Path

WORD = "unhinged"


def resolve_output_dir() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    output_dir = resolve_output_dir()
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
