# https://leetcode.com/problems/first-bad-version
import pytest

VERSION = 4


def isBadVersion(version: int) -> bool:
    return version == VERSION


class Solution:
    def firstBadVersion(self, n: int) -> int:
        return self.firstBadVersion_bin_search(n)

    @staticmethod
    def firstBadVersion_bin_search(n: int) -> int:
        low, high = 1, n
        while low < high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low


@pytest.mark.parametrize(
    "n, expected",
    [
        ([5, 4]),
    ],
)
def test_firstBadVersion(n, expected):
    assert Solution().firstBadVersion(n) == expected
