import pytest


class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        return self.findCenter_oneline(edges)

    def findCenter_oneline(self, edges: list[list[int]]) -> int:
        return (set(edges[0]) & set(edges[1])).pop()

    def findCenter_readable(self, edges: list[list[int]]) -> int:
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        else:
            return edges[0][1]


@pytest.mark.parametrize(
    "edges,expected",
    [
        ([[1, 2], [2, 3], [4, 2]], 2),
        ([[1, 2], [5, 1], [1, 3], [1, 4]], 1),
    ],
)
def test_find_center(edges, expected):
    assert Solution().findCenter(edges) == expected
