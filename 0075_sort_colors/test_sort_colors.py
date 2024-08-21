# https://leetcode.com/problems/sort-colors
import pytest


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        return self.sort_colors_dutch(nums)

    @staticmethod
    def sort_colors_dutch(nums: list[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

    def sortColors_merge_sort(self, nums: list[int]) -> None:
        if len(nums) > 1:
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]
            # split list into halves
            self.sortColors(left)
            self.sortColors(right)

            i = j = k = 0
            # Copy data to temp arrays left[] and right[]
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1

    @staticmethod
    def sortColors_quick_sort(nums: list[int]) -> None:
        # Function to find the partition position
        def partition(array, low, high):
            # Choose the rightmost element as pivot
            pivot = array[high]

            # Pointer for greater element
            i = low - 1

            # Traverse through all elements
            # compare each element with pivot
            for j in range(low, high):
                if array[j] <= pivot:
                    # If element smaller than pivot is found
                    # swap it with the greater element pointed by i
                    i = i + 1

                    # Swapping element at i with element at j
                    (array[i], array[j]) = (array[j], array[i])

            # Swap the pivot element with
            # the greater element specified by i
            (array[i + 1], array[high]) = (array[high], array[i + 1])

            # Return the position from where partition is done
            return i + 1

        # Function to perform quicksort
        def quick_sort(array, low, high):
            if low < high:
                # Find pivot element such that
                # element smaller than pivot are on the left
                # element greater than pivot are on the right
                pi = partition(array, low, high)

                # Recursive call on the left of pivot
                quick_sort(array, low, pi - 1)

                # Recursive call on the right of pivot
                quick_sort(array, pi + 1, high)

        quick_sort(nums, 0, len(nums) - 1)


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 2, 1, 1, 0, 1, 2, 1, 2], [0, 0, 1, 1, 1, 1, 2, 2, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
    ],
)
def test_sort_colors(nums, expected):
    Solution().sortColors(nums)
    assert nums == expected
