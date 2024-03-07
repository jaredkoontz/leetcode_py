import pytest


class Solution(object):
    def lengthOfLastWordMine(self, s):
        """
        :type s: str
        :rtype: int
        """

        words = s.strip().split(" ")
        return len(words[-1])

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_len = len(s)
        n = 0
        for i in range(str_len, 0, -1):
            if s[i - 1] != " ":
                while i > 0 and s[i - 1] != " ":
                    n += 1
                    i -= 1
                return n
        return n


@pytest.mark.parametrize(
    "target,expected",
    [
        ("Hello World", 5),
        ("a", 1),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6),
    ],
)
def test_last_word_len(target, expected):
    assert Solution().lengthOfLastWord(target) == expected
