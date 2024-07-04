import pytest


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        return self.canJump_mine(nums)

    @staticmethod
    def canJump_mine(nums: list[int]) -> bool:
        n = len(nums)
        goal = n - 1

        for i in range(n - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
    ],
)
def test_canJump(nums, expected):
    assert Solution().canJump(nums) == expected
