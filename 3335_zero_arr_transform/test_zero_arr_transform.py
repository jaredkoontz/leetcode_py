# https://leetcode.com/problems/zero-array-transformation-i
import itertools

import pytest


class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        return self.isZeroArray_final(nums, queries)

    @staticmethod
    def isZeroArray_diff_arr(nums: list[int], queries: list[list[int]]) -> bool:
        delta_array = [0] * (len(nums) + 1)
        for left, right in queries:
            delta_array[left] += 1
            delta_array[right + 1] -= 1
        operation_counts = []
        current_operations = 0
        for delta in delta_array:
            current_operations += delta
            operation_counts.append(current_operations)
        for operations, target in zip(operation_counts, nums):
            if operations < target:
                return False
        return True

    @staticmethod
    def isZeroArray_final(nums: list[int], queries: list[list[int]]) -> bool:
        diff = [0] * (len(nums) + 1)
        for left, right in queries:
            diff[left] += 1
            diff[right + 1] -= 1
        for num, ops in zip(nums, itertools.accumulate(diff)):
            if num > ops:
                return False
        return True

    @staticmethod
    def isZeroArray_mine(nums: list[int], queries: list[list[int]]) -> bool:
        if max(nums) > len(queries):
            return False

        for curr_range in queries:
            start = curr_range[0]
            end = curr_range[-1]
            for i in range(start, end + 1):
                if nums[i] > 0:
                    nums[i] -= 1
        for n in nums:
            if n > 0:
                return False
        return True


@pytest.mark.parametrize(
    "nums,queries,expected",
    [
        ([4, 3, 2, 1], [[1, 3], [1, 3], [1, 3], [1, 3]], False),
        ([1, 0, 1], [[0, 2]], True),
        ([4, 3, 2, 1], [[1, 3], [0, 2]], False),
    ],
)
def test_isZeroArray(nums, queries, expected):
    try:
        assert Solution().isZeroArray(nums, queries) == expected
    except AssertionError:
        print(nums)
        assert False
