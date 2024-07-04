import pytest


class Solution:
    def minimumPushes(self, word: str) -> int:
        return self.minimumPushes_mine(word)

    @staticmethod
    def minimumPushes_mine(word: str) -> int:
        keys_availble = 8
        keys_used = 0
        buttons_pressed = 0
        for _ in word:
            buttons_pressed += 1 * ((keys_used // keys_availble) + 1)
            keys_used += 1
        return buttons_pressed


@pytest.mark.parametrize(
    "word,expected",
    [
        ("abcde", 5),
        ("xycdefghij", 12),
    ],
)
def test_minimum_pushes(word, expected):
    assert Solution().minimumPushes(word) == expected
