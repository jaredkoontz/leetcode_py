# https://leetcode.com/problems/minimum-moves-to-convert-string
import pytest


class Solution:
    def minimumMoves(self, s: str) -> int:
        return self.minimumMoves_mine(s)

    @staticmethod
    def minimumMoves_mine(s: str) -> int:
        start = 0
        end = len(s)
        min_moves = 0

        while start < end:
            if s[start] == "X":
                next_end = start + 3 if start + 3 < end else end
                chars = s[start:next_end]
                if "X" in chars:
                    min_moves += 1
                start = next_end
            else:
                start += 1
        return min_moves


@pytest.mark.parametrize(
    "s, expected",
    [
        ("OXOX", 1),
        ("XXX", 1),
        ("XXOX", 2),
        ("OOOO", 0),
    ],
)
def test_min_moves(s, expected):
    assert Solution().minimumMoves(s) == expected
