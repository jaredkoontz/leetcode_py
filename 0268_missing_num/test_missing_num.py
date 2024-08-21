# https://leetcode.com/problems/missing-number
import pytest


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return self.missingNumber_multiplication(nums)

    @staticmethod
    def missingNumber_multiplication(nums: list[int]) -> int:
        n = len(nums) + 1
        return n * (n - 1) // 2 - sum(nums)

    @staticmethod
    def missingNumber_adding(nums: list[int]) -> int:
        return sum([i for i in range(len(nums) + 1)]) - sum(nums)


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    ],
)
def test_missingNumber(nums, expected):
    assert Solution().missingNumber(nums) == expected
