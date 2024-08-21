# https://leetcode.com/problems/k-diff-pairs-in-an-array
from collections import Counter

import pytest


class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        return self.findPairs_counter(nums, k)

    @staticmethod
    def findPairs_counter(nums: list[int], k: int) -> int:
        counter = Counter(nums)
        count = 0
        for key, value in counter.items():
            if k == 0:
                if value >= 2:
                    count += 1
            else:
                if key - k in counter:
                    count += 1

        return count

    @staticmethod
    def findPairs_naive(nums: list[int], k: int) -> int:
        unique_pairs = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    unique_pairs.add((max(nums[i], nums[j]), min(nums[i], nums[j])))
        return len(unique_pairs)


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([3, 1, 4, 1, 5], 2, 2),
        ([1, 2, 3, 4, 5], 1, 4),
        ([1, 3, 1, 5, 4], 0, 1),
    ],
)
def test_findPairs(nums, k, expected):
    assert Solution().findPairs(nums, k) == expected
