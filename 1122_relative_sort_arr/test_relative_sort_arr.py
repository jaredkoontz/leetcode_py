# https://leetcode.com/problems/relative-sort-array
from collections import Counter

import pytest


class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        return self.relativeSortArray_mine(arr1, arr2)

    @staticmethod
    def relativeSortArray_mine(arr1: list[int], arr2: list[int]) -> list[int]:
        counter = Counter(arr1)
        ret = []
        for val in arr2:
            if val in counter:
                ret += [val] * counter[val]
                counter.pop(val)
        for num, count in sorted(counter.items()):
            ret += [num] * count

        return ret


@pytest.mark.parametrize(
    "arr1, arr2, expected",
    [
        (
                [
                    2,
                    21,
                    43,
                    38,
                    0,
                    42,
                    33,
                    7,
                    24,
                    13,
                    12,
                    27,
                    12,
                    24,
                    5,
                    23,
                    29,
                    48,
                    30,
                    31,
                ],
                [2, 42, 38, 0, 43, 21],
                [
                    2,
                    42,
                    38,
                    0,
                    43,
                    21,
                    5,
                    7,
                    12,
                    12,
                    13,
                    23,
                    24,
                    24,
                    27,
                    29,
                    30,
                    31,
                    33,
                    48,
                ],
        ),
        (
                [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19],
                [2, 1, 4, 3, 9, 6],
                [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19],
        ),
        ([28, 6, 22, 8, 44, 17], [22, 28, 8, 6], [22, 28, 8, 6, 17, 44]),
    ],
)
def test_relative_sort_arr(arr1, arr2, expected):
    assert Solution().relativeSortArray(arr1, arr2) == expected
