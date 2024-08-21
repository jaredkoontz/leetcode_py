# https://leetcode.com/problems/greatest-common-divisor-of-strings
import math

import pytest


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        return self.gcdOfStrings_len(str1, str2)

    @staticmethod
    def gcdOfStrings_gcd(str1: str, str2: str) -> str:
        if (str1 + str2) == (str2 + str1):
            common_str_length = math.gcd(len(str1), len(str2))
            return str1[:common_str_length]

        return ""

    @staticmethod
    def gcdOfStrings_len(str1: str, str2: str) -> str:
        a = len(str1)
        b = len(str2)
        if str1 + str2 != str2 + str1:
            return ""

        while b != 0:
            a, b = b, a % b

        return str1[:a]

    @staticmethod
    def gcdOfStrings_recursive(str1: str, str2: str) -> str:
        def helper(s1, s2):
            if s1 == s2:
                return s1

            if len(s1) == len(s2):
                return ""

            if (len(s1) < len(s2)) and s2.startswith(s1):
                return helper(s2[len(s1) :], s1)
            elif (len(s2) < len(s1)) and s1.startswith(s2):
                return helper(s1[len(s2) :], s2)
            else:
                return ""

        return helper(str1, str2)


@pytest.mark.parametrize(
    "str1, str2, expected",
    [
        ("AB", "ABC", ""),
        ("ABCABC", "ABC", "ABC"),
        ("ABABAB", "ABAB", "AB"),
        ("LEET", "CODE", ""),
    ],
)
def test_gcdOfStrings(str1, str2, expected):
    assert Solution().gcdOfStrings(str1, str2) == expected
