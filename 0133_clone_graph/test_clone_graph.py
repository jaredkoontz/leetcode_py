# https://leetcode.com/problems/clone-graph
from collections import deque

import pytest

from helpers.graph import create_adj_list
from helpers.graph import create_graph
from helpers.graph import is_same_graph
from helpers.graph import Node


class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:
        return self.cloneGraph_bfs(node)

    @staticmethod
    def cloneGraph_recursive(node: Node | None) -> Node | None:
        if not node:
            return None

        clones = {}

        def clone(n: Node):
            if n not in clones:
                clones[n] = Node(n.val)
                clones[n].neighbors = list(map(clone, n.neighbors))

            return clones[n]

        return clone(node)

    @staticmethod
    def cloneGraph_dfs(node: Node | None) -> Node | None:
        if not node:
            return node

            # create new root
        root = Node(node.val)
        # use stack to DFS through all the nodes
        stack = [node]
        # because "Node.val is unique for each node", use a hashmap to store each node
        # in order to check if a node has been visited
        nodes = {node.val: root}

        while stack:
            top = stack.pop()

            for neighbor in top.neighbors:
                if neighbor.val not in nodes:
                    # for the nodes haven't been visited
                    stack.append(neighbor)
                    nodes[neighbor.val] = Node(neighbor.val)
                nodes[top.val].neighbors.append(nodes[neighbor.val])

        return root

    @staticmethod
    def cloneGraph_bfs(node: Node | None) -> Node | None:
        if not node:
            return None

        root = Node(node.val)
        val_node_map = {node.val: root}

        visited = {node}
        queue = deque([node])
        while queue:
            temp = queue.pop()
            for neigh in temp.neighbors:
                if neigh.val not in val_node_map:
                    val_node_map[neigh.val] = Node(neigh.val)
                val_node_map[temp.val].neighbors.append(val_node_map[neigh.val])
                if neigh not in visited:
                    visited.add(neigh)
                    queue.appendleft(neigh)

        return root


@pytest.mark.parametrize(
    "adj_list,expected",
    [
        ([[1], [0, 2], [1]], [[1], [0, 2], [1]]),
        ([[]], [[]]),
    ],
)
def test_cloneGraph(adj_list, expected):
    first_graph = create_graph(adj_list)
    assert create_adj_list(first_graph) == expected
    second_graph = Solution().cloneGraph(first_graph)
    assert create_adj_list(second_graph) == expected
    assert is_same_graph(first_graph, second_graph)
