import pytest


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return self.lengthOfLastWord_theirs(s)

    @staticmethod
    def lengthOfLastWord_mine(s: str) -> int:
        words = s.strip().split(" ")
        return len(words[-1])

    @staticmethod
    def lengthOfLastWord_theirs(s: str) -> int:
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
