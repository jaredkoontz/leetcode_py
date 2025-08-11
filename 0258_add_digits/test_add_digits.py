# https://leetcode.com/problems/add-digits
import pytest


class Solution:
    def addDigits(self, num: int) -> int:
        return self.addDigits_rec(num)

    @staticmethod
    def addDigits_rec(num: int) -> int:
        def helper(my_num):
            if my_num < 10:
                return my_num

            digits = []
            while my_num >= 10:
                digits.append(my_num % 10)
                my_num //= 10
            digits.append(my_num)
            return helper(sum(digits))

        return helper(num)


@pytest.mark.parametrize(
    "num,expected",
    [
        # (38, 2),
        # (0, 0),
        (10, 1),
        # (1, 1),
        # (11, 2),
        # (9999, 9),
    ],
)
def test_addDigits(num: int, expected: int):
    assert Solution().addDigits(num) == expected
