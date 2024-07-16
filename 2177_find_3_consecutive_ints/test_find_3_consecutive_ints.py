import pytest


class Solution:
    def sumOfThree(self, num: int) -> list[int]:
        return self.sumOfThree_no_add(num)

    @staticmethod
    def sumOfThree_no_add(num: int) -> list[int]:
        if num // 3 != num / 3:
            return []
        return [num // 3 - 1, num // 3, num // 3 + 1]

    @staticmethod
    def sumOfThree_mine(num: int) -> list[int]:
        middle = num // 3
        if (middle - 1) + middle + (middle + 1) == num:
            return [middle - 1, middle, middle + 1]
        return []


@pytest.mark.parametrize("num,expected", [(33, [10, 11, 12]), (4, [])])
def test_find_3_consecutive_ints(num, expected):
    assert Solution().sumOfThree(num) == expected
