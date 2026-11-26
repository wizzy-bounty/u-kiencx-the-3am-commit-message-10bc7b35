import os
from pathlib import Path

TEXT_OPENING = "One star: your gravity makes my luggage kneel and your coins look like tiny edible discs, "
TEXT_CLOSING = "but the martabak manis made me leave my invasion map as a tip."
TEXT = TEXT_OPENING + TEXT_CLOSING


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
