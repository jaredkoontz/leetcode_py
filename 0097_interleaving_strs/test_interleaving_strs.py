# https://leetcode.com/problems/interleaving-string
import pytest


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return self.isInterleave_dp(s1, s2, s3)

    @staticmethod
    def isInterleave_dp(s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                # can we use str2
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
                # already false, do not need to do anything
        return dp[0][0]

    @staticmethod
    def isInterleave_memo(s1: str, s2: str, s3: str) -> bool:
        dp = {}

        # k = i + j
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in dp:
                return dp[(i, j)]
            # can we use str1
            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
            # can we use str2
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True

            dp[(i, j)] = False
            return False

        return dfs(0, 0)


@pytest.mark.parametrize(
    "s1,s2,s3,expected",
    [
        ("aabcc", "dbbca", "aadbbcbcac", True),
        ("aabcc", "dbbca", "aadbbbaccc", False),
        ("", "", "", True),
    ],
)
def test_isInterleave(s1, s2, s3, expected):
    assert Solution().isInterleave(s1, s2, s3) == expected
