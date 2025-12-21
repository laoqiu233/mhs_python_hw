import numpy as np
from mixins import FileIOMixin, PrettyStrMixin
from numpy.lib.mixins import NDArrayOperatorsMixin


class MatrixNP(NDArrayOperatorsMixin, FileIOMixin, PrettyStrMixin):
    __array_priority__ = 1000  # чтобы операции с ndarray предпочитали наш тип

    def __init__(self, data):
        self.data = data

    def __array__(self, dtype=None):
        return np.asarray(self._data, dtype=dtype)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        # преобразуем входы в ndarray
        in_arrays = []
        for x in inputs:
            if isinstance(x, MatrixNP):
                in_arrays.append(x._data)
            else:
                in_arrays.append(x)

        result = getattr(ufunc, method)(*in_arrays, **kwargs)

        if isinstance(result, tuple):
            return tuple(MatrixNP(x) if isinstance(x, np.ndarray) else x for x in result)

        if isinstance(result, np.ndarray):
            return MatrixNP(result)
        return result

    def __repr__(self):
        return f"MatrixNP(shape={self.shape})"


if __name__ == "__main__":
    a_data = np.random.randint(0, 10, (10, 10))
    b_data = np.random.randint(0, 10, (10, 10))

    a = MatrixNP(a_data.tolist())
    b = MatrixNP(b_data.tolist())

    print("Matrix A:")
    print(a)
    print("Matrix B:")
    print(b)

    a.to_txt("artifacts/2/a.txt")
    b.to_txt("artifacts/2/b.txt")

    sum_result = a + b
    sum_result.to_txt("artifacts/2/matrix+.txt")
    print("Sum result:")
    print(sum_result)

    mul_result = a * b
    mul_result.to_txt("artifacts/2/matrix*.txt")
    print("Mul result:")
    print(mul_result)

    matmul_result = a @ b
    matmul_result.to_txt("artifacts/2/matrix@.txt")
    print("Matmul result:")
    print(matmul_result)
