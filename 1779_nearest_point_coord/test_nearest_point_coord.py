import pytest


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        return self.nearestValidPoint_mine(x, y, points)

    @staticmethod
    def nearestValidPoint_mine(x: int, y: int, points: list[list[int]]) -> int:
        min_dist = float("inf")
        ret = -1

        for index, point_pair in enumerate(points):
            candi_x, candi_y = point_pair[0], point_pair[1]
            if x == candi_x or y == candi_y:
                man_dist = abs(x - candi_x) + abs(y - candi_y)
                if man_dist < min_dist:
                    min_dist = man_dist
                    ret = index

        return ret


@pytest.mark.parametrize(
    "x,y,points,expected",
    [
        (3, 4, [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]], 2),
        (3, 4, [[3, 4]], 0),
        (3, 4, [[2, 3]], -1),
    ],
)
def test_nearestValidPoint(x, y, points, expected):
    assert Solution().nearestValidPoint_mine(x, y, points) == expected
