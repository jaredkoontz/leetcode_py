import pytest


class Solution:
    def isUgly(self, n: int) -> bool:
        return self.isUgly_stack(n)

    @staticmethod
    def isUgly_rec(n: int) -> bool:
        def _helper(num):
            if num == 0:
                return False
            elif num == 1:
                return True
            elif num % 2 == 0:
                return _helper(num / 2)
            elif num % 3 == 0:
                return _helper(num / 3)
            elif num % 5 == 0:
                return _helper(num / 5)
            else:
                return False

        return _helper(n)

    @staticmethod
    def isUgly_stack(n: int) -> bool:
        def _is_ugly(num):
            divisors = {2, 3, 5}
            stack = [divmod(num, divisor) for divisor in divisors]
            while stack:
                num, remainder = stack.pop()
                if remainder == 0:
                    if num in divisors or num == 1:
                        return True
                    elif num > 1:
                        stack += [divmod(num, divisor) for divisor in divisors]
            return False

        if n == 1:
            return True
        return _is_ugly(n)


@pytest.mark.parametrize(
    "n,expected",
    [
        (2, True),
        (6, True),
        (1, True),
        (14, False),
    ],
)
def test_isUgly(n, expected):
    assert Solution().isUgly(n) == expected
