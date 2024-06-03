import pytest


class Solution:
    def scoreOfString(self, s: str) -> int:
        return self.scoreOfString_for(s)

    def scoreOfString_for(self, s: str) -> int:
        score = 0
        prev = ord(s[0])
        for i in range(1, len(s)):
            score += abs(ord(s[i]) - prev)
            prev = ord(s[i])
        return score

    def scoreOfString_while(self, s: str) -> int:
        index = 0
        total = 0
        while index < len(s) - 1:
            curr_val = ord(s[index]) - ord("a")
            next_val = ord(s[index + 1]) - ord("a")
            total += abs(curr_val - next_val)
            index += 1
        return total


@pytest.mark.parametrize(
    "s, expected",
    [
        ("hello", 13),
        ("zaz", 50),
    ],
)
def test_scoreOfString(s, expected):
    assert Solution().scoreOfString(s) == expected
