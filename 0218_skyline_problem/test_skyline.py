# https://leetcode.com/problems/the-skyline-problem
from heapq import heappop
from heapq import heappush

import pytest


class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        return self.getSkyline_divide_conquer(buildings)

    def getSkyline_divide_conquer(self, buildings: list[list[int]]) -> list[list[int]]:
        def _merge(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
            # Define the merging function
            ans = []  # Initialize the result list
            i = 0  # Left half's index
            j = 0  # Right half's index
            leftY = 0  # Initialize the ongoing height of the left half
            rightY = 0  # Initialize the ongoing height of the right half

            while i < len(left) and j < len(right):
                # Choose the point with smaller x-coordinate to process first
                if left[i][0] < right[j][0]:
                    # If the left point is processed first, update the ongoing height of the left half
                    leftY = left[i][1]
                    # Add the current point to the result list, with the larger height of the two halves
                    _addPoint(ans, left[i][0], max(left[i][1], rightY))
                    i += 1  # Move to the next point in the left half
                else:
                    # If the right point is processed first, update the ongoing height of the right half
                    rightY = right[j][1]
                    # Add the current point to the result list, with the larger height of the two halves
                    _addPoint(ans, right[j][0], max(right[j][1], leftY))
                    j += 1  # Move to the next point in the right half

            # Add any remaining points in the left half to the result list
            while i < len(left):
                _addPoint(ans, left[i][0], left[i][1])
                i += 1

            # Add any remaining points in the right half to the result list
            while j < len(right):
                _addPoint(ans, right[j][0], right[j][1])
                j += 1

            return ans

        def _addPoint(ans: list[list[int]], x: int, y: int) -> None:
            # Helper function to add a point to the result list
            if ans and ans[-1][0] == x:
                # If the current point has the same x-coordinate as the previous one, update the height of the previous one
                ans[-1][1] = y
                return
            if ans and ans[-1][1] == y:
                # If the current point has the same height as the previous one, skip it
                return
            # Otherwise, add the current point to the result list
            ans.append([x, y])

        # Define the recursive function to split the buildings and merge the sub-results
        n = len(buildings)
        if n == 0:
            return []  # Base case: no building
        if n == 1:
            # Base case: only one building, return its two corners
            left, right, height = buildings[0]
            return [[left, height], [right, 0]]

        # Split the buildings into two halves and recursively solve them
        left = self.getSkyline_divide_conquer(buildings[: n // 2])
        right = self.getSkyline_divide_conquer(buildings[n // 2:])
        # Merge the results of the two halves
        return _merge(left, right)

    @staticmethod
    def getSkyline_segment_tree(buildings: list[list[int]]) -> list[list[int]]:
        tree = SegmentTreeNode.create_tree(buildings)
        skyline = []
        prev_value = 0
        for point, value in tree.traverse():
            if value != prev_value:
                skyline.append([point, value])
            prev_value = value
        return skyline

    @staticmethod
    def getSkyline_sort(buildings: list[list[int]]) -> list[list[int]]:
        def addsky(pos, hei):
            if sky[-1][1] != hei:
                sky.append([pos, hei])

        sky = [[-1, 0]]

        # possible corner positions
        position = set([b[0] for b in buildings] + [b[1] for b in buildings])

        # live buildings
        live = []

        i = 0

        for t in sorted(position):
            # add the new buildings whose left side is lefter than position t
            while i < len(buildings) and buildings[i][0] <= t:
                heappush(live, (-buildings[i][2], buildings[i][1]))
                i += 1

            # remove the past buildings whose right side is lefter than position t
            while live and live[0][1] <= t:
                heappop(live)

            # pick the highest existing building at this moment
            h = -live[0][0] if live else 0
            addsky(t, h)

        return sky[1:]

    @staticmethod
    def getSkyline_heap(buildings: list[list[int]]) -> list[list[int]]:
        # add start-building events
        # also add end-building events(acts as buildings with 0 height)
        # and sort the events in left -> right order
        events = [(L, -H, R) for L, R, H in buildings]
        events += list({(R, 0, 0) for _, R, _ in buildings})
        events.sort()

        # res: result, [x, height]
        # live: heap, [-height, ending position]
        res = [[0, 0]]
        live = [(0, float("inf"))]
        for pos, negH, R in events:
            # 1, pop buildings that are already ended
            # 2, if it's the start-building event, make the building alive
            # 3, if previous keypoint height != current highest height, edit the result
            while live[0][1] <= pos:
                heappop(live)
            if negH:
                heappush(live, (negH, R))
            if res[-1][1] != -live[0][0]:
                res += [[pos, -live[0][0]]]
        return res[1:]


class SegmentTreeNode:
    def __init__(self, left, right, left_child=None, right_child=None):
        self.left = left
        self.right = right
        self.left_child = left_child
        self.right_child = right_child
        self.value = 0

    @classmethod
    def create_node(cls, begin, end, points):
        if begin == end:
            return cls(points[begin], points[begin + 1])
        mid = (begin + end) // 2
        left_child = cls.create_node(begin, mid, points)
        right_child = cls.create_node(mid + 1, end, points)
        return cls(points[begin], points[end + 1], left_child, right_child)

    @classmethod
    def create_tree(cls, segments):
        points = []
        for left, right, _ in segments:
            points.append(left)
            points.append(right)
        points = sorted(set(points))
        points.append(float("inf"))
        root = cls.create_node(0, len(points) - 2, points)

        segments.sort(key=lambda s: s[2])
        for left, right, value in segments:
            root.update(left, right, value)
        return root

    def update(self, left, right, value):
        left = max(left, self.left)
        right = min(right, self.right)
        if left >= right:
            return
        if self.left == left and self.right == right:
            self.value = value
        else:
            if self.value is not None:
                self.left_child.value = self.value
                self.right_child.value = self.value
                self.value = None
            self.left_child.update(left, right, value)
            self.right_child.update(left, right, value)

    def traverse(self):
        if self.value is None:
            yield from self.left_child.traverse()
            yield from self.right_child.traverse()
        else:
            yield self.left, self.value


@pytest.mark.parametrize(
    "buildings,expected",
    [
        (
                [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]],
                [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]],
        ),
        ([[0, 2, 3], [2, 5, 3]], [[0, 3], [5, 0]]),
    ],
)
def test_getSkyline(buildings, expected):
    assert Solution().getSkyline(buildings) == expected
