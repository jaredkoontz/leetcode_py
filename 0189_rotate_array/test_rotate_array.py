# https://leetcode.com/problems/rotate-array
import pytest


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        return self.rotate_python(nums, k)

    @staticmethod
    def rotate_python(nums: list[int], k: int) -> None:
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    @staticmethod
    def rotate_reverse(nums: list[int], k: int) -> None:
        def reverse(left=0, right=len(nums) - 1):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1

        k = k % len(nums)

        reverse()
        reverse(right=k - 1)
        reverse(left=k)

    @staticmethod
    def rotate_verbose(nums: list[int], k: int) -> None:
        k = k % len(nums)
        left, right = 0, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        left, right = 0, k - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        left, right = k, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    @staticmethod
    def rotate_naive(nums: list[int], k: int) -> None:
        length = len(nums)
        new_array = [0] * length
        for i in range(length):
            new_index = (i + k) % length
            new_array[new_index] = nums[i]
        for i in range(length):
            nums[i] = new_array[i]


@pytest.mark.parametrize(
    "l1,k,expected",
    [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
    ],
)
def test_rotate(l1, k, expected):
    Solution().rotate(l1, k)
    assert l1 == expected
