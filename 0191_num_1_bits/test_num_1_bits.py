import pytest


class Solution:
    def hammingWeight(self, n: int) -> int:
        return self.hammingWeight_mine(n)

    @staticmethod
    def hammingWeight_mine(n: int) -> int:
        count = 0
        while n > 0:
            if n & 1:
                count += 1
            n >>= 1
        return count


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, 1),
        (2, 1),
        (3, 2),
    ],
)
def test_hammingWeight(n, expected):
    assert Solution().hammingWeight(n) == expected
