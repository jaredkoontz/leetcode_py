# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/
import pytest


class Solution:
    def minBitFlips(self, start: int, goal: int) -> tuple[int, int]:
        """
        Basically XOR the two numbers and count the number of set bits.
        But why is that?

        10 -> 7

        7 ->  111
        10 -> 1010

            0111
          ^ 1010
            1101

            so we need to set 3 bits. we can then just count those bits by the following methods
        """
        return self.minBitFlips_mine(start, goal)

    @staticmethod
    def minBitFlips_mine(start: int, goal: int) -> tuple[int, int]:
        def count_set_bits_and(n):
            count = 0
            while n:
                n &= n - 1  # Clears the lowest set bit
                count += 1
            return count

        def count_set_bits_count(n):
            return bin(n).count("1")

        def count_set_bits_shift(n):
            count = 0
            while n:
                if n & 1:
                    count += 1
                n >>= 1
            return count

        options = [count_set_bits_and, count_set_bits_count, count_set_bits_shift]
        return options[2](start ^ goal)


@pytest.mark.parametrize(
    "start,goal,expected",
    [
        (10, 7, 3),
        (3, 4, 3),
    ],
)
def test_minBitFlips(start, goal, expected):
    assert Solution().minBitFlips(start, goal) == expected
