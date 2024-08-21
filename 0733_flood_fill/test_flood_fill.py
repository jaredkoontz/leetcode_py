# https://leetcode.com/problems/flood-fill
import pytest

# todo more at https://leetcode.com/problems/flood-fill/solutions/109604/easy-python-dfs-no-need-for-visited/


class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        return self.floodFill_mine(image, sr, sc, color)

    @staticmethod
    def floodFill_mine(
        image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        m, n = len(image), len(image[0])
        start_color = image[sr][sc]

        if color == start_color:
            return image

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or image[i][j] != start_color:
                return

            image[i][j] = color
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        dfs(sr, sc)
        return image


@pytest.mark.parametrize(
    "image,sr,sc,color,expected",
    [
        ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2, [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
        ([[0, 0, 0], [0, 0, 0]], 0, 0, 0, [[0, 0, 0], [0, 0, 0]]),
    ],
)
def test_floodFill(image, sr, sc, color, expected):
    assert Solution().floodFill(image, sr, sc, color) == expected
