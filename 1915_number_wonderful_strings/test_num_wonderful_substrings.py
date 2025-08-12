# https://leetcode.com/problems/number-of-wonderful-substrings
import pytest


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        return self.wonderfulSubstrings_mine(word)

    @staticmethod
    def wonderfulSubstrings_mine(word: str) -> int:
        # bitmask is 10 bits, each bit 2 values, 2^10 = 1024
        count = [0] * 1024
        # 0 means empty string, which has all its bits 0
        count[0] = 1
        ans = 0
        cur = 0

        for c in word:
            cur ^= 1 << (ord(c) - ord("a"))
            ans += count[cur]
            # flip each bit and see if there's matching prefix
            for i in range(10):
                temp = cur ^ (1 << i)
                ans += count[temp]
            count[cur] += 1
        return ans


@pytest.mark.parametrize(
    "word,expected,word_list",
    [
        (
            "aba",
            4,
            [
                "a",
                "b",
                "a",
                "aba",
            ],
        ),
        ("aabb", 9, ["a", "aa", "aab", "aabb", "a", "abb", "b", "bb", "b"]),
    ],
)
def test_wonderful_substrings(word, expected, word_list):
    assert Solution().wonderfulSubstrings(word) == expected
