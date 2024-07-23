import pytest


class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        return self.findDifference_set_diff(nums1, nums2)

    @staticmethod
    def findDifference_set_diff(nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        return [list(nums1_set - nums2_set), list(nums2_set - nums1_set)]

    @staticmethod
    def findDifference_append(nums1: list[int], nums2: list[int]) -> list[list[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        arr1 = []
        arr2 = []
        for num in s1:
            if num not in s2:
                arr1.append(num)
        for num in s2:
            if num not in s1:
                arr2.append(num)

        return [arr1, arr2]


@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        ([1, 2, 3], [2, 4, 6], [[1, 3], [4, 6]]),
        ([1, 2, 3, 3], [1, 1, 2, 2], [[3], []]),
    ],
)
def test_find_difference(nums1, nums2, expected):
    assert Solution().findDifference(nums1, nums2) == expected
