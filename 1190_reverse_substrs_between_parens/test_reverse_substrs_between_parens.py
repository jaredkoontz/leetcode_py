import pytest


class Solution:
    def reverseParentheses(self, s: str) -> str:
        return self.reverseParentheses_stack(s)

    @staticmethod
    def reverseParentheses_stack(s: str) -> str:
        stack = []
        curr_word = ""
        for x in s:
            if x == "(":
                stack.append(curr_word)
                curr_word = ""
            elif x == ")":
                curr_word = curr_word[::-1]
                curr_word = stack.pop() + curr_word
            else:
                curr_word += x
        return curr_word

    @staticmethod
    def reverseParentheses_brute(s: str) -> str:
        res = [""]
        for c in s:
            if c == "(":
                res.append("")
            elif c == ")":
                res[len(res) - 2] += res.pop()[::-1]
            else:
                res[-1] += c
        return "".join(res)

    @staticmethod
    def reverseParentheses_wormhole(s: str) -> str:
        opened = []
        pair = {}
        for index, c in enumerate(s):
            if c == "(":
                opened.append(index)
            if c == ")":
                j = opened.pop()
                pair[index], pair[j] = j, index
        res = []
        index, direction = 0, 1
        while index < len(s):
            if s[index] in "()":
                index = pair[index]
                # turn around
                direction = -direction
            else:
                res.append(s[index])
            index += direction
        return "".join(res)


@pytest.mark.parametrize(
    "s,expected",
    [
        ("(abcd)", "dcba"),
        ("(u(love)i)", "iloveu"),
        ("(ed(et(oc))el)", "leetcode"),
    ],
)
def test_reverseParentheses(s, expected):
    assert Solution().reverseParentheses(s) == expected
