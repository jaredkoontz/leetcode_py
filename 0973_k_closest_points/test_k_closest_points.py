# https://leetcode.com/problems/k-closest-points-to-origin
import heapq
import math

import pytest


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        return self.kClosest_heap(points, k)

    @staticmethod
    def kClosest_heap(points: list[list[int]], k: int) -> list[list[int]]:
        ret = []

        my_heap = []
        for point_pair in points:
            x, y = point_pair[0], point_pair[1]
            euc_distance = math.sqrt(x * x + y * y)
            # can restrict size of k
            heapq.heappush(my_heap, (euc_distance, [x, y]))
        print(my_heap)

        for i in range(k):
            euc_distance, point_pair = heapq.heappop(my_heap)
            ret.append(point_pair)

        return ret


@pytest.mark.parametrize(
    "points,k,expected",
    [
        ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
        ([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]),
    ],
)
def test_kClosest(points, k, expected):
    assert Solution().kClosest(points, k) == expected
