# https://leetcode.com/problems/move-zeroes
import pytest


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        return self.moveZeroes_mine(nums)

    @staticmethod
    def moveZeroes_mine(nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
        ([1], [1]),
        ([2], [2]),
    ],
)
def test_move_zeroes(nums, expected):
    Solution().moveZeroes(nums)
    assert nums == expected
