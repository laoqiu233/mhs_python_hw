import sys
from typing import TextIO


def _nl(io: TextIO):
    lines = io.readlines()
    max_digits = len(str(len(lines)))
    print(*[f"{i:<{max_digits}d} {line}" for i, line in enumerate(lines, 1)], sep="", end="")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as file:
            _nl(file)
    else:
        _nl(sys.stdin)
