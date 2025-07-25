# https://leetcode.com/problems/excel-sheet-column-number
import pytest


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        return self.titleToNumber_mine(columnTitle)

    @staticmethod
    def titleToNumber_mine(columnTitle: str) -> int:
        result = 0
        for i in range(len(columnTitle)):
            c = columnTitle[i]
            result = result * 26 + (ord(c) - ord("A") + 1)
        return result


@pytest.mark.parametrize(
    "columnTitle,expected",
    [
        ("A", 1),
        ("B", 2),
        ("AA", 27),
        ("AB", 28),
        ("ZY", 701),
    ],
)
def test_titleToNumber(columnTitle, expected) -> None:
    assert Solution().titleToNumber(columnTitle) == expected
