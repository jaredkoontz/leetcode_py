# https://leetcode.com/problems/regular-expression-matching
from functools import lru_cache

import pytest


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.isMatch_dp(s, p)

    @staticmethod
    def isMatch_mine(s: str, p: str) -> bool:
        m, n = len(s), len(p)

        @lru_cache(None)
        def dp(i, j):
            # Both strings consumed
            if i < 0 and j < 0:
                return True
            # Pattern exhausted but string remains
            if j < 0:
                return False
            # String exhausted: pattern must be 'x*' chunks
            if i < 0:
                # Check if the remaining pattern is all in x*
                if p[j] == "*":
                    return dp(i, j - 2)
                return False

            if p[j] == s[i] or p[j] == ".":
                return dp(i - 1, j - 1)

            if p[j] == "*":
                # '*' modifies p[j-1]
                if j == 0:
                    return False  # '*' can't be first
                if p[j - 1] == s[i] or p[j - 1] == ".":
                    return dp(i - 1, j) or dp(i, j - 2)
                else:
                    return dp(i, j - 2)  # '*' represents zero occurrence

            return False

        return dp(m - 1, n - 1)

    @staticmethod
    def isMatch_dp(s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] in {s[i - 1], "."}:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] in {s[i - 1], "."}:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[m][n]


@pytest.mark.parametrize(
    "s, p, expected",
    [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
    ],
)
def test_isMatch(s, p, expected):
    assert Solution().isMatch(s, p) == expected
