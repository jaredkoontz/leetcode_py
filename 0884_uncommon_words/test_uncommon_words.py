# https://leetcode.com/problems/uncommon-words-from-two-sentences
from collections import Counter

import pytest


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        return self.uncommonFromSentences_one_dict(s1, s2)

    @staticmethod
    def uncommonFromSentences_one_dict(s1: str, s2: str) -> list[str]:
        my_dict = Counter(s1.split())
        my_dict.update(s2.split())
        return [word for word, count in my_dict.items() if count == 1]

    @staticmethod
    def uncommonFromSentences_two_dicts(s1: str, s2: str) -> list[str]:
        count1 = Counter(s1.split())
        count2 = Counter(s2.split())

        ret = []

        for word, count in count1.items():
            if count == 1:
                if word not in count2:
                    ret.append(word)
        for word, count in count2.items():
            if count == 1:
                if word not in count1:
                    ret.append(word)
        return ret


@pytest.mark.parametrize(
    "s1,s2,expected",
    [
        ("this apple is sweet", "this apple is sour", ["sweet", "sour"]),
        ("apple apple", "banana", ["banana"]),
    ],
)
def test_uncommonFromSentences(s1, s2, expected):
    assert Solution().uncommonFromSentences(s1, s2) == expected
