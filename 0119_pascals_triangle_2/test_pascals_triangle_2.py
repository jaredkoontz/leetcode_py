# https://leetcode.com/problems/pascals-triangle-ii
import pytest


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        return self.getRow_formula(rowIndex)

    @staticmethod
    def getRow_formula(rowIndex: int) -> list[int]:
        rowIndex += 1  # Convert to 1-indexed for formula
        ans = []
        val = 1
        ans.append(val)

        for c in range(1, rowIndex):
            val *= rowIndex - c
            val //= c
            ans.append(val)

        return ans


@pytest.mark.parametrize(
    "row_index,expected",
    [
        (0, [1]),
        (1, [1, 1]),
        (2, [1, 2, 1]),
        (3, [1, 3, 3, 1]),
        (4, [1, 4, 6, 4, 1]),
    ],
)
def test_get_row(row_index, expected):
    assert Solution().getRow(row_index) == expected
