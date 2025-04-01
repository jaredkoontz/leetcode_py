# https://leetcode.com/problems/maximum-difference-between-increasing-elements
import heapq

import pytest


class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        return self.maximumDifference_smarter(nums)

    @staticmethod
    def maximumDifference_smarter(nums: list[int]) -> int:
        profit = -1
        buy = nums[0]
        for num in nums:
            profit = max(profit, num - buy)
            buy = min(buy, num)
        return -1 if profit <= 0 else profit

    @staticmethod
    def maximumDifference_heap(nums: list[int]) -> int:
        heap = []
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    heapq.heappush(heap, -(nums[j] - nums[i]))

        return -heapq.heappop(heap) if len(heap) else -1


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([7, 1, 5, 4], 4),
        ([9, 4, 3, 2], -1),
        ([1, 5, 2, 10], 9),
    ],
)
def test_maximumDifference(nums, expected):
    assert Solution().maximumDifference(nums) == expected
