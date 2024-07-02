from collections import Counter

import pytest


class Solution:
    def minimumPushes(self, word: str) -> int:
        keys_availble = 8
        counter = Counter(word)
        keys_used = 0
        buttons_pressed = 0
        for _, val in counter.most_common():
            buttons_pressed += val * ((keys_used // keys_availble) + 1)
            keys_used += 1
        return buttons_pressed


@pytest.mark.parametrize(
    "word,expected",
    [
        ("abcde", 5),
        ("xyzxyzxyzxyz", 12),
        ("aabbccddeeffgghhiiiiii", 24),
    ],
)
def test_minimum_pushes(word, expected):
    assert Solution().minimumPushes(word) == expected
