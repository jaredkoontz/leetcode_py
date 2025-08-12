# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three
from functools import cache

import pytest


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        return self.checkPowersOfThree_mine(n)

    @staticmethod
    def checkPowersOfThree_greedy(n: int) -> bool:
        # intuition is we are always going to take the largest one we can,
        # if we always do that, and it is 0, we are good
        i = 0
        while 3 ** (i + 1) <= n:
            i += 1

        # greedy remove largest
        while i >= 0:
            power = 3**i
            if power <= n:
                n -= power
            if power <= n:
                return False
            # decrement it whether we picked this or not.
            i -= 1

        return n == 0

    @staticmethod
    def checkPowersOfThree_mine(n: int) -> bool:
        works = [False]

        @cache
        def dfs(curr_power, curr_sum):
            if 3**curr_power > n:
                return
            if 3**curr_power + curr_sum == n:
                works[0] = True

            # take the current_power
            dfs(curr_power + 1, 3**curr_power + curr_sum)
            # don't take the current_power
            dfs(curr_power + 1, curr_sum)

        dfs(0, 0)
        return works[0]


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, True),
        (2, False),
        (3, True),
        (4, True),
        (5, False),
        (6, False),
        (12, True),
        (91, True),
        (21, False),
    ],
)
def test_checkPowersOfThree(n: int, expected: bool) -> None:
    assert Solution().checkPowersOfThree(n) == expected
