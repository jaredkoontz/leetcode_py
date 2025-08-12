# https://leetcode.com/problems/find-the-safest-path-in-a-grid
import heapq
import math
from collections import deque

import pytest

ROW_DIR = (0, 0, -1, 1)
COL_DIR = (-1, 1, 0, 0)


class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        return self.maximumSafenessFactor_mine(grid)

    @staticmethod
    def maximumSafenessFactor_mine(grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return 0

        dirns = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        theives = deque([])
        distances = [[math.inf] * n for _ in range(n)]

        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    distances[row][col] = 0
                    theives.append([row, col])

        dist = 0
        while theives:
            for _ in range(len(theives)):
                x, y = theives.popleft()

                for dx, dy in dirns:
                    new_x, new_y = x + dx, y + dy

                    if 0 <= new_x < n and 0 <= new_y < n:
                        if distances[new_x][new_y] > dist + 1:
                            distances[new_x][new_y] = dist + 1
                            theives.append([new_x, new_y])

            dist += 1

        max_heap = [(-distances[n - 1][n - 1], n - 1, n - 1)]
        seen = {n - 1, n - 1}

        while max_heap:
            curr_dist, x, y = heapq.heappop(max_heap)

            if x == 0 and y == 0:
                return -curr_dist

            for dx, dy in dirns:
                new_x, new_y = x + dx, y + dy

                if 0 <= new_x < n and 0 <= new_y < n and (new_x, new_y) not in seen:
                    new_distance = max(-distances[new_x][new_y], curr_dist)
                    heapq.heappush(max_heap, (new_distance, new_x, new_y))
                    seen.add((new_x, new_y))

        return -1

    @staticmethod
    def maximumSafenessFactor_bfs(grid: list[list[int]]) -> int:
        def bfs(n):
            q = deque()

            for i in range(n):
                for j in range(n):
                    if grid[i][j]:
                        score[i][j] = 0
                        q.append((i, j))

            while q:
                x, y = q.popleft()
                s = score[x][y]

                for i in range(4):
                    new_x = x + ROW_DIR[i]
                    new_y = y + COL_DIR[i]

                    if (
                        0 <= new_x < n
                        and 0 <= new_y < n
                        and score[new_x][new_y] > s + 1
                    ):
                        score[new_x][new_y] = s + 1
                        q.append((new_x, new_y))

        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return 0

        score = [[float("inf")] * n for _ in range(n)]
        bfs(n)

        vis = [[False] * n for _ in range(n)]
        pq = [(-score[0][0], 0, 0)]
        heapq.heapify(pq)

        while pq:
            safe, x, y = heapq.heappop(pq)
            safe = -safe

            if x == n - 1 and y == n - 1:
                return safe

            vis[x][y] = True

            for i in range(4):
                new_x = x + ROW_DIR[i]
                new_y = y + COL_DIR[i]

                if 0 <= new_x < n and 0 <= new_y < n and not vis[new_x][new_y]:
                    s = min(safe, score[new_x][new_y])
                    heapq.heappush(pq, (-s, new_x, new_y))
                    vis[new_x][new_y] = True

        return -1


@pytest.mark.parametrize(
    "grid,expected",
    [
        ([[1, 0, 0], [0, 0, 0], [0, 0, 1]], 0),
        ([[0, 0, 1], [0, 0, 0], [0, 0, 0]], 2),
        ([[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]], 2),
    ],
)
def test_maximumSafenessFactor(grid, expected):
    assert Solution().maximumSafenessFactor(grid) == expected
