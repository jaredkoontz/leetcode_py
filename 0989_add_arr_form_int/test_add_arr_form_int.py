# https://leetcode.com/problems/add-to-array-form-of-integer
import pytest


class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        return self.addToArrayForm_mine(num, k)

    @staticmethod
    def addToArrayForm_mine(num: list[int], k: int) -> list[int]:
        curr_place = 1
        carry = k

        while True:
            if curr_place > len(num):
                num.insert(0, 0)
            curr_val = num[-curr_place]
            curr_val += carry
            if curr_val > 9:
                new_val = curr_val % 10
                carry = curr_val // 10
                num[-curr_place] = new_val
            else:
                num[-curr_place] = curr_val
                break
            curr_place += 1

        return num


@pytest.mark.parametrize(
    "num,k,expected",
    [
        ([1, 2, 0, 0], 34, [1, 2, 3, 4]),
        ([2, 7, 4], 181, [4, 5, 5]),
        ([2, 1, 5], 806, [1, 0, 2, 1]),
        ([5], 1000, [1, 0, 0, 5]),
    ],
)
def test_addToArrayForm(num, k, expected):
    assert Solution().addToArrayForm(num, k) == expected
