# https://leetcode.com/problems/count-elements-with-maximum-frequency
import pytest


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        return self.maxFrequencyElements_mine(nums)

    @staticmethod
    def maxFrequencyElements_mine(nums: list[int]) -> int:
        frequencies = {}
        total_frequency = 0
        max_frequency = -1

        for num in nums:
            if num not in frequencies:
                frequencies[num] = frequencies.get(num, 1)
            else:
                frequencies[num] += 1
            max_frequency = max(max_frequency, frequencies[num])

        for frequency in frequencies.values():
            if frequency == max_frequency:
                total_frequency += frequency

        return total_frequency

    @staticmethod
    def maxFrequencyElements_theirs(nums: list[int]) -> int:
        frequencies = [0] * 101
        max_frequency = 0
        for x in nums:
            frequencies[x] += 1
            max_frequency = max(max_frequency, frequencies[x])
        ans = 0
        for f in frequencies:
            if f == max_frequency:
                ans += f
        return ans

    @staticmethod
    def maxFrequencyElements_theirs2(nums: list[int]) -> int:
        frequencies = [0] * 101
        max_frequency = 0
        f = 0
        for x in nums:
            frequencies[x] += 1
            # taking advantage of false = 0 and true = 1
            f += frequencies[x] == max_frequency
            if frequencies[x] > max_frequency:
                f = 1
                max_frequency = frequencies[x]
        return f * max_frequency


@pytest.mark.parametrize(
    "l1, expected",
    [
        ([1, 2, 2, 3, 1, 4], 4),
        ([1, 2, 3, 4, 5], 5),
        ([], 0),
        ([1], 1),
    ],
)
def test_maxFrequencyElements(l1, expected):
    assert Solution().maxFrequencyElements(l1) == expected
