"""Summarize a UTF-8 text file using the course note's file and function topics."""

import sys


def summarize(text: str) -> tuple[int, int, int]:
    """Return line, whitespace-separated token, and character counts."""
    return len(text.splitlines()), len(text.split()), len(text)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(f"usage: python3 {argv[0]} FILE", file=sys.stderr)
        return 2

    try:
        with open(argv[1], encoding="utf-8") as source:
            content = source.read()
    except (OSError, UnicodeError) as error:
        print(f"cannot read {argv[1]}: {error}", file=sys.stderr)
        return 1

    lines, words, characters = summarize(content)
    print(f"lines: {lines}")
    print(f"words: {words}")
    print(f"characters: {characters}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
