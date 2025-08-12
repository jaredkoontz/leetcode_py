# https://leetcode.com/problems/validate-binary-search-tree
import pytest

from helpers.bin_tree import TreeNode
from helpers.bin_tree import make_tree


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        return self.isValidBST_iter(root)

    @staticmethod
    def isValidBST_rec(root: TreeNode | None) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if node.val <= left or node.val >= right:
                return False
            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf"))

    @staticmethod
    def isValidBST_iter(root: TreeNode | None) -> bool:
        if root is None:
            return True
        stack = []
        pre = None
        while root is not None or stack:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre is not None and root.val <= pre.val:
                return False
            pre = root
            root = root.right

        return True


@pytest.mark.parametrize(
    "root,expected",
    [
        ([5, 4, 6, None, None, 3, 7], False),
        ([2, 1, 3], True),
        ([2, 2, 2], False),
        ([5, 1, 4, None, None, 3, 6], False),
    ],
)
def test_isValidBST(root, expected):
    assert Solution().isValidBST(make_tree(root)) == expected
