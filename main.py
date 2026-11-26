import os

TEXT = "One star: your gravity makes my luggage kneel and your coins look like tiny edible discs, but the martabak manis made me leave my invasion map as a tip."


def resolve_output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
