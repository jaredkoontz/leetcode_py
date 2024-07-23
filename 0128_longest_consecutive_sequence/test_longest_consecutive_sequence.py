import pytest


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        return self.longestConsecutive_mine(nums)

    @staticmethod
    def longestConsecutive_mine(nums: list[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums:
                curr_longest = 1
                curr_num = num + 1
                while curr_num in nums:
                    curr_num += 1
                    curr_longest += 1
                longest = max(longest, curr_longest)
        return longest


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
    ],
)
def test_longest_consecutive(nums, expected):
    assert Solution().longestConsecutive(nums) == expected
