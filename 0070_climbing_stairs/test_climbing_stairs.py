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

        dp = [0] * (n + 1)
        dp[1] = dp[0] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    @staticmethod
    def climbStairs_bottom_optimal(n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one

    def climbStairs_naive(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        return self.climbStairs_naive(n - 1) + self.climbStairs_naive(n - 2)


@pytest.mark.parametrize(
    "n,expected", [(1, 1), (2, 2), (3, 3), (5, 8), (7, 21), (44, 1134903170)]
)
def test_climbStairs(n, expected):
    assert Solution().climbStairs(n) == expected
