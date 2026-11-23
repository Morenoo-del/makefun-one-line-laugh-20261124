"""One-Line Laugh entry: write a single funny line to /output/entry.txt."""

import os

LINE = (
    "I bought a planner to finally get my life together, and now the most "
    "organized thing in my life is the drawer where it sits, unopened."
)


def main() -> None:
    # Gate: one sentence, UTF-8, 1-200 chars, not only whitespace.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
