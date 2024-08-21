# https://leetcode.com/problems/maximum-subarray
from functools import cache

import pytest


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        return self.maxSubArray_kadanes(nums)

    @staticmethod
    def maxSubArray_divide_and_conquer_optimal(nums: list[int]) -> int:
        pre, suf = [*nums], [*nums]
        for i in range(1, len(nums)):
            pre[i] += max(0, pre[i - 1])
        for i in range(len(nums) - 2, -1, -1):
            suf[i] += max(0, suf[i + 1])

        def maxSubArray(A, L, R):
            if L == R:
                return A[L]
            mid = (L + R) // 2
            return max(
                maxSubArray(A, L, mid),
                maxSubArray(A, mid + 1, R),
                pre[mid] + suf[mid + 1],
            )

        return maxSubArray(nums, 0, len(nums) - 1)

    @staticmethod
    def maxSubArray_divide_and_conquer(nums: list[int]) -> int:
        def maxSubArray(A, L, R):
            if L > R:
                return float("-inf")
            mid, left_sum, right_sum, cur_sum = (L + R) // 2, 0, 0, 0
            for i in range(mid - 1, L - 1, -1):
                left_sum = max(left_sum, cur_sum := cur_sum + A[i])
            cur_sum = 0
            for i in range(mid + 1, R + 1):
                right_sum = max(right_sum, cur_sum := cur_sum + A[i])
            return max(
                maxSubArray(A, L, mid - 1),
                maxSubArray(A, mid + 1, R),
                left_sum + A[mid] + right_sum,
            )

        return maxSubArray(nums, 0, len(nums) - 1)

    @staticmethod
    def maxSubArray_tabulation(nums: list[int]) -> int:
        dp = [[0] * len(nums) for i in range(2)]
        dp[0][0], dp[1][0] = nums[0], nums[0]
        for i in range(1, len(nums)):
            dp[1][i] = max(nums[i], nums[i] + dp[1][i - 1])
            dp[0][i] = max(dp[0][i - 1], dp[1][i])
        return dp[0][-1]

    @staticmethod
    def maxSubArray_memo(nums: list[int]) -> int:
        @cache
        def solve(i, must_pick):
            if i >= len(nums):
                return 0 if must_pick else float("-inf")
            return max(
                nums[i] + solve(i + 1, True), 0 if must_pick else solve(i + 1, False)
            )

        return solve(0, False)

    @staticmethod
    def maxSubArray_recursive(nums: list[int]) -> int:
        def solve(i, must_pick):
            if i >= len(nums):
                return 0 if must_pick else float("-inf")
            return max(
                nums[i] + solve(i + 1, True), 0 if must_pick else solve(i + 1, False)
            )

        return solve(0, False)

    @staticmethod
    def maxSubArray_brute_force(nums: list[int]) -> int:
        ans = float("-inf")
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                ans = max(ans, cur_sum)
        return ans

    @staticmethod
    def maxSubArray_kadanes(nums: list[int]) -> int:
        curr_sum = 0
        max_sum = float("-inf")
        n = len(nums)

        for i in range(n):
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0

        return max_sum


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([-2, 1, -3, -4, -1, 2, 1, -100, 4], 4),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
    ],
)
def test_maxSubArray(l1, expected):
    assert Solution().maxSubArray(l1) == expected
