# https://leetcode.com/problems/island-perimeter
import pytest


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        return self.islandPerimeter_mine(grid)

    @staticmethod
    def islandPerimeter_mine(grid: list[list[int]]) -> int:
        height, width, perimeter = len(grid), len(grid[0]), 0

        # Iterate through each cell
        for row in range(height):
            for col in range(width):
                # Is this a land cell?
                if grid[row][col] == 1:
                    # Top edge
                    if row == 0 or grid[row - 1][col] == 0:
                        perimeter += 1

                    # Bottom edge
                    if row == height - 1 or grid[row + 1][col] == 0:
                        perimeter += 1

                    # Left edge
                    if col == 0 or grid[row][col - 1] == 0:
                        perimeter += 1

                    # Right edge
                    if col == width - 1 or grid[row][col + 1] == 0:
                        perimeter += 1

        return perimeter

    @staticmethod
    def islandPerimeter_theirs(grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        perimeter = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    perimeter += 4
                    for i_off, j_off in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        r, c = i + i_off, j + j_off
                        if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                            perimeter -= 1
        return perimeter


@pytest.mark.parametrize(
    "grid,expected",
    [
        ([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]], 16),
        ([[1]], 4),
        ([[1, 0]], 4),
    ],
)
def test_islandPerimeter(grid, expected):
    assert Solution().islandPerimeter(grid) == expected
