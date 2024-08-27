# https://leetcode.com/problems/maximum-number-of-points-with-cost
import pytest


class Solution:
    def maxPoints(self, P: list[list[int]]) -> int:
        return self.maxPoints_leet(P)

    @staticmethod
    def maxPoints_leet(P: list[list[int]]) -> int:
        m, n = len(P), len(P[0])
        if m == 1:
            return max(P[0])
        if n == 1:
            return sum(sum(x) for x in P)

        def left(arr):
            lft = [arr[0]] + [0] * (n - 1)
            for i in range(1, n):
                lft[i] = max(lft[i - 1] - 1, arr[i])
            return lft

        def right(arr):
            rgt = [0] * (n - 1) + [arr[-1]]
            for i in range(n - 2, -1, -1):
                rgt[i] = max(rgt[i + 1] - 1, arr[i])
            return rgt

        pre = P[0]
        for i in range(m - 1):
            lft, rgt, cur = left(pre), right(pre), [0] * n
            for j in range(n):
                cur[j] = P[i + 1][j] + max(lft[j], rgt[j])
            pre = cur[:]

        return max(pre)


@pytest.mark.parametrize(
    "P,expected",
    [
        ([[1, 2, 3], [1, 5, 1], [3, 1, 1]], 9),
        ([[1, 5], [2, 3], [4, 2]], 11),
    ],
)
def test_maxPoints(P, expected):
    assert Solution().maxPoints(P) == expected
