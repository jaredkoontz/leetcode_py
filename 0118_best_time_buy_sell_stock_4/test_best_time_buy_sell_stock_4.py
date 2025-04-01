# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv
import pytest


class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        return self.maxProfit_dp(k, prices)

    @staticmethod
    def maxProfit_dp(k: int, prices: list[int]) -> int:
        if not prices:
            return 0

        dp = [0 for _ in range(len(prices))]

        for t in range(1, k + 1):
            pos = -prices[0]
            profit = 0
            for i in range(1, len(prices)):
                pos = max(pos, dp[i] - prices[i])
                profit = max(profit, pos + prices[i])
                dp[i] = profit

        return dp[len(prices) - 1]

    @staticmethod
    def maxProfit_state(k: int, prices: list[int]) -> int:
        N = len(prices)

        def quickSolve():
            ans = 0
            for i in range(1, N):
                ans += max(0, prices[i] - prices[i - 1])
            return ans

        if k >= N // 2:
            return quickSolve()

        states = [
            [float("-inf")] * (2 * k + 1) for _ in range(2)
        ]  # 2k+1 states: s0 h1 s1 h2 s2... hk sk
        states[0][0] = states[1][0] = 0

        for i, v in enumerate(prices):
            for state in range(2 * k):
                states[i & 1][state + 1] = max(
                    states[1 - i & 1][state + 1],
                    states[1 - i & 1][state] - ((-1) ** state) * v,
                )

        return max(states[i & 1])


@pytest.mark.parametrize(
    "k,prices,expected",
    [
        (2, [2, 4, 1], 2),
        (2, [3, 2, 6, 5, 0, 3], 7),
    ],
)
def test_maxProfit(k, prices, expected):
    assert Solution().maxProfit(k, prices) == expected
