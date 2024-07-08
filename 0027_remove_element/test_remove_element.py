import pytest


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        return self.removeElement_mine(nums, val)

    @staticmethod
    def removeElement_mine(nums: list[int], val: int) -> int:
        index = 0
        while index < len(nums):
            if nums[index] == val:
                del nums[index]
                index -= 1
            index += 1
        return len(nums)


@pytest.mark.parametrize(
    "nums,val,expected",
    [
        ([3, 2, 2, 3], 3, 2),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5),
        ([0, 1, 2, 2, 3, 0, 4, 2], 7, 8),
    ],
)
def test_remove_element(nums, val, expected):
    assert Solution().removeElement(nums, val) == expected
