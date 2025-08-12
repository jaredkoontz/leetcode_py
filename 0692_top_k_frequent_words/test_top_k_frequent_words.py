# https://leetcode.com/problems/top-k-frequent-words
import heapq

import pytest


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        return self.topKFrequent_mine(words, k)

    @staticmethod
    def topKFrequent_mine(words: list[str], k: int) -> list[str]:
        word_map = {}
        my_heap = []
        for w in words:
            word_map[w] = word_map.get(w, 0) + 1

        for w in word_map:
            heapq.heappush(my_heap, (-word_map.get(w), w))

        return [heapq.heappop(my_heap)[1] for _ in range(k)]


@pytest.mark.parametrize(
    "l1,k,expected",
    [
        (["i", "love", "leetcode", "i", "love", "coding"], 2, ["i", "love"]),
        (
                ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
                4,
                ["the", "is", "sunny", "day"],
        ),
    ],
)
def test_topKFrequent(l1, k, expected):
    assert Solution().topKFrequent(l1, k) == expected
