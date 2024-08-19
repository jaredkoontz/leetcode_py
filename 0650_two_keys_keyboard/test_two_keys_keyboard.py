import pytest


class Solution:
    def minSteps(self, n: int) -> int:
        return self.minSteps_dp(n)

    @staticmethod
    def minSteps_prime_factors(n: int) -> int:
        ans = 0
        d = 2
        while n > 1:
            # If d is prime factor, keep dividing
            # n by d until is no longer divisible
            while n % d == 0:
                ans += d
                n //= d
            d += 1
        return ans

    @staticmethod
    def minSteps_dp(n: int) -> int:
        dp = [1_000] * (n + 1)
        dp[1] = 0
        for i in range(2, n + 1):
            for j in range(1, (i // 2) + 1):
                # Copy All and Paste (i-j) / j times
                # for all valid j's
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)
        return dp[n]

    @staticmethod
    def minSteps_backtrack_mine(n: int) -> int:
        def dfs(clipboard, screen, num_steps):
            if len(screen) == n:
                return num_steps

            if len(screen) > n:
                return

            # copy and paste
            dfs(clipboard + screen, clipboard + screen, num_steps + 2)
            # paste
            dfs(clipboard, screen + clipboard, num_steps + 1)

        return dfs("", "A", 0)

    @staticmethod
    def minSteps_backtrack_cache(n: int) -> int:
        cache = {}

        def dfs(curr_len, paste_len):
            # base case: reached n A's, don't need more operations
            if curr_len == n:
                return 0
            # base case: exceeded n `A`s, not a valid sequence, so
            # return max value
            if curr_len > n:
                return 1000
            if cache.get((curr_len, paste_len)):
                return cache[(curr_len, paste_len)]

            # copy all + paste
            opt1 = 2 + dfs(curr_len * 2, curr_len)
            # paste
            opt2 = 1 + dfs(curr_len + paste_len, paste_len)
            cache[(curr_len, paste_len)] = min(opt1, opt2)
            return cache[(curr_len, paste_len)]

        if n == 1:
            return 0

        return 1 + dfs(1, 1)

    @staticmethod
    def minSteps_backtrack(n: int) -> int:
        def dfs(curr_len, paste_len):
            # base case: reached n A's, don't need more operations
            if curr_len == n:
                return 0
            # base case: exceeded n `A`s, not a valid sequence, so
            # return max value
            if curr_len > n:
                return 1000

            # copy all + paste
            opt1 = 2 + dfs(curr_len * 2, curr_len)
            # paste
            opt2 = 1 + dfs(curr_len + paste_len, paste_len)

            return min(opt1, opt2)

        if n == 1:
            return 0

        return 1 + dfs(1, 1)


@pytest.mark.parametrize(
    "n,expected",
    [
        (3, 3),
        (199, 199),
        (212, 57),
        (303, 104),
        (1, 0),
    ],
)
def test_minSteps(n, expected):
    assert Solution().minSteps_backtrack(n) == expected
