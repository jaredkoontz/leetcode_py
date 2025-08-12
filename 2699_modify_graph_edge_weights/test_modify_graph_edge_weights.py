# https://leetcode.com/problems/modify-graph-edge-weights
import heapq

import pytest

from helpers.testing_helpers import freeze_nested_lists


class Solution:
    def modifiedGraphEdges(
            self, n: int, edges: list[list[int]], source: int, destination: int, target: int
    ) -> list[list[int]]:
        return self.modifiedGraphEdges_dijkstra(n, edges, source, destination, target)

    @staticmethod
    def modifiedGraphEdges_dijkstra(
            n: int, edges: list[list[int]], source: int, destination: int, target: int
    ) -> list[list[int]]:
        def fill(edges):
            for edge in edges:
                if edge[2] == -1:
                    edge[2] = int(2e9)
            return edges

        def dijkstra(adjs, distTo, pq):
            while pq:
                curr_dist, curr = heapq.heappop(pq)

                for next_node, weight in adjs[curr].items():
                    if weight > 0:
                        if distTo[next_node] - weight > distTo[curr]:
                            distTo[next_node] = distTo[curr] + weight
                            heapq.heappush(pq, (distTo[next_node], next_node))

        adjs = [{} for _ in range(n)]

        for edge in edges:
            adjs[edge[0]][edge[1]] = edge[2]
            adjs[edge[1]][edge[0]] = edge[2]

        distTo = [float("inf")] * n
        distTo[source] = 0

        pq = [(0, source)]
        heapq.heapify(pq)

        dijkstra(adjs, distTo, pq)

        if distTo[destination] == target:
            return fill(edges)
        elif distTo[destination] < target:
            return []

        for edge in edges:
            if edge[2] == -1:
                edge[2] = 1
                adjs[edge[0]][edge[1]] = 1
                adjs[edge[1]][edge[0]] = 1

                pq = [(distTo[edge[0]], edge[0]), (distTo[edge[1]], edge[1])]

                dijkstra(adjs, distTo, pq)

                if distTo[destination] == target:
                    return fill(edges)
                elif distTo[destination] < target:
                    edge[2] += target - distTo[destination]
                    adjs[edge[0]][edge[1]] = edge[2]
                    adjs[edge[1]][edge[0]] = edge[2]
                    return fill(edges)

        return []


@pytest.mark.parametrize(
    "n,edges,source,destination,target,expected",
    [
        (
                5,
                [[4, 1, -1], [2, 0, -1], [0, 3, -1], [4, 3, -1]],
                0,
                1,
                5,
                [[4, 1, 1], [2, 0, 1], [0, 3, 1], [4, 3, 3]],
        ),
        (3, [[0, 1, -1], [0, 2, 5]], 0, 2, 6, []),
        (
                4,
                [[1, 0, 4], [1, 2, 3], [2, 3, 5], [0, 3, -1]],
                0,
                2,
                6,
                [[1, 0, 4], [1, 2, 3], [2, 3, 5], [0, 3, 1]],
        ),
    ],
)
def test_modifiedGraphEdges(n, edges, source, destination, target, expected):
    frozen1, frozen2 = freeze_nested_lists(
        Solution().modifiedGraphEdges(n, edges, source, destination, target), expected
    )
    assert frozen1 == frozen2
