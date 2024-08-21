# https://leetcode.com/problems/sort-array-by-increasing-frequency
import heapq
from collections import Counter

import pytest


class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        return self.frequencySort_heap(nums)

    @staticmethod
    def frequencySort_single_in_place(nums: list[int]) -> list[int]:
        counter = Counter(nums)
        return sorted(nums, key=lambda x: (counter[x], -x))

    @staticmethod
    def frequencySort_heap(nums: list[int]) -> list[int]:
        d = Counter(nums)
        heap = []
        arr = []
        for count, item in d.items():
            heapq.heappush(heap, [item, -count])
        while heap:
            item, count = heapq.heappop(heap)
            for _ in range(item):
                arr.append(count * (-1))
        return arr

    @staticmethod
    def frequencySort_double_sort(nums: list[int]) -> list[int]:
        counter = Counter(nums).most_common()
        counter.sort(key=lambda x: x[0], reverse=True)
        counter.sort(key=lambda x: x[1])

        ret = []
        for a, b in counter:
            ret += [a] * b

        return ret

    @staticmethod
    def frequencySort_single_sort(nums: list[int]) -> list[int]:
        counter = Counter(nums).most_common()
        counter.sort(key=lambda x: (x[1], -x[0]))

        ret = []
        for a, b in counter:
            ret += [a] * b

        return ret


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 1, 2, 2, 2, 3], [3, 1, 1, 2, 2, 2]),
        ([2, 3, 1, 3, 2], [1, 3, 3, 2, 2]),
        ([-1, 1, -6, 4, 5, -6, 1, 4, 1], [5, -1, 4, 4, -6, -6, 1, 1, 1]),
    ],
)
def test_sort_by_inc_freq(nums, expected):
    assert Solution().frequencySort(nums) == expected
