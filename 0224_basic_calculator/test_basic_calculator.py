# https://leetcode.com/problems/basic-calculator
import pytest


class Solution:
    def calculate(self, s: str) -> int:
        return self.calculate_theirs(s)

    @staticmethod
    def calculate_theirs(s: str) -> int:
        """
        1. Take 3 containers:
        num -> to store current num value only
        sign -> to store sign value, initially +1
        res -> to store sum
        When ( comes these containers used for calculate sum of intergers within () brackets.
        --------------------
        2. When c is + or -
        Move num to res, because we need to empty num for next integer value.
        set num = 0
        sign = update with c
        --------------------
        3. When c is '('
        Here, we need num, res, sign to calculate sum of integers within ()
        So, move num and sign to stack => [num, sign]
        Now reset - res = 0, num = 0, sign = 1 (default)
        --------------------
        4. When c is ')' -> 2-(3+4), Here res=3, num=4, sign=1 stack [2, -]
        res +=sign*num -> calculate sum for num first, then pop items from stack, res=7
        res *=stack.pop() - > Pop sign(+ or -) to multiply with res, res = 7*(-1)
        res +=stack.pop() - > Pop integer and add with prev. sum, res = -7 + 2 - 5
        --------------------
        Simple Example: 2 - 3
        Initially res will have 2,i.e. res = 2
        then store '-' in sign. it will be used when 3 comes. ie. sign = -1
        Now 3 comes => res = res + num*sign
        Return statement: res+num*sign => res = 2 + 3(-1) = 2 - 3 = -1
        """
        num = 0
        sign = 1
        res = 0
        stack = []
        for i in range(len(s)):  # iterate till last character
            c = s[i]
            if c.isdigit():  # process if there is digit
                num = num * 10 + int(c)  # for consecutive digits 98 => 9x10 + 8 = 98
            elif c in "-+":  # check for - and +
                res += num * sign
                sign = -1 if c == "-" else 1
                num = 0
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num * sign

    # todo WIP
    @staticmethod
    def calculate_mine(s: str) -> int:
        def _change_to_rpn(with_spaces: str) -> list[int | str]:
            infix = "".join(with_spaces.split())
            operators = {"+", "-", "*", "/", "(", ")", "^"}
            priority = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
            stack = []
            postfix = []
            i = 0
            while i < len(infix):
                character = infix[i]

                if character not in operators:
                    character = ""
                    while i < len(infix) and infix[i] not in operators:
                        character += infix[i]
                        i += 1
                    postfix.append(int(character))
                    i -= 1

                elif character == "(":
                    stack.append(character)
                elif character == ")":
                    while stack and stack[-1] != "(":
                        postfix += stack.pop()
                    stack.pop()
                else:
                    while (
                            stack
                            and stack[-1] != "("
                            and priority[character] <= priority[stack[-1]]
                    ):
                        postfix += stack.pop()
                    stack.append(character)
                i += 1
            while stack:
                postfix += stack.pop()
            return postfix

        def _eval_rpn(rpn: list[int]) -> int:
            stack = []
            for token in rpn:
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
                            stack.append(op2 / op1)
                else:
                    stack.append(int(token))
            return stack.pop()

        return _eval_rpn(_change_to_rpn(s))


@pytest.mark.parametrize(
    "s,expected",
    [
        ("1-(     -2)", 3),
        ("2147483647", 2147483647),
        ("1+1", 2),
        (" 2-1 + 2", 3),
        ("(1+(4+5+2)-3)+(6+8)", 23),
    ],
)
def test_calculate(s, expected):
    assert Solution().calculate(s) == expected
