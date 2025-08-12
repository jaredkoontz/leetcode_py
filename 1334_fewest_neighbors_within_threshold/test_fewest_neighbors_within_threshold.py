# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance
import heapq
from collections import deque

import pytest


class Solution:
    def findTheCity(
        self, n: int, edges: list[list[int]], distanceThreshold: int
    ) -> int:
        return self.findTheCity_floyd_warshall(n, edges, distanceThreshold)

    @staticmethod
    def findTheCity_dijkstra(
        n: int, edges: list[list[int]], distanceThreshold: int
    ) -> int:
        def dijkstra(
            n: int,
            adjacency_list: list[list[tuple]],
            shortest_path_distances: list[int],
            source: int,
        ):
            # Priority queue to process nodes with the smallest distance first
            priority_queue = [(0, source)]
            shortest_path_distances[:] = [float("inf")] * n
            shortest_path_distances[source] = 0  # Distance to itself is zero

            # Process nodes in priority order
            while priority_queue:
                current_distance, current_city = heapq.heappop(priority_queue)
                if current_distance > shortest_path_distances[current_city]:
                    continue

                # Update distances to neighboring cities
                for neighbor_city, edge_weight in adjacency_list[current_city]:
                    if (
                        shortest_path_distances[neighbor_city]
                        > current_distance + edge_weight
                    ):
                        shortest_path_distances[neighbor_city] = (
                            current_distance + edge_weight
                        )
                        heapq.heappush(
                            priority_queue,
                            (shortest_path_distances[neighbor_city], neighbor_city),
                        )

            # Determine the city with the fewest number of reachable cities within the distance threshold

        def get_city_with_fewest_reachable(
            n: int,
            shortest_path_matrix: list[list[int]],
            distance_threshold: int,
        ) -> int:
            city_with_fewest_reachable = -1
            fewest_reachable_count = n

            # Count number of cities reachable within the distance threshold for each city
            for i in range(n):
                reachable_count = sum(
                    1
                    for j in range(n)
                    if i != j and shortest_path_matrix[i][j] <= distance_threshold
                )

                # Update the city with the fewest reachable cities
                if reachable_count <= fewest_reachable_count:
                    fewest_reachable_count = reachable_count
                    city_with_fewest_reachable = i
            return city_with_fewest_reachable

        # Adjacency list to store the graph
        adjacency_list = [[] for _ in range(n)]

        # Matrix to store shortest path distances from each city
        shortest_path_matrix = [[float("inf")] * n for _ in range(n)]

        # Initialize adjacency list and shortest path matrix
        for i in range(n):
            shortest_path_matrix[i][i] = 0  # Distance to itself is zero

        # Populate the adjacency list with edges
        for start, end, weight in edges:
            adjacency_list[start].append((end, weight))
            adjacency_list[end].append((start, weight))  # For undirected graph

        # Compute shortest paths from each city using Dijkstra's algorithm
        for i in range(n):
            dijkstra(n, adjacency_list, shortest_path_matrix[i], i)

        # Find the city with the fewest number of reachable cities within the distance threshold
        return get_city_with_fewest_reachable(
            n, shortest_path_matrix, distanceThreshold
        )

    @staticmethod
    def findTheCity_bellman_ford(
        n: int, edges: list[list[int]], distanceThreshold: int
    ) -> int:
        def bellmanFord(
            n: int,
            edges: list[list[int]],
            shortestPathDistances: list[int],
            source: int,
        ) -> None:
            # Initialize distances from the source
            shortestPathDistances[:] = [float("inf")] * n
            shortestPathDistances[source] = 0  # Distance to source itself is zero

            # Relax edges up to n-1 times with early stopping
            for _ in range(n - 1):
                updated = False
                for start, end, weight in edges:
                    if (
                        shortestPathDistances[start] != float("inf")
                        and shortestPathDistances[start] + weight
                        < shortestPathDistances[end]
                    ):
                        shortestPathDistances[end] = (
                            shortestPathDistances[start] + weight
                        )
                        updated = True
                    if (
                        shortestPathDistances[end] != float("inf")
                        and shortestPathDistances[end] + weight
                        < shortestPathDistances[start]
                    ):
                        shortestPathDistances[start] = (
                            shortestPathDistances[end] + weight
                        )
                        updated = True
                if not updated:
                    break  # Stop early if no updates

            # Determine the city with the fewest number of reachable cities within the distance threshold

        def getCityWithFewestReachable(
            n: int,
            shortestPathMatrix: list[list[int]],
            distanceThreshold: int,
        ) -> int:
            cityWithFewestReachable = -1
            fewestReachableCount = n

            # Count number of cities reachable within the distance threshold for each city
            for i in range(n):
                reachableCount = 0
                for j in range(n):
                    if i == j:
                        continue  # Skip self
                    if shortestPathMatrix[i][j] <= distanceThreshold:
                        reachableCount += 1

                # Update the city with the fewest reachable cities
                if reachableCount <= fewestReachableCount:
                    fewestReachableCount = reachableCount
                    cityWithFewestReachable = i
            return cityWithFewestReachable

        # Large value to represent infinity
        INF = int(1e9) + 7
        # Matrix to store shortest path distances from each city
        shortestPathMatrix = [[INF] * n for _ in range(n)]

        # Initialize shortest path matrix
        for i in range(n):
            shortestPathMatrix[i][i] = 0

        # Populate the matrix with initial edge weights
        for start, end, weight in edges:
            shortestPathMatrix[start][end] = weight
            shortestPathMatrix[end][start] = weight  # For undirected graph

        # Compute shortest paths from each city using Bellman-Ford algorithm
        for i in range(n):
            bellmanFord(n, edges, shortestPathMatrix[i], i)

        # Find the city with the fewest number of reachable cities within the distance threshold
        return getCityWithFewestReachable(n, shortestPathMatrix, distanceThreshold)

        # Bellman-Ford algorithm to find shortest paths from a source city

    @staticmethod
    def findTheCity_spfa(n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        def spfa(
            self,
            n: int,
            adjacency_list: list[list[tuple]],
            shortest_path_distances: list[int],
            source: int,
        ):
            # Queue to process nodes with updated shortest path distances
            queue = deque([source])
            update_count = [0] * n
            shortest_path_distances[:] = [float("inf")] * n
            shortest_path_distances[source] = 0  # Dist to source itself is zero

            # Process nodes in queue
            while queue:
                current_city = queue.popleft()
                for neighbor_city, edge_weight in adjacency_list[current_city]:
                    if (
                        shortest_path_distances[neighbor_city]
                        > shortest_path_distances[current_city] + edge_weight
                    ):
                        shortest_path_distances[neighbor_city] = (
                            shortest_path_distances[current_city] + edge_weight
                        )
                        update_count[neighbor_city] += 1
                        queue.append(neighbor_city)

                        # Detect negative weight cycles (not expected in this problem)

                        if update_count[neighbor_city] > n:
                            print("Negative weight cycle detected")

            # Determine the city with the fewest number of reachable cities within the distance threshold

        def get_city_with_fewest_reachable(
            n: int,
            shortest_path_matrix: list[list[int]],
            distance_threshold: int,
        ) -> int:
            city_with_fewest_reachable = -1
            fewest_reachable_count = n
            # Count number of cities reachable within the distance threshold for each city
            for i in range(n):
                reachable_count = sum(
                    1
                    for j in range(n)
                    if i != j and shortest_path_matrix[i][j] <= distance_threshold
                )
                # Update the city with the fewest reachable cities
                if reachable_count <= fewest_reachable_count:
                    fewest_reachable_count = reachable_count
                    city_with_fewest_reachable = i

            return city_with_fewest_reachable

        # Adjacency list to store the graph
        adjacency_list = [[] for _ in range(n)]
        # Matrix to store shortest path distances from each city
        shortest_path_matrix = [[float("inf")] * n for _ in range(n)]

        # Initialize adjacency list and shortest path matrix
        for i in range(n):
            shortest_path_matrix[i][i] = 0  # Dist to itself is zero

        # Populate the adjacency list with edges
        for start, end, weight in edges:
            adjacency_list[start].append((end, weight))
            adjacency_list[end].append((start, weight))  # For undirected

        # Compute shortest paths from each city using SPFA algorithm
        for i in range(n):
            spfa(n, adjacency_list, shortest_path_matrix[i], i)

        # Find the city with the fewest number of reachable cities within the distance threshold
        return get_city_with_fewest_reachable(
            n, shortest_path_matrix, distanceThreshold
        )

        # SPFA algorithm to find shortest paths from a source city

    @staticmethod
    def findTheCity_floyd_warshall(
        n: int, edges: list[list[int]], distanceThreshold: int
    ) -> int:
        # Floyd-Warshall algorithm to compute shortest paths between all pairs of cities
        def floyd(n: int, distance_matrix: list[list[int]]):
            # Update distances for each intermediate city

            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        # Update shortest path from i to j through k
                        distance_matrix[i][j] = min(
                            distance_matrix[i][j],
                            distance_matrix[i][k] + distance_matrix[k][j],
                        )

        # Determine the city with the fewest number of reachable cities within the distance threshold
        def get_city_with_fewest_reachable(
            n: int, distance_matrix: list[list[int]], distance_threshold: int
        ) -> int:
            city_with_fewest_reachable = -1
            fewest_reachable_count = n

            # Count number of cities reachable within the distance threshold for each city
            for i in range(n):
                reachable_count = sum(
                    1
                    for j in range(n)
                    if i != j and distance_matrix[i][j] <= distance_threshold
                )
                # Update the city with the fewest reachable cities
                if reachable_count <= fewest_reachable_count:
                    fewest_reachable_count = reachable_count
                    city_with_fewest_reachable = i
            return city_with_fewest_reachable

        # Large value to represent infinity
        INF = int(1e9 + 7)
        # Distance matrix to store shortest paths between all pairs of cities
        distance_matrix = [[INF] * n for _ in range(n)]

        # Initialize distance matrix
        for i in range(n):
            distance_matrix[i][i] = 0  # Distance to itself is zero

        # Populate the distance matrix with initial edge weights
        for start, end, weight in edges:
            distance_matrix[start][end] = weight
            distance_matrix[end][start] = weight  # For undirected graph

        # Compute shortest paths using Floyd-Warshall algorithm
        floyd(n, distance_matrix)

        # Find the city with the fewest number of reachable cities within the distance threshold
        return get_city_with_fewest_reachable(n, distance_matrix, distanceThreshold)


@pytest.mark.parametrize(
    "n,edges,dist,expected",
    [
        (4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4, 3),
        (5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2, 0),
    ],
)
def test_findTheCity(n, edges, dist, expected):
    assert Solution().findTheCity(n, edges, dist) == expected
