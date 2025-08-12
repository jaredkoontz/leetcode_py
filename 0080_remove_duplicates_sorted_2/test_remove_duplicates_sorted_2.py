# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
import pytest


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        return self.removeDuplicates_clean(nums)

    @staticmethod
    def removeDuplicates_clean(nums: list[int]) -> int:
        i = 0
        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
        return i

    @staticmethod
    def removeDuplicates_mine(nums: list[int]) -> int:
        if not nums:
            return 0
        index = 1
        last = nums[0]
        count = 1

        while index < len(nums):
            while index < len(nums) and last == nums[index]:
                if count >= 2:
                    del nums[index]
                    index -= 1
                    count -= 1
                count += 1
                index += 1
            count = 1
            last = nums[index] if index < len(nums) else last
            index += 1
        return len(nums)


@pytest.mark.parametrize(
    "l1,l2,expected",
    [
        (
            [1, 1, 1, 2, 2, 3],
            [1, 1, 2, 2, 3],
            5,
        ),
        (
            [0, 0, 1, 1, 1, 1, 2, 3, 3],
            [0, 0, 1, 1, 2, 3, 3],
            7,
        ),
    ],
)
def test_remove_duplicates(l1, l2, expected):
    changed = Solution().removeDuplicates(l1)
    assert changed == expected
