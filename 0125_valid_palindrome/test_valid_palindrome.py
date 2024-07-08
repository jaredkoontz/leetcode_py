import re

import pytest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        return self.isPalindrome_no_preprocess(s)

    @staticmethod
    def isPalindrome_no_preprocess(s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True

    @staticmethod
    def isPalindrome_preprocess(s: str) -> bool:
        preprocessed = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        if not preprocessed:
            return True
        return preprocessed == preprocessed[::-1]


@pytest.mark.parametrize(
    "s,expected",
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
    ],
)
def test_is_palindrome(s, expected):
    assert Solution().isPalindrome(s) == expected
