import numpy as np
from mixins import FileIOMixin, HashMixin, MatrixData, PrettyStrMixin


class MatrixBasic(HashMixin, FileIOMixin, PrettyStrMixin):
    _data: list[list[float]]

    def __init__(self, data: list[list[float]]):
        self.data = data  # использую сеттер из MatrixData

    def __add__(self, other: MatrixData) -> "MatrixBasic":
        if self.shape != other.shape:
            raise ValueError(f"shape mismatch {self.shape} vs {other.shape}")

        r, c = self.shape
        out = [[self.data[i][j] + other.data[i][j] for j in range(c)] for i in range(r)]
        return MatrixBasic(out)

    def __mul__(self, other: MatrixData) -> "MatrixBasic":
        if self.shape != other.shape:
            raise ValueError(f"shape mismatch {self.shape} vs {other.shape}")

        r, c = self.shape
        out = [[self.data[i][j] * other.data[i][j] for j in range(c)] for i in range(r)]
        return MatrixBasic(out)

    def __matmul__(self, other: "MatrixBasic") -> "MatrixBasic":
        r1, c1 = self.shape
        r2, c2 = other.shape
        if c1 != r2:
            raise ValueError(f"shape mismatch {self.shape} vs {other.shape}")

        out = [[0.0 for _ in range(c2)] for _ in range(r1)]
        for i in range(r1):
            for k in range(c1):
                aik = self._data[i][k]
                for j in range(c2):
                    out[i][j] += aik * other._data[k][j]
        return MatrixBasic(out)

    def __repr__(self):
        return f"MatrixBasic(shape={self.shape})"


if __name__ == "__main__":
    a_data = np.random.randint(0, 10, (10, 10))
    b_data = np.random.randint(0, 10, (10, 10))

    a = MatrixBasic(a_data.tolist())
    b = MatrixBasic(b_data.tolist())

    print("Matrix A:")
    print(a)
    print("Matrix B:")
    print(b)

    a.to_txt("artifacts/1/a.txt")
    b.to_txt("artifacts/1/b.txt")

    sum_result = a + b
    sum_result.to_txt("artifacts/1/matrix+.txt")
    print("Sum result:")
    print(sum_result)

    mul_result = a * b
    mul_result.to_txt("artifacts/1/matrix*.txt")
    print("Mul result:")
    print(mul_result)

    matmul_result = a @ b
    matmul_result.to_txt("artifacts/1/matrix@.txt")
    print("Matmul result:")
    print(matmul_result)
