# https://leetcode.com/problems/different-ways-to-add-parentheses
import pytest

from helpers.testing_helpers import compare_flat_lists


class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        return self.diffWaysToCompute_mine(expression)

    @staticmethod
    def diffWaysToCompute_mine(expression: str) -> list[int]:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
        }

        def backtrack(left, right):
            res = []
            for i in range(left, right + 1):
                op = expression[i]
                if op in operations:
                    nums1 = backtrack(left, i - 1)
                    nums2 = backtrack(i + 1, right)
                    for n1 in nums1:
                        for n2 in nums2:
                            res.append(operations[op](n1, n2))
            if not res:
                res.append(int(expression[left : right + 1]))
            return res

        return backtrack(0, len(expression) - 1)


@pytest.mark.parametrize(
    "expression,expected",
    [
        ("10-1", [9]),
        ("100-1", [99]),
        ("10-20*2", [-30, -20]),
        ("2-1-1", [0, 2]),
        ("2*3-4*5", [-34, -14, -10, -10, 10]),
    ],
)
def test_diffWaysToCompute(expression: str, expected: list[int]) -> None:
    assert compare_flat_lists(Solution().diffWaysToCompute(expression), expected)
