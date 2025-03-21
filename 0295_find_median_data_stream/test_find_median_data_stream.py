# https://leetcode.com/problems/find-median-from-data-stream
import bisect
import heapq

import pytest


class MedianFinderHeap:
    def __init__(self):
        # smaller half: return the max; keep q1 equal to or larger than q2
        self.q1 = []
        # larger half: return min
        self.q2 = []

    def addNum(self, num: int) -> None:
        if len(self.q1) == len(self.q2):
            if len(self.q1) == 0 or num <= self.q2[0]:
                heapq.heappush(self.q1, -num)
            else:
                heapq.heappush(self.q2, num)
                min_val = heapq.heappop(self.q2)
                heapq.heappush(self.q1, -min_val)
        else:
            if num > -self.q1[0]:
                heapq.heappush(self.q2, num)
            else:
                heapq.heappush(self.q1, -num)
                max_val = -heapq.heappop(self.q1)
                heapq.heappush(self.q2, max_val)

    def findMedian(self) -> float:
        if len(self.q1) == len(self.q2):
            return (-self.q1[0] + self.q2[0]) / 2.0
        else:
            return -self.q1[0]


class MedianFinderBisect:
    class sortedlist(list):
        """just a list but with an insort (insert into sorted position)"""

        def insort(self, x):
            bisect.insort(self, x)

    def __init__(self):
        self.my_data = self.sortedlist()

    def addNum(self, num: int) -> None:
        self.my_data.insort(num)

    def findMedian(self) -> float:
        length = len(self.my_data)
        if length == 0:
            return 0
        halfway = length // 2
        if length & 1 == 1:
            # odd
            return float(self.my_data[halfway])
        else:
            return (self.my_data[halfway - 1] + self.my_data[halfway]) / 2


MedianFinder = MedianFinderBisect


@pytest.mark.parametrize(
    "operations, init, expected",
    [
        (
            ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
            [[], [1], [2], [], [3], []],
            [None, None, None, 1.5, None, 2.0],
        ),
    ],
)
def test_median_finder(operations, init, expected):
    median_finder = None
    for op, components, curr_val in zip(operations, init, expected):
        if op == "MedianFinder":
            median_finder = MedianFinder()
        elif op == "addNum":
            assert median_finder.addNum(components[0]) == curr_val
        else:
            assert median_finder.findMedian() == curr_val
