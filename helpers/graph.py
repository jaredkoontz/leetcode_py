from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self):
        return f"{self.val=} {self.neighbors=}"


def create_graph(adj_list: list[list[int]]) -> Node | None:
    vertex_count = len(adj_list)
    vertex_list = [Node(i) for i in range(vertex_count)]
    for i, origin in enumerate(vertex_list):
        edges = adj_list[i]
        for edge in edges:
            node = vertex_list[edge]
            origin.neighbors.append(node)

    return vertex_list[0] if len(vertex_list) > 0 else None


def create_adj_list(node: Node) -> list[list[int]]:
    queue = [node]
    visited = set()
    all_nodes = []

    while queue:
        current = queue.pop(0)
        if current.val not in visited:
            visited.add(current.val)
            all_nodes.append(current)
            for neighbor in current.neighbors:
                if neighbor.val not in visited:
                    queue.append(neighbor)

    # Create a map from node value to index
    val_to_index = {node.val: index for index, node in enumerate(all_nodes)}

    # Create the adjacency list
    adjacency_list = [[] for _ in range(len(all_nodes))]

    for node in all_nodes:
        node_index = val_to_index[node.val]
        for neighbor in node.neighbors:
            neighbor_index = val_to_index[neighbor.val]
            adjacency_list[node_index].append(neighbor_index)

    return adjacency_list


def is_same_graph(a: Node, b: Node):
    """currently must start from same node"""
    if a is None and b is None:
        return True
    elif a is None or b is None:
        return False

    a_visited = set()
    b_visited = set()
    if a.val != b.val:
        return False

    queue = deque([(a, b)])

    while queue:
        a, b = queue.pop()
        if a.val != b.val:
            return False

        a_visited.add(a)
        b_visited.add(b)

        a_neigh = sorted(a.neighbors, key=lambda x: x.val)
        b_neigh = sorted(b.neighbors, key=lambda x: x.val)

        for a_nei, b_nei in zip(a_neigh, b_neigh):
            if a_nei not in a_visited and b_nei not in b_visited:
                queue.appendleft((a_nei, b_nei))
            elif (a_nei not in a_visited) ^ (b_nei not in b_visited):
                return False

    return True
