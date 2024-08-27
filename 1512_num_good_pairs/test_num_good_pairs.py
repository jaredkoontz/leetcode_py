# https://leetcode.com/problems/number-of-good-pairs
from collections import Counter

import pytest


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        return self.numIdenticalPairs_hash_map(nums)

    @staticmethod
    def numIdenticalPairs_hash_map(nums: list[int]) -> int:
        hm = {}
        good_pairs = 0
        for i, num in enumerate(nums):
            friend_count = hm.get(num, 0)
            good_pairs += friend_count
            hm[num] = friend_count + 1
        return good_pairs

    @staticmethod
    def numIdenticalPairs_counter(nums: list[int]) -> int:
        good_pairs = 0
        counter = Counter(nums)

        for i, num in enumerate(nums):
            counter[num] -= 1
            good_pairs += counter[num]

        return good_pairs

    @staticmethod
    def numIdenticalPairs_naive(nums: list[int]) -> int:
        good_pairs = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] == nums[j] and i < j:
                    good_pairs += 1
        return good_pairs


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3, 1, 1, 3], 4),
        ([1, 1, 1, 1], 6),
        ([1, 2, 3], 0),
    ],
)
def test_numIdenticalPairs(nums, expected):
    assert Solution().numIdenticalPairs(nums) == expected
