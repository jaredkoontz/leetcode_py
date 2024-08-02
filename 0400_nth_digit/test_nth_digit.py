import pytest


class Solution:
    def findNthDigit(self, n: int) -> int:
        return self.findNthDigit_mine(n)

    @staticmethod
    def findNthDigit_bin_search(n: int) -> int:
        def count_before(x):
            p = pl = 1
            count = 0
            while p * 10 < x:
                count += 9 * p * pl
                p *= 10
                pl += 1
            count += (x - p) * pl
            return count

        lo = 0
        hi = n
        target = None
        while lo <= hi:
            mid = (lo + hi) // 2
            if count_before(mid) < n:
                target = mid
                lo = mid + 1
            else:
                hi = mid - 1
        assert target
        rem = n - count_before(target)
        return int(str(target)[rem - 1])

    @staticmethod
    def findNthDigit_mine(n: int) -> int:
        start, size = 1, 1
        while n > size:
            n, start = n - size, start + 1
            size = len(str(start))
        return int(str(start)[n - 1])


@pytest.mark.parametrize(
    "n,expected",
    [
        (3, 3),
        (11, 0),
    ],
)
def test_find_nth_digit(n, expected):
    assert Solution().findNthDigit(n) == expected
