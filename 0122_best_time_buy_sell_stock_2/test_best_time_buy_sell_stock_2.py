# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
import functools
import math

import pytest


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        return self.maxProfit_dp(prices)

    @staticmethod
    def maxProfit_dont_overthink(prices: list[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

    @staticmethod
    def maxProfit_dp(prices: list[int]) -> int:
        hold_stock, keep_cash = 0, 1

        dp = {(-1, hold_stock): -math.inf, (-1, keep_cash): 0}

        for day, stock_price in enumerate(prices):
            # If today we have stock, either we already had it yesterday, or we just buy stock and hold it today.
            dp[day, hold_stock] = max(
                dp[day - 1, hold_stock], dp[day - 1, keep_cash] - stock_price
            )

            # If today we keep cash, either we already kept cash yesterday, or we just sell out stock today
            dp[day, keep_cash] = max(
                dp[day - 1, keep_cash], dp[day - 1, hold_stock] + stock_price
            )

        last_day = len(prices) - 1
        return dp[last_day, keep_cash]

    @staticmethod
    def maxProfit_memo(prices: list[int]) -> int:
        @functools.cache
        def trade(day_d):
            if day_d == 0:
                return -prices[day_d], 0

            prev_hold, prev_not_hold = trade(day_d - 1)

            my_hold = max(prev_hold, prev_not_hold - prices[day_d])
            my_not_hold = max(prev_not_hold, prev_hold + prices[day_d])

            return my_hold, my_not_hold

        last_day = len(prices) - 1
        hold, not_hold = trade(last_day)
        return max(hold, not_hold)

    @staticmethod
    def maxProfit_rec(prices: list[int]) -> int:
        @functools.cache
        def dfs(day, has_share, curr_profit):
            if day >= len(prices):
                max_profit[0] = max(curr_profit, max_profit[0])
                return 0

            curr_price = prices[day]

            # buy today
            if not has_share:
                dfs(day + 1, not has_share, curr_profit - curr_price)
            # sell today
            if has_share:
                dfs(day + 1, not has_share, curr_profit + curr_price)
            # skip today
            dfs(day + 1, has_share, curr_profit)

        max_profit = [0]
        dfs(0, False, 0)
        return max_profit[0]


@pytest.mark.parametrize(
    "prices,expected",
    [
        ([7, 1, 5, 3, 6, 4], 7),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0),
    ],
)
def test_maxProfit(prices, expected):
    assert Solution().maxProfit(prices) == expected
