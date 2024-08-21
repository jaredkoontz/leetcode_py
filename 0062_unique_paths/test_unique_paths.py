# https://leetcode.com/problems/unique-paths
from functools import cache
from itertools import product

import pytest


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.uniquePaths_space_optimized(m, n)

    @staticmethod
    def uniquePaths_bottom_up(m: int, n: int) -> int:
        # Create a 2D DP table filled with zeros
        dp = [[0] * n for _ in range(m)]

        # Initialize the rightmost column and bottom row to 1
        for i in range(m):
            dp[i][n - 1] = 1
        for j in range(n):
            dp[m - 1][j] = 1

        # Fill in the DP table bottom-up
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        # Return the result stored in the top-left corner
        return dp[0][0]

    @staticmethod
    def uniquePaths_top_down(m: int, n: int) -> int:
        def backtrack(x: int, y: int, my_memo: list[list[int]]) -> int:
            # If we reach the destination (bottom-right corner), return 1
            if x == m - 1 and y == n - 1:
                return 1

            # If we have already computed the result for this cell, return it from the memo table
            if my_memo[x][y] != -1:
                return my_memo[x][y]

            # Calculate the number of unique paths by moving right and down
            right_paths = 0
            down_paths = 0

            # Check if it's valid to move right
            if x < m - 1:
                right_paths = backtrack(x + 1, y, my_memo)

            # Check if it's valid to move down
            if y < n - 1:
                down_paths = backtrack(x, y + 1, my_memo)

            # Store the result in the memo table and return it
            my_memo[x][y] = right_paths + down_paths
            return my_memo[x][y]

        # Create a memoization table to store computed results
        memo = [[-1 for _ in range(n)] for _ in range(m)]

        # Call the recursive function to compute unique paths
        return backtrack(0, 0, memo)

    @staticmethod
    def uniquePaths_space_optimized(m: int, n: int) -> int:
        dp = [[1] * n for _ in range(2)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i & 1][j] = dp[(i - 1) & 1][j] + dp[i & 1][j - 1]
        return dp[(m - 1) & 1][-1]

    @staticmethod
    def uniquePaths_tabulation(m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for i, j in product(range(1, m), range(1, n)):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    @staticmethod
    def uniquePaths_dp(m: int, n: int) -> int:
        @cache
        def backtrack(rows, cols):
            if rows >= m or cols >= n:
                return 0
            if rows == m - 1 and cols == n - 1:
                return 1
            return backtrack(rows + 1, cols) + backtrack(rows, cols + 1)

        return backtrack(0, 0)


@pytest.mark.parametrize(
    "m,n,expected",
    [
        (3, 7, 28),
        (3, 2, 3),
    ],
)
def test_unique_paths(m: int, n: int, expected):
    assert Solution().uniquePaths(m, n) == expected
