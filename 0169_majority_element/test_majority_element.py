from collections import Counter

import pytest


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        return self.majorityElement_voting(nums)

    @staticmethod
    def majorityElement_sort(nums: list[int]) -> int:
        sort = sorted(nums)
        return sort[len(nums) // 2]

    @staticmethod
    def majorityElement_hash_map(nums: list[int]) -> int:
        counter = Counter(nums)
        return counter.most_common(1)[0][0]

    @staticmethod
    def majorityElement_voting(nums: list[int]) -> int:
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
    ],
)
def test_majorityElement(nums, expected):
    assert Solution().majorityElement(nums) == expected
