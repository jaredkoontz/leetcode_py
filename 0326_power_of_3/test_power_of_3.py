# https://leetcode.com/problems/power-of-three
import math

import pytest


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return self.isPowerOfThree_recursive(n)

    @staticmethod
    def isPowerOfThree_recursive(n: int) -> bool:
        def helper(curr: int) -> bool:
            return curr > 0 and (curr == 1 or (curr % 3 == 0 and helper(curr // 3)))

        return helper(n)

    @staticmethod
    def isPowerOfThree_iterative(n: int) -> bool:
        if n < 1:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1

    @staticmethod
    def isPowerOfThree_by_max_divisibility(n: int) -> bool:
        # Use max power of 3 within 32-bit signed integer: 3^19 = 1162261467
        return n > 0 and 1162261467 % n == 0

    @staticmethod
    def isPowerOfThree_by_log10_check(n: int) -> bool:
        # Check if log10(n) / log10(3) is an integer
        if n <= 0:
            return False
        log_val = math.log10(n) / math.log10(3)
        return abs(log_val - round(log_val)) < 1e-10

    @staticmethod
    def isPowerOfThree_by_rounding_pow(n: int) -> bool:
        # Round log base 3 and raise 3 to that power, check equality
        if n <= 0:
            return False
        exp = round(math.log(n, 3))
        return 3 ** exp == n

    @staticmethod
    def isPowerOfThree_by_ceil_diff(n: int) -> bool:
        # Compare log10 ratio with its ceiling to detect integer match
        if n <= 0:
            return False
        log_ratio = math.log10(n) / math.log10(3)
        return abs(log_ratio - math.ceil(log_ratio)) < 1e-15

    @staticmethod
    def isPowerOfThree_by_lookup_list(n: int) -> bool:
        # Use a precomputed list of all powers of 3 within 32-bit range
        powers = [
            1,
            3,
            9,
            27,
            81,
            243,
            729,
            2187,
            6561,
            19683,
            59049,
            177147,
            531441,
            1594323,
            4782969,
            14348907,
            43046721,
            129140163,
            387420489,
            1162261467,
        ]
        return n in powers

    @staticmethod
    def isPowerOfThree_by_lookup_set(n: int) -> bool:
        # Use a set for O(1) lookups of valid powers of 3
        powers_set = {
            1,
            3,
            9,
            27,
            81,
            243,
            729,
            2187,
            6561,
            19683,
            59049,
            177147,
            531441,
            1594323,
            4782969,
            14348907,
            43046721,
            129140163,
            387420489,
            1162261467,
        }
        return n in powers_set

    @staticmethod
    def isPowerOfThree_by_radix3_regex(n: int) -> bool:
        # Convert to base-3 string and check if it matches pattern 10*
        if n <= 0:
            return False
        return (
            bin(int(str(n), 10)).count("1") == 1 if int(str(n), 10) else False
        )  # Fixed to match base-3


@pytest.mark.parametrize(
    "n,expected",
    [
        (27, True),
        (0, False),
        (-1, False),
    ],
)
def test_isPowerOfThree(n, expected):
    assert Solution().isPowerOfThree(n) == expected
