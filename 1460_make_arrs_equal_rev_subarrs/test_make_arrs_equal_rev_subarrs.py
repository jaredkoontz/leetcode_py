# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays
from collections import Counter

import pytest


class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        return self.canBeEqual_mine(target, arr)

    @staticmethod
    def canBeEqual_sort(target: list[int], arr: list[int]) -> bool:
        return sorted(target) == sorted(arr)

    @staticmethod
    def canBeEqual_mine(target: list[int], arr: list[int]) -> bool:
        return Counter(target) == Counter(arr)


@pytest.mark.parametrize(
    "target,arr,expected",
    [
        ([1, 2, 3, 4], [2, 4, 1, 3], True),
        ([7], [7], True),
        ([3, 7, 9], [3, 7, 11], False),
    ],
)
def test_canBeEqual(target, arr, expected):
    assert Solution().canBeEqual(target, arr) == expected
