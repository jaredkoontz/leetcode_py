import pytest


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        return self.pivotIndex_mine(nums)

    @staticmethod
    def pivotIndex_mine(nums: list[int]) -> int:
        left_sum, right_sum = 0, sum(nums)
        for idx, ele in enumerate(nums):
            right_sum -= ele
            if left_sum == right_sum:
                return idx
            left_sum += ele
        return -1


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 7, 3, 6, 5, 6], 3),
        ([1, 2, 3], -1),
        ([2, 1, -1], 0),
    ],
)
def test_pivotIndex(nums, expected):
    assert Solution().pivotIndex(nums) == expected
