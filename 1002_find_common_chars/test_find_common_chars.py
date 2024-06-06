from collections import Counter
from functools import reduce

import pytest

from helpers.test_helpers import compare_flat_lists


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        return self.commonChars_set(words)

    @staticmethod
    def commonChars_set(words: list[str]) -> list[str]:
        if len(words) == 1:
            return words

        result = []
        chars = set(words[0])

        for char in chars:
            frequency = min([word.count(char) for word in words])
            result += frequency * [char]

        return result

    @staticmethod
    def commonChars_counter_magic(words: list[str]) -> list[str]:
        if len(words) <= 1:
            return []

        counters = []
        for word in words:
            counters.append(Counter(word))
        main_counter = counters[0]

        for counter_index in range(1, len(counters)):
            main_counter = main_counter & counters[counter_index]
        return [x for x in main_counter.elements()]

    @staticmethod
    def commonChars_one_line(words: list[str]) -> list[str]:
        return [x for x in reduce(lambda a, b: a & b, map(Counter, words)).elements()]

    def commonChars_mine(self, words: list[str]) -> list[str]:
        char_maps = self._create_char_maps(words)
        common_chars = []

        for letter_index in range(26):
            curr_val = char_maps[0][letter_index]
            min_uses = curr_val

            if curr_val > 0:
                for map_index in range(1, len(words)):
                    min_uses = min(min_uses, char_maps[map_index][letter_index])
                    if char_maps[map_index][letter_index] == 0:
                        break
                else:
                    for i in range(min_uses):
                        common_chars.append(chr(ord("a") + letter_index))

        return common_chars

    @staticmethod
    def _create_char_maps(words: list[str]) -> list[list[int]]:
        char_maps = []
        for word in words:
            char_map = [0] * 26
            for ch in word:
                in_map = ord(ch) - ord("a")
                char_map[in_map] += 1
            char_maps.append(char_map)
        return char_maps


@pytest.mark.parametrize(
    "words,expected",
    [
        (["bella", "label", "roller"], ["e", "l", "l"]),
        (["cool", "lock", "cook"], ["c", "o"]),
    ],
)
def test_find_common_chars(words, expected):
    assert compare_flat_lists(Solution().commonChars(words), expected)
