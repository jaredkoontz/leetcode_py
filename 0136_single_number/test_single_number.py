# https://leetcode.com/problems/single-number
import pytest


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return self.singleNumber_mine(nums)

    @staticmethod
    def singleNumber_mine(nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num

        return result


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
        ([1, 0, 1], 0),
    ],
)
def test_singleNumber(nums, expected):
    assert Solution().singleNumber(nums) == expected
