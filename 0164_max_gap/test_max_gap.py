# https://leetcode.com/problems/maximum-gap
import math

import pytest


class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        return self.maximumGap_sort(nums)

    @staticmethod
    def maximumGap_sort(nums: list[int]) -> int:
        # nlogn
        if not nums or len(nums) == 1:
            return 0
        nums.sort()
        max_dist = float("-inf")
        for index in range(1, len(nums)):
            last = nums[index - 1]
            curr = nums[index]
            max_dist = max(max_dist, curr - last)

        return max_dist

    @staticmethod
    def maximumGap_linear(nums: list[int]) -> int:
        """
                Suppose in our integer array N elements, the min value is min and the max value is max. Then the maximum gap will be greater or equal to ceiling[(max - min ) / (N - 1)].
        Let bucketSize = ceiling[(max - min ) / (N - 1)].
        We divide all numbers in the array into N buckets, each bucket has size of bucketSize, where i-th (zero-based index) bucket contains all numbers in range [min + i*bucketSize, min + (i+1)*bucketSize).
        Because maximum gap is always greater or equal to bucketSize so in each bucket, we only need to store max element and min element, skip middle elements (min < middle < max) in the same bucket.
        Finally, we only need to compare max number in current bucket and min number in next bucket to get the relatively large gap and find out which two bucket have the maximum gap.
        """
        # n
        mi, ma, n = min(nums), max(nums), len(nums)
        if mi == ma:
            return 0  # All elements are the same
        bucket_size = math.ceil((ma - mi) / (n - 1))
        min_bucket = [math.inf] * n
        max_bucket = [-math.inf] * n
        for x in nums:
            idx = (x - mi) // bucket_size
            min_bucket[idx] = min(min_bucket[idx], x)
            max_bucket[idx] = max(max_bucket[idx], x)

        max_gap = bucket_size  # Maximum gap is always greater or equal to bucket_size
        prev = max_bucket[0]  # We always have 0th bucket
        for i in range(1, n):
            if min_bucket[i] == math.inf:
                continue  # Skip empty bucket
            max_gap = max(max_gap, min_bucket[i] - prev)
            prev = max_bucket[i]
        return max_gap


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([3, 6, 9, 1], 3),
        ([10], 0),
    ],
)
def test_maximumGap(nums, expected):
    assert Solution().maximumGap(nums) == expected
