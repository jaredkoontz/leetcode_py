import collections

import pytest

from helpers.test_helpers import compare_flat_lists


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return self.intersect_two_pointer(nums1, nums2)

    @staticmethod
    def intersect_two_pointer(nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()

        ans = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ans.append(nums1[i])
                i += 1
                j += 1
        return ans

    @staticmethod
    def intersect_cache(nums1: list[int], nums2: list[int]) -> list[int]:
        counter1 = collections.Counter(nums1)
        counter2 = collections.Counter(nums2)

        ret = []

        for key in counter1:
            num_of_elements = min(counter1[key], counter2[key])
            for i in range(num_of_elements):
                ret.append(key)

        return ret


@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        ([1, 2, 2, 1], [2, 2], [2, 2]),
        ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9]),
    ],
)
def test_intersect(nums1, nums2, expected):
    assert compare_flat_lists(Solution().intersect(nums1, nums2), expected)
