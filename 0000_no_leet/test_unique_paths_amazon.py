import pytest


def unique_paths(m: int, n: int) -> list[str]:
    def backtrack(rows, cols, path):
        if rows == m - 1 and cols == n - 1:
            res.append("".join(path))
            return

        if rows < m:
            path.append("D")
            backtrack(rows + 1, cols, path)
            path.pop()

        if cols < n:
            path.append("R")
            backtrack(rows, cols + 1, path)
            path.pop()

    res = []
    backtrack(0, 0, [])
    return res


@pytest.mark.parametrize(
    "rows, cols, expected",
    [
        (3, 3, ["DDRR", "DRDR", "DRRD", "RDDR", "RDRD", "RRDD"]),
        (2, 2, ["DR", "RD"]),
        (1, 1, [""]),
        (3, 2, ["DDR", "DRD", "RDD"]),
    ],
)
def test_unique_paths(rows, cols, expected):
    assert unique_paths(rows, cols) == expected
