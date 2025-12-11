import sys
from typing import TextIO


def _tail(io: TextIO, n: int, name: str):
    if name:
        print(f"==> {name} <==")

    lines = io.readlines()
    output_lines = lines[-n:]
    print(*output_lines, sep="", end="")


files = sys.argv[1:]

if files:
    for file in files:
        with open(file) as f:
            _tail(f, 10, "" if len(files) == 1 else file)
else:
    _tail(sys.stdin, 17, "")
