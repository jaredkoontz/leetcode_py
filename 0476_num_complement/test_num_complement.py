# https://leetcode.com/problems/number-complement
import math

import pytest


class Solution:
    def findComplement(self, num: int) -> int:
        return self.findComplement_xor(num)

    @staticmethod
    def findComplement_naive(num: int) -> int:
        res, ind = 0, 0
        while num > 0:
            # Find single digit from low to high significance
            digit = num % 2
            flipped_digit = 0 if digit == 1 else 1  # Flip digit
            res += flipped_digit << ind
            num //= 2
            ind += 1
        return res

    @staticmethod
    def findComplement_all_masks(num: int) -> int:
        if num == 0:
            return 1
        mask = num
        mask |= mask >> 1
        mask |= mask >> 2
        mask |= mask >> 4
        mask |= mask >> 8
        mask |= mask >> 16
        return num ^ mask

    @staticmethod
    def findComplement_math(num: int) -> int:
        if num == 0:
            return 1
        exponent = int(math.log2(num)) + 1
        flipper = int(math.pow(2, exponent)) - 1
        return num ^ flipper

    @staticmethod
    def findComplement_xor(num: int) -> int:
        mask = 1
        while mask < num:
            mask = (mask << 1) | 1
            # mask = mask*2 + 1
        return mask ^ num
        # return mask - N


@pytest.mark.parametrize(
    "num,expected",
    [
        (5, 2),
        (1, 0),
        (7, 0),
        (13, 2),
        (101, 26),
    ],
)
def test_findComplement(num, expected):
    assert Solution().findComplement(num) == expected
