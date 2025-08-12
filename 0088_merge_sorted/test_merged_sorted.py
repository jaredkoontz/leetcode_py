# https://leetcode.com/problems/merge-sorted-array
import pytest


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        return self.merge_ascending(nums1, m, nums2, n)

    @staticmethod
    def merge_ascending(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if n == 0:
            return
        pointer1 = 0
        pointer2 = 0
        for i in range(len(nums1)):
            if nums1[pointer1] < nums2[pointer2] and pointer1 < m:
                pointer1 += 1
            else:
                nums1[pointer1 + 1:] = nums1[pointer1:-1]
                nums1[pointer1] = nums2[pointer2]
                pointer2 += 1
                pointer1 += 1
                m += 1
            if pointer2 >= n:
                break

    @staticmethod
    def merge_sort(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        for j in range(n):
            nums1[m + j] = nums2[j]
        nums1.sort()

    @staticmethod
    def merge_two_pointer(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1_pointer, nums2_pointer, end = m - 1, n - 1, m + n - 1
        while nums2_pointer >= 0:
            if nums1_pointer >= 0 and nums1[nums1_pointer] > nums2[nums2_pointer]:
                nums1[end] = nums1[nums1_pointer]
                nums1_pointer -= 1
            else:
                nums1[end] = nums2[nums2_pointer]
                nums2_pointer -= 1
            end -= 1


@pytest.mark.parametrize(
    "nums1,m,nums2,n,expected",
    [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
    ],
)
def test_merge(nums1, nums2, m, n, expected):
    sol = Solution()
    sol.merge(nums1, m, nums2, n)
    assert nums1 == expected
