# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts
import heapq
from collections import Counter

import pytest


class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        return self.minimumOperations_hash_map(nums)

    @staticmethod
    def minimumOperations_hash_map(nums: list[int]) -> int:
        my_map = {}
        counter = 0
        for n in nums:
            my_map[n] = my_map.get(n, 0) + 1

        for num in my_map.keys():
            if num != 0:
                counter += 1

        return counter

    @staticmethod
    def minimumOperations_counter(nums: list[int]) -> int:
        counts = Counter(nums)
        non_zero_counts = 0

        for num in counts.keys():
            if num != 0:
                non_zero_counts += 1

        return non_zero_counts

    @staticmethod
    def minimumOperations_heap(nums: list[int]) -> int:
        my_heap = []
        max_num = float("-inf")
        counter = 0
        for num in nums:
            max_num = max(num, max_num)
            if num != 0:
                heapq.heappush(my_heap, num)
        subtracted = 0
        while max_num > 0:
            curr_min = 0
            while not curr_min:
                curr_min = heapq.heappop(my_heap) - subtracted
            counter += 1
            max_num -= curr_min
            subtracted += curr_min
        return counter


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([30, 58, 36, 65], 4),
        ([1, 1, 1, 2, 2, 2, 3, 3], 3),
        ([1, 5, 0, 3, 5], 3),
        ([0], 0),
        ([1], 1),
        ([1, 4, 0, 3, 5], 4),
        ([1, 2, 3, 5], 4),
    ],
)
def test_make_array_zero(nums, expected):
    assert Solution().minimumOperations(nums) == expected
