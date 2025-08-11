import pytest


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        return self.change_memo(amount, coins)

    @staticmethod
    def change_cache(amount: int, coins: list[int]) -> int:
        total = [0]

        def dfs(index, curr_amount, my_coins):
            if index >= len(coins) or curr_amount > amount:
                return
            new_total = curr_amount + coins[index]
            if new_total == amount:
                print(f"found {coins[index]=}\n{my_coins=}")
                total[0] += 1
                return
            else:
                # skip current coin
                dfs(index + 1, curr_amount, my_coins)
                # take the current coin and don't advance
                dfs(index, new_total, my_coins + [coins[index]])
                # take current coin and advance
                dfs(index + 1, new_total, my_coins + [coins[index]])

        dfs(0, 0, [])
        return total[0]

    @staticmethod
    def change_memo(amount: int, coins: list[int]) -> int:
        memo = {}

        def dfs(index, curr_amount):
            if curr_amount == amount:
                return 1
            if index == len(coins) or curr_amount > amount:
                return 0

            wanted_tuple = (index, curr_amount)
            if wanted_tuple in memo:
                return memo[wanted_tuple]

            new_amount = dfs(index, curr_amount + coins[index]) + dfs(
                index + 1, curr_amount
            )
            memo[(index, curr_amount)] = new_amount
            return memo[wanted_tuple]

        return dfs(0, 0)

    @staticmethod
    def change_dp(amount: int, coins: list[int]) -> int:
        dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)
        for i in range(1, amount + 1):
            for j in range(len(coins) - 1, -1, -1):
                dp[i][j] = dp[i][j + 1]
                if i - coins[j] >= 0:
                    dp[i][j] += dp[i - coins[j]][j]

        return dp[amount][0]

    @staticmethod
    def change_dp_optimal(amount: int, coins: list[int]) -> int:
        # essentially the same as above, but we are changing the order.
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]


@pytest.mark.parametrize(
    "amount, coins, expected",
    [
        (5, [1, 2, 5], 4),
        (3, [2], 0),
        (10, [10], 1),
    ],
)
def test_change(amount, coins, expected):
    assert Solution().change(amount, coins) == expected
