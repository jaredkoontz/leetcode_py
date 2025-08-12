# https://leetcode.com/problems/spiral-matrix-iii
import pytest


class Solution:
    def spiralMatrixIII(
            self, rows: int, cols: int, rStart: int, cStart: int
    ) -> list[list[int]]:
        return self.spiralMatrixIII_readable(rows, cols, rStart, cStart)

    @staticmethod
    def spiralMatrixIII_simulation(
            rows: int, cols: int, rStart: int, cStart: int
    ) -> list[list[int]]:
        # Store all possible directions in an array.
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        traversed = []

        # Initial step size is 1, value of d represents the current direction.
        step = 1
        direction = 0
        while len(traversed) < rows * cols:
            # direction = 0 -> East, direction = 1 -> South
            # direction = 2 -> West, direction = 3 -> North
            for _ in range(2):
                for _ in range(step):
                    # Validate the current position
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        traversed.append([rStart, cStart])
                    # Make changes to the current position.
                    rStart += directions[direction][0]
                    cStart += directions[direction][1]

                direction = (direction + 1) % 4
            step += 1
        return traversed

    @staticmethod
    def spiralMatrixIII_readable(n: int, m: int, row: int, col: int) -> list[list[int]]:
        def isValid(r: int, c: int, n: int, m: int, result: list[list[int]]) -> int:
            if 0 <= r < n and 0 <= c < m:
                result.append([r, c])
                return 1
            return 0

        res_count = 1
        total_count = n * m
        res = [[row, col]]
        x, y = 1, 2
        while res_count < total_count:
            for _ in range(x):
                col += 1
                res_count += isValid(row, col, n, m, res)

            for _ in range(x):
                row += 1
                res_count += isValid(row, col, n, m, res)

            for _ in range(y):
                col -= 1
                res_count += isValid(row, col, n, m, res)

            for _ in range(y):
                row -= 1
                res_count += isValid(row, col, n, m, res)

            x += 2
            y += 2
        return res


@pytest.mark.parametrize(
    "rows,cols,rStart,cStart,expected",
    [
        (1, 4, 0, 0, [[0, 0], [0, 1], [0, 2], [0, 3]]),
        (
                5,
                6,
                1,
                4,
                [
                    [1, 4],
                    [1, 5],
                    [2, 5],
                    [2, 4],
                    [2, 3],
                    [1, 3],
                    [0, 3],
                    [0, 4],
                    [0, 5],
                    [3, 5],
                    [3, 4],
                    [3, 3],
                    [3, 2],
                    [2, 2],
                    [1, 2],
                    [0, 2],
                    [4, 5],
                    [4, 4],
                    [4, 3],
                    [4, 2],
                    [4, 1],
                    [3, 1],
                    [2, 1],
                    [1, 1],
                    [0, 1],
                    [4, 0],
                    [3, 0],
                    [2, 0],
                    [1, 0],
                    [0, 0],
                ],
        ),
    ],
)
def test_spiralMatrixIII(rows, cols, rStart, cStart, expected):
    assert Solution().spiralMatrixIII(rows, cols, rStart, cStart) == expected
