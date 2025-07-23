import pytest


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return self.isPowerOfTwo_rec(n)

    @staticmethod
    def isPowerOfTwo_shift(n: int) -> bool:
        if n <= 0:
            return False

        w = n - 1
        while w:
            if w & 1:
                w >>= 1
            else:
                return False
        return True

    @staticmethod
    def isPowerOfTwo_oneline(n: int) -> bool:
        if n < 1:
            return False
        return (n & (n - 1)) == 0

    @staticmethod
    def isPowerOfTwo_rec(n: int) -> bool:
        def helper(w):
            if w <= 0:
                return False
            if w == 1:
                return True
            if w & 1:
                return False
            return helper(w >> 1)

        return helper(n)


@pytest.mark.parametrize(
    "n,expected",
    [
        (0, False),
        (1, True),
        (2, True),
        (3, False),
        (16, True),
    ],
)
def test_isPowerOfTwo(n, expected):
    assert Solution().isPowerOfTwo(n) == expected
