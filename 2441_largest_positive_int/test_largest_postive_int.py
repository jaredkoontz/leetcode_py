import pytest


class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        return self.findMaxK_mine(nums)

    @staticmethod
    def findMaxK_mine(nums: list[int]) -> int:
        curr_max = -1
        nums_set = set()
        for k in nums:
            if k < 0:
                positive = k * -1
                if positive in nums_set:
                    curr_max = max(positive, curr_max)
            else:
                negative = k * -1
                if negative in nums_set:
                    curr_max = max(k, curr_max)
            nums_set.add(k)

        return curr_max


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([-1, 2, -3, 3], 3),
        ([-1, 10, 6, 7, -7, 1], 7),
        ([-10, 8, 6, 7, -2, -3], -1),
        ([1, -1], 1),
        ([1, -2], -1),
    ],
)
def test_find_max_k(nums, expected):
    assert Solution().findMaxK(nums) == expected
