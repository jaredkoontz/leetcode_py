from collections import Counter

import pytest


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        return self.uniqueOccurrences_counter(arr)

    @staticmethod
    def uniqueOccurrences_counter(arr: list[int]) -> bool:
        counter = Counter(arr)
        return len(set(counter.values())) == len(counter.values())


@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, 2, 1, 1, 3], True),
        ([1, 2], False),
        ([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], True),
    ],
)
def test_uniqueOccurrences(arr, expected):
    assert Solution().uniqueOccurrences(arr) == expected
