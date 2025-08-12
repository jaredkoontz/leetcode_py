# https://leetcode.com/problems/isomorphic-strings
import pytest


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.isIsomorphic_mine(s, t)

    @staticmethod
    def isIsomorphic_mine(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map, t_map = {}, {}
        for s_char, t_char in zip(s, t):
            if (s_char in s_map and s_map[s_char] != t_char) or (
                    t_char in t_map and t_map[t_char] != s_char
            ):
                return False
            s_map[s_char], t_map[t_char] = t_char, s_char
        return True


@pytest.mark.parametrize(
    "s,t,expected",
    [
        ("badc", "baba", False),
        ("bbbaaaba", "aaabbbba", False),
        ("egg", "add", True),
        ("foo", "bar", False),
        ("paper", "title", True),
    ],
)
def test_isIsomorphic(s, t, expected):
    assert Solution().isIsomorphic(s, t) == expected
