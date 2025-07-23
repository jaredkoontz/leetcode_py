# https://leetcode.com/problems/integer-to-roman
import pytest

MAPPINGS = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
}


class Solution:
    def intToRoman(self, num: int) -> str:
        return self.intToRoman_mine(num)

    @staticmethod
    def intToRoman_mine(num: int) -> str:
        ret_str = ""
        while num > 0:
            for key in MAPPINGS:
                if num >= key:
                    ret_str += MAPPINGS[key]
                    num -= key
                    break
        return ret_str


@pytest.mark.parametrize(
    "num,expected",
    [
        (1, "I"),
        (2, "II"),
        (3, "III"),
        (4, "IV"),
        (5, "V"),
        (6, "VI"),
        (20, "XX"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
    ],
)
def test_integer_to_roman(num, expected):
    assert Solution().intToRoman(num) == expected
