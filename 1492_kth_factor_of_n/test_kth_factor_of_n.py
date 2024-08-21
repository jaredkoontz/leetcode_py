# https://leetcode.com/problems/the-kth-factor-of-n
import pytest


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        return self.kthFactor_mine(n, k)

    @staticmethod
    def kthFactor_mine(n: int, k: int) -> int:
        counter = 1
        for i in range(1, (n // 2) + 1):
            if n % i == 0:
                counter += 1
                if counter == k + 1:
                    return i
        if counter == k:
            return n
        return -1


@pytest.mark.parametrize(
    "n,k,expected",
    [
        (12, 3, 3),
        (7, 2, 7),
        (4, 4, -1),
        (5, 4, -1),
        (7, 4, -1),
        (4, 2, 2),
    ],
)
def test_kth_factor(n, k, expected):
    assert Solution().kthFactor(n, k) == expected
