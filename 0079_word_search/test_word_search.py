# https://leetcode.com/problems/word-search
import pytest


# more at https://leetcode.com/problems/word-search/solutions/27660/python-dfs-solution-with-comments/


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True

        return False

    def backtrack(self, row, col, suffix):
        if len(suffix) == 0:
            return True

        if (
            row < 0
            or row == self.ROWS
            or col < 0
            or col == self.COLS
            or self.board[row][col] != suffix[0]
        ):
            return False
        ret = False
        self.board[row][col] = "#"
        for row_offset, col_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ret = self.backtrack(row + row_offset, col + col_offset, suffix[1:])
            if ret:
                break
        self.board[row][col] = suffix[0]
        return ret


@pytest.mark.parametrize(
    "board, word, expected",
    [
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCCED",
            True,
        ),
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "SEE",
            True,
        ),
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCB",
            False,
        ),
    ],
)
def test_exist(board, word, expected):
    assert Solution().exist(board, word) == expected
