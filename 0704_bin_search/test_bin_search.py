# https://leetcode.com/problems/binary-search
import pytest


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return self.search_mine(nums, target)

    @staticmethod
    def search_mine(nums: list[int], target: int) -> int:
        high = len(nums)
        low = 0
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
    ],
)
def test_search(nums: list[int], target: int, expected):
    assert Solution().search(nums, target) == expected
