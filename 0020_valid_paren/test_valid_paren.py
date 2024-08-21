# https://leetcode.com/problems/valid-parentheses
import pytest


class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        if not s:
            return False

        bracket_pairs = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for c in s:
            if c in bracket_pairs.keys():
                stack.append(c)
            else:
                try:
                    last = stack.pop()
                except IndexError:
                    return False
                if bracket_pairs.get(last) != c:
                    return False

        return len(stack) == 0


@pytest.mark.parametrize(
    "s,expected",
    [
        ("()", True),
        ("(){}[]", True),
        ("(]", False),
        ("(({}))", True),
        ("(()", False),
        ("", False),
    ],
)
def test_valid_parens(s, expected):
    assert Solution().isValid(s) == expected
