import re
import sys
from typing import TextIO


def _wc(io: TextIO, name: str) -> tuple[int, int, int]:
    content = io.read()
    bytes_count = len(content)
    lines_count = content.count("\n")
    words_count = len(re.findall(r"\S+", content))

    print(f"{lines_count} {words_count} {bytes_count} {name}")

    return (bytes_count, lines_count, words_count)


files = sys.argv[1:]

if files:
    total_bytes = 0
    total_lines = 0
    total_words = 0
    for file in files:
        with open(file) as f:
            bytes_count, lines_count, words_count = _wc(f, file)
            total_bytes += bytes_count
            total_lines += lines_count
            total_words += words_count
    if len(files) > 1:
        print(f"{total_lines} {total_words} {total_bytes} total")
else:
    _wc(sys.stdin, "")
