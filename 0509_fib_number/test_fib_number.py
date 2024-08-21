# https://leetcode.com/problems/fibonacci-number
import pytest


class Solution:
    def fib(self, n: int) -> int:
        return self.fib_bottom_up_optimal(n)

    def fib_naive(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib_naive(n - 1) + self.fib_naive(n - 2)

    @staticmethod
    def fib_memo(n: int) -> int:
        def helper(curr_fib: int, memo: dict[int, int]):
            if curr_fib not in memo:
                memo[curr_fib] = helper(curr_fib - 1, memo) + helper(curr_fib - 2, memo)
            return memo[curr_fib]

        return helper(n, {0: 0, 1: 1})

    @staticmethod
    def fib_bottom_up_dp(n: int) -> int:
        helper = [0] * (n + 1)
        helper[0] = helper[1] = 1
        for i in range(2, n):
            helper[i] = helper[i - 1] + helper[i - 2]
        return helper[n - 1]

    @staticmethod
    def fib_bottom_up_optimal(n: int) -> int:
        if n == 0:
            return 0
        one, two = 1, 1
        for i in range(2, n):
            temp = one
            one = one + two
            two = temp

        return one


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
        (11, 89),
    ],
)
def test_fib(n, expected):
    assert Solution().fib(n) == expected
