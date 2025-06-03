# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference
import pytest


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return self.differenceOfSums_mine(n, m)

    @staticmethod
    def differenceOfSums_mine(n: int, m: int) -> int:
        all_nums1 = 0
        all_nums2 = 0
        for x in range(1, n + 1):
            if x % m != 0:
                all_nums1 += x
            else:
                all_nums2 += x

        return all_nums1 - all_nums2


@pytest.mark.parametrize(
    "n,m,expected",
    [
        (10, 3, 19),
        (5, 6, 15),
        (5, 1, -15),
    ],
)
def test_differenceOfSums(n, m, expected):
    assert Solution().differenceOfSums(n, m) == expected
