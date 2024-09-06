# https://leetcode.com/problems/sum-of-digits-of-string-after-convert
import pytest


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        return self.getLucky_list_comp(s, k)

    @staticmethod
    def getLucky_list_comp(s: str, k: int) -> int:
        starter = "".join([str(ord(c) - ord("a") + 1) for c in s])
        total = starter
        for _ in range(k):
            total = str(sum(int(c) for c in total))
        return int(total)

    @staticmethod
    def getLucky_mine(s: str, k: int) -> int:
        curr_str = ""
        for c in s:
            curr_str += str(ord(c) - ord("a") + 1)

        for _ in range(k):
            total = 0
            for c in curr_str:
                total += int(c)
            curr_str = str(total)
        return int(curr_str)


@pytest.mark.parametrize(
    "s,k,expected",
    [
        ("iiii", 1, 36),
        ("leetcode", 2, 6),
    ],
)
def test_getLucky(s, k, expected):
    assert Solution().getLucky(s, k) == expected
