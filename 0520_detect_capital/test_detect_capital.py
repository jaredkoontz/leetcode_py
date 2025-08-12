# https://leetcode.com/problems/detect-capital
import pytest


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return self.detectCapitalUse_iter(word)

    @staticmethod
    def detectCapitalUse_iter(word: str) -> bool:
        def is_capital(letter: str):
            return ord("A") <= ord(letter) <= ord("Z")

        index = 0
        small = 0

        for i, let in enumerate(word):
            if is_capital(let) and small == 0:
                index = i
            elif word[i].islower() and index == 0:
                small = 1
            else:
                return False

        return True

    @staticmethod
    def detectCapitalUse_python(word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()


@pytest.mark.parametrize(
    "word,expected",
    [
        ("USA", True),
        ("FlaG", False),
        ("leetcode", True),
        ("G", True),
        ("Aa", True),
        ("AAa", False),
    ],
)
def test_detectCapitalUse(word, expected):
    assert Solution().detectCapitalUse(word) == expected
