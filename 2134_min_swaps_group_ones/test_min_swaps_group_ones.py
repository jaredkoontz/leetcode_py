# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii
import pytest


class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        return self.minSwaps_sliding_mine(nums)

    @staticmethod
    def minSwaps_sliding_mine(nums: list[int]) -> int:
        n = len(nums)

        # total number of ones
        ones = 0
        for i in range(n):
            if nums[i] == 1:
                ones += 1

        # if there are 1 or fewer ones, no swaps are needed
        if ones <= 1:
            return 0

        # sliding window length
        k = ones
        count = 0

        # count ones in the initial window of size k
        for i in range(k):
            if nums[i] == 1:
                count += 1

        max_ones = count

        # slide the window across the array
        for i in range(k, n + k):
            # if element removing from window is 1, then decrease count
            if nums[i - k] == 1:
                count -= 1

            # if element adding to window is 1, then increase count
            if nums[i % n] == 1:
                count += 1

            # maintaining max_ones for all sub arrays of length k
            max_ones = max(max_ones, count)

        # (total length of subarray - ones in the sub array found)
        return k - max_ones

    @staticmethod
    def minSwaps_sliding_constant_space(nums: list[int]) -> int:
        ones, n = nums.count(1), len(nums)
        x, ones_in_window = 0, 0
        for i in range(n * 2):
            if i >= ones and nums[i % n - ones]:
                x -= 1
            if nums[i % n] == 1:
                x += 1
            ones_in_window = max(x, ones_in_window)
        return ones - ones_in_window

    @staticmethod
    def minSwaps_sliding(nums: list[int]) -> int:
        ones = nums.count(1)
        nums = nums + nums
        x, ones_in_window = 0, 0
        for i in range(len(nums)):
            if i >= ones and nums[i - ones]:
                x -= 1
            if nums[i] == 1:
                x += 1
            ones_in_window = max(x, ones_in_window)
        return ones - ones_in_window


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([0, 1, 0, 1, 1, 0, 0], 1),
        ([0, 1, 1, 1, 0, 0, 1, 1, 0], 2),
        ([1, 1, 0, 0, 1], 0),
    ],
)
def test_minSwaps(nums, expected):
    assert Solution().minSwaps(nums) == expected
