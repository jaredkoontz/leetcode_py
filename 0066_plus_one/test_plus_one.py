# https://leetcode.com/problems/plus-one
import pytest


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        return self.plusOne_theirs(digits)

    @staticmethod
    def plusOneMine(digits: list[int]) -> list[int]:
        if digits:
            last_val = -1
            if digits[-1] == 9:
                while digits[last_val] == 9:
                    digits[last_val] = 0
                    last_val -= 1
                    if len(digits) < abs(last_val):
                        break
                if len(digits) < abs(last_val):
                    digits.append(0)
            digits[last_val] += 1
        return digits

    @staticmethod
    def plusOne_theirs(digits: list[int]) -> list[int]:
        if digits:
            for i in reversed(range(len(digits))):
                if digits[i] < 9:
                    digits[i] += 1
                    return digits
                digits[i] = 0

            digits[0] = 1
            digits.append(0)

        return digits


@pytest.mark.parametrize(
    "given,expected",
    [
        ([], []),
        ([8, 9, 9, 9], [9, 0, 0, 0]),
        ([0], [1]),
        ([9], [1, 0]),
        ([9, 9], [1, 0, 0]),
        ([9, 9, 9], [1, 0, 0, 0]),
        ([9, 9, 9, 9], [1, 0, 0, 0, 0]),
        ([1, 2, 3], [1, 2, 4]),
        ([4, 3, 2, 1], [4, 3, 2, 2]),
    ],
)
def test_plus_one(given, expected):
    assert Solution().plusOne(given) == expected
