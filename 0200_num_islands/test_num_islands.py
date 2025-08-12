# https://leetcode.com/problems/number-of-islands
from collections import deque

import pytest


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        return self.numIslands_neet(grid)

    @staticmethod
    def numIslands_neet(grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        # we could get rid of visited, if we mark the island as something other than a 1 or 0.
        # don't want to modify the input, however.
        visited = set()
        num_islands = 0

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            while queue:
                # can make dfs if we do pop rather than popleft
                curr_row, curr_col = queue.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    r, c = curr_row + dr, curr_col + dc
                    if (
                        # r in range(rows)
                        # and curr_col in range(cols)
                        0 <= r < rows
                        and 0 <= c < cols
                        and grid[r][c] == "1"
                        and (r, c) not in visited
                    ):
                        queue.append((r, c))
                        visited.add((r, c))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    num_islands += 1

        return num_islands

    @staticmethod
    def numIslands_dfs(grid: list[list[str]]) -> int:
        def dfs(curr_grid, row, col):
            if (
                row < 0
                or col < 0
                or row >= len(curr_grid)
                or col >= len(curr_grid[0])
                or curr_grid[row][col] != "1"
            ):
                return
            curr_grid[row][col] = "#"
            dfs(curr_grid, row + 1, col)
            dfs(curr_grid, row - 1, col)
            dfs(curr_grid, row, col + 1)
            dfs(curr_grid, row, col - 1)

        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    count += 1
        return count

    @staticmethod
    def numIslands_dfs_2(grid: list[list[str]]) -> int:
        def dfs(curr_grid, row, col):
            curr_grid[row][col] = 0
            for dr, dc in (1, 0), (-1, 0), (0, -1), (0, 1):
                r = row + dr
                c = col + dc
                if (
                    0 <= r < len(curr_grid)
                    and 0 <= c < len(curr_grid[0])
                    and curr_grid[r][c] == "1"
                ):
                    dfs(curr_grid, r, c)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    count += 1
        return count

    @staticmethod
    def numIslands_bfs(grid: list[list[str]]) -> int:
        def bfs(my_grid, row, col):
            queue = deque([(row, col)])
            while queue:
                row, col = queue.popleft()
                for row, col in (
                    [row + 1, col],
                    [row, col + 1],
                    [row - 1, col],
                    [row, col - 1],
                ):
                    if (
                        0 <= row < len(my_grid)
                        and 0 <= col < len(my_grid[0])
                        and my_grid[row][col] == "1"
                    ):
                        my_grid[row][col] = "0"
                        queue.append((row, col))

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    bfs(grid, i, j)
                    count += 1
        return count


@pytest.mark.parametrize(
    "grid,expected",
    [
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            1,
        ),
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            3,
        ),
    ],
)
def test_num_islands(grid, expected):
    assert Solution().numIslands(grid) == expected
