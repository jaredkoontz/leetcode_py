import heapq

import pytest


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val: int) -> int:
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)

        else:
            heapq.heappushpop(self.pool, val)

        return self.pool[0]


@pytest.mark.parametrize(
    "operations, init, expected",
    [
        (
            ["KthLargest", "add", "add", "add", "add", "add"],
            [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]],
            [0, 4, 5, 5, 8, 8],
        ),
    ],
)
def test_kth_smallest(operations, init, expected):
    k = None
    for op, components, curr_k in zip(operations, init, expected):
        if op == "KthLargest":
            k = KthLargest(components[0], components[1])
        else:
            assert k.add(components[0]) == curr_k
