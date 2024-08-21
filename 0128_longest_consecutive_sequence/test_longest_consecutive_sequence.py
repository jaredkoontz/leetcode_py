# https://leetcode.com/problems/longest-consecutive-sequence
import pytest


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        return self.longestConsecutive_mine(nums)

    @staticmethod
    def longestConsecutive_naive(nums):
        def contains(nums, target):
            for num in nums:
                if num == target:
                    return True
            return False

        longest_consecutive_sequence = 0
        for num in nums:
            current_number = num
            current_consecutive_sequence = 1
            while contains(nums, current_number + 1):
                current_number += 1
                current_consecutive_sequence += 1
            longest_consecutive_sequence = max(
                longest_consecutive_sequence, current_consecutive_sequence
            )

        return longest_consecutive_sequence

    @staticmethod
    def longestConsecutive_sort(nums):
        if not nums:
            return 0

        nums.sort()
        longest_consecutive_sequence = 0
        current_consecutive_sequence = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    current_consecutive_sequence += 1
                else:
                    longest_consecutive_sequence = max(
                        longest_consecutive_sequence, current_consecutive_sequence
                    )
                    current_consecutive_sequence = 1

        return max(longest_consecutive_sequence, current_consecutive_sequence)

    @staticmethod
    def longestConsecutive_hash(nums):
        num_map = {num: True for num in nums}

        for num in nums:
            if num - 1 in num_map:
                num_map[num] = False

        max_len = 0
        for num in nums:
            if num_map[num]:
                count = 0
                while num + count in num_map:
                    count += 1
                max_len = max(max_len, count)

        return max_len

    @staticmethod
    def longestConsecutive_hash_optimal(nums):
        num_set = set(nums)
        longest_consecutive_sequence = 0

        for num in nums:
            if num - 1 not in num_set:
                current_number = num
                current_consecutive_sequence = 1

                while current_number + 1 in num_set:
                    current_number += 1
                    current_consecutive_sequence += 1

                longest_consecutive_sequence = max(
                    longest_consecutive_sequence, current_consecutive_sequence
                )

        return longest_consecutive_sequence

    @staticmethod
    def longestConsecutive_mine(nums: list[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums:
                curr_longest = 1
                curr_num = num + 1
                while curr_num in nums:
                    curr_num += 1
                    curr_longest += 1
                longest = max(longest, curr_longest)
        return longest


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
    ],
)
def test_longest_consecutive(nums, expected):
    assert Solution().longestConsecutive(nums) == expected
