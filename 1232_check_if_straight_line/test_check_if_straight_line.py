# https://leetcode.com/problems/check-if-it-is-a-straight-line/
import pytest


class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        return self.checkStraightLine_one_line(coordinates)

    @staticmethod
    def checkStraightLine_one_line(coordinates: list[list[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[:2]
        return all((x1 - x0) * (y - y1) == (x - x1) * (y1 - y0) for x, y in coordinates)

    @staticmethod
    def checkStraightLine_slope(coordinates: list[list[int]]) -> bool:
        if len(coordinates) == 1:
            return True
        (x0, y0), (x1, y1) = coordinates[:2]
        for x, y in coordinates:
            if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
                return False
        return True


@pytest.mark.parametrize(
    "coordinates,expected",
    [
        ([[0, 0], [0, 1], [0, -1]], True),
        ([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]], True),
        ([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]], False),
    ],
)
def test_checkStraightLine(coordinates, expected):
    assert Solution().checkStraightLine(coordinates) == expected
