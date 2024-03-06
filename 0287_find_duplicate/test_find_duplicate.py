from typing import List

import pytest


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return self.findDuplicate_c_space(nums)

    def findDuplicate_c_space(self, nums: List[int]) -> int:
        print(f"{nums=}")
        slow, fast = 0, 0
        print(f"{slow=}, {fast=}")
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print(f"{slow=}, {fast=}")
            if slow == fast:
                break

        slow2 = 0

        print(f"{slow=}, {slow2=}")
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            print(f"{slow=}, {slow2=}")
            if slow == slow2:
                break
        return slow

    def findDuplicate_two_pointer(self, nums: List[int]) -> int:
        # same as above, just a little cleaner
        # Treat each (key, value) pair of the array as the (pointer, next) node of the linked list,
        # thus the duplicated number will be the beginning of the cycle in the linked list.
        # Besides, there is always a cycle in the linked list which
        # starts from the first element of the array.
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

    def findDuplicate_bin_search(self, nums: List[int]) -> int:
        # Time:  O(nlogn)
        # Space: O(1)
        left, right = 1, len(nums) - 1

        while left <= right:
            mid = left + (right - left) / 2
            # Get count of num <= mid.
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def findDuplicate_marker(self, nums: List[int]) -> int:
        # Time:  O(n)
        # Space: O(n)
        duplicate = 0
        # Mark the value as visited by negative.
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
            else:
                duplicate = abs(num)
                break
        # Rollback the value.
        for num in nums:
            if nums[abs(num) - 1] < 0:
                nums[abs(num) - 1] *= -1
            else:
                break
        return duplicate

    def findDuplicate_ez(self, nums: List[int]) -> int:
        my_map = {}
        for num in nums:
            if num in my_map:
                return num
            else:
                my_map[num] = num


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
        ([3, 3, 3, 3, 3], 3),
        ([3, 1, 2, 3], 3),
        ([1, 3, 2, 3], 3),
    ],
)
def test_find_duplicate(nums, expected):
    assert Solution().findDuplicate(nums) == expected
