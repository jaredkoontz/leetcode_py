import functools

import pytest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.longestPalindrome_backtrack(s)

    @staticmethod
    def longestPalindrome_backtrack(s: str) -> str:
        longest = ""

        @functools.cache
        def dfs(left, right):
            if left > right:
                return
            if is_palindrome(s[left:right]):
                nonlocal longest
                if len(s[left:right]) > len(longest):
                    longest = s[left:right]
            dfs(left + 1, right)
            dfs(left, right - 1)

        def is_palindrome(substr):
            return substr == substr[::-1]

        dfs(0, len(s))
        return longest


@pytest.mark.parametrize(
    "s,expected",
    [
        ("babad", "aba"),
        ("cbbd", "bb"),
        ("abbcccbbbcaaccbababcbcabca", "cbababc"),
    ],
)
def test_longestPalindrome(s, expected):
    assert Solution().longestPalindrome(s) == expected
