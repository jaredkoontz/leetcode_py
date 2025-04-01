# https://leetcode.com/problems/missing-number
import pytest


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return self.missingNumber_xor(nums)

    @staticmethod
    def missingNumber_xor(nums: list[int]) -> int:
        res = len(nums)
        for i in range(res):
            res ^= i
            res ^= nums[i]
        return res

    @staticmethod
    def missingNumber_binsearch(nums: list[int]) -> int:
        nums.sort()
        start, end = 0, len(nums)
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > mid:
                end = mid
            else:
                start = mid + 1
        return start

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
