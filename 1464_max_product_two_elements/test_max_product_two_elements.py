import heapq

import pytest


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        return self.maxProduct_mine(nums)

    @staticmethod
    def maxProduct_mine(nums: list[int]) -> int:
        my_heap = []
        for i in range(len(nums)):
            if len(my_heap) > 1:
                heapq.heappushpop(my_heap, nums[i])
            else:
                heapq.heappush(my_heap, nums[i])

        return (my_heap[0] - 1) * (my_heap[1] - 1)


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([3, 4, 5, 2], 12),
        ([1, 5, 4, 5], 16),
        ([3, 7], 12),
        ([1, 4, 6, 2], 15),
        ([2, 7, 5, 2], 24),
        ([7, 19, 5, 2], 108),
        ([-100, -99, 3, 4], 6),
    ],
)
def test_max_product_two_elements(nums, expected):
    assert Solution().maxProduct(nums) == expected
