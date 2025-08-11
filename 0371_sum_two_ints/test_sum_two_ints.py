import pytest


class Solution:
    """
    the basic intuition is to use bitwise operations to sum the two numbers

    XOR (^) works like an addition without a carry:
    0 + 0 = 0
    0 + 1 = 1
    1 + 0 = 1
    1 + 1 = 0 (carry needed)
    AND (&) finds where both bits are 1 — the positions that need a carry.
    Left shift (<<) moves the carry to the next higher bit position

    """

    def getSum(self, a: int, b: int) -> int:
        return self.getSum_bitwise(a, b)

    @staticmethod
    def getSum_bitwise(a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        # handle negative numbers
        return a if a <= max_int else ~(a ^ mask)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (-1, -2, -3),
        (-1, 2, 1),
        (1, -2, -1),
    ],
)
def test_get_sum(a, b, expected):
    assert Solution().getSum(a, b) == expected
