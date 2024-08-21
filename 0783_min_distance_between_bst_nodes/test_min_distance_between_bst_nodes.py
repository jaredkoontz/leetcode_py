# https://leetcode.com/problems/minimum-distance-between-bst-nodes
import pytest

from helpers.bin_tree import make_tree
from helpers.bin_tree import TreeNode


class Solution:
    def minDiffInBST(self, root: TreeNode | None) -> int:
        return self.minDiffInBST_stack(root)

    @staticmethod
    def minDiffInBST_morris(root: TreeNode | None) -> int:
        if not root:
            return 0

        min_diff = float("inf")
        pre = None
        while root:
            if not root.left:
                if pre:
                    min_diff = min(min_diff, root.val - pre.val)
                pre = root
                root = root.right
            else:
                max_right = root.left
                while max_right.right and max_right.right != root:
                    max_right = max_right.right
                if not max_right.right:
                    max_right.right = root
                    root = root.left
                else:
                    max_right.right = None
                    if pre:
                        min_diff = min(min_diff, root.val - pre.val)
                    pre = root
                    root = root.right
        return min_diff

    @staticmethod
    def minDiffInBST_stack(root: TreeNode | None) -> int:
        if not root:
            return 0

        stack = []
        min_diff = float("inf")
        pre = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre:
                min_diff = min(min_diff, root.val - pre.val)
            pre = root
            root = root.right
        return min_diff

    @staticmethod
    def minDiffInBST_recursive(root: TreeNode | None) -> int:
        def dfs(node, previous, min_diff):
            if not node:
                return previous
            previous = dfs(node.left, previous, min_diff)
            if previous:
                min_diff[0] = min(min_diff[0], node.val - previous.val)
            previous = node
            return dfs(node.right, previous, min_diff)

        if not root:
            return 0

        min_val = [float("inf")]
        dfs(root, None, min_val)
        return int(min_val[0])


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([4, 2, 6, 1, 3], 1),
        ([1, 0, 48, None, None, 12, 49], 1),
        ([27, None, 34, None, 58, 50, None, 44], 6),
    ],
)
def test_min_distance_between_bst_nodes(l1, expected):
    assert Solution().minDiffInBST(make_tree(l1)) == expected
