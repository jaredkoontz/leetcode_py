"""
Problem Statement
Given an array of integers ( A ), and two integers ( S ) (start value) and ( D ) (destination value), you are allowed to
perform any of the following operations on a value ( x ):

Add an element from ( A ) to ( x ): ( x + A[i] )
Subtract an element from ( A ) from ( x ): ( x - A[i] )
Perform a bitwise XOR of an element from ( A ) with ( x ): ( x XOR A[i] )
Each operation counts as one move. Determine the minimum number of moves required to transform the integer ( S ) into
the integer ( D ) using the operations above. If it's not possible to achieve this transformation,
return (-1).
"""

import pytest


def min_moves_to_transform(arr: list[int], start: int, destination: int) -> int:
    if start == destination:
        return 0

    queue = [(start, 0)]
    visited = set()
    visited.add(start)
    while queue:
        start_val, num_moves = queue.pop(0)
        for val in arr:
            for new_val in (start_val + val, start_val - val, start_val ^ val):
                if new_val == destination:
                    return num_moves + 1
                if new_val not in visited:
                    visited.add(new_val)
                    queue.append((new_val, num_moves + 1))
    return -1


@pytest.mark.parametrize(
    "arr,start,destination,expected",
    [
        ([6, 2, 7, 7], 10, 21, 3),
        ([6, 2, 7, 7], 10, 14, 2),
        ([6, 2, 7, 7], 10, 12, 1),
        ([2, 4, 12], 2, 12, 2),
        ([3, 5, 7], 0, -4, 2),
    ],
)
def test_min_moves_to_transform(arr, start, destination, expected):
    assert min_moves_to_transform(arr, start, destination) == expected
