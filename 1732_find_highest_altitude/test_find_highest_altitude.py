# https://leetcode.com/problems/find-the-highest-altitude
import pytest


class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        return self.largestAltitude_mine(gain)

    @staticmethod
    def largestAltitude_mine(gain: list[int]) -> int:
        current_alt = 0
        highest_alt = current_alt

        for alt in gain:
            current_alt += alt
            highest_alt = max(current_alt, highest_alt)

        return highest_alt


@pytest.mark.parametrize(
    "gain,expected",
    [
        ([-5, 1, 5, 0, -7], 1),
        ([-4, -3, -2, -1, 4, 3, 2], 0),
    ],
)
def test_largestAltitude(gain, expected):
    assert Solution().largestAltitude(gain) == expected
