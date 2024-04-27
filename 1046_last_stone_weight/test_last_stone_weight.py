import bisect
import heapq

import pytest


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        return self.lastStoneWeight_heap(stones)

    @staticmethod
    def lastStoneWeight_heap(stones: list[int]) -> int:
        for i in range(len(stones)):
            # negate to force max heap
            stones[i] *= -1

        heapq.heapify(stones)

        while len(stones) > 1:
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)
            if stone_1:
                heapq.heappush(stones, stone_1 - stone_2)

        return -heapq.heappop(stones) if stones else 0

    @staticmethod
    def lastStoneWeight_insort(stones: list[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            bisect.insort(stones, stones.pop() - stones.pop())
        return stones[0]


@pytest.mark.parametrize(
    "stones, expected",
    [
        ([2, 7, 4, 1, 8, 1], 1),
        ([1], 1),
        ([3], 3),
    ],
)
def test_last_stone_weight(stones, expected):
    assert Solution().lastStoneWeight(stones) == expected
