# https://leetcode.com/problems/max-consecutive-ones
import pytest


class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        return self.findMaxConsecutiveOnes_mine(nums)

    @staticmethod
    def findMaxConsecutiveOnes_mine(nums: list[int]) -> int:
        max_count = 0
        current_count = 0

        for num in nums:
            if num == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0

        return max_count


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 1, 0, 1, 1, 1], 3),
        ([1, 0, 1, 1, 0, 1], 2),
    ],
)
def test_max_product_two_elements(nums, expected):
    assert Solution().findMaxConsecutiveOnes(nums) == expected
