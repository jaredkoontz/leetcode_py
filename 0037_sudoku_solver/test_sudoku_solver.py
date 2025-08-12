# https://leetcode.com/problems/sudoku-solver
from collections import defaultdict

import pytest


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        self.solveSudoku_mine(board)

    @staticmethod
    def solveSudoku_mine(board: list[list[str]]) -> None:
        n = 9

        def isValid(row, col, ch):
            row, col = int(row), int(col)

            for i in range(9):
                if board[i][col] == ch:
                    return False
                if board[row][i] == ch:
                    return False

                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == ch:
                    return False

            return True

        def solve(row, col):
            if row == n:
                return True
            if col == n:
                return solve(row + 1, 0)

            if board[row][col] == ".":
                for i in range(1, n + 1):
                    if isValid(row, col, str(i)):
                        board[row][col] = str(i)

                        if solve(row, col + 1):
                            return True
                        else:
                            board[row][col] = "."
                return False
            else:
                return solve(row, col + 1)

        solve(0, 0)

    def solveSudoku_theirs(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def backtrack(i, j):
            # traverse col then row
            # print(j, i)
            if j >= 9:
                self.found = True
                return
            elif board[i][j] != ".":
                if i >= 8:
                    backtrack(0, j + 1)
                else:
                    backtrack(i + 1, j)
            else:
                cur_list = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
                for val in row_set[i]:
                    cur_list.discard(val)
                for val in col_set[j]:
                    cur_list.discard(val)
                for val in square_set[(i // 3, j // 3)]:
                    cur_list.discard(val)

                for val in cur_list:
                    if (
                            val in row_set[i]
                            or val in col_set[j]
                            or val in square_set[(i // 3, j // 3)]
                    ):
                        continue
                    board[i][j] = val
                    row_set[i].add(val)
                    col_set[j].add(val)
                    square_set[(i // 3, j // 3)].add(val)
                    if i >= 8:
                        backtrack(0, j + 1)
                    else:
                        backtrack(i + 1, j)
                    if self.found:
                        return
                    row_set[i].remove(val)
                    col_set[j].remove(val)
                    square_set[(i // 3, j // 3)].remove(val)
                    board[i][j] = "."

        row_set = defaultdict(set)
        col_set = defaultdict(set)
        square_set = defaultdict(set)
        res = []
        self.found = False

        for x in range(9):
            for y in range(9):
                if board[x][y] != ".":
                    row_set[x].add(board[x][y])
                    col_set[y].add(board[x][y])
                    square_set[(x // 3, y // 3)].add(board[x][y])

        backtrack(0, 0)
        board = res


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
                [
                    ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                    ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                    ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                    ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                    ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                    ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                    ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                    ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                    ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
                ],
        ),
    ],
)
def test_solveSudoku(board: list[list[str]], expected: list[list[str]]) -> None:
    Solution().solveSudoku(board)
    assert expected == board
