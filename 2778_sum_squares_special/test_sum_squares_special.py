# https://leetcode.com/problems/sum-of-squares-of-special-elements/
import pytest


class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        return self.sumOfSquares_final(nums)

    @staticmethod
    def sumOfSquares_final(nums: list[int]) -> int:
        special = 0
        n = len(nums)
        for i, num in enumerate(nums, 1):
            if n % i == 0:
                special += num * num
        return special

    @staticmethod
    def sumOfSquares_mine(nums: list[int]) -> int:
        special = []
        n = len(nums)
        for i, num in enumerate(nums, 1):
            if n % i == 0:
                special.append(num * num)
        return sum(special)


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3, 4], 21),
        ([2, 7, 1, 19, 18, 3], 63),
    ],
)
def test_sum_of_squares(nums, expected):
    assert Solution().sumOfSquares(nums) == expected
