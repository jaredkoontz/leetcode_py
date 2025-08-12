# https://leetcode.com/problems/string-to-integer-atoi
import pytest

MAPPING = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 0,
}

MAX_INT = 2**31 - 1
MIN_INT = -(2**31)


class Solution:
    def myAtoi(self, s: str) -> int:
        return self.myAtoi_mine(s)

    @staticmethod
    def myAtoi_shorter(s: str) -> int:
        length, i, sign, res = len(s), 0, +1, ""

        while i < length and s[i] == " ":
            i = i + 1

        if i < length and s[i] in ("-", "+"):
            sign, i = -1 if s[i] == "-" else +1, i + 1

        while i < length and s[i].isdigit():
            res, i = res + s[i], i + 1

        return max(-(2**31), min(sign * int(res or 0), 2**31 - 1))

    @staticmethod
    def myAtoi_no_int(s: str) -> int:
        def limit(x: int) -> int:
            if x > MAX_INT:
                return MAX_INT
            if x < MIN_INT:
                return MIN_INT
            return x

        s = s.lstrip(" ")
        if not s:
            return 0

        sign = -1 if s[0] == "-" else 1
        if sign != 1 or s[0] == "+":
            s = s[1:]

        res = 0
        for c in s:
            if c not in MAPPING:
                return limit(res * sign)

            res *= 10
            res += MAPPING[c]

        return limit(res * sign)

    @staticmethod
    def myAtoi_mine(s: str) -> int:
        value, state, pos, sign = 0, 0, 0, 1

        if len(s) == 0:
            return 0

        while pos < len(s):
            current_char = s[pos]
            if state == 0:
                if current_char == " ":
                    state = 0
                elif current_char == "+" or current_char == "-":
                    state = 1
                    sign = 1 if current_char == "+" else -1
                elif current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    return 0
            elif state == 1:
                if current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    return 0
            elif state == 2:
                if current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    break
            else:
                return 0
            pos += 1

        value = sign * value
        value = min(value, 2**31 - 1)
        value = max(-(2**31), value)

        return value


@pytest.mark.parametrize(
    "s,expected",
    [
        ("42", 42),
        (" -042", -42),
        ("1337c0d3", 1337),
    ],
)
def test_myAtoi(s, expected):
    assert Solution().myAtoi(s) == expected
