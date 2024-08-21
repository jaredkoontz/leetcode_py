import heapq

import pytest


class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        return self.numberGame_heap(nums)

    @staticmethod
    def numberGame_heap(nums: list[int]) -> list[int]:
        ret = []
        heapq.heapify(nums)
        while nums:
            alices_move = heapq.heappop(nums)
            bobs_move = heapq.heappop(nums)
            ret.append(bobs_move)
            ret.append(alices_move)
        return ret

    @staticmethod
    def numberGame_sort(nums: list[int]) -> list[int]:
        ret = []
        nums.sort(reverse=True)
        while nums:
            alices_move = nums.pop()
            bobs_move = nums.pop()
            ret.append(bobs_move)
            ret.append(alices_move)
        return ret


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([5, 4, 2, 3], [3, 2, 5, 4]),
        ([2, 5], [5, 2]),
    ],
)
def test_numberGame(nums, expected):
    assert Solution().numberGame(nums) == expected
