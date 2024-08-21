# https://leetcode.com/problems/invert-binary-tree
import pytest

from helpers.bin_tree import compare_trees
from helpers.bin_tree import make_tree
from helpers.bin_tree import TreeNode


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        return self.invertTree_recursive(root)

    @staticmethod
    def invertTree_recursive(root: TreeNode | None) -> TreeNode | None:
        def invert(node: TreeNode | None) -> TreeNode | None:
            if node is None:
                return
            node.left, node.right = node.right, node.left
            invert(node.left)
            invert(node.right)

        invert(root)
        return root

    @staticmethod
    def invertTree_stack(root: TreeNode | None) -> TreeNode | None:
        if not root:
            return

        stack = [root]
        while stack:
            node = stack.pop()
            left, right = node.left, node.right
            node.left, node.right = right, left
            if left:
                stack.append(left)
            if right:
                stack.append(right)
        return root


@pytest.mark.parametrize(
    "root,expected",
    [
        ([1, 2], [1, None, 2]),
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ([2, 1, 3], [2, 3, 1]),
        ([], []),
    ],
)
def test_invert_binary_tree(root, expected):
    assert compare_trees(Solution().invertTree(make_tree(root)), make_tree(expected))
