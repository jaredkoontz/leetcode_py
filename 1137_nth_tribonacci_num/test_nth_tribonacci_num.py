# https://leetcode.com/problems/n-th-tribonacci-number
import functools

import pytest


class Solution:
    def tribonacci(self, n: int) -> int:
        return self.tribonacci_optimal(n)

    @staticmethod
    def tribonacci_optimal(n: int) -> int:
        if n < 1:
            return 0
        if n == 1 or n == 2:
            return 1

        first = 0
        second = 1
        third = 1

        for i in range(2, n):
            temp = third
            third = first + second + third
            first = second
            second = temp
        return third

    @staticmethod
    def tribonacci_memo(n: int) -> int:
        if n < 1:
            return 0
        if n == 1 or n == 2:
            return 1

        memo = [0] * (n + 1)
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1
        for i in range(3, n + 1):
            memo[i] = memo[i - 3] + memo[i - 2] + memo[i - 1]
        return memo[n]

    @staticmethod
    def tribonacci_cache(n: int) -> int:
        @functools.cache
        def helper(num):
            if num < 1:
                return 0
            if num == 1 or num == 2:
                return 1
            return helper(num - 1) + helper(num - 2) + helper(num - 3)

        return helper(n)

    @staticmethod
    def tribonacci_naive(n: int) -> int:
        def helper(num):
            if num < 1:
                return 0
            if num == 1 or num == 2:
                return 1
            return helper(num - 1) + helper(num - 2) + helper(num - 3)

        return helper(n)


@pytest.mark.parametrize(
    "n,expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 4),
        (5, 7),
        (6, 13),
        (7, 24),
        (25, 1_389_537),
    ],
)
def test_tribonacci(n, expected):
    assert Solution().tribonacci(n) == expected
