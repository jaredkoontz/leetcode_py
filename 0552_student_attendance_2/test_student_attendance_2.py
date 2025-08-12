# https://leetcode.com/problems/student-attendance-record-ii
import pytest


class Solution:
    def checkRecord(self, n: int) -> int:
        return self.checkRecord_mine(n)

    @staticmethod
    def checkRecord_mine(n: int) -> int:
        """
        Suppose dp[i] is the number of all the rewarded sequences without 'A'
        having their length equals to i, then we have:
            1. Number of sequence ends with 'P': dp[i - 1]
            2. Number of sequence ends with 'L':
                2.1 Number of sequence ends with 'PL': dp[i - 2]
                2.2 Number of sequence ends with 'LL':
                    2.2.1 Number of sequence ends with 'PLL': dp[i - 3]
                    2.2.2 Number of sequence ends with 'LLL': 0 (not allowed)

            So dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3], 3 <= i <= n

        Then all the rewarding sequences with length n are divided into
        two cases as follows:
            1. Number of sequences without 'A': dp[n]
            2. Number of sequence with A in the middle, since we could only
                have at most one A in the sequence to get it rewarded,
                suppose A is at the ith position, then we have:
                    A[i] = dp[i] * dp[n - 1 - i]

                Then the number of such sequences is:
                    sum(A[i] for i in range(n))

        Then our final result will be dp[n] + sum(A[i] for i in range(n)).

        Corner cases:
            1. dp[0] = 1: which means the only case when the sequence is an
                empty string.
            2. dp[1] = 2: 'L', 'P'
            3. dp[2] = 4: 'LL', 'LP', 'PL', 'PP'
        """
        if not n:
            return 0

        if n == 1:
            return 3

        mod = 10 ** 9 + 7
        dp = [1, 2, 4] + [0] * (n - 2)

        # Calculate sequences without 'A'.
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % mod

        # Calculate final result.
        result = dp[n] % mod
        for i in range(n):
            result += (dp[i] * dp[n - 1 - i]) % mod

        return result % mod


@pytest.mark.parametrize(
    "n,expected",
    [
        (2, 8),
        (1, 3),
        (10101, 183236316),
    ],
)
def test_checkRecord(n, expected):
    assert Solution().checkRecord(n) == expected
