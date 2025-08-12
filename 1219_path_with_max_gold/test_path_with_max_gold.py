# https://leetcode.com/problems/path-with-maximum-gold
from collections import deque

import pytest


class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        return self.getMaximumGold_dfs(grid)

    @staticmethod
    def getMaximumGold_backtrack(grid: list[list[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def backtrack(gold, x, y):
            if not (0 <= x < rows and 0 <= y < columns) or grid[x][y] == 0:
                return gold

            curr_gold = 0
            val = grid[x][y]
            grid[x][y] = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                curr_gold = max(curr_gold, backtrack(gold + val, nx, ny))
            grid[x][y] = val
            return curr_gold

        total_gold = sum(sum(row) for row in grid)
        max_gold = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]:
                    max_gold = max(max_gold, backtrack(0, i, j))
                    if max_gold == total_gold:
                        return total_gold

        return max_gold

    @staticmethod
    def getMaximumGold_bruh(grid: list[list[int]]) -> int:
        grid = (
            [[0] * (len(grid[0]) + 2)]
            + [[0] + r + [0] for r in grid]
            + [[0] * (len(grid[0]) + 2)]
        )
        rows, columns = len(grid), len(grid[0])

        def directions(i, j):
            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                n_i = i + di
                n_j = j + dj
                if grid[n_i][n_j]:
                    yield n_i, n_j

        def sum_component(component):
            return sum(grid[r][c] for (r, c) in component)

        already_in_cc = [[False] * len(grid[0]) for _ in grid]

        def cc(r, c):
            component = [(r, c)]
            queue = deque([(r, c)], maxlen=25)
            already_in_cc[r][c] = True

            while queue:
                (i, j) = queue.popleft()
                for new_i, new_j in ((i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)):
                    if grid[new_i][new_j] and not already_in_cc[new_i][new_j]:
                        already_in_cc[new_i][new_j] = True
                        component.append((new_i, new_j))
                        queue.append((new_i, new_j))
            return component

        components = []
        for row in range(rows):
            for col in range(columns):
                if not already_in_cc[row][col] and grid[row][col]:
                    components.append(cc(row, col))

        def brute_force(component, current_best):
            if len(component) == 1:
                return grid[component[0][0]][component[0][1]]
            comp_sum = sum_component(component)
            if comp_sum <= current_best:
                return current_best

            def recur(r, c, score):
                temp = grid[r][c]
                score += temp
                grid[r][c] = 0
                best = score
                for n_r, n_c in ((r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)):
                    if grid[n_r][n_c]:
                        best = max(best, recur(n_r, n_c, score))
                grid[r][c] = temp
                return best

            best = 0
            for r, c in (
                (r, c) for (r, c) in component if len(list(directions(r, c))) == 1
            ):
                best = max(best, recur(r, c, 0))
                if best == comp_sum:
                    return best
            if best == 0:
                for r, c in (
                    (r, c) for (r, c) in component if len(list(directions(r, c))) == 2
                ):
                    best = max(best, recur(r, c, 0))
                    if best == comp_sum:
                        return best

            return best

        cur_best = 0
        for col in sorted(components, key=sum_component, reverse=True):
            cur_best = max(cur_best, brute_force(col, cur_best))
        return cur_best

    @staticmethod
    def getMaximumGold_dfs(grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        direction = (0, 1, 0, -1, 0)

        def dfs(row, col):
            if row < 0 or row == m or col < 0 or col == n or grid[row][col] == 0:
                return 0
            ret = 0
            org_gold = grid[row][col]
            grid[row][col] = 0
            for i in range(4):
                ret = max(ret, dfs(row + direction[i], col + direction[i + 1]))
            grid[row][col] = org_gold
            return ret + grid[row][col]

        ans = 0
        for r in range(m):
            for c in range(n):
                ans = max(ans, dfs(r, c))
        return ans


@pytest.mark.parametrize(
    "grid,expected",
    [
        ([[0, 6, 0], [5, 8, 7], [0, 9, 0]], 24),
        ([[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]], 28),
    ],
)
def test_getMaximumGold(grid, expected):
    assert Solution().getMaximumGold(grid) == expected
