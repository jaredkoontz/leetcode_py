import pytest


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        return self.isSubsequence_mine(s, t)

    @staticmethod
    def isSubsequence_mine(s: str, t: str) -> bool:
        s_pointer = 0
        t_pointer = 0
        while t_pointer < len(t) and s_pointer < len(s):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            t_pointer += 1
        return s_pointer == len(s)


@pytest.mark.parametrize(
    "s,t,expected",
    [
        ("abc", "ahbgdc", True),
        ("axc", "ahbgdc", False),
    ],
)
def test_isSubsequence(s, t, expected):
    assert Solution().isSubsequence(s, t) == expected
