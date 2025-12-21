class MatrixData:
    @property
    def data(self) -> list[list[float]]:
        if self._data is None:
            self._data = []
        return self._data

    @data.setter
    def data(self, value: list[list[float]]):
        if len(value) <= 0 or not all(len(row) == len(value[0]) for row in value):
            raise ValueError("data must be a non-empty rectangle matrix")
        self._data = [list(row) for row in value]  # copy

    @property
    def shape(self) -> tuple[int, int]:
        return (len(self.data), len(self.data[0]))


class FileIOMixin(MatrixData):
    def to_txt(self, path: str):
        with open(path, "w", encoding="utf-8") as f:
            for row in self.data:
                f.write(" ".join(map(str, row)) + "\n")


class PrettyStrMixin(MatrixData):
    def __str__(self) -> str:
        srows = [[str(x) for x in row] for row in self.data]
        n_cols = len(srows[0])
        widths = [0] * n_cols
        for j in range(n_cols):
            widths[j] = max(len(r[j]) for r in srows)
        hline = "+" + "+".join("-" * (w + 2) for w in widths) + "+"
        lines = [hline]
        for r in srows:
            line = "| " + " | ".join(r[j].rjust(widths[j]) for j in range(n_cols)) + " |"
            lines.append(line)
            lines.append(hline)
        return "\n".join(lines)


class HashMixin(MatrixData):
    def __eq__(self, other) -> bool:
        if not isinstance(other, MatrixData):
            return False
        return self.data == other.data

    """
    hash = (sum(all_elements) + 31*rows + 17*cols) mod 2**32
    Эта функция легко даёт коллизии (например, разные матрицы с одинаковой суммой).
    """

    def __hash__(self) -> int:
        r, c = self.shape
        s = sum([sum(row) for row in self.data])
        return int((s + 31 * r + 17 * c) % (2**32))
