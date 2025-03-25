# https://leetcode.com/problems/perfect-squares
import functools
import sys

import pytest


class Solution:
    def numSquares(self, n: int) -> int:
        return self.numSquares_memo(n)

    @staticmethod
    def numSquares_memo(n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0
        for current_number in range(1, n + 1):
            for s in range(1, current_number + 1):
                square = s * s
                if (current_number - square) < 0:
                    break
                remaining = current_number - square
                dp[current_number] = min(dp[current_number], 1 + dp[remaining])

        return dp[n]

    @staticmethod
    def numSquares_naive(n: int) -> int:
        @functools.cache
        def helper(remaining, steps):
            if remaining == 0:
                min_squares[0] = min(steps, min_squares[0])

            for square in squares:
                new_total = remaining - square
                if new_total >= 0:
                    helper(remaining - square, steps + 1)

        min_squares = [sys.maxsize]
        squares = []
        sq = 1
        while sq * sq <= n:
            squares.append(sq * sq)
            sq += 1

        helper(n, 0)
        return min_squares[0]


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 1),
        (5, 2),
        (6, 3),
        (7, 4),
        (8, 2),
        (9, 1),
        (10, 2),
        (11, 3),
        (12, 3),
        (13, 2),
        # (14,3),
        # (15,4),
        # (16,1),
        # (17,2),
        (191, 4),
        (346, 2),
        (347, 3),
    ],
)
def test_numSquares(n, expected):
    assert Solution().numSquares(n) == expected
