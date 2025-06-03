# https://leetcode.com/problems/find-missing-and-repeated-values/
from collections import Counter

import pytest


class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        return self.findMissingAndRepeatedValues_mine(grid)

    @staticmethod
    def findMissingAndRepeatedValues_counter(grid: list[list[int]]) -> list[int]:
        # Flatten 2D array
        count = Counter(sum(grid, []))

        result = []

        for key in count:
            if count[key] == 2:
                result.append(key)
                break

        for i in range(1, len(grid[0]) ** 2 + 1):
            if i not in count.keys():
                result.append(i)
                break

        return result

    @staticmethod
    def findMissingAndRepeatedValues_mine(grid: list[list[int]]) -> list[int]:
        rows = len(grid)
        cols = len(grid[0])

        a = 0
        b = 0

        total = rows * cols

        nums = {x for x in range(1, total + 1)}

        for r in range(0, rows):
            for c in range(0, cols):
                candi = grid[r][c]
                if candi not in nums:
                    a = candi
                else:
                    nums.remove(candi)
        b = next(iter(nums))
        return [a, b]


@pytest.mark.parametrize(
    "grid,expected",
    [
        ([[1, 3], [2, 2]], [2, 4]),
        ([[9, 1, 7], [8, 9, 2], [3, 4, 6]], [9, 5]),
    ],
)
def test_findMissingAndRepeatedValues(grid, expected):
    assert Solution().findMissingAndRepeatedValues(grid) == expected
