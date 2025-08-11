from functools import lru_cache

import pytest


class Solution:
    def checkValidString(self, s: str) -> bool:
        return self.checkValidString_recursive(s)

    @staticmethod
    @lru_cache
    def checkValidString_recursive(s: str) -> bool:
        n = len(s)

        def dfs(ind: int, open_count: int) -> bool:
            if ind == n:
                return open_count == 0

            ch = s[ind]
            if ch == "*":
                # Try as '('
                if dfs(ind + 1, open_count + 1):
                    return True
                # Try as ')'
                if open_count > 0 and dfs(ind + 1, open_count - 1):
                    return True
                # Try as empty
                if dfs(ind + 1, open_count):
                    return True
                return False
            elif ch == "(":
                return dfs(ind + 1, open_count + 1)
            else:  # ch == ')'
                if open_count == 0:
                    return False
                return dfs(ind + 1, open_count - 1)

        return dfs(0, 0)

    @staticmethod
    def checkValidString_dp(s: str) -> bool:
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        dp[n][0] = True

        for ind in range(n - 1, -1, -1):
            for open_count in range(n):
                ch = s[ind]
                if ch == "*":
                    # as '('
                    if dp[ind + 1][open_count + 1]:
                        dp[ind][open_count] = True
                        continue
                    # as ')'
                    if open_count > 0 and dp[ind + 1][open_count - 1]:
                        dp[ind][open_count] = True
                        continue
                    # as empty
                    if dp[ind + 1][open_count]:
                        dp[ind][open_count] = True
                elif ch == "(":
                    if dp[ind + 1][open_count + 1]:
                        dp[ind][open_count] = True
                else:  # ch == ')'
                    if open_count > 0 and dp[ind + 1][open_count - 1]:
                        dp[ind][open_count] = True

        return dp[0][0]


@pytest.mark.parametrize(
    "s,expected",
    [
        ("()", True),
        ("()()", True),
        ("(*)", True),
        ("())", False),
    ],
)
def test_checkValidString(s, expected):
    assert expected == Solution().checkValidString(s)
