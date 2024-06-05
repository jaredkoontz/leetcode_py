import heapq
from collections import Counter

import pytest

from helpers.test_helpers import compare_flat_lists


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return self.topKFrequent_heap(nums, k)

    def topKFrequent_bucket(self, nums: list[int], k: int) -> list[int]:
        cnt = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for val, freq in cnt.items():
            buckets[freq].append(val)
        # could also do
        # return list(chain(*buckets[::-1]))[:k]
        res = []
        for bucket in reversed(buckets):
            for val in bucket:
                res.append(val)
                k -= 1
                if k == 0:
                    return res

    def topKFrequent_smart(self, nums: list[int], k: int) -> list[int]:
        cnt = Counter(nums)
        # Counter.most_common method is just a shell over heapq.nlargest, see the
        # https://github.com/python/cpython/blob/1b85f4ec45a5d63188ee3866bd55eb29fdec7fbf/Lib/collections/__init__.py#L575
        return [val for val, _ in cnt.most_common(k)]

    def topKFrequent_heap(self, nums: list[int], k: int) -> list[int]:
        heap = []
        ans = []
        counter = Counter(nums)
        for num, count in counter.items():
            heapq.heappush(heap, (-count, num))

        while len(ans) != k:
            ans.append(heapq.heappop(heap)[1])
        return ans


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
    ],
)
def test_top_k_frequent(nums, k, expected):
    assert compare_flat_lists(Solution().topKFrequent(nums, k), expected)
