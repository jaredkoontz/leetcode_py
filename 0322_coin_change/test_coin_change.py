import pytest


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        return self.coinChange_iterative(coins, amount)

    @staticmethod
    def coinChange_iterative(coins: list[int], amount: int) -> int:
        if amount < 1:
            return 0

        dp = [0] + [float("inf")] * amount
        for total in range(1, amount + 1):
            for coin in coins:
                if total >= coin:
                    dp[total] = min(dp[total], dp[total - coin] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1

    @staticmethod
    def coinChange_rec(coins: list[int], amount: int) -> int:
        if amount < 1:
            return 0

        def helper(rem, count):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            if count[rem - 1] != 0:
                return count[rem - 1]

            min_coins = float("inf")
            for coin in coins:
                res = helper(rem - coin, count)
                if 0 <= res < min_coins:
                    min_coins = 1 + res

            count[rem - 1] = -1 if min_coins == float("inf") else min_coins
            return count[rem - 1]

        return helper(amount, [0] * amount)


@pytest.mark.parametrize(
    "coins, amount, expected",
    [
        ([186, 419, 83, 408], 6249, 20),
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
    ],
)
def test_coin_change(coins, amount, expected):
    assert Solution().coinChange(coins, amount) == expected
