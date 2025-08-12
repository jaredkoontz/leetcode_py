# https://leetcode.com/problems/regions-cut-by-slashes
import pytest


class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        return self.regionsBySlashes_flood_fill(grid)

    @staticmethod
    def regionsBySlashes_flood_fill(grid: list[str]) -> int:
        # Directions for traversal: right, left, down, up
        DIRECTIONS = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        # Flood fill algorithm to mark all cells in a region
        def _flood_fill(expanded_grid, row, col):
            queue = [(row, col)]
            expanded_grid[row][col] = 1

            while queue:
                current_cell = queue.pop(0)
                # Check all four directions from the current cell
                for direction in DIRECTIONS:
                    new_row = direction[0] + current_cell[0]
                    new_col = direction[1] + current_cell[1]
                    # If the new cell is valid and unvisited, mark it and add to queue
                    if _is_valid_cell(expanded_grid, new_row, new_col):
                        expanded_grid[new_row][new_col] = 1
                        queue.append((new_row, new_col))

        # Check if a cell is within bounds and unvisited
        def _is_valid_cell(expanded_grid, row, col):
            n = len(expanded_grid)
            return (
                    row >= 0
                    and col >= 0
                    and row < n
                    and col < n
                    and expanded_grid[row][col] == 0
            )

        grid_size = len(grid)
        # Create a 3x3 matrix for each cell in the original grid
        expanded_grid = [[0] * (grid_size * 3) for _ in range(grid_size * 3)]

        # Populate the expanded grid based on the original grid
        # 1 represents a barrier in the expanded grid
        for i in range(grid_size):
            for j in range(grid_size):
                base_row = i * 3
                base_col = j * 3
                # Check the character in the original grid
                if grid[i][j] == "\\":
                    # Mark diagonal for backslash
                    expanded_grid[base_row][base_col] = 1
                    expanded_grid[base_row + 1][base_col + 1] = 1
                    expanded_grid[base_row + 2][base_col + 2] = 1
                elif grid[i][j] == "/":
                    # Mark diagonal for forward slash
                    expanded_grid[base_row][base_col + 2] = 1
                    expanded_grid[base_row + 1][base_col + 1] = 1
                    expanded_grid[base_row + 2][base_col] = 1

        region_count = 0
        # Count regions using flood fill
        for i in range(grid_size * 3):
            for j in range(grid_size * 3):
                # If we find an unvisited cell (0), it's a new region
                if expanded_grid[i][j] == 0:
                    # Fill that region
                    _flood_fill(expanded_grid, i, j)
                    region_count += 1

        return region_count

    @staticmethod
    def regionsBySlashes_dfs(grid: list[str]) -> int:
        def dfs(i: int, j: int) -> int:
            if min(i, j) < 0 or max(i, j) >= len(g) or g[i][j] != 0:
                return 0
            g[i][j] = 1
            return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)

        n, regions = len(grid), 0
        g = [[0] * n * 3 for _ in range(n * 3)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == "/":
                    g[i * 3][j * 3 + 2] = g[i * 3 + 1][j * 3 + 1] = g[i * 3 + 2][
                        j * 3
                        ] = 1
                elif grid[i][j] == "\\":
                    g[i * 3][j * 3] = g[i * 3 + 1][j * 3 + 1] = g[i * 3 + 2][
                        j * 3 + 2
                        ] = 1
        for i in range(n * 3):
            for j in range(n * 3):
                regions += 1 if dfs(i, j) > 0 else 0
        return regions


@pytest.mark.parametrize(
    "grid,expected",
    [
        ([" /", "/ "], 2),
        ([" /", "  "], 1),
        (["/\\", "\\/"], 5),
    ],
)
def test_regionsBySlashes(grid, expected):
    assert Solution().regionsBySlashes(grid) == expected
