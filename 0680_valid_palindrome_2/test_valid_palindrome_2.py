# https://leetcode.com/problems/valid-palindrome-ii
import pytest


class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.validPalindrome_mine(s)

    @staticmethod
    def validPalindrome_mine(s: str) -> bool:
        def verify(string, left, right, deleted):
            while left < right:
                if string[left] != string[right]:
                    if deleted:
                        return False
                    else:
                        return verify(string, left + 1, right, True) or verify(
                            string, left, right - 1, True
                        )
                else:
                    left += 1
                    right -= 1
            return True

        return verify(s, 0, len(s) - 1, False)


@pytest.mark.parametrize(
    "s,expected",
    [
        (
                "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga",
                True,
        ),
        ("deeee", True),
        ("aba", True),
        ("abca", True),
        ("abc", False),
    ],
)
def test_valid_palindrome(s, expected):
    assert Solution().validPalindrome(s) == expected
