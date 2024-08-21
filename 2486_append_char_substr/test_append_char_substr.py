# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence
import pytest


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        return self.appendCharacters_iter_sum(s, t)

    @staticmethod
    def appendCharacters_iter_sum(s: str, t: str) -> int:
        s_iter = iter(s)
        matching_count = sum(1 for char in t if char in s_iter)
        return len(t) - matching_count

    @staticmethod
    def appendCharacters_two_pointer(s: str, t: str) -> int:
        s_index = 0
        t_index = 0
        s_length = len(s)
        t_length = len(t)
        while s_length > s_index and t_length > t_index:
            if s[s_index] == t[t_index]:
                t_index += 1
            s_index += 1

        return t_length - t_index


@pytest.mark.parametrize(
    "s,t,expected",
    [
        ("coaching", "coding", 4),
        ("abcde", "a", 0),
        ("z", "abcde", 5),
        ("lbg", "g", 0),
    ],
)
def test_append_characters(s, t, expected):
    assert Solution().appendCharacters(s, t) == expected
