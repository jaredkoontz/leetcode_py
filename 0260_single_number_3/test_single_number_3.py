import pytest

from helpers.testing_helpers import compare_flat_lists


class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        return self.singleNumber_learning(nums)

    @staticmethod
    def singleNumber_learning(nums: list[int]) -> list[int]:
        first_xor_sec, mask, first = 0, 1, 0
        # get first xor of first and sec
        # Get xor of first and sec
        for num in nums:
            first_xor_sec ^= num

        # Get rightmost set bit in above xor
        while not (first_xor_sec & mask):
            mask <<= 1

        # Get first distinct number
        for num in nums:
            if num & mask:
                first ^= num

        # Return ans
        return [first, first_xor_sec ^ first]

    @staticmethod
    def singleNumber_xor(nums: list[int]) -> list[int]:
        diff = 0
        # XOR of the two numbers we need to find
        for num in nums:
            diff ^= num
        # Get its last set bit
        diff &= -diff

        ret = [0, 0]
        for num in nums:
            if num & diff == 0:
                # the bit is not set
                ret[0] ^= num
            else:
                ret[1] ^= num
        return ret

    @staticmethod
    def singleNumber_sorting(nums: list[int]) -> list[int]:
        nums.sort()
        index = 0
        appears_once = []
        while index < len(nums):
            if index < len(nums) - 1 and nums[index] == nums[index + 1]:
                index += 2
            else:
                appears_once.append(nums[index])
                index += 1

        return appears_once

    @staticmethod
    def singleNumber_extra_space(nums: list[int]) -> list[int]:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                nums_set.remove(num)
            else:
                nums_set.add(num)
        return list(nums_set)


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 1, 3, 2, 5], [3, 5]),
        ([-1, 0], [-1, 0]),
        ([0, 1], [1, 0]),
    ],
)
def test_singleNumber(nums, expected):
    assert compare_flat_lists(Solution().singleNumber(nums), expected)
