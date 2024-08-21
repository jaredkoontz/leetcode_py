# https://leetcode.com/problems/determine-if-two-strings-are-close
from collections import Counter

import pytest


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return self.closeStrings_counter(word1, word2)

    @staticmethod
    def closeStrings_counter(word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        word1_counter = Counter(word1)
        word2_counter = Counter(word2)
        if set(word1_counter.keys()) == set(word2_counter.keys()):
            # could also sort the values
            if Counter(word2_counter.values()) == Counter(word1_counter.values()):
                return True
        return False


@pytest.mark.parametrize(
    "word1,word2,expected",
    [
        ("abbzzca", "babzzcz", False),
        ("abc", "bca", True),
        ("a", "aa", False),
        ("cabbba", "abbccc", True),
    ],
)
def test_closeStrings(word1, word2, expected):
    assert Solution().closeStrings(word1, word2) == expected
