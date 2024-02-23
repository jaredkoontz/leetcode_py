import pytest


class Solution(object):
    def two_pass_twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        number_map = {}
        length = len(nums)
        for i in range(length):
            number_map[nums[i]] = i

        for i in range(length):
            candidate = nums[i]
            wanted = target - candidate
            if wanted in number_map and number_map[wanted] != i:
                return [i, number_map[wanted]]
        return []

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        number_map = {}

        for i in range(len(nums)):
            candidate = target - nums[i]
            if candidate in number_map:
                return [number_map[candidate],i]
            else:
                number_map[nums[i]] = i

@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_two_sum(nums, target, expected):
    assert Solution().twoSum(nums, target) == expected
