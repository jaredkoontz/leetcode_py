import pytest


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        distinct = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[distinct] = nums[i]
                distinct += 1

        return distinct


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 1, 2], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
        ([], 0),
        ([0, 1, 2, 3], 4),
        ([0, 1, 2, 3, 3, 3, 3], 4),
    ],
)
def test_remove_duplicates(nums, expected):
    assert Solution().removeDuplicates(nums) == expected
