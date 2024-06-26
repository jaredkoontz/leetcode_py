from math import sqrt

import pytest


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        return self.judgeSquareSum_sqrt(c)

    @staticmethod
    def judgeSquareSum_sqrt(c: int) -> bool:
        # Since a^2 + b^2 = c => a = sqrt(c - b^2) => a <= sqrt(c).
        for a in range(int(sqrt(c)) + 1):
            b = sqrt(c - a**2)
            if b == int(b):
                return True
        return False

    @staticmethod
    def judgeSquareSum_hash(c: int) -> bool:
        """
        Pre-compute squares number in range [0...c] and add to our set.
        Iterate aSquare in set, if there exists bSquare
            (where bSquare = c - aSquare) in the squareSet then return True.
        """
        my_set = set()
        for a in range(c):
            my_set.add(a**2)
        for val in my_set:
            b_square = c - val
            if b_square in my_set:
                return True
        return False

    @staticmethod
    def judgeSquareSum_two_pointer(c: int) -> bool:
        """
        We can use Two Pointers to search a pair of (left, right), so that left^2 + right^2 = c.
        Start with left = 0, right = int(sqrt(c)).
        while left <= right:
        Let cur = left^2 + right^2.
        If cur == c then we found a perfect match -> return True
        Else if cur < c, we need to increase cur, so left += 1.
        Else we need to decrease cur, so right -= 1.
        """
        left = 0
        right = int(sqrt(c))
        while left <= right:
            cur = left**2 + right**2
            if cur == c:
                return True
            elif cur < c:
                left = left + 1
            else:
                right = right - 1
        return False

    @staticmethod
    def judgeSquareSum_naive(c: int) -> bool:
        if c == 1 or c == 0:
            return True
        for i in range(0, (c // 2) + 1):
            for j in range(0, (c // 2) + 1):
                if i**2 + j**2 == c:
                    return True
        return False


@pytest.mark.parametrize(
    "c,expected",
    [
        (5, True),
        (3, False),
        (4, True),
        (1, True),
        (10000000, True),
    ],
)
def test_sum_square_nums(c, expected):
    assert Solution().judgeSquareSum(c) == expected
