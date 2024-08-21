# https://leetcode.com/problems/contains-duplicate-ii
import pytest


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        return self.containsNearbyDuplicate_hash_map(nums, k)

    @staticmethod
    def containsNearbyDuplicate_naive(nums: list[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True

        return False

    @staticmethod
    def containsNearbyDuplicate_hash_map(nums: list[int], k: int) -> bool:
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([1, 2, 3, 1], 3, True),
        ([1, 0, 1, 1], 1, True),
        ([1, 2, 3, 1, 2, 3], 2, False),
    ],
)
def test_containsNearbyDuplicate(nums, k, expected):
    assert Solution().containsNearbyDuplicate(nums, k) == expected
