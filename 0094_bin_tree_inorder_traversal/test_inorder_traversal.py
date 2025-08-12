# https://leetcode.com/problems/binary-tree-inorder-traversal
import pytest

from helpers.bin_tree import make_tree
from helpers.bin_tree import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        return self.inorderTraversal_stack(root)

    @staticmethod
    def inorderTraversal_stack(root: TreeNode | None) -> list[int]:
        result = []
        stack = []
        current = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result

    @staticmethod
    def inorderTraversal_rec(root: TreeNode | None) -> list[int]:
        my_list = []

        def inorder(node):
            if node:
                inorder(node.left)
                my_list.append(node.val)
                inorder(node.right)

        inorder(root)
        return my_list


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([1, None, 2, 3], [1, 3, 2]),
        ([1, 4, 2, 3], [3, 4, 1, 2]),
        ([1, 5, 2, 3, 4], [3, 5, 4, 1, 2]),
        ([], []),
        ([1], [1]),
    ],
)
def test_inorderTraversal(l1, expected):
    assert Solution().inorderTraversal(make_tree(l1)) == expected
