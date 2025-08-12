# https://leetcode.com/problems/magic-squares-in-grid
import pytest


class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        return self.numMagicSquaresInside_mine(grid)

    @staticmethod
    def numMagicSquaresInside_traits(grid: list[list[int]]) -> int:
        def _isMagicSquare(grid, row, col):
            # The sequences are each repeated twice to account for
            # the different possible starting points of the sequence
            # in the magic square
            sequence = "2943816729438167"
            sequence_reversed = "7618349276183492"

            border = []
            # Flattened indices for bordering elements of 3x3 grid
            border_indices = [0, 1, 2, 5, 8, 7, 6, 3]
            for i in border_indices:
                num = grid[row + i // 3][col + (i % 3)]
                border.append(str(num))

            border_converted = "".join(border)

            # Make sure the sequence starts at one of the corners
            return (
                    grid[row][col] % 2 == 0
                    and (
                            sequence.find(border_converted) != -1
                            or sequence_reversed.find(border_converted) != -1
                    )
                    and grid[row + 1][col + 1] == 5
            )

        ans = 0
        m = len(grid)
        n = len(grid[0])
        for row in range(m - 2):
            for col in range(n - 2):
                if _isMagicSquare(grid, row, col):
                    ans += 1
        return ans

    @staticmethod
    def numMagicSquaresInside_scan(grid: list[list[int]]) -> int:
        def _isMagicSquare(grid, row, col):
            seen = [False] * 10
            for i in range(3):
                for j in range(3):
                    num = grid[row + i][col + j]
                    if num < 1 or num > 9:
                        return False
                    if seen[num]:
                        return False
                    seen[num] = True

            # Check if diagonal sums are the same
            diagonal1 = grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]
            diagonal2 = grid[row + 2][col] + grid[row + 1][col + 1] + grid[row][col + 2]

            if diagonal1 != diagonal2:
                return False

            # Check if all row sums are the same as the diagonal sums
            row1 = grid[row][col] + grid[row][col + 1] + grid[row][col + 2]
            row2 = grid[row + 1][col] + grid[row + 1][col + 1] + grid[row + 1][col + 2]
            row3 = grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col + 2]

            if not (row1 == diagonal1 and row2 == diagonal1 and row3 == diagonal1):
                return False

            # Check if all column sums are the same as the diagonal sums
            col1 = grid[row][col] + grid[row + 1][col] + grid[row + 2][col]
            col2 = grid[row][col + 1] + grid[row + 1][col + 1] + grid[row + 2][col + 1]
            col3 = grid[row][col + 2] + grid[row + 1][col + 2] + grid[row + 2][col + 2]

            if not (col1 == diagonal1 and col2 == diagonal1 and col3 == diagonal1):
                return False

            return True

        ans = 0
        m = len(grid)
        n = len(grid[0])
        for row in range(m - 2):
            for col in range(n - 2):
                if _isMagicSquare(grid, row, col):
                    ans += 1
        return ans

    @staticmethod
    def numMagicSquaresInside_mine(grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        result = 0

        def isMagic(my_grid, row, col):
            record = [0] * 10
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if (
                            my_grid[i][j] < 1
                            or my_grid[i][j] > 9
                            or record[my_grid[i][j]] > 0
                    ):
                        return False
                    record[my_grid[i][j]] = 1

            sum1 = (
                    my_grid[row][col]
                    + my_grid[row + 1][col + 1]
                    + my_grid[row + 2][col + 2]
            )
            sum2 = (
                    my_grid[row][col + 2]
                    + my_grid[row + 1][col + 1]
                    + my_grid[row + 2][col]
            )
            if sum1 != sum2:
                return False

            for i in range(3):
                if (
                        my_grid[row + i][col]
                        + my_grid[row + i][col + 1]
                        + my_grid[row + i][col + 2]
                        != sum1
                        or my_grid[row][col + i]
                        + my_grid[row + 1][col + i]
                        + my_grid[row + 2][col + i]
                        != sum1
                ):
                    return False

            return True

        for i in range(m - 2):
            for j in range(n - 2):
                if isMagic(grid, i, j):
                    result += 1

        return result


@pytest.mark.parametrize(
    "grid,expected",
    [
        ([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]], 1),
        ([[8]], 0),
    ],
)
def test_numMagicSquaresInside(grid, expected):
    assert Solution().numMagicSquaresInside(grid) == expected
