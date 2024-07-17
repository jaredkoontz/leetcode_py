from collections import deque

import pytest

from helpers.bin_tree import make_tree
from helpers.bin_tree import TreeNode
from helpers.test_helpers import compare_flat_lists


class Solution:
    def delNodes(self, root: TreeNode | None, to_delete: list[int]) -> list[TreeNode]:
        return self.delNodes_stack(root, to_delete)

    @staticmethod
    def delNodes_stack(root: TreeNode | None, to_delete: list[int]) -> list[TreeNode]:
        target = set(to_delete)
        res = []
        if root is None:
            return res
        stack = [(root, True)]
        while stack:
            curr_node, is_root = stack.pop()
            if curr_node.val in target:
                if curr_node.left:
                    stack.append((curr_node.left, True))
                if curr_node.right:
                    stack.append((curr_node.right, True))
            else:
                if is_root:
                    res.append(curr_node)
                if curr_node.left:
                    next_node = curr_node.left
                    if curr_node.left.val in target:
                        curr_node.left = None
                    stack.append((next_node, False))
                if curr_node.right:
                    next_node = curr_node.right
                    if curr_node.right.val in target:
                        curr_node.right = None
                    stack.append((next_node, False))

        return res

    @staticmethod
    def delNodes_q(root: TreeNode | None, to_delete: list[int]) -> list[TreeNode]:
        ans = []
        target = set(to_delete)

        queue = deque([(root, True)])

        while queue:
            curr_node, is_root = queue.popleft()
            if curr_node.val in target:
                if curr_node.left:
                    queue.append((curr_node.left, True))
                if curr_node.right:
                    queue.append((curr_node.right, True))
            else:
                if is_root:
                    ans.append(curr_node)
                if curr_node.left:
                    next_node = curr_node.left
                    if curr_node.left.val in target:
                        curr_node.left = None
                    queue.append((next_node, False))
                if curr_node.right:
                    next_node = curr_node.right
                    if curr_node.right.val in target:
                        curr_node.right = None
                    queue.append((next_node, False))

        return ans

    @staticmethod
    def delNodes_rec(root: TreeNode | None, to_delete: list[int]) -> list[TreeNode]:
        to_delete = set(to_delete)
        res = []

        def walk(node, parent_exist):
            if node is None:
                return None
            if node.val in to_delete:
                node.left = walk(node.left, parent_exist=False)
                node.right = walk(node.right, parent_exist=False)
                return None
            else:
                if not parent_exist:
                    res.append(node)
                node.left = walk(node.left, parent_exist=True)
                node.right = walk(node.right, parent_exist=True)
                return node

        walk(root, parent_exist=False)
        return res


@pytest.mark.parametrize(
    "root,to_delete,expected",
    [
        ([1, 2, 3, 4, 5, 6, 7], [3, 5], [[1, 2, None, 4], [6], [7]]),
        ([1, 2, 4, None, 3], [3], [[1, 2, 4]]),
    ],
)
def test_delete_nodes_return_forest(root, to_delete, expected):
    expected_forest = [make_tree(tree) for tree in expected]
    compare_flat_lists(Solution().delNodes(make_tree(root), to_delete), expected_forest)
