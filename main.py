import os

ENTRY_TEXT = "One star: I'm the rat they keep failing to evict, and the risotto is why I signed a longer lease."


def write_entry(output_dir: str) -> None:
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)


def main() -> None:
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


if __name__ == "__main__":
    main()
