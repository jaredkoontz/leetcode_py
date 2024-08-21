# https://leetcode.com/problems/sort-an-array
import heapq

import pytest


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        return self.sortArray_mine(nums)

    @staticmethod
    def sortArray_mine(nums: list[int]) -> list[int]:
        sorted_arr = []
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
        while heap:
            val = heapq.heappop(heap)
            sorted_arr.append(val)

        return sorted_arr

    @staticmethod
    def bubbleSort(nums):
        n = len(nums)
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

    @staticmethod
    def insertionSort(nums):
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key

    @staticmethod
    def selectionSort(nums):
        for i in range(len(nums)):
            _min = min(nums[i:])
            min_index = nums[i:].index(_min)
            nums[i + min_index] = nums[i]
            nums[i] = _min
        return nums

    @staticmethod
    def quickSort(nums):
        def helper(head, tail):
            if head >= tail:
                return
            left, right = head, tail
            m = (right - left) // 2 + left
            pivot = nums[m]
            while right >= left:
                while right >= left and nums[left] < pivot:
                    left += 1
                while right >= left and nums[right] > pivot:
                    right -= 1
                if right >= left:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
            helper(head, right)
            helper(left, tail)

        helper(0, len(nums) - 1)
        return nums

    def mergeSort(self, nums):
        if len(nums) > 1:
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]

            self.mergeSort(left)
            self.mergeSort(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1

    @staticmethod
    def heapSort(nums):
        def heapify(nums, n, i):
            left = 2 * i + 1
            right = 2 * i + 2

            largest = i
            if left < n and nums[largest] < nums[left]:
                largest = left

            if right < n and nums[largest] < nums[right]:
                largest = right

            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]

                heapify(nums, n, largest)

        n = len(nums)

        for i in range(n // 2 + 1)[::-1]:
            heapify(nums, n, i)

        for i in range(n)[::-1]:
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums, i, 0)


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([5, 2, 3, 1], [1, 2, 3, 5]),
        ([5, 1, 1, 2, 0, 0], [0, 0, 1, 1, 2, 5]),
    ],
)
def test_sort_arr(nums, expected):
    assert Solution().sortArray(nums) == expected
