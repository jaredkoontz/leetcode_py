import collections

import pytest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.isAnagram_mine(s, t)

    @staticmethod
    def isAnagram_clean(s: str, t: str) -> bool:
        dictionary = {}

        for letter in s:
            dictionary[letter] = dictionary.get(letter, 0) + 1

        for letter in t:
            dictionary[letter] = dictionary.get(letter, 0) - 1

        for letter in dictionary:
            if dictionary[letter] != 0:
                return False

        return True

    @staticmethod
    def isAnagram_counter(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = collections.Counter(s)
        t_count = collections.Counter(t)

        return s_count == t_count

    @staticmethod
    def isAnagram_mine(s: str, t: str) -> bool:
        letter_map = {}
        for ch in s:
            if ch in letter_map:
                letter_map[ch] += 1
            else:
                letter_map[ch] = 1

        for ch in t:
            if ch not in letter_map:
                return False
            else:
                letter_map[ch] -= 1
                if letter_map[ch] == 0:
                    del letter_map[ch]

        return True if not letter_map else False


@pytest.mark.parametrize(
    "s,t,expected",
    [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("", "", True),
        ("a", "a", True),
        ("ab", "ba", True),
    ],
)
def test_valid_anagram(s, t, expected):
    assert Solution().isAnagram(s, t) == expected
