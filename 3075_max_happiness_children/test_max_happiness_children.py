import pytest

from helpers.heap import MaxHeap


class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        my_heap = MaxHeap(k)
        counter = 0
        turns = 0
        for h in happiness:
            my_heap.add(h)

        for happiest in my_heap.getTop():
            counter += max(happiest - turns, 0)
            turns += 1

        return counter


@pytest.mark.parametrize(
    "l1,k,expected",
    [
        ([12, 1, 42], 3, 53),
        ([2, 98, 45], 1, 98),
        ([1, 2, 3], 2, 4),
        ([1, 1, 1, 1], 2, 1),
        ([2, 3, 4, 5], 1, 5),
        ([2, 3, 5, 5], 2, 9),
    ],
)
def test_max_happiness_sum(l1, k, expected):
    assert Solution().maximumHappinessSum(l1, k) == expected
