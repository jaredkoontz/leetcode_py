# https://leetcode.com/problems/range-sum-of-bst
import pytest

from helpers.bin_tree import TreeNode
from helpers.bin_tree import make_tree


class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        return self.rangeSumBST_dfs(root, low, high)

    @staticmethod
    def rangeSumBST_dfs(root: TreeNode | None, low: int, high: int) -> int:
        if not root:
            return 0
        total = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                total += node.val
            if node.left:
                if node.val > low:
                    stack.append(node.left)
            if node.right:
                if node.val < high:
                    stack.append(node.right)
        return total


@pytest.mark.parametrize(
    "root,low,high,expected",
    [
        ([10, 5, 15, 3, 7, None, 18], 7, 15, 32),
        ([10, 5, 15, 3, 7, 13, 18, 1, None, 6], 6, 10, 23),
    ],
)
def test_rangeSumBST(root, low, high, expected):
    assert Solution().rangeSumBST(make_tree(root), low, high) == expected
