# https://leetcode.com/problems/convert-a-number-to-hexadecimal
from collections import deque

import pytest


class Solution:
    def toHex(self, num: int) -> str:
        return self.toHex_mine(num)

    @staticmethod
    def toHex_mine(num: int) -> str:
        char_map = [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
        ]
        res = deque()
        if num == 0:
            return "0"
        while num != 0 and len(res) < 8:
            index = num & 0xF
            res.appendleft(char_map[index])
            num >>= 4
        return "".join(res)


@pytest.mark.parametrize(
    "num,expected",
    [
        (26, "1a"),
        (0, "0"),
        (-1, "ffffffff"),
    ],
)
def test_toHex(num, expected):
    assert Solution().toHex(num) == expected
