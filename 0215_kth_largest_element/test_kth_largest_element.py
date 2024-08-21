# https://leetcode.com/problems/kth-largest-element-in-an-array
import heapq
import random

import pytest


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return self.findKthLargest_mine(nums, k)

    @staticmethod
    def findKthLargest_sort(nums: list[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]

    @staticmethod
    def findKthLargest_heap(nums: list[int], k: int) -> int:
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)

        return min_heap[0]

    @staticmethod
    def findKthLargest_quick_select(nums: list[int], k: int) -> int:
        def partition(nums, left, right, pivot_index):
            pivot = nums[pivot_index]
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            stored_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[i], nums[stored_index] = nums[stored_index], nums[i]
                    stored_index += 1
            nums[right], nums[stored_index] = nums[stored_index], nums[right]
            return stored_index

        left, right = 0, len(nums) - 1
        while True:
            pivot_index = random.randint(left, right)
            new_pivot_index = partition(nums, left, right, pivot_index)
            if new_pivot_index == len(nums) - k:
                return nums[new_pivot_index]
            elif new_pivot_index > len(nums) - k:
                right = new_pivot_index - 1
            else:
                left = new_pivot_index + 1

    @staticmethod
    def findKthLargest_mine(nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[k - 1]


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    ],
)
def test_kth_largest(nums, k, expected):
    assert Solution().findKthLargest(nums, k) == expected
