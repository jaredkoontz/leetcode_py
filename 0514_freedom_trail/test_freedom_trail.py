from functools import cache

import pytest

# https://leetcode.com/problems/freedom-trail/

def steps(i, k, M):
    x = abs(i - k)
    # minimum x steps to rotate the ring from i..k
    return min(x, M - x)


class Solution:

    def findRotateSteps(self, ring: str, key: str) -> int:
        return self.findRotateSteps_bottom_up_dp(ring, key)

    @staticmethod
    def findRotateSteps_naive(ring: str, key: str) -> int:
        M, N = len(ring), len(key)

        def go(i=0, j=0, best=float("inf")):
            if j == N:
                return 0
            for k in range(M):
                if ring[k] == key[j]:
                    # min steps to reach key[j] from each ring[i] is the min steps to reach key[j + 1] from ring[k],
                    # find optimal k via exhaustive search
                    best = min(best, 1 + steps(i, k, M) + go(k, j + 1))
            return best

        # when the ring starts at i = 0
        # (i.e. index 0 is aligned with the 12:00 direction of the ring)
        # return the min steps to construct key[j = 0..N - 1]
        return go()

    @staticmethod
    def findRotateSteps_memo(ring: str, key: str) -> int:
        M, N = len(ring), len(key)

        @cache
        def go(i=0, j=0, best=float("inf")):
            if j == N:
                return 0
            for k in range(M):
                if ring[k] == key[j]:
                    # min steps to reach key[j] from each ring[i] is the min steps to reach key[j + 1] from ring[k],
                    # find optimal k via exhaustive search
                    best = min(best, 1 + steps(i, k, M) + go(k, j + 1))
            return best

        # when the ring starts at i = 0
        # (i.e. index 0 is aligned with the 12:00 direction of the ring)
        # return the min steps to construct key[j = 0..N - 1]
        return go()

    @staticmethod
    def findRotateSteps_bottom_up_dp(ring: str, key: str) -> int:
        M, N = len(ring), len(key)

        dp = [[float("inf") for _ in range(N + 1)] for _ in range(M)]  # memo
        for i in range(M):
            dp[i][N] = 0  # base case
        for j in range(N - 1, -1, -1):  # key j
            for i in range(M):  # cur i
                for k in range(
                    M
                ):  # pre i (optimal k-th value is found as the recursive stack unwinds)
                    if ring[k] == key[j]:
                        # min steps to reach key[j] from each ring[i] is the min steps to reach key[j + 1] from ring[k],
                        # find optimal k via exhaustive search
                        dp[i][j] = min(dp[i][j], 1 + steps(i, k, M) + dp[k][j + 1])
        # when the ring starts at i = 0
        # (i.e. index 0 is aligned with the 12:00 direction of the ring)
        # return the min steps to construct key[j = 0..N - 1]
        return dp[0][0]


@pytest.mark.parametrize(
    "ring, key, expected",
    [
        ("godding", "gd", 4),
        ("godding", "godding", 13),
    ],
)
def test_findRotateSteps(ring, key, expected):
    assert Solution().findRotateSteps(ring, key) == expected
