# https://leetcode.com/problems/shuffle-the-array/
import pytest


class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        return self.shuffle_mine(nums, n)

    @staticmethod
    def shuffle_mine(nums: list[int], n: int) -> list[int]:
        ret_arr = []
        for i in range(len(nums) - n):
            ret_arr.append(nums[i])
            ret_arr.append(nums[len(nums) - n + i])

        return ret_arr

    @staticmethod
    def shuffle_two_pointer(nums: list[int], n: int) -> list[int]:
        result = []
        pointer1, pointer2 = 0, n
        for _ in range(n):
            result.append(nums[pointer1])
            result.append(nums[pointer2])
            pointer1 += 1
            pointer2 += 1
        return result

    @staticmethod
    def shuffle_pythonic(nums: list[int], n: int) -> list[int]:
        first_half = nums[:n]
        second_half = nums[n:]
        return [item for pair in zip(first_half, second_half) for item in pair]


@pytest.mark.parametrize(
    "nums,n,expected",
    [
        ([2, 5, 1, 3, 4, 7], 3, []),
        ([1, 2, 3, 4, 4, 3, 2, 1], 4, []),
        ([1, 1, 2, 2], 2, []),
        ([1, 1, 2, 2], 3, []),
    ],
)
def test_max_product_two_elements(nums, n, expected):
    assert Solution().shuffle(nums, n) == expected
