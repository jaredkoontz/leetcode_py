# https://leetcode.com/problems/path-with-maximum-probability
import heapq
from collections import defaultdict
from collections import deque

import pytest


class State:
    def __init__(self, node: int, prob: float):
        self.node = node
        self.prob = prob

    def __str__(self):
        return f"{self.node=} {self.prob=}"

    def __lt__(self, other):
        # Reverse order to create a max-heap based on probability
        return self.prob > other.prob


def _create_graph(edges: list[list[int]], succProb: list[float]):
    graph = defaultdict(list)
    for i, (u, v) in enumerate(edges):
        graph[u].append((v, succProb[i]))
        graph[v].append((u, succProb[i]))
    return graph


class Solution:
    def maxProbability(
            self,
            n: int,
            edges: list[list[int]],
            succProb: list[float],
            start_node: int,
            end_node: int,
    ) -> float:
        return self.maxProbability_bfs(n, edges, succProb, start_node, end_node)

    @staticmethod
    def maxProbability_dijkstra(
            n: int,
            edges: list[list[int]],
            succProb: list[float],
            start_node: int,
            end_node: int,
    ) -> float:
        graph = _create_graph(edges, succProb)

        probs = [0.0] * n
        probs[start_node] = 1.0
        pq = []
        heapq.heappush(pq, State(start_node, 1.0))

        while pq:
            state = heapq.heappop(pq)
            parent = state.node
            prob = state.prob

            if parent == end_node:
                return prob

            for child, edge_prob in graph[parent]:
                new_prob = prob * edge_prob
                if new_prob > probs[child]:
                    probs[child] = new_prob
                    heapq.heappush(pq, State(child, new_prob))

        return 0.0

    @staticmethod
    def maxProbability_bfs(
            n: int,
            edges: list[list[int]],
            succProb: list[float],
            start_node: int,
            end_node: int,
    ) -> float:
        graph = _create_graph(edges, succProb)
        probs = [0.0] * n
        queue = deque([State(start_node, 1.0)])

        while queue:
            state = queue.popleft()
            parent, prob = state.node, state.prob

            for neighbor, edge_prob in graph[parent]:
                new_prob = prob * edge_prob
                if new_prob > probs[neighbor]:
                    probs[neighbor] = new_prob
                    queue.append(State(neighbor, new_prob))

        return probs[end_node]


@pytest.mark.parametrize(
    "n,edges,succProb,start,end,expected",
    [
        (3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2, 0.25000),
        (3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2, 0.30000),
        (3, [[0, 1]], [0.5], 0, 2, 0.00000),
    ],
)
def test_maxProbability(n, edges, succProb, start, end, expected):
    assert Solution().maxProbability(n, edges, succProb, start, end) == expected
