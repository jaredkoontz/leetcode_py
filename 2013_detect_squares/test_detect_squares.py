# https://leetcode.com/problems/detect-squares
from collections import Counter
from collections import defaultdict

import pytest


class DetectSquares:
    def __init__(self):
        # Initialize a dictionary where each key is an x-coordinate that maps to a Counter
        # which holds y-coordinates and their corresponding counts.
        self.coord_count = defaultdict(Counter)

    def add(self, point: list[int]) -> None:
        # Add a point to the collection. The point is a list of two integers [x, y].
        x, y = point
        # Increment the count of the point in the corresponding x's Counter by 1.
        self.coord_count[x][y] += 1

    def count(self, point: list[int]) -> int:
        # Count how many squares can be formed with the given point as one of the vertices.
        # The point is a list of two integers [x, y].
        x1, y1 = point
        # If the x-coordinate of the given point isn't in our record, return 0 because no squares can be formed.
        if x1 not in self.coord_count:
            return 0

        total_squares = 0  # Initialize the number of squares to 0.

        # Iterate over all the unique x-coordinates in our dictionary.
        for x2 in self.coord_count.keys():
            # We need two distinct x-coordinates for a square (the length of the square side).
            if x2 != x1:
                # Compute the side length of the potential square.
                d = x2 - x1
                # Check for the top right and bottom right points of the square.
                total_squares += (
                        self.coord_count[x2][y1]
                        * self.coord_count[x1][y1 + d]
                        * self.coord_count[x2][y1 + d]
                )
                # Check for the top left and bottom left points of the square if the y-axis distance is within bounds.
                total_squares += (
                        self.coord_count[x2][y1]
                        * self.coord_count[x1][y1 - d]
                        * self.coord_count[x2][y1 - d]
                )

        # Return the total number of squares found.
        return total_squares


@pytest.mark.parametrize(
    "operations, init, expected",
    [
        (
                ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"],
                [
                    [],
                    [[3, 10]],
                    [[11, 2]],
                    [[3, 2]],
                    [[11, 10]],
                    [[14, 8]],
                    [[11, 2]],
                    [[11, 10]],
                ],
                [None, None, None, None, 1, 0, None, 2],
        ),
    ],
)
def test_kth_smallest(operations, init, expected):
    ds = None
    for op, components, curr_expected in zip(operations, init, expected):
        if op == "DetectSquares":
            ds = DetectSquares()
        elif op == "add":
            ds.add(components[0])
        else:
            assert op == "count"
            assert ds.count(components[0]) == curr_expected
