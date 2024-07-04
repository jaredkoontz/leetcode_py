import pytest


class Solution:
    def specialArray(self, nums: list[int]) -> int:
        return self.specialArray_mine(nums)

    @staticmethod
    def specialArray_mine(nums: list[int]) -> int:
        max_val = max(nums)

        for i in range(0, max_val + 1):
            counter = 0
            for num in nums:
                if num >= i:
                    counter += 1
            if counter == i:
                return i

        return -1


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([3, 5], 2),
        ([0, 0], -1),
        ([0, 4, 3, 0, 4], 3),
    ],
)
def test_special_array(nums, expected):
    assert Solution().specialArray(nums) == expected
