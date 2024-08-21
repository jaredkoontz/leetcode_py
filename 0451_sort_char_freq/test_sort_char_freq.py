# https://leetcode.com/problems/sort-characters-by-frequency
import heapq
from collections import Counter

import pytest


class Solution:
    def frequencySort(self, s: str) -> str:
        # assert (
        #     self.frequencySort_dict(s)
        #     == self.frequencySort_list(s)
        #     == self.frequencySort_heap(s)
        # )
        return self.frequencySort_heap(s)

    @staticmethod
    def frequencySort_dict(s: str) -> str:
        # Count frequency of each character
        freq = Counter(s)

        # Sort characters by frequency in descending order
        sorted_characters = sorted(freq.keys(), key=lambda x: (-freq[x], x))

        # Build the result string
        result = "".join([char * freq[char] for char in sorted_characters])

        return result

    @staticmethod
    def frequencySort_list(s: str) -> str:
        output = []
        for letter in set(s):
            count = s.count(letter)
            output.append(letter * count)
            print(output)
        output = sorted(output, key=len, reverse=True)
        return "".join(output)

    @staticmethod
    def frequencySort_heap(s: str) -> str:
        my_map = {}
        my_str = ""
        for char in s:
            my_map[char] = my_map.get(char, 0) + 1
        my_list = []
        for char, freq in my_map.items():
            heapq.heappush(my_list, (-freq, char))
        while my_list:
            freq, char = heapq.heappop(my_list)
            my_str += char * -freq
        return my_str


@pytest.mark.parametrize(
    "s,expected",
    [
        ("tree", "eert"),
        ("cccaaa", "aaaccc"),
        ("Aab", "Aab"),
        ("Aaabb", "aabbA"),
        ("Babb", "bbBa"),
    ],
)
def test_frequency_sort(s, expected):
    assert Solution().frequencySort(s) == expected
