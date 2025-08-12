# https://leetcode.com/problems/second-minimum-time-to-reach-destination
import heapq
import math
from collections import defaultdict
from collections import deque

import pytest


class Solution:
    def secondMinimum(
        self, n: int, edges: list[list[int]], time: int, change: int
    ) -> int:
        return self.secondMinimum_bfs(n, edges, time, change)

    @staticmethod
    def secondMinimum_dijkstra(
        n: int, edges: list[list[int]], time: int, change: int
    ) -> int:
        # prepare the graph adjacency list
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        dist1 = [float("inf")] * (n + 1)
        dist2 = [float("inf")] * (n + 1)
        freq = [0] * (n + 1)
        queue = [(0, 1)]
        dist1[1] = 0

        while queue:
            timeTaken, node = heapq.heappop(queue)
            freq[node] += 1

            # If the node is being visited for the second time and is 'n', return the
            # answer.
            if freq[node] == 2 and node == n:
                return timeTaken
            # If the current light is red, wait till the path turns green.
            if (timeTaken // change) % 2:
                timeTaken = change * (timeTaken // change + 1) + time
            else:
                timeTaken = timeTaken + time

            for neighbor in adj[node]:
                # Ignore nodes that have already popped out twice, we are not interested in
                # visiting them again.
                if freq[neighbor] == 2:
                    continue

                # Update dist1 if it's more than the current timeTaken and store its value in
                # dist2 since that becomes the second minimum value now.
                if dist1[neighbor] > timeTaken:
                    dist2[neighbor] = dist1[neighbor]
                    dist1[neighbor] = timeTaken
                    heapq.heappush(queue, (timeTaken, neighbor))
                elif dist2[neighbor] > timeTaken and dist1[neighbor] != timeTaken:
                    dist2[neighbor] = timeTaken
                    heapq.heappush(queue, (timeTaken, neighbor))
        return 0

    @staticmethod
    def secondMinimum_bfs(
        n: int, edges: list[list[int]], time: int, change: int
    ) -> int:
        adj = defaultdict(list)
        for edge in edges:
            a, b = edge
            adj[a].append(b)
            adj[b].append(a)

        dist1, dist2 = [-1] * (n + 1), [-1] * (n + 1)
        queue = deque([(1, 1)])
        dist1[1] = 0

        while queue:
            node, freq = queue.popleft()
            timeTaken = dist1[node] if freq == 1 else dist2[node]

            if (timeTaken // change) % 2 == 1:
                timeTaken = change * (timeTaken // change + 1) + time
            else:
                timeTaken = timeTaken + time

            for neighbor in adj[node]:
                if dist1[neighbor] == -1:
                    dist1[neighbor] = timeTaken
                    queue.append((neighbor, 1))
                elif dist2[neighbor] == -1 and dist1[neighbor] != timeTaken:
                    if neighbor == n:
                        return timeTaken
                    dist2[neighbor] = timeTaken
                    queue.append((neighbor, 2))
        return 0

    @staticmethod
    def secondMinimum_leet(
        n: int, edges: list[list[int]], time: int, change: int
    ) -> int:
        D = [[] for _ in range(n + 1)]
        D[1] = [0]
        G, heap = defaultdict(list), [(0, 1)]

        for a, b in edges:
            G[a] += [b]
            G[b] += [a]

        while heap:
            min_dist, idx = heapq.heappop(heap)
            if idx == n and len(D[n]) == 2:
                return max(D[n])

            for neib in G[idx]:
                if (min_dist // change) % 2 == 0:
                    cand = min_dist + time
                else:
                    cand = math.ceil(min_dist / (2 * change)) * (2 * change) + time

                if not D[neib] or (len(D[neib]) == 1 and D[neib] != [cand]):
                    D[neib] += [cand]
                    heapq.heappush(heap, (cand, neib))


@pytest.mark.parametrize(
    "n,edges,time,change,expected",
    [
        (5, [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], 3, 5, 13),
        (2, [[1, 2]], 3, 2, 11),
    ],
)
def test_secondMinimum(n, edges, time, change, expected):
    assert Solution().secondMinimum(n, edges, time, change) == expected
