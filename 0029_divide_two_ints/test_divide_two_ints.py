# https://leetcode.com/problems/divide-two-integers
import pytest


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = self.divide_long(dividend, divisor)
        return min(max(result, -(2**31)), 2**31 - 1)  # Clamp to 32-bit signed int range

    def divide_long(self, dividend: int, divisor: int) -> int:
        # Handle sign
        negative = (dividend < 0) != (divisor < 0)

        # Convert to positive using abs and cast to long
        dividend, divisor = abs(dividend), abs(divisor)

        # Base case
        if dividend < divisor:
            return 0

        # Double the divisor until it's just below the dividend
        sum_ = divisor
        divide = 1
        while (sum_ + sum_) <= dividend:
            sum_ += sum_
            divide += divide

        # Recurse for the remaining part and accumulate a result
        result = divide + self.divide_long(dividend - sum_, divisor)

        return -result if negative else result

    @staticmethod
    def divide2(dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1
        sign = True
        if dividend < 0 < divisor:
            sign = False
        if dividend >= 0 > divisor:
            sign = False
        n = abs(dividend)
        d = abs(divisor)
        Q = 0
        while n >= d:
            power = 0
            while n >= d * (2**power):
                power += 1
            Q += 2 ** (power - 1)
            n = n - d * (2 ** (power - 1))
        if Q > 2**31 - 1 and sign:
            return 2**31 - 1
        if Q < -(2**31) and sign:
            return -(2**31)
        if not sign:
            return Q * -1
        else:
            return Q


@pytest.mark.parametrize(
    "dividend, divisor, result", [(1, 2, 0), (10, 3, 3), (7, -3, -2)]
)
def test_divide(dividend, divisor, result):
    assert Solution().divide(dividend, divisor) == result
