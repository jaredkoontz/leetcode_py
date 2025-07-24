# https://leetcode.com/problems/count-and-say
import pytest


class Solution:
    def countAndSay(self, n: int) -> str:
        return self.countAndSay_mine(n)

    @staticmethod
    def countAndSay_mine(n: int) -> str:
        curr = "1"

        for _ in range(1, n):
            prev = curr
            curr = ""
            count = 1
            say = prev[0]

            for j in range(1, len(prev)):
                if prev[j] != say:
                    curr += str(count) + say
                    count = 1
                    say = prev[j]
                else:
                    count += 1

            curr += str(count) + say

        return curr


@pytest.mark.parametrize("n, expected", [(4, "1211"), (1, "1")])
def test_countAndSay(n, expected):
    assert Solution().countAndSay(n) == expected
