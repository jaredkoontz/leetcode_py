# https://leetcode.com/problems/minimum-increment-to-make-array-unique
import collections

import pytest


class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        return self.minIncrementForUnique_mine(nums)

    @staticmethod
    def minIncrementForUnique_mine(nums: list[int]) -> int:
        frequencies = collections.Counter(nums)
        res = 0
        for num in list(sorted(frequencies.keys())):
            curr = num
            while frequencies[curr] >= 2:
                res += frequencies[curr] - 1
                frequencies[curr + 1] += frequencies[curr] - 1
                frequencies[curr] = 1
                curr += 1
        return res

    @staticmethod
    def minIncrementForUnique_union(nums: list[int]) -> int:
        root = {}

        def find(x):
            root[x] = find(root[x] + 1) if x in root else x
            return root[x]

        return sum(find(a) - a for a in nums)

    @staticmethod
    def minIncrementForUnique_collections(nums: list[int]) -> int:
        c = collections.Counter(nums)
        res = need = 0
        for x in sorted(c):
            res += c[x] * max(need - x, 0) + c[x] * (c[x] - 1) / 2
            need = max(need, x) + c[x]
        return res

    @staticmethod
    def minIncrementForUnique_sort(nums: list[int]) -> int:
        res = need = 0
        for i in sorted(nums):
            res += max(need - i, 0)
            need = max(need + 1, i + 1)
        return res

    @staticmethod
    def minIncrementForUnique_naive(nums: list[int]) -> int:
        used_vals = set()
        index = 0
        changes = 0
        while index < len(nums):
            if nums[index] not in used_vals:
                used_vals.add(nums[index])
            else:
                while nums[index] in used_vals:
                    nums[index] += 1
                    changes += 1
                used_vals.add(nums[index])
            index += 1
        return changes


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 2], 1),
        ([3, 2, 1, 2, 1, 7], 6),
    ],
)
def test_min_increment_make_arr_unique(nums, expected):
    assert Solution().minIncrementForUnique(nums) == expected
