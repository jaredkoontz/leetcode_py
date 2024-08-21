# https://leetcode.com/problems/evaluate-reverse-polish-notation
import pytest


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        return self.evalRPN_mine(tokens)

    @staticmethod
    def evalRPN_mine(tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token in ["+", "-", "/", "*"]:
                op1 = stack.pop()
                op2 = stack.pop()
                match token:
                    case "+":
                        stack.append(op2 + op1)
                    case "-":
                        stack.append(op2 - op1)
                    case "*":
                        stack.append(op2 * op1)
                    case "/":
                        stack.append(int(op2 / op1))
            else:
                stack.append(int(token))
        return stack.pop()


@pytest.mark.parametrize(
    "tokens,expected",
    [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ],
)
def test_evalRPN(tokens, expected):
    assert Solution().evalRPN(tokens) == expected
