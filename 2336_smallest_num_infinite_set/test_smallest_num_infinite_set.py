import heapq

import pytest


class SmallestInfiniteHeap:
    def __init__(self):
        self.heap = [1]
        self.largest = 1
        self.map = dict()
        self.map[1] = True

    def popSmallest(self) -> int:
        sm = heapq.heappop(self.heap)
        self.map[sm] = False
        self.largest += 1
        heapq.heappush(self.heap, self.largest)

        return sm

    def addBack(self, num: int) -> None:
        if num in self.map and not self.map[num]:
            heapq.heappush(self.heap, num)
            self.map[num] = 1


class SmallestInfiniteSet:
    def __init__(self):
        self.cur = 1
        self.s = set()

    def popSmallest(self):
        if self.s:
            res = min(self.s)
            self.s.remove(res)
            return res
        else:
            self.cur += 1
            return self.cur - 1

    def addBack(self, num):
        if self.cur > num:
            self.s.add(num)


@pytest.mark.parametrize(
    "operations,vals,expected",
    [
        (
            [
                "SmallestInfiniteSet",
                "addBack",
                "popSmallest",
                "popSmallest",
                "popSmallest",
                "addBack",
                "popSmallest",
                "popSmallest",
                "popSmallest",
            ],
            [[], [2], [], [], [], [1], [], [], []],
            [None, None, 1, 2, 3, None, 1, 4, 5],
        )
    ],
)
def test_smallest_num_infinite_set(operations, vals, expected):
    s = SmallestInfiniteSet()
    for operation, val, expected in zip(operations, vals, expected):
        # noinspection PyNoneFunctionAssignment
        if operation == "addBack":
            ret = s.addBack(val[0])
        elif operation == "popSmallest":
            ret = s.popSmallest()
        else:
            # constructor
            ret = None
        assert expected == ret
