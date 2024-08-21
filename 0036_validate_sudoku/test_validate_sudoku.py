# https://leetcode.com/problems/valid-sudoku
import pytest


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        return self.isValidSudoku_one_loop(board)

    @staticmethod
    def isValidSudoku_one_loop(board: list[list[str]]) -> bool:
        row_count = 9
        column_count = row_count
        rows = [{} for _ in range(row_count)]
        cols = [{} for _ in range(row_count)]
        boxes = [{} for _ in range(row_count)]

        for row in range(row_count):
            for column in range(column_count):
                if board[row][column] != ".":
                    num = board[row][column]
                    box_index = (row // 3) * 3 + (column // 3)
                    if (
                        (num in rows[row])
                        or (num in cols[column])
                        or (num in boxes[box_index])
                    ):
                        return False
                    rows[row][num] = True
                    cols[column][num] = True
                    boxes[box_index][num] = True
        return True

    @staticmethod
    def isValidSudoku_mine(board: list[list[str]]) -> bool:
        def validate_rows() -> bool:
            for row in board:
                if not valid_unit(row):
                    return False
            return True

        def validate_columns() -> bool:
            for col in zip(*board):
                if not valid_unit(col):
                    return False
            return True

        def validate_boxes() -> bool:
            for i in (0, 3, 6):
                for j in (0, 3, 6):
                    square = []
                    for x in range(i, i + 3):
                        for y in range(j, j + 3):
                            square.append(board[x][y])
                    if not valid_unit(square):
                        return False
            return True

        def valid_unit(unit: list[str]) -> bool:
            unit = [x for x in unit if x != "."]
            return len(set(unit)) == len(unit)

        if validate_rows() and validate_columns() and validate_boxes():
            return True

        return False


@pytest.mark.parametrize(
    "board,expected",
    [
        (
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            True,
        ),
        (
            [
                ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            False,
        ),
    ],
)
def test_isValidSudoku(board: list[list[str]], expected: bool):
    assert Solution().isValidSudoku(board) == expected
