# https://leetcode.com/problems/valid-parentheses
import pytest


class Solution:
    def isValid(self, s: str) -> bool:
        return self.isValid_mine(s)

    @staticmethod
    def isValid_mine_old(s: str) -> bool:
        open_parens = ["(", "[", "{"]
        closed_parens = [")", "]", "}"]
        paren_map = {x: open_parens[i] for i, x in enumerate(closed_parens)}
        my_stack = []
        for char in s:
            if char in open_parens:
                my_stack.append(char)
            elif char in closed_parens:
                try:
                    last_seen = my_stack.pop()
                except IndexError:
                    return False

                opening_paren = paren_map.get(char)
                if not opening_paren or opening_paren != last_seen:
                    return False
            else:
                return False
        return len(my_stack) == 0

    @staticmethod
    def isValid_mine(s: str) -> bool:
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
        ("()[]{}", True),
        ("(]", False),
        ("(){}[]", True),
        ("(]", False),
        ("(({}))", True),
        ("(()", False),
        ("", False),
    ],
)
def test_valid_parens(s, expected):
    assert Solution().isValid(s) == expected
