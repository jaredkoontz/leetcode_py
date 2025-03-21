# https://leetcode.com/problems/delete-greatest-value-in-each-row
import pytest


class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        return self.deleteGreatestValue_mine(grid)

    @staticmethod
    def deleteGreatestValue_one_line(grid: list[list[int]]) -> int:
        return sum(max(c) for c in zip(*[sorted(r) for r in grid]))

    @staticmethod
    def deleteGreatestValue_mine(grid: list[list[int]]) -> int:
        if not grid:
            return 0
        counts = 0
        while grid[0]:
            local_max = float("-inf")
            for row in grid:
                max_index = max(range(len(row)), key=row.__getitem__)
                local_max = max(local_max, row[max_index])
                del row[max_index]
            counts += local_max
        return counts


@pytest.mark.parametrize(
    "grid,expected",
    [
        ([[1, 2, 4], [3, 3, 1]], 8),
        ([[10]], 10),
        ([[]], 0),
    ],
)
def test_deleteGreatestValue(grid, expected):
    assert Solution().deleteGreatestValue(grid) == expected
