# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order
import heapq

import pytest


class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        return self.minSubsequence_mine(nums)

    @staticmethod
    def minSubsequence_mine(nums: list[int]) -> list[int]:
        nums.sort(reverse=True)
        left_sum, right_sum = 0, sum(nums)
        for ix, num in enumerate(nums):
            right_sum -= num
            left_sum += num
            if left_sum > right_sum:
                return nums[: ix + 1]

    @staticmethod
    def minSubsequence_count_sort(nums: list[int]) -> list[int]:
        counter = [0] * 101
        total = sum(nums)
        for num in nums:
            counter[num] += 1

        curr_sum = 0
        results = []
        for i in range(100, 0, -1):
            while counter[i] > 0 and curr_sum <= (total - curr_sum):
                curr_sum += i
                results.append(i)
                counter[i] -= 1

        return results

    @staticmethod
    def minSubsequence_heap(nums: list[int]) -> list[int]:
        res = []
        sub_sum = 0
        half_sum = sum(nums) // 2
        pq = [-num for num in nums]
        heapq.heapify(pq)

        while sub_sum <= half_sum:
            top = -heapq.heappop(pq)
            res.append(top)
            sub_sum += top

        return res


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([4, 3, 10, 9, 8], [10, 9]),
        ([4, 4, 7, 6, 7], [7, 7, 6]),
    ],
)
def test_min_subsequence(nums, expected):
    assert Solution().minSubsequence(nums) == expected
