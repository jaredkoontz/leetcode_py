# https://leetcode.com/problems/generate-parentheses
import pytest


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        return self.generateParenthesis_readable(n)

    @staticmethod
    def generateParenthesis_readable(n: int) -> list[str]:
        res = []

        def recurse(n_open: int, n_close: int, curr: list[str]):
            if n_open == n_close == n:
                res.append("".join(curr))
                return

            if n_open < n:
                recurse(n_open + 1, n_close, curr + ["("])

            if n_open > n_close:
                recurse(n_open, n_close + 1, curr + [")"])

        recurse(0, 0, [])
        return res

    @staticmethod
    def generateParenthesis_dfs(n: int) -> list[str]:
        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return

            if left < n:
                dfs(left + 1, right, s + "(")

            if right < left:
                dfs(left, right + 1, s + ")")

        res = []
        dfs(0, 0, "")
        return res

    @staticmethod
    def generateParenthesis_backtrack(n: int) -> list[str]:
        sol = []
        ans = []

        def backtrack(num_open, num_closed):
            if num_open == num_closed == n:
                ans.append("".join(sol))
                return
            if num_open < n:
                sol.append("(")
                backtrack(num_open + 1, num_closed)
                sol.pop()
            if num_closed < num_open:
                sol.append(")")
                backtrack(num_open, num_closed + 1)
                sol.pop()

        backtrack(0, 0)
        return ans


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, ["()"]),
        (2, ["(())", "()()"]),
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        (
                4,
                [
                    "(((())))",
                    "((()()))",
                    "((())())",
                    "((()))()",
                    "(()(()))",
                    "(()()())",
                    "(()())()",
                    "(())(())",
                    "(())()()",
                    "()((()))",
                    "()(()())",
                    "()(())()",
                    "()()(())",
                    "()()()()",
                ],
        ),
        (
                5,
                [
                    "((((()))))",
                    "(((()())))",
                    "(((())()))",
                    "(((()))())",
                    "(((())))()",
                    "((()(())))",
                    "((()()()))",
                    "((()())())",
                    "((()()))()",
                    "((())(()))",
                    "((())()())",
                    "((())())()",
                    "((()))(())",
                    "((()))()()",
                    "(()((())))",
                    "(()(()()))",
                    "(()(())())",
                    "(()(()))()",
                    "(()()(()))",
                    "(()()()())",
                    "(()()())()",
                    "(()())(())",
                    "(()())()()",
                    "(())((()))",
                    "(())(()())",
                    "(())(())()",
                    "(())()(())",
                    "(())()()()",
                    "()(((())))",
                    "()((()()))",
                    "()((())())",
                    "()((()))()",
                    "()(()(()))",
                    "()(()()())",
                    "()(()())()",
                    "()(())(())",
                    "()(())()()",
                    "()()((()))",
                    "()()(()())",
                    "()()(())()",
                    "()()()(())",
                    "()()()()()",
                ],
        ),
    ],
)
def test_valid_parens(n, expected):
    assert Solution().generateParenthesis(n) == expected
