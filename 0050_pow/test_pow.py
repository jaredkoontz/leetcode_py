# https://leetcode.com/problems/powx-n
import pytest


class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.myPow_divide_conquer(x, n)

    @staticmethod
    def myPow_linear(x: float, n: int) -> float:
        negative = False
        ans = x
        if n < 0:
            negative = True
            n *= -1

        for i in range(1, n):
            ans = ans * x
        return 1 / ans if negative else ans

    @staticmethod
    def myPow_divide_conquer(x: float, n: int) -> float:
        def helper(base, exponent):
            if exponent == 0:
                return 1
            if base == 0:
                return 0
            # could be smarter and pass in (x*x) rather than just x and remove the second result = (line27)
            # result = helper(base*base, exponent//2)
            result = helper(base, exponent // 2)
            result = result * result
            return base * result if exponent % 2 else result

        res = helper(x, abs(n))
        return res if n > 0 else 1 / res


@pytest.mark.parametrize(
    "x,n,expected",
    [
        (2.0, 10, 1024.00000),
        (2.10000, 3, 9.261),
        (2.0, -2, 0.25),
    ],
)
def test_pow(x, n, expected):
    assert round(Solution().myPow(x, n), 10) == round(expected, 10)
