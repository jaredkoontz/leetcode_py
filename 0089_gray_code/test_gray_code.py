# https://leetcode.com/problems/gray-code
import pytest


class Solution:
    def grayCode(self, n: int) -> list[int]:
        return self.grayCode_xor(n)

    @staticmethod
    def grayCode_xor(n: int) -> list[int]:
        result = []
        for i in range(0, 1 << n):
            result.append(i ^ (i >> 1))
        return result


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, [0, 1]),
        (2, [0, 1, 3, 2]),
        (3, [0, 1, 3, 2, 6, 7, 5, 4]),
    ],
)
def test_gray_code(n: int, expected: list[int]):
    assert Solution().grayCode(n) == expected
