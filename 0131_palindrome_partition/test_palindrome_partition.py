from functools import cache

import pytest

from helpers.test_helpers import compare_nested_lists


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


class Solution:
    def partition(self, s: str) -> list[list[str]]:
        return self.partition_cache(s)

    @staticmethod
    def partition_cache(s: str) -> list[list[str]]:
        @cache
        def _partition(i):
            if i == len(s) - 1:
                return [[s[i]]]

            res = []
            for j in range(i + 1, len(s)):
                curr = s[i:j]
                if is_palindrome(curr):
                    temp = _partition(j)
                    for part in temp:
                        res.append([curr] + part)

            if is_palindrome(s[i:]):
                res.append([s[i:]])

            return res

        return _partition(0)

    @staticmethod
    def partition_dfs(s: str) -> list[list[str]]:
        res = []

        def dfs(my_str: str, j: int, path: list[str], result: list[list[str]]) -> None:
            if j == len(my_str):
                result.append(path)
                return
            for i in range(j, len(my_str)):
                if is_palindrome(my_str[j : i + 1]):
                    dfs(my_str, i + 1, path + [my_str[j : i + 1]], result)

        dfs(s, 0, [], res)
        return res


@pytest.mark.parametrize(
    "s,expected",
    [
        ("aab", [["a", "a", "b"], ["aa", "b"]]),
        ("a", [["a"]]),
    ],
)
def test_palindrome_partition(s, expected):
    assert compare_nested_lists(Solution().partition(s), expected)
