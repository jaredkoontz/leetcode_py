# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered
import pytest


class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        return self.isCovered_line_sweep_no_prefix(ranges, left, right)

    @staticmethod
    def isCovered_line_sweep_no_prefix(
            ranges: list[list[int]], left: int, right: int
    ) -> bool:
        diff = [0] * 52

        for start, end in ranges:
            diff[start] += 1
            if end + 1 < 52:
                diff[end + 1] -= 1

        prefix = 0
        for i in range(1, right + 1):
            prefix += diff[i]
            if left <= i <= right and prefix == 0:
                return False
        return True

    @staticmethod
    def isCovered_line_sweep(ranges: list[list[int]], left: int, right: int) -> bool:
        diff = [0] * 52  # Assuming values in range [1, 50]

        for start, end in ranges:
            diff[start] += 1
            if end + 1 < 52:
                diff[end + 1] -= 1

        prefix = 0
        for i in range(1, 52):
            prefix += diff[i]
            if left <= i <= right and prefix <= 0:
                return False
        return True

    @staticmethod
    def isCovered_greedy_sorting(
            ranges: list[list[int]], left: int, right: int
    ) -> bool:
        ranges.sort()
        for start, end in ranges:
            if start <= left <= end:
                if end >= right:
                    return True
                left = end + 1  # shrink the uncovered range
        return False

    @staticmethod
    def isCovered_hashmap(ranges: list[list[int]], left: int, right: int) -> bool:
        covered = set()
        for start, end in ranges:
            for i in range(start, end + 1):
                covered.add(i)

        for i in range(left, right + 1):
            if i not in covered:
                return False
        return True


@pytest.mark.parametrize(
    "ranges,left,right,expected",
    [
        ([[1, 2], [3, 4], [5, 6]], 2, 5, True),
        ([[1, 10], [10, 20]], 21, 21, False),
        ([[37, 49], [5, 17], [8, 32]], 29, 49, False),
    ],
)
def test_isCovered(ranges, left, right, expected):
    assert Solution().isCovered(ranges, left, right) == expected
