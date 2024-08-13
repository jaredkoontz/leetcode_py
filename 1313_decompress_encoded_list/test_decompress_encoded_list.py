import pytest


class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        return self.decompressRLElist_mine(nums)

    @staticmethod
    def decompressRLElist_mine(nums: list[int]) -> list[int]:
        new_arr = []
        pos = 0
        while pos < len(nums):
            freq = nums[pos]
            pos += 1
            val = nums[pos]
            new_arr += [val] * freq
            pos += 1

        return new_arr


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3, 4], [2, 4, 4, 4]),
        ([1, 1, 2, 3], [1, 3, 3]),
    ],
)
def test_decompressRLElist(nums, expected):
    assert Solution().decompressRLElist(nums) == expected
