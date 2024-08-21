# https://leetcode.com/problems/combination-sum-iv
import pytest


class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        return self.combinationSum4_dp(nums, target)

    @staticmethod
    def combinationSum4_single_arr_dp(nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]

        return dp[target]

    @staticmethod
    def combinationSum4_dp(nums: list[int], target: int) -> int:
        # why is it 1?!?!?
        dp = {0: 1}
        for total in range(1, target + 1):
            dp[total] = 0
            for n in nums:
                dp[total] += dp.get(total - n, 0)
        return dp[target]

    @staticmethod
    def combinationSum4_cache(nums: list[int], target: int) -> int:
        nums.sort()
        memo = {}

        def helper(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 1
            if n < nums[0]:
                return 0

            count = 0
            for num in nums:
                if n - num < 0:
                    break
                count += helper(n - num)

            memo[n] = count
            return count

        return helper(target)

    @staticmethod
    def combinationSum4_backtrack(nums: list[int], target: int) -> int:
        """TLE"""
        num_combos = 0

        def dfs(curr_sum):
            nonlocal num_combos
            if curr_sum == target:
                num_combos += 1
                return
            if curr_sum > target:
                return

            for num in nums:
                dfs(curr_sum + num)

        dfs(0)
        return num_combos


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([1, 2, 3], 32, 181_997_601),
        ([1, 2, 3], 4, 7),
        ([9], 3, 0),
    ],
)
def test_combinationSum4(nums, target, expected):
    assert Solution().combinationSum4(nums, target) == expected
