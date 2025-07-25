# https://leetcode.com/problems/first-missing-positive
import pytest


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        return self.firstMissingPositive_mine(nums)

    @staticmethod
    def firstMissingPositive_mine(nums: list[int]) -> int:
        i = 0
        n = len(nums)

        while i < n:
            correct_pos = nums[i] - 1
            if 1 <= nums[i] <= n and nums[i] != nums[correct_pos]:
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 0], 3),
        ([3, 4, -1, 1], 2),
        ([7, 8, 9, 11, 12], 1),
    ],
)
def test_firstMissingPositive(nums: list[int], expected: int) -> None:
    assert Solution().firstMissingPositive(nums) == expected
