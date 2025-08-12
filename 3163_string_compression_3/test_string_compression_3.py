# https://leetcode.com/problems/string-compression-iii
import pytest


class Solution:
    def compressedString(self, word: str) -> str:
        return self.compressedString_mine(word)

    @staticmethod
    def compressedString_mine(word: str) -> str:
        def create_encoding(letter: str, num: int) -> str:
            ret = ""
            while num > 9:
                ret += f"9{letter}"
                num -= 9
            return f"{ret}{num}{letter}"

        cmp = ""
        index = 0
        old_index = 0
        while index < len(word):
            while index < len(word) - 1 and word[index + 1] == word[index]:
                index += 1

            saved_letter = word[index]
            index += 1
            cmp += create_encoding(saved_letter, index - old_index)
            old_index = index
        return cmp


@pytest.mark.parametrize(
    "word,expected",
    [
        ("abcde", "1a1b1c1d1e"),
        ("aaaaaaaaaaaaaabb", "9a5a2b"),
        (
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabb",
                "9a9a9a9a9a9a2a2b",
        ),
    ],
)
def test_compressedString(word, expected):
    assert Solution().compressedString(word) == expected
