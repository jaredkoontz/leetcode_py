# https://leetcode.com/problems/reverse-bits
import pytest


class Solution:
    def reverseBits(self, n: int) -> int:
        return self.reverseBits_mine(n)

    @staticmethod
    def reverseBits_mine(n: int) -> int:
        reverse_n = 0
        # we cannot simply loop while n>0 because we care about the 0s padding the left
        # of the 32bit number

        for _ in range(32):
            right_most = n & 1
            reverse_n <<= 1
            reverse_n += right_most

            n >>= 1
        return reverse_n


@pytest.mark.parametrize(
    "n,expected",
    [
        (43261596, 964_176_192),
        (4294967293, 3_221_225_471),
        (127, 4_261_412_864),
        (0, 0),
    ],
)
def test_reverseBits(n, expected):
    assert Solution().reverseBits(n) == expected
