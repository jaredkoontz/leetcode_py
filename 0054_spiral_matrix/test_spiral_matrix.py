# https://leetcode.com/problems/spiral-matrix
import pytest


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        return self.spiralOrder_neet(matrix)

    @staticmethod
    def spiralOrder_neet(matrix: list[list[int]]) -> list[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        i, j = 0, 0
        up, right, down, left = 0, 1, 2, 3
        direction = right

        up_wall = 0
        right_wall = n
        down_wall = m
        left_wall = -1

        while len(ans) != m * n:
            if direction == right:
                while j < right_wall:
                    ans.append(matrix[i][j])
                    j += 1
                i, j = i + 1, j - 1
                right_wall -= 1
                direction = down
            elif direction == down:
                while i < down_wall:
                    ans.append(matrix[i][j])
                    i += 1
                i, j = i - 1, j - 1
                down_wall -= 1
                direction = left
            elif direction == left:
                while j > left_wall:
                    ans.append(matrix[i][j])
                    j -= 1
                i, j = i - 1, j + 1
                left_wall += 1
                direction = up
            else:
                while i > up_wall:
                    ans.append(matrix[i][j])
                    i -= 1
                i, j = i + 1, j + 1
                up_wall += 1
                direction = right

        return ans
        # Time: O(m*n)
        # Space: O(1)

    @staticmethod
    def spiralOrder_mine(matrix: list[list[int]]) -> list[int]:
        ret = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # get top row
            for i in range(left, right):
                ret.append(matrix[top][i])
            top += 1
            # get right column
            for i in range(top, bottom):
                ret.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break

            # get bottom row
            for i in range(right - 1, left - 1, -1):
                ret.append(matrix[bottom - 1][i])
            bottom -= 1

            # get left column
            for i in range(bottom - 1, top - 1, -1):
                ret.append(matrix[i][left])
            left += 1
        return ret


@pytest.mark.parametrize(
    "matrix,expected",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        (
                [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        ),
    ],
)
def test_spiralOrder(matrix, expected):
    assert Solution().spiralOrder(matrix) == expected
