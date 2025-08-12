# https://leetcode.com/problems/excel-sheet-column-title
import pytest


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        return self.convertToTitle_mine(columnNumber)

    @staticmethod
    def convertToTitle_mine(columnNumber: int) -> str:
        tracker = columnNumber
        str_val = ""

        while tracker > 0:
            remainder = (tracker - 1) % 26
            # little ascii magic - basically get the letter from the number. There are a bunch of
            # other ways to do this. you can have an array of a-z with a being 0 if excel cant do ascii magic
            str_val = f"{chr(97 + remainder) + str_val}"
            tracker = (tracker - remainder) // 26

        return str_val.upper()


@pytest.mark.parametrize(
    "given,expected",
    (
            ([0, ""]),
            ([1, "a"]),
            ([25, "y"]),
            ([26, "z"]),
            ([27, "aa"]),
            ([28, "ab"]),
            ([105, "da"]),
            ([701, "zy"]),
            ([702, "zz"]),
            ([703, "aaa"]),
            ([99914, "eqtv"]),
            ([7239, "jrk"]),
    ),
)
def test_int_to_column(given, expected):
    assert Solution().convertToTitle(given) == expected.upper()
