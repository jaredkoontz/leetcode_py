import heapq

from helpers.types import CT


class MaxHeap:
    def __init__(self, top_n: int):
        self.h = []
        self.length = top_n
        heapq.heapify(self.h)

    def add(self, element: CT):
        if len(self.h) < self.length:
            heapq.heappush(self.h, element)
        else:
            heapq.heappushpop(self.h, element)

    def getTop(self) -> list[CT]:
        return heapq.nlargest(self.length, self.h)
