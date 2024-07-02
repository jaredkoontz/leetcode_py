import math

import pytest


class Solution:
    def reverse(self, x: int) -> int:
        return self.reverse_mine_no_str(x)

    @staticmethod
    def reverse_no_str(x: int) -> int:
        max_int = 2**31 - 1
        min_int = -(2**31)
        reverse = 0

        while x != 0:
            if reverse > max_int / 10 or reverse < min_int / 10:
                return 0
            digit = x % 10 if x > 0 else x % -10
            reverse = reverse * 10 + digit
            x = math.trunc(x / 10)

        return reverse

    @staticmethod
    def reverse_mine_no_str(x: int) -> int:
        max_int = 2**31 - 1
        min_int = -(2**31)
        reverse = 0
        negative = x < 0

        x = -x if negative else x

        while x != 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x //= 10

        if reverse > max_int or reverse < min_int:
            return 0
        return reverse if not negative else -reverse

    @staticmethod
    def reverse_mine(x: int) -> int:
        if not x:
            return 0
        nums = []
        negative = False
        max_int, min_int = 2**31 - 1, -(2**31)

        if x < 0:
            negative = True
            x *= -1
        while x > 0:
            nums.append(x % 10)
            x //= 10
        as_int = int("".join(map(str, nums)))
        if as_int >= max_int or as_int <= min_int:
            return 0
        return as_int if not negative else as_int * -1


@pytest.mark.parametrize(
    "x,expected",
    [
        (0, 0),
        (10, 1),
        (123, 321),
        (-123, -321),
        (120, 21),
        (1_534_236_469, 0),
    ],
)
def test_reverse(x, expected):
    assert Solution().reverse(x) == expected
