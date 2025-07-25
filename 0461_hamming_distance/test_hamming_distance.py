# https://leetcode.com/problems/hamming-distance
import pytest


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return self.hammingDistance_mine(x, y)

    @staticmethod
    def hammingDistance_smarter(x: int, y: int) -> int:
        xor = x ^ y
        distance = 0
        while xor:
            distance += 1
            xor = xor & (xor - 1)
        return distance

    @staticmethod
    def hammingDistance_mine(x: int, y: int) -> int:
        hamming_distance = 0
        while x > 0 or y > 0:
            last_x = x & 1
            last_y = y & 1
            if last_x ^ last_y:
                hamming_distance += 1
            x >>= 1
            y >>= 1
        return hamming_distance


@pytest.mark.parametrize(
    "x,y,expected",
    [
        (1, 1, 0),
        (1, 4, 2),
        (3, 1, 1),
        (3, 0, 2),
    ],
)
def test_hamming_distance(x, y, expected):
    assert Solution().hammingDistance(x, y) == expected
