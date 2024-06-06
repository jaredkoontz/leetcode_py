from functools import lru_cache

import pytest


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        return self.uniquePathsWithObstacles_bottom_up(obstacleGrid)

    def uniquePathsWithObstacles_top_down(self, obstacleGrid: list[list[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        @lru_cache(maxsize=None)
        def dfs(i, j):
            if obstacleGrid[i][j]:  # hit an obstacle
                return 0
            if i == rows - 1 and j == cols - 1:  # reach the end
                return 1
            count = 0
            if i < rows - 1:
                count += dfs(i + 1, j)  # go down
            if j < cols - 1:
                count += dfs(i, j + 1)  # go right
            return count

        return dfs(0, 0)

    def uniquePathsWithObstacles_bottom_up(self, obstacleGrid: list[list[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        previous = [0] * n
        current = [0] * n
        previous[0] = 1

        for i in range(m):
            current[0] = 0 if obstacleGrid[i][0] == 1 else previous[0]
            for j in range(1, n):
                current[j] = (
                    0 if obstacleGrid[i][j] == 1 else current[j - 1] + previous[j]
                )
            previous[:] = current

        return previous[n - 1]


@pytest.mark.parametrize(
    "obstacleGrid, expected",
    [
        ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2),
        ([[0, 1], [0, 0]], 1),
    ],
)
def test_uniquePathsWithObstacles(obstacleGrid, expected):
    assert Solution().uniquePathsWithObstacles(obstacleGrid) == expected
