# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves
import heapq

import pytest


class Solution:
    def minDifference(self, nums: list[int]) -> int:
        return self.minDifference_best_heap(nums)

    @staticmethod
    def minDifference_heap(nums: list[int]) -> int:
        heapq.heapify(nums)
        small = heapq.nsmallest(4, nums)
        large = heapq.nlargest(4, nums)
        large.reverse()
        return min(x - y for x, y in zip(large, small))

    @staticmethod
    def minDifference_best_heap(nums: list[int]) -> int:
        if len(nums) <= 4:
            return 0

        smallest = heapq.nsmallest(4, nums)
        largest = heapq.nlargest(4, nums)

        return min(
            largest[0] - smallest[3],
            largest[1] - smallest[2],
            largest[2] - smallest[1],
            largest[3] - smallest[0],
        )

    @staticmethod
    def minDifference_verbose(nums: list[int]) -> int:
        if len(nums) <= 4:
            return 0

        max1, max2, max3, max4 = (
            float("-inf"),
            float("-inf"),
            float("-inf"),
            float("-inf"),
        )
        min1, min2, min3, min4 = (
            float("inf"),
            float("inf"),
            float("inf"),
            float(" inf"),
        )

        for num in nums:
            if num > max1:
                max4, max3, max2, max1 = max3, max2, max1, num
            elif num > max2:
                max4, max3, max2 = max3, max2, num
            elif num > max3:
                max4, max3 = max3, num
            elif num > max4:
                max4 = num

            if num < min1:
                min4, min3, min2, min1 = min3, min2, min1, num
            elif num < min2:
                min4, min3, min2 = min3, min2, num
            elif num < min3:
                min4, min3 = min3, num
            elif num < min4:
                min4 = num

        return min(max1 - min4, max2 - min3, max3 - min2, max4 - min1)

    @staticmethod
    def minDifference_best(nums: list[int]) -> int:
        def shift(a: list[int], start: int) -> None:
            last = a[-1]
            for i in range(len(a) - 1, start, -1):
                a[i] = a[i - 1]
            if len(a) < 4:
                a.append(last)

        if len(nums) <= 4:
            return 0

        min4 = [float("inf")] * 4
        max4 = [float("-inf")] * 4

        for num in nums:
            added = False
            for j in range(4):
                if num < min4[j]:
                    shift(min4, j)
                    min4[j] = num
                    added = True
                    break
            if not added and min4[-1] == float("inf"):
                min4[-1] = num

        for num in nums:
            added = False
            for j in range(4):
                if num > max4[j]:
                    shift(max4, j)
                    max4[j] = num
                    added = True
                    break
            if not added and max4[-1] == float("-inf"):
                max4[-1] = num

        ans = max4[0] - min4[0]
        for i in range(4):
            ans = min(ans, max4[3 - i] - min4[i])

        return ans

    @staticmethod
    def minDifference_sliding_window(nums: list[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        k = len(nums) - 3
        ans = nums[-1] - nums[0]
        for i in range(k - 1, len(nums)):
            ans = min(ans, nums[i] - nums[i - k + 1])
        return ans

    @staticmethod
    def minDifference_greedy(nums: list[int]) -> int:
        if len(nums) <= 3:
            return 0
        nums.sort()
        ans = nums[-1] - nums[0]
        for i in range(4):
            ans = min(ans, nums[-(4 - i)] - nums[i])
        return ans


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([5, 3, 2, 4], 0),
        ([1, 5, 0, 10, 14], 1),
        ([3, 100, 20], 0),
    ],
)
def test_min_diff_between_largest_smallest(nums, expected):
    assert Solution().minDifference(nums) == expected
