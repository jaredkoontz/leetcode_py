from collections import Counter

import pytest


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return self.canConstruct_replace(ransomNote, magazine)

    @staticmethod
    def canConstruct_replace(ransomNote: str, magazine: str) -> bool:
        for note_char in ransomNote:
            if note_char not in magazine:
                return False
            magazine = magazine.replace(note_char, " ", 1)
        return True

    @staticmethod
    def canConstruct_readable(ransomNote: str, magazine: str) -> bool:
        d1 = Counter(ransomNote)
        d2 = Counter(magazine)
        for c, v in d1.items():
            if v > d2[c]:
                return False
        return True

    @staticmethod
    def canConstruct_mine(ransomNote: str, magazine: str) -> bool:
        note = Counter(ransomNote)
        for c in magazine:
            in_note = note[c]
            if in_note > 1:
                note[c] -= 1
            else:
                del note[c]
        if not note:
            return True
        return False


@pytest.mark.parametrize(
    "ransomNote, magazine, expected",
    [
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True),
        ("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj", True),
    ],
)
def test_ransom_note(ransomNote, magazine, expected):
    assert Solution().canConstruct(ransomNote, magazine) == expected
