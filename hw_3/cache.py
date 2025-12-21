from matrix import MatrixBasic
from mixins import HashMixin


class MatrixCached(MatrixBasic, HashMixin):
    _MATMUL_CACHE: dict[tuple[int, int], list[list[float]]] = {}

    def __matmul__(self, other: MatrixBasic) -> "MatrixCached":
        key = (hash(self), hash(other))
        cached = MatrixCached._MATMUL_CACHE.get(key)
        if cached is not None:
            return MatrixCached(cached)

        res = super().__matmul__(other)
        MatrixCached._MATMUL_CACHE[key] = res.data
        return MatrixCached(res.data)


if __name__ == "__main__":
    A = MatrixBasic([[1, 0], [0, 0]])
    C = MatrixBasic([[0, 1], [0, 0]])

    B = MatrixBasic([[1, 2], [3, 4]])
    D = MatrixBasic([[1, 2], [3, 4]])

    print("Matrix A:")
    print(A)
    print("Matrix B:")
    print(B)
    print("Matrix C:")
    print(C)
    print("Matrix D:")
    print(D)

    print(f"Matrix A and C equality: {A == C}")
    print(f"Matrix B and D equality: {B == D}")
    print(f"Matrix A and C hash values {hash(A)} and {hash(C)}")
    ab = A @ B
    cd = C @ D
    print("Matrix A and B matmul result:")
    print(ab)
    print("Matrix C and D matmul result:")
    print(cd)
    print(f"ab == cd: {ab == cd}")

    print("Now using cached version:")

    A = MatrixCached([[1, 0], [0, 0]])
    C = MatrixCached([[0, 1], [0, 0]])

    B = MatrixCached([[1, 2], [3, 4]])
    D = MatrixCached([[1, 2], [3, 4]])

    cached_ab = A @ B
    cached_cd = C @ D
    print("Cached matrix A and B matmul result:")
    print(cached_ab)
    print("Cached matrix C and D matmul result:")
    print(cached_cd)
    print(f"cached_ab == cached_cd: {cached_ab == cached_cd}")

    A.to_txt("artifacts/3/A.txt")
    B.to_txt("artifacts/3/B.txt")
    C.to_txt("artifacts/3/C.txt")
    D.to_txt("artifacts/3/D.txt")
    ab.to_txt("artifacts/3/AB.txt")
    cd.to_txt("artifacts/3/CD.txt")
    cached_ab.to_txt("artifacts/3/AB_CACHED.txt")
    cached_cd.to_txt("artifacts/3/CD_CACHED.txt")

    with open("artifacts/3/hash.txt", "w") as f:
        f.write(f"Hash of Matrix A: {hash(A)}\n")
        f.write(f"Hash of Matrix B: {hash(B)}\n")
        f.write(f"Hash of Matrix C: {hash(C)}\n")
        f.write(f"Hash of Matrix D: {hash(D)}\n")
        f.write(f"Hash of Matrix AB (non-cached): {hash(ab)}\n")
        f.write(f"Hash of Matrix CD (non-cached): {hash(cd)}\n")
        f.write(f"Hash of Matrix AB (cached): {hash(cached_ab)}\n")
        f.write(f"Hash of Matrix CD (cached): {hash(cached_cd)}\n")
