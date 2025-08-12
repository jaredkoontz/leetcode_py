# https://leetcode.com/problems/binary-tree-preorder-traversal
import pytest

from helpers.bin_tree import make_tree
from helpers.bin_tree import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        return self.preorderTraversal_iter(root)

    @staticmethod
    def preorderTraversal_iter(root: TreeNode | None) -> list[int]:
        result = []
        if not root:
            return result

        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

    @staticmethod
    def preorderTraversal_rec(root: TreeNode | None) -> list[int]:
        my_list = []

        def preorder(node):
            if node:
                my_list.append(node.val)
                preorder(node.left)
                preorder(node.right)

        preorder(root)
        return my_list


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([1, None, 2, 3], [1, 2, 3]),
        ([1, 4, 2, 3], [1, 4, 3, 2]),
        ([1, 5, 2, 3, 4], [1, 5, 3, 4, 2]),
        ([], []),
        ([1], [1]),
    ],
)
def test_preorderTraversal(l1, expected):
    assert Solution().preorderTraversal(make_tree(l1)) == expected
