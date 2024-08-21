# https://leetcode.com/problems/maximum-number-of-balloons
from collections import Counter

import pytest


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return self.maxNumberOfBalloons_map(text)

    @staticmethod
    def maxNumberOfBalloons_map(text: str) -> int:
        count = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        for char in text:
            if char in count:
                count[char] += 1

        count["l"] //= 2
        count["o"] //= 2
        ans = min(count.values())
        return ans

    @staticmethod
    def maxNumberOfBalloons_counter(text: str) -> int:
        counter = Counter(text)

        b_count = counter["b"]
        a_count = counter["a"]
        l_count = counter["l"] // 2
        o_count = counter["o"] // 2
        n_count = counter["n"]

        return min(b_count, a_count, l_count, o_count, n_count)


@pytest.mark.parametrize(
    "text,expected",
    [
        ("nlaebolko", 1),
        ("loonbalxballpoon", 2),
        ("leetcode", 0),
    ],
)
def test_max_num_balloons(text, expected):
    assert Solution().maxNumberOfBalloons(text) == expected
