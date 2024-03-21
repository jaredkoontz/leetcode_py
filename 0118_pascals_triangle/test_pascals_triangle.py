import pytest


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        return self.generate_dp(numRows)

    @staticmethod
    def generate_mine(numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []

        first_row = [1]
        rows = [first_row]

        for _ in range(1, numRows):
            row = [1]
            for i in range(1, len(rows[-1])):
                num = rows[-1][i] + rows[-1][i - 1]
                row.append(num)
            row.append(1)
            rows.append(row)

        return rows

    def generate_recursion(self, numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        previous = self.generate_recursion(numRows - 1)
        new_row = [1] * numRows

        for i in range(1, numRows - 1):
            new_row[i] = previous[-1][i - 1] + previous[-1][i]

        previous.append(new_row)
        return previous

    def generate_dp(self, numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        prev_rows = self.generate_dp(numRows - 1)
        prev_row = prev_rows[-1]
        current_row = [1]

        for i in range(1, numRows - 1):
            current_row.append(prev_row[i - 1] + prev_row[i])

        current_row.append(1)
        prev_rows.append(current_row)

        return prev_rows


@pytest.mark.parametrize(
    "rows,expected",
    [
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
        (4, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]),
        (3, [[1], [1, 1], [1, 2, 1]]),
        (2, [[1], [1, 1]]),
        (1, [[1]]),
    ],
)
def test_generate(rows, expected):
    assert Solution().generate(rows) == expected
