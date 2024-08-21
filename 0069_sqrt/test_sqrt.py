# https://leetcode.com/problems/sqrtx
import pytest


class Solution:
    def mySqrt(self, x: int) -> int:
        return self.mySqrt_bin(x)

    @staticmethod
    def mySqrt_linear(x: int) -> int:
        number = 1
        square = 1
        while square < x:
            number += 1
            square = number * number
        if square > x:
            number -= 1
        return number

    @staticmethod
    def mySqrt_bin(x: int) -> int:
        low, high = 0, x
        result = 0
        while low <= high:
            # this could overflow
            # mid = (low + high)
            # so we cut down our search space
            mid = low + ((high - low) // 2)
            candidate = mid * mid
            if candidate > x:
                high = mid - 1
            elif candidate < x:
                low = mid + 1
                result = mid
            else:
                return mid
        return result


@pytest.mark.parametrize(
    "x,expected",
    [
        (4, 2),
        (8, 2),
        (9, 3),
        (16, 4),
        (27, 5),
        (100, 10),
        (114, 10),
        (69, 8),
        (420, 20),
        (1000123, 1000),
    ],
)
def test_sqrt(x, expected):
    assert Solution().mySqrt(x) == expected
