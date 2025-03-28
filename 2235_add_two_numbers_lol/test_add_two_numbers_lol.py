# https://leetcode.com/problems/add-two-integers
import heapq

import pytest


class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return self.coward_sum(num1, num2)

    @staticmethod
    def binary_search_sum(num1: int, num2: int) -> int:
        """Binary search approach to find the sum."""
        left, right = -200, 200
        while left < right:
            mid = (left + right) >> 1
            if mid == num1 + num2:
                return mid
            if mid < num1 + num2:
                left = mid + 1
            else:
                right = mid - 1
        return left

    @staticmethod
    def brute_force_sum(num1: int, num2: int) -> int:
        """Brute force approach to find the sum."""
        for i in range(-200, 201):
            if num1 + num2 == i:
                return i
        return -1

    @staticmethod
    def dijkstra_sum(num1: int, num2: int) -> int:
        """Using Dijkstra's shortest path algorithm."""

        def _dfs(dest: int, source: int, adj: list[list[tuple]], dis: list[int]) -> int:
            """Helper function for Dijkstra's algorithm."""
            dis[source] = 0
            pq = [(0, source)]
            while pq:
                cur_dist, cur_node = heapq.heappop(pq)
                dis[cur_node] = cur_dist
                for neighbor, weight in adj[cur_node]:
                    if cur_dist + weight < dis[neighbor]:
                        heapq.heappush(pq, (cur_dist + weight, neighbor))
            return dis[dest]

        adj = [[] for _ in range(3)]
        dis = [float("inf")] * 3
        adj[0].append((1, num1))
        adj[1].append((2, num2))
        return _dfs(2, 0, adj, dis)

    @staticmethod
    def floyd_sum(num1: int, num2: int) -> int:
        """Using Floyd-Warshall shortest path algorithm."""

        def _floyd(dest: int, source: int, dis: list[list[int]]) -> int:
            """Helper function for Floyd-Warshall algorithm."""
            for k in range(3):
                for i in range(3):
                    for j in range(3):
                        dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
            return dis[source][dest]

        dis = [[10000] * 3 for _ in range(3)]
        dis[0][1] = num1
        dis[1][2] = num2
        return _floyd(2, 0, dis)

    @staticmethod
    def prefix_sum(num1: int, num2: int) -> int:
        """Prefix sum approach."""
        A = [num1, num2]
        prefix_sum = [0] * (len(A) + 1)
        for i in range(len(A)):
            prefix_sum[i + 1] = prefix_sum[i] + A[i]
        return prefix_sum[len(A)]

    @staticmethod
    def bit_manipulation_sum(num1: int, num2: int) -> int:
        """Using bitwise operations to compute sum."""

        def helper(n1, n2):
            if num2 == 0:
                return num1
            helper(n1 ^ n2, (n1 & n2) << 1)

        return helper(num1, num2)

    @staticmethod
    def divide_and_conquer_sum(num1: int, num2: int) -> int:
        """Divide and conquer approach."""

        def _divide_and_conquer(left: int, right: int, A: list[int]) -> int:
            """Helper function for divide and conquer approach."""
            if left == right:
                return A[left]
            m = (left + right) >> 1
            return _divide_and_conquer(left, m, A) + _divide_and_conquer(
                m + 1, right, A
            )

        A = [0, num1, num2]
        return _divide_and_conquer(1, 2, A)

    def bellman_ford_sum(self, num1: int, num2: int) -> int:
        """Using Bellman-Ford algorithm."""

        def _bellman_ford(src: int, dest: int, edges: list[tuple]) -> int:
            """Helper function for Bellman-Ford algorithm."""
            dis = [float("inf")] * 3
            dis[src] = 0
            for _ in range(2):
                for u, v, w in edges:
                    if dis[u] != float("inf") and dis[u] + w < dis[v]:
                        dis[v] = dis[u] + w
            return dis[dest]

        edges = [(0, 1, num1), (1, 2, num2)]
        return _bellman_ford(0, 2, edges)

    @staticmethod
    def exponentiation_by_squaring_sum(num1: int, num2: int) -> int:
        """Using exponentiation by squaring."""

        def pow_mod(x: int, exp: int, mod: int) -> int:
            if exp == 0:
                return 1
            t = pow_mod(x, exp // 2, mod)
            t = t * t % mod
            return t if exp % 2 == 0 else t * x % mod

        return pow_mod(num1, 1, int(1e9 + 7)) + pow_mod(num2, 1, int(1e9 + 7))

    @staticmethod
    def evaluation_of_string_expression_sum(num1: int, num2: int) -> int:
        """Evaluating the sum using string expression."""
        expression = f"{num1} + {num2}"
        return eval(expression)

    @staticmethod
    def coward_sum(num1, num2):
        # only for the craven
        return num1 + num2


@pytest.mark.parametrize(
    "num1,num2,expected",
    [
        (12, 5, 17),
        (-10, 4, -6),
    ],
)
def test_sum(num1, num2, expected):
    assert Solution().sum(num1, num2) == expected
