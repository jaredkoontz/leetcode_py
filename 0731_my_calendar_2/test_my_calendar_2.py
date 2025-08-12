# https://leetcode.com/problems/my-calendar-ii
from collections import defaultdict

import pytest


class CalendarTwo:
    def __init__(self):
        self.m = defaultdict(int)

    def book(self, start, end):
        self.m[start] += 1
        self.m[end] -= 1

        count = 0
        for time in sorted(self.m):
            count += self.m[time]
            if count == 3:
                # Triple booking detected, revert changes
                self.m[start] -= 1
                self.m[end] += 1
                return False

        return True


MyCalendarTwo = CalendarTwo


@pytest.mark.parametrize(
    "operations, init, expected",
    [
        (
            ["MyCalendarTwo", "book", "book", "book", "book", "book", "book"],
            [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]],
            [None, True, True, True, False, True, True],
        ),
    ],
)
def test_calendar(operations, init, expected):
    calendar = None
    for op, components, curr_val in zip(operations, init, expected):
        if op == "MyCalendarTwo":
            calendar = MyCalendarTwo()
        else:
            assert calendar.book(components[0], components[1]) == curr_val
