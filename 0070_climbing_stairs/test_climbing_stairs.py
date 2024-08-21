# https://leetcode.com/problems/climbing-stairs
import functools

import pytest


class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climbStairs_bottom_optimal(n)

    @staticmethod
    def climbStairs_memo(n: int) -> int:
        def helper(step: int, memo: dict[int, int]) -> int:
            if step == 0 or step == 1:
                return 1
            if step not in memo:
                memo[step] = helper(step - 1, memo) + helper(step - 2, memo)
            return memo[step]

        return helper(n, {})

    @staticmethod
    def climbStairs_bottom_up_dp(n: int) -> int:
        if n == 0 or n == 1:
            return 1

        memo = [0] * (n + 1)
        memo[1] = 1
        memo[2] = 2
        for i in range(2, n):
            memo[i + 1] = memo[i] + memo[i - 1]

        return memo[n]

    @staticmethod
    def climbStairs_bottom_optimal(n: int) -> int:
        if n <= 2:
            return n

        first = 1
        second = 2

        for i in range(2, n):
            temp = second
            second = first + second
            first = temp
        return second

    @staticmethod
    def climbStairs_cache(n: int) -> int:
        @functools.cache
        def helper(curr_step):
            if curr_step <= 2:
                return curr_step
            return helper(curr_step - 1) + helper(curr_step - 2)

        return helper(n)

    @staticmethod
    def climbStairs_naive(n: int) -> int:
        def helper(curr_step):
            if curr_step <= 2:
                return curr_step

            return helper(curr_step - 1) + helper(curr_step - 2)

        return helper(n)


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (6, 13),
        (7, 21),
        (8, 34),
        (44, 1134903170),
    ],
)
def test_climbStairs(n, expected):
    assert Solution().climbStairs(n) == expected
