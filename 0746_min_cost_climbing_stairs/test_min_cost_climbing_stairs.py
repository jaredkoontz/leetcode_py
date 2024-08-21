# https://leetcode.com/problems/min-cost-climbing-stairs
import functools
from collections import deque

import pytest


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        return self.minCostClimbingStairs_optimal(cost)

    @staticmethod
    def minCostClimbingStairs_optimal(cost: list[int]) -> int:
        n = len(cost)
        if n <= 1:
            return min(cost)
        first = cost[0]
        second = cost[1]
        if n <= 2:
            return min(first, second)
        for i in range(2, n):
            curr = cost[i] + min(first, second)
            first = second
            second = curr
        return min(first, second)

    @staticmethod
    def minCostClimbingStairs_memo_iter_inc(cost: list[int]) -> int:
        n = len(cost)
        if n <= 1:
            return min(cost)
        dp = [0] * n
        for i in range(n):
            if i < 2:
                dp[i] = cost[i]
            else:
                dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        return min(dp[-1], dp[-2])

    @staticmethod
    def minCostClimbingStairs_memo_iter_desc(cost: list[int]) -> int:
        n = len(cost)
        if n <= 1:
            return min(cost)

        cost.append(0)

        for i in range(n - 3, -1, -1):
            min_val = cost[i] + min(cost[i + 1], cost[i + 2])
            cost[i] = min_val
        return min(cost[0], cost[1])

    @staticmethod
    def minCostClimbingStairs_memo_rec(cost: list[int]) -> int:
        cost_len = len(cost)
        dp = [0] * cost_len

        if cost_len <= 1:
            return min(cost)

        def dfs(n):
            if n < 0:
                return 0
            if n == 1 or n == 0:
                return cost[n]
            if dp[n] != 0:
                return dp[n]
            dp[n] = cost[n] + min(dfs(n - 1), dfs(n - 2))
            return dp[n]

        return min(dfs(cost_len - 1), dfs(cost_len - 2))

    @staticmethod
    def minCostClimbingStairs_rec(cost: list[int]) -> int:
        def dfs(n):
            if n < 2:
                return cost[n]
            return cost[n] + min(dfs(n - 1), dfs(n - 2))

        cost_len = len(cost)
        return min(dfs(cost_len - 1), dfs(cost_len - 2))

    @staticmethod
    def minCostClimbingStairs_cache(cost: list[int]) -> int:
        @functools.cache
        def dfs(n):
            if n < 2:
                return cost[n]
            return cost[n] + min(dfs(n - 1), dfs(n - 2))

        cost_len = len(cost)
        return min(dfs(cost_len - 1), dfs(cost_len - 2))

    @staticmethod
    def minCostClimbingStairs_bfs(cost: list[int]) -> int:
        cost_len = len(cost)
        last_positions = (cost_len - 1, cost_len - 2)
        if cost_len <= 1:
            return min(cost)
        start = 0
        total_cost = float("inf")
        queue = deque()
        # tuple of (index, cost)
        queue.append((start, cost[start]))
        queue.append((start + 1, cost[start + 1]))
        while queue:
            # could do dfs with popleft()
            index, cost_at_pos = queue.pop()
            if index in last_positions:
                total_cost = min(total_cost, cost_at_pos)
            if index + 1 < cost_len:
                queue.append((index + 1, cost_at_pos + cost[index + 1]))
            if index + 2 < cost_len:
                queue.append((index + 2, cost_at_pos + cost[index + 2]))
        return total_cost


@pytest.mark.parametrize(
    "cost,expected",
    [
        ([0, 2, 2], 2),
        ([0, 2, 2, 1], 2),
        ([10, 15, 20], 15),
        ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
        ([0, 2], 0),
        ([2], 2),
    ],
)
def test_min_cost_climbing_stairs(cost, expected):
    assert Solution().minCostClimbingStairs(cost) == expected
