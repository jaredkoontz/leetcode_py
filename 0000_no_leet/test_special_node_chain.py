from collections import deque

import pytest

from helpers.bin_tree import make_tree
from helpers.bin_tree import TreeNode


"""
The problem :
There is a binary tree (a sample tree was made with “/”, “\” ). Tree has total three kind of nodes.

Normal nodes : with two children
Leaf nodes : no children
Special nodes : only one children.
Multiple consecutive Special nodes make a Special nodes Chain.
like (a → b → c) are the node chain, so length is 3 here.
"""


def find_max_chain(root: TreeNode) -> int:
    return _find_max_chain_queue(root)


def _find_max_chain_rec(root: TreeNode) -> int:
    if not root:
        return 0

    max_length = 0

    def dfs(node, chain_length):
        nonlocal max_length
        max_length = max(max_length, chain_length)

        # leaf node
        if not node.left and not node.right:
            return

        # normal node
        if node.left and node.right:
            dfs(node.left, 1)
            dfs(node.right, 1)
        elif node.left:  # special
            dfs(node.left, chain_length + 1)
        else:  # special
            dfs(node.right, chain_length + 1)

        return

    dfs(root, 1)
    return max_length


def _find_max_chain_queue(root: TreeNode) -> int:
    if not root:
        return 0

    queue = deque()
    first_stop = (root, 1)
    queue.append(first_stop)
    max_chain = float("-inf")

    while queue:
        node, current_chain = queue.popleft()
        # xor operator
        max_chain = max(current_chain, max_chain)
        if bool(node.left) != bool(node.right):
            current_chain += 1
        else:
            current_chain = 1
        if node.left:
            queue.append((node.left, current_chain))
        if node.right:
            queue.append((node.right, current_chain))

    return max_chain


def find_all_chains(root: TreeNode) -> dict[int, list[int]]:
    return _find_all_chains_queue(root)


# todo finish
def _find_all_chains_rec(root: TreeNode) -> dict[int, list[int]]:
    def dfs(node, chain_length):
        # leaf node
        if not node.left and not node.right:
            if chain_length > 0:
                unique_chain_length[chain_length] += 1
            return

        # normal node
        if node.left and node.right:
            if chain_length > 0:
                unique_chain_length[chain_length] += 1
            dfs(node.left, 0)
            dfs(node.right, 0)
        elif node.left:  # special
            dfs(node.left, chain_length + 1)
        else:  # special
            dfs(node.right, chain_length + 1)

        return

    unique_chain_length = {}

    dfs(root, 0)
    return unique_chain_length


def _find_all_chains_queue(root: TreeNode) -> dict[int, list[int]]:
    if not root:
        return {}

    chain_map = {}
    queue = deque()
    first_stop = (root, 1, [root.val])
    queue.append(first_stop)

    while queue:
        node, current_chain_length, current_chain = queue.popleft()

        if bool(node.left) != bool(node.right):
            current_chain_length += 1
        else:
            if chain_map.get(current_chain_length):
                chain_map[current_chain_length] += current_chain
            else:
                chain_map[current_chain_length] = current_chain
            current_chain_length = 1
            current_chain = []

        if node.left:
            queue.append(
                (node.left, current_chain_length, current_chain + [node.left.val])
            )
        if node.right:
            queue.append(
                (node.right, current_chain_length, current_chain + [node.right.val])
            )

    return chain_map


@pytest.mark.parametrize(
    "root,expected",
    [
        ([1, None, 2], 2),
        ([1, None, 2, None, 3], 3),
        ([4, 7, 2, 9, 6, 3, 1], 1),
        ([2, 3, 1], 1),
        ([], 0),
    ],
)
def test_find_max_chain(root, expected):
    assert find_max_chain(make_tree(root)) == expected


@pytest.mark.parametrize(
    "root,expected",
    [
        ([1, None, 2], {2: [1, 2]}),
        ([1, None, 2, None, 3], {3: [1, 2, 3]}),
        ([4, 7, 2, 9, 6, 3, 1], {1: [4, 7, 2, 9, 6, 3, 1]}),
        ([2, 3, 1], {1: [2, 3, 1]}),
        ([], {}),
    ],
)
def test_find_all_chains(root, expected):
    assert find_all_chains(make_tree(root)) == expected
