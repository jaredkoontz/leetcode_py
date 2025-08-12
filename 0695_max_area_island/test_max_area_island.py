# https://leetcode.com/problems/max-area-of-island
from itertools import product

import pytest


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        return self.maxAreaOfIsland_mine(grid)

    @staticmethod
    def maxAreaOfIsland_mine(grid: list[list[int]]) -> int:
        max_area = 0
        m, n = len(grid), len(grid[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = 0
                    stack = [(i, j)]
                    visited.add((i, j))
                    while stack:
                        new_i, new_j = stack.pop()
                        area += 1
                        for i_off, j_off in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            r, c = new_i + i_off, new_j + j_off
                            if (
                                    0 <= r < m
                                    and 0 <= c < n
                                    and grid[r][c]
                                    and (r, c) not in visited
                            ):
                                visited.add((r, c))
                                stack.append((r, c))
                    max_area = max(area, max_area)
        return max_area

    @staticmethod
    def maxAreaOfIsland_recursive(grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
            return 0

        areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        return max(areas) if areas else 0

    @staticmethod
    def maxAreaOfIsland_product(grid: list[list[int]]) -> int:
        ans, n, m = 0, len(grid), len(grid[0])

        def trav(i: int, j: int) -> int:
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + trav(i - 1, j) + trav(i, j - 1) + trav(i + 1, j) + trav(i, j + 1)

        for i, j in product(range(n), range(m)):
            if grid[i][j]:
                ans = max(ans, trav(i, j))
        return ans


@pytest.mark.parametrize(
    "grid, expected",
    [
        (
                [
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                ],
                6,
        ),
        ([[0, 0, 0, 0, 0, 0, 0, 0]], 0),
    ],
)
def test_maxAreaOfIsland(grid, expected):
    assert Solution().maxAreaOfIsland(grid) == expected
