import pytest


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return self.containsDuplicate_mine(nums)

    @staticmethod
    def containsDuplicate_mine(nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

    @staticmethod
    def containsDuplicate_one_line(nums: list[int]) -> bool:
        return len(nums) != len(set(nums))


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 2], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ],
)
def test_contains_duplicate(nums, expected):
    assert Solution().containsDuplicate(nums) == expected
