# https://leetcode.com/problems/divide-array-into-equal-pairs/
from collections import Counter

import pytest


class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        return self.divideArray_mine(nums)

    @staticmethod
    def divideArray_mine(nums: list[int]) -> bool:
        counter = Counter(nums)
        for item, count in counter.items():
            if count & 1 == 1:
                return False

        return True


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([3, 2, 3, 2, 2, 2], True),
        ([1, 2, 3, 4], False),
    ],
)
def test_divideArray(nums, expected):
    assert Solution().divideArray(nums) == expected
