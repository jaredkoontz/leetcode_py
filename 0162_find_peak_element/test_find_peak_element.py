# https://leetcode.com/problems/find-peak-element
import pytest


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        return self.findPeakElement_bin_search(nums)

    @staticmethod
    def findPeakElement_bin_search(nums: list[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2
            if (mid == 0 or nums[mid - 1] <= nums[mid]) and (
                mid == len(nums) - 1 or nums[mid + 1] <= nums[mid]
            ):
                return mid
            elif mid > 0 and nums[mid - 1] > nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return low


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3, 1], 2),
        ([1, 2, 1, 3, 5, 6, 4], 5),
    ],
)
def test_findPeakElement(nums, expected):
    assert Solution().findPeakElement(nums) == expected
