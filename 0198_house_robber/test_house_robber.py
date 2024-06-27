import pytest


class Solution:
    def rob(self, nums: list[int]) -> int:
        return self.rob_bottom_up_optimal(nums)

    @staticmethod
    def rob_recursive(nums: list[int]) -> int:
        def rob_helper(my_nums, index):
            if index < 0:
                return 0
            return max(
                rob_helper(my_nums, index - 2) + my_nums[index],
                rob_helper(my_nums, index - 1),
            )

        return rob_helper(nums, len(nums) - 1)

    @staticmethod
    def rob_memo(nums: list[int]) -> int:
        def rob_helper(my_nums, index, my_memo):
            if index < 0:
                return 0
            if my_memo[index] > 0:
                return my_memo[index]
            result = max(
                rob_helper(my_nums, index - 2, my_memo) + my_nums[index],
                rob_helper(my_nums, index - 1, my_memo),
            )
            memo[index] = result
            return result

        memo = [0] * len(nums)
        return rob_helper(nums, len(nums) - 1, memo)

    @staticmethod
    def rob_bottom_up(nums: list[int]) -> int:
        if not nums:
            return 0
        memo = [0] * (len(nums) + 1)
        memo[0] = 0
        memo[1] = nums[0]
        for i in range(1, len(nums)):
            value = nums[i]
            memo[i + 1] = max(memo[i], memo[i - 1] + value)
        return memo[-1]

    @staticmethod
    def rob_bottom_up_optimal(nums: list[int]) -> int:
        if not nums:
            return 0
        last = 0
        now = 0
        for num in nums:
            tmp = last
            last = max(now + num, last)
            now = tmp
        return last


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
    ],
)
def test_rob(nums, expected):
    assert Solution().rob(nums) == expected
