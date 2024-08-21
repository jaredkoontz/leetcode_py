# https://leetcode.com/problems/happy-number
import pytest


class Solution:
    def isHappy(self, n: int) -> bool:
        return self.isHappy_two_pointer(n)

    @staticmethod
    def isHappy_set(n: int) -> bool:
        def sum_squares(number):
            res = []
            while number > 0:
                number, remainder = divmod(number, 10)
                res.insert(0, remainder)
            return sum([x * x for x in res])

        seen = {n}
        while n != 1:
            n = sum_squares(n)
            if n in seen:
                return False
            seen.add(n)
        return True

    @staticmethod
    def isHappy_two_pointer(n: int) -> bool:
        def squared(num):
            result = 0
            while num > 0:
                last = num % 10
                result += last * last
                num = num // 10
            return result

        slow = squared(n)
        fast = squared(squared(n))

        while slow != fast and fast != 1:
            slow = squared(slow)
            fast = squared(squared(fast))

        return fast == 1


@pytest.mark.parametrize(
    "n,expected",
    [
        (19, True),
        (2, False),
    ],
)
def test_isHappy(n, expected):
    assert Solution().isHappy(n) == expected
