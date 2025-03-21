# https://leetcode.com/problems/find-eventual-safe-states
import pytest


class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        return self.eventualSafeNodes_iter(graph)

    @staticmethod
    def eventualSafeNodes_rec(graph: list[list[int]]) -> list[int]:
        def dfs(src):
            visited[src] = True

            node = graph[src]
            for neighbor in node:
                if not visited[neighbor] and dfs(neighbor):
                    return True
                if not can_exit[neighbor]:
                    return True
            can_exit[src] = True
            return False

        n = len(graph)
        visited = [False] * n
        can_exit = [False] * n

        for i in range(n):
            if not visited[i]:
                dfs(i)

        return [i for i in range(n) if can_exit[i]]

    @staticmethod
    def eventualSafeNodes_iter(graph: list[list[int]]) -> list[int]:
        def is_safe(adj: list[int]):
            return not adj or all([can_exit[neigh] for neigh in adj])

        if not graph:
            return []

        n = len(graph)
        visited = [False] * n
        can_exit = [False] * n

        stack = [x for x in range(len(graph))]
        while stack:
            node = stack.pop()
            adj_list = graph[node]
            visited[node] = True

            if is_safe(adj_list):
                can_exit[node] = True

            for neighbor in adj_list:
                if not visited[neighbor]:
                    stack.append(node)
                    stack.append(neighbor)
        return [i for i in range(n) if can_exit[i]]


@pytest.mark.parametrize(
    "graph,expected",
    [
        ([[], [0, 2, 3, 4], [3], [4], []], [0, 1, 2, 3, 4]),
        ([[1, 2], [2, 3], [5], [0], [5], [], []], [2, 4, 5, 6]),
        ([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []], [4]),
        ([[1], [0], []], [2]),
        ([[1], [0], [0]], []),
    ],
)
def test_eventualSafeNodes(graph, expected):
    assert Solution().eventualSafeNodes(graph) == expected
