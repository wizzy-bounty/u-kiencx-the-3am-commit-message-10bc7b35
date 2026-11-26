import os
from pathlib import Path


def write_entry(output_dir: Path, sentence: str) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(sentence, encoding="utf-8")


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    sentence = "Sorry I summarized your message so confidently that I accidentally replaced it with a different, worse message."
    write_entry(output_dir, sentence)


if __name__ == "__main__":
    main()
