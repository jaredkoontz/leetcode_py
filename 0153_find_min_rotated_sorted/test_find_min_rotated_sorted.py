# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
import pytest


class Solution:
    def findMin(self, nums: list[int]) -> int:
        return self.findMin_mine(nums)

    @staticmethod
    def findMin_mine(nums: list[int]) -> int:
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[start] < nums[end]:
                end = mid
            elif nums[start] < nums[mid]:
                start = mid
            else:
                end = mid
        return min(nums[start], nums[end])


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
    ],
)
def test_findMin(nums, expected):
    assert Solution().findMin(nums) == expected
