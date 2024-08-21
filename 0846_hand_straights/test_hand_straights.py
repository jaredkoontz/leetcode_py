# https://leetcode.com/problems/hand-of-straights
import collections
import heapq

import pytest


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        return self.isNStraightHand_queue(hand, groupSize)

    @staticmethod
    def isNStraightHand_heap(hand: list[int], groupSize: int) -> bool:
        hand_counter = collections.defaultdict(int)
        for val in hand:
            hand_counter[val] += 1

        all_keys = list(hand_counter.keys())
        heapq.heapify(all_keys)

        while all_keys:
            cur = all_keys[0]

            for i in range(cur, cur + groupSize):
                if i not in hand_counter:
                    return False
                hand_counter[i] -= 1
                if hand_counter[i] == 0:
                    if i != all_keys[0]:
                        return False
                    heapq.heappop(all_keys)

        return True

    @staticmethod
    def isNStraightHand_queue(hand: list[int], groupSize: int) -> bool:
        c = collections.Counter(hand)
        start = collections.deque()
        last_checked, opened = -1, 0
        for i in sorted(c):
            if opened > c[i] or opened > 0 and i > last_checked + 1:
                return False
            start.append(c[i] - opened)
            last_checked, opened = i, c[i]
            if len(start) == groupSize:
                opened -= start.popleft()
        return opened == 0

    @staticmethod
    def isNStraightHand_mine(hand: list[int], groupSize: int) -> bool:
        c = collections.Counter(hand)
        for i in sorted(c):
            if c[i] > 0:
                for j in range(groupSize)[::-1]:
                    c[i + j] -= c[i]
                    if c[i + j] < 0:
                        return False
        return True


@pytest.mark.parametrize(
    "hand,groupSize,expected",
    [
        ([1, 2, 3, 6, 2, 3, 4, 7, 8], 3, True),
        ([1, 2, 3, 4, 5], 4, False),
        ([8, 10, 12], 3, False),
    ],
)
def test_isNStraightHand(hand, groupSize, expected):
    assert Solution().isNStraightHand(hand, groupSize) == expected
