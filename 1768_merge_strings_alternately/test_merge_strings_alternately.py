# https://leetcode.com/problems/merge-strings-alternately
from itertools import zip_longest

import pytest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return self.mergeAlternately_zip(word1, word2)

    @staticmethod
    def mergeAlternately_two_pointer(word1: str, word2: str) -> str:
        result = ""
        i1, i2 = 0, 0
        while not ((i1 >= len(word1)) and (i2 >= len(word2))):
            if (i1 >= len(word1)) and (i2 < len(word2)):
                result += word2[i2]
            elif (i1 < len(word1)) and (i2 >= len(word2)):
                result += word1[i1]
            else:
                result += word1[i1] + word2[i2]
            i1 += 1
            i2 += 1
        return result

    @staticmethod
    def mergeAlternately_single_pointer(word1: str, word2: str) -> str:
        i = 0
        res = []
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                res.append(word1[i])
            if i < len(word2):
                res.append(word2[i])
            i += 1
        return "".join(res)

    @staticmethod
    def mergeAlternately_zip(word1: str, word2: str) -> str:
        result = ""
        index = 0
        for char1, char2 in zip(word1, word2):
            result += char1 + char2
            index += 1
        if index < len(word1):
            result += word1[index:]
        if index < len(word2):
            result += word2[index:]
        return result

    @staticmethod
    def mergeAlternately_zip_longest(word1: str, word2: str) -> str:
        result = ""
        for char1, char2 in zip_longest(word1, word2):
            if not char1:
                result += char2
            elif not char2:
                result += char1
            else:
                result += char1 + char2
        return result


@pytest.mark.parametrize(
    "word1,word2,expected",
    [
        ("abc", "pqr", "apbqcr"),
        ("ab", "pqrs", "apbqrs"),
        ("abcd", "pq", "apbqcd"),
    ],
)
def test_merge_alternately(word1, word2, expected):
    assert Solution().mergeAlternately(word1, word2) == expected
