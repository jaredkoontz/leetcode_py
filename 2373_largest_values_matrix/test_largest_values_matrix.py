import pytest


class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        # assert (
        #     self.largestLocal_sliding_window_optimal(grid)
        #     == self.largestLocal_sliding_window(grid)
        #     == self.largestLocal_naive_2(grid)
        #     == self.largestLocal_naive(grid)
        # )
        return self.largestLocal_sliding_window_optimal(grid)

    @staticmethod
    def largestLocal_sliding_window_optimal(grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)

        for i in range(1, n - 1):
            for j in range(1, n - 1):
                temp = 0

                for k in range(i - 1, i + 2):
                    for left in range(j - 1, j + 2):
                        temp = max(temp, grid[k][left])

                grid[i - 1][j - 1] = temp

        n = len(grid)
        grid = [row[: n - 2] for row in grid[: n - 2]]

        return grid

    @staticmethod
    def largestLocal_sliding_window(grid: list[list[int]]) -> list[list[int]]:
        n, res = len(grid), []

        for i in range(1, n - 1):
            temp_row = []
            for j in range(1, n - 1):
                temp = 0

                for k in range(i - 1, i + 2):
                    for left in range(j - 1, j + 2):
                        temp = max(temp, grid[k][left])

                temp_row.append(temp)
            res.append(temp_row)

        return res

    @staticmethod
    def largestLocal_naive_2(grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        ans = [[0] * (n - 2) for _ in range(n - 2)]

        for i in range(n - 2):
            for j in range(n - 2):
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        ans[i][j] = max(ans[i][j], grid[r][c])
        return ans

    @staticmethod
    def largestLocal_naive(grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        ans = []

        for i in range(n - 2):
            res = []

            for j in range(n - 2):
                k = [
                    grid[i][j],
                    grid[i][j + 1],
                    grid[i][j + 2],
                    grid[i + 1][j],
                    grid[i + 1][j + 1],
                    grid[i + 1][j + 2],
                    grid[i + 2][j],
                    grid[i + 2][j + 1],
                    grid[i + 2][j + 2],
                ]
                m = max(k)
                res.append(m)

            ans.append(res)

        return ans


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]], [[9, 9], [8, 6]]),
        (
            [
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 2, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
            ],
            [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
        ),
    ],
)
def test_largest_values_matrix(l1, expected):
    assert Solution().largestLocal(l1) == expected
