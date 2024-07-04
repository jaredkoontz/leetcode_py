import pytest


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        return self.searchInsert_mine(nums, target)

    @staticmethod
    def searchInsert_mine(nums: list[int], target: int) -> int:
        if not nums:
            return 0
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        return left + 1 if nums[left] < target else left


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([], 0, 0),
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
    ],
)
def test_searchInsert(nums, target, expected):
    assert Solution().searchInsert(nums, target) == expected
