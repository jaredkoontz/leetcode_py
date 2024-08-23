# https://leetcode.com/problems/fraction-addition-and-subtraction/
import fractions
import re

import pytest


class Solution:
    def fractionAddition(self, expression: str) -> str:
        return self.fractionAddition_fraction_mod(expression)

    @staticmethod
    def fractionAddition_fraction_mod(expression: str) -> str:
        curr_fractions = []
        # separate expression into signed numbers
        nums = re.split("/|(?=[-+])", expression)
        nums = list(filter(None, nums))

        for i in range(0, len(nums), 2):
            curr_num = int(nums[i])
            curr_denom = int(nums[i + 1])
            curr_fractions.append(fractions.Fraction(curr_num, curr_denom))
        while len(curr_fractions) > 1:
            frac_1 = curr_fractions.pop()
            frac_2 = curr_fractions.pop()
            curr_fractions.append(frac_1 + frac_2)

        return f"{curr_fractions[0].numerator}/{curr_fractions[0].denominator}"

    @staticmethod
    def fractionAddition_re(expression: str) -> str:
        def _find_gcd(a: int, b: int) -> int:
            if a == 0:
                return b
            return _find_gcd(b % a, a)

        num = 0
        denom = 1

        # separate expression into signed numbers
        nums = re.split("/|(?=[-+])", expression)
        nums = list(filter(None, nums))

        for i in range(0, len(nums), 2):
            curr_num = int(nums[i])
            curr_denom = int(nums[i + 1])

            num = num * curr_denom + curr_num * denom
            denom = denom * curr_denom

        gcd = abs(_find_gcd(num, denom))

        num //= gcd
        denom //= gcd

        return f"{num}/{denom}"

    @staticmethod
    def fractionAddition_string_parse(expression: str) -> str:
        def _find_gcd(a, b):
            if a == 0:
                return b
            return _find_gcd(b % a, a)

        def _collect_digit(index):
            current_num = 0
            while index < len(expression) and expression[index].isdigit():
                value = int(expression[index])
                current_num = current_num * 10 + value
                index += 1

            return current_num, index

        num = 0
        denom = 1

        i = 0
        while i < len(expression):
            is_negative = False

            # check for sign
            if expression[i] == "-" or expression[i] == "+":
                if expression[i] == "-":
                    is_negative = True
                # move to next character
                i += 1

            # build numerator
            curr_num, i = _collect_digit(i)

            if is_negative:
                curr_num *= -1

            # skip divisor
            i += 1

            curr_denom, i = _collect_digit(i)

            # add fractions together using common denominator
            num = num * curr_denom + curr_num * denom
            denom = denom * curr_denom

        gcd = abs(_find_gcd(num, denom))

        # reduce fractions
        num //= gcd
        denom //= gcd

        return f"{num}/{denom}"


@pytest.mark.parametrize(
    "expression,expected",
    [
        ("-1/2+1/2", "0/1"),
        ("-1/2+1/2+1/3", "1/3"),
        ("1/3-1/2", "-1/6"),
    ],
)
def test_fractionAddition(expression, expected):
    assert Solution().fractionAddition(expression) == expected
