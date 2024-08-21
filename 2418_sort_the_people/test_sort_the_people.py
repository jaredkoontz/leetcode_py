# https://leetcode.com/problems/sort-the-people
import pytest


class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        return self.sortPeople_mine(names, heights)

    @staticmethod
    def sortPeople_mine(names: list[str], heights: list[int]) -> list[str]:
        people = list(zip(heights, names))
        people.sort(reverse=True, key=lambda x: x[0])
        return [name for height, name in people]


@pytest.mark.parametrize(
    "names,heights,expected",
    [
        (["Mary", "John", "Emma"], [180, 165, 170], ["Mary", "Emma", "John"]),
        (["Alice", "Bob", "Bob"], [155, 185, 150], ["Bob", "Alice", "Bob"]),
    ],
)
def test_sortPeople(names, heights, expected):
    assert Solution().sortPeople(names, heights) == expected
