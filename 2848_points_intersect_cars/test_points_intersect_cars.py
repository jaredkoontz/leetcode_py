# https://leetcode.com/problems/points-that-intersect-with-cars
import pytest


class Solution:
    def numberOfPoints(self, nums: list[list[int]]) -> int:
        return self.maximumPopulation_mine(nums)

    @staticmethod
    def maximumPopulation_num_line(nums: list[list[int]]) -> int:
        line = [0] * 102

        for start, end in nums:
            line[start] += 1
            if end + 1 < 102:
                line[end + 1] -= 1

        ans = 0
        count = 0
        for i in range(102):
            count += line[i]
            if count > 0:
                ans += 1

        return ans

    @staticmethod
    def maximumPopulation_theirs(nums: list[list[int]]) -> int:
        nums.sort()
        result = nums[0][1] - nums[0][0] + 1
        current_end = nums[0][1]
        for start, end in nums[1:]:
            if start > current_end:
                result += end - start + 1
                current_end = end
            elif end >= current_end:
                result += end - current_end
                current_end = end
        return result

    @staticmethod
    def maximumPopulation_mine(nums: list[list[int]]) -> int:
        merged_intervals = []
        for curr_inter in sorted(nums, key=lambda x: x[0]):
            if merged_intervals and merged_intervals[-1][1] >= curr_inter[0]:
                merged_intervals[-1][1] = max(curr_inter[1], merged_intervals[-1][1])
            else:
                merged_intervals += [curr_inter]
        possible = 0
        for curr_range in merged_intervals:
            possible += (curr_range[1] - curr_range[0]) + 1
        return possible


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([[4, 4], [9, 10], [9, 10], [3, 8]], 8),
        ([[3, 6], [1, 5], [4, 7]], 7),
        ([[1, 3], [5, 8]], 7),
        ([[1, 3], [6, 8]], 6),
        ([[1, 2], [4, 8]], 7),
        ([[1, 2], [7, 8], [3, 4]], 6),
    ],
)
def test_numberOfPoints(nums, expected):
    assert Solution().numberOfPoints(nums) == expected
