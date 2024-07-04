import pytest

# https://leetcode.com/problems/summary-ranges/description/


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        return self.summaryRanges_mine(nums)

    @staticmethod
    def summaryRanges_mine(nums: list[int]) -> list[str]:
        if not nums:
            return []
        lower, upper = nums[0], nums[0]
        ret = []

        n = len(nums)
        for i in range(1, n):
            if nums[i] != nums[i - 1] + 1:
                if lower == upper:
                    ret.append(f"{lower}")
                else:
                    ret.append(f"{lower}->{upper}")
                lower = nums[i]
            upper = nums[i]
        if lower == upper:
            ret.append(f"{lower}")
        else:
            ret.append(f"{lower}->{upper}")
        return ret


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),
        ([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"]),
    ],
)
def test_summaryRanges(nums, expected):
    assert Solution().summaryRanges(nums) == expected
