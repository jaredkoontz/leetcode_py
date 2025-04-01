# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii
import functools

import pytest


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        return self.maxProfit_dp(prices)

    @staticmethod
    def maxProfit_state_repr(prices: list[int]) -> int:
        if not prices:
            return 0
        s1, s2, s3, s4 = -prices[0], float("-inf"), float("-inf"), float("-inf")

        for p in prices:
            # our first state, we bought our first share
            s1 = max(s1, -p)
            # our second state we sold our second share
            s2 = max(s2, s1 + p)
            # our third state, we bought our second share
            s3 = max(s3, s2 - p)
            # our fourth state, we sold our second share
            s4 = max(s4, s3 + p)
        return max(s4, 0)

    @staticmethod
    def maxProfit_dp(prices: list[int]) -> int:
        if not prices:
            return 0

        dp = [0 for _ in range(len(prices))]

        for t in range(1, 2 + 1):
            pos = -prices[0]
            profit = 0
            for i in range(1, len(prices)):
                pos = max(pos, dp[i] - prices[i])
                profit = max(profit, pos + prices[i])
                dp[i] = profit

        return dp[len(prices) - 1]

    @staticmethod
    def maxProfit_rec(prices: list[int]) -> int:
        @functools.cache
        def dfs(day, has_share, curr_profit, transaction_number):
            if day >= len(prices):
                max_profit[0] = max(curr_profit, max_profit[0])
                return 0
            if transaction_number >= 2:
                max_profit[0] = max(curr_profit, max_profit[0])
                return 0

            curr_price = prices[day]

            # buy today
            if not has_share:
                dfs(
                    day + 1, not has_share, curr_profit - curr_price, transaction_number
                )
            # sell today
            if has_share:
                dfs(
                    day + 1,
                    not has_share,
                    curr_profit + curr_price,
                    transaction_number + 1,
                )
            # skip today
            dfs(day + 1, has_share, curr_profit, transaction_number)

        max_profit = [0]
        dfs(0, False, 0, 0)
        return max_profit[0]


@pytest.mark.parametrize(
    "prices,expected",
    [
        ([3, 3, 5, 0, 0, 3, 1, 4], 6),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0),
        ([7, 1, 5, 3, 6, 4], 7),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0),
    ],
)
def test_maxProfit(prices, expected):
    assert Solution().maxProfit(prices) == expected
