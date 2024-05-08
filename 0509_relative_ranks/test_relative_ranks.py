from heapq import heappop
from heapq import heappush

import pytest


class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        return self.findRelativeRanks_heap(score)

    @staticmethod
    def findRelativeRanks_sorting(score: list[int]) -> list[str]:
        # fill out a list with our top 3 winners, followed by the remaining ranks as str
        str_ranks = list(map(str, range(4, len(score) + 1)))
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + str_ranks
        # sort scores
        place = sorted(score, reverse=True)
        # create a dict for mapping the score list value (key) sorted list (val)
        mapping_dict = dict(zip(place, rank))

        return [mapping_dict.get(s) for s in score]

    @staticmethod
    def findRelativeRanks_heap(score: list[int]) -> list[str]:
        max_heap = []
        for i, s in enumerate(score):
            heappush(max_heap, (-s, i))

        res = ["0"] * len(score)
        place = 1
        while max_heap:
            _, position = heappop(max_heap)
            if place == 1:
                rank = "Gold Medal"
            elif place == 2:
                rank = "Silver Medal"
            elif place == 3:
                rank = "Bronze Medal"
            else:
                rank = str(place)

            res[position] = rank
            place += 1

        return res


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([5, 4, 3, 2, 1], ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]),
        ([10, 3, 8, 9, 4], ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]),
    ],
)
def test_findRelativeRanks(l1, expected):
    assert Solution().findRelativeRanks(l1) == expected
