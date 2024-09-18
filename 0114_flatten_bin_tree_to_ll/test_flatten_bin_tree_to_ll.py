# https://leetcode.com/problems/flatten-binary-tree-to-linked-list
import pytest

from helpers.bin_tree import compare_trees
from helpers.bin_tree import make_tree
from helpers.bin_tree import TreeNode


class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        return self.flatten_rec(root)

    @staticmethod
    def flatten_rec(root: TreeNode | None) -> None:
        def pre_order(node):
            nonlocal prev
            if not node:
                return None
            pre_order(node.right)
            pre_order(node.left)

            node.right = prev
            node.left = None
            prev = node

        prev = None
        return pre_order(root)

    @staticmethod
    def flatten_iter(root: TreeNode | None) -> None:
        if not root:
            return None
        stack = [root]
        prev = root
        while stack:
            # pre order
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            # change to new right
            prev = node
            if stack:
                new_right = stack.pop()
                prev.right = new_right
                prev.left = None
                stack.append(new_right)


@pytest.mark.parametrize(
    "root,expected",
    [
        ([1, 2, 5, 3, 4, None, 6], [1, None, 2, None, 3, None, 4, None, 5, None, 6]),
        ([], []),
        ([0], [0]),
    ],
)
def test_flatten(root, expected):
    root_tree = make_tree(root)
    Solution().flatten(root_tree)
    assert compare_trees(root_tree, make_tree(expected))
