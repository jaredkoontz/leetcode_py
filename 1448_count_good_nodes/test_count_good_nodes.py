# https://leetcode.com/problems/count-good-nodes-in-binary-tree
from collections import deque

import pytest

from helpers.bin_tree import TreeNode
from helpers.bin_tree import make_tree


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodes_queue(root)

    @staticmethod
    def goodNodes_queue(root: TreeNode) -> int:
        good_nodes = 0
        queue = deque()

        queue.append((root, float("-inf")))
        while queue:
            node, parent_val = queue.popleft()
            if parent_val <= node.val:
                good_nodes += 1
            if node.left:
                queue.append((node.left, max(node.val, parent_val)))
            if node.right:
                queue.append((node.right, max(node.val, parent_val)))
        return good_nodes

    @staticmethod
    def goodNodes_rec(root: TreeNode) -> int:
        # dfs recurse down the tree with a maxValue that you update
        # have dfs take max value, have res = 1 if value of tree is <= maxVal else 0
        # update max value
        # recurse left and right with new max value
        # if not root return 0
        def dfs(node, max_val):
            if not node:
                return 0

            res = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)
            res += dfs(node.left, max_val)
            res += dfs(node.right, max_val)
            return res

        return dfs(root, root.val)


@pytest.mark.parametrize(
    "root,expected",
    [
        ([0, None, 1, 2, 3, None, None, 4, 5, None, 6, None, None, None, 7], 8),
        ([0, None, 1, 2, 3, None, None, 4, None, None, 6, None, None, None, 7], 6),
        ([1, 1, 1, None, 1, None, None, 1, 1, None, 1], 7),
        ([1], 1),
        ([3, 1, 4, 3, None, 1, 5], 4),
        ([3, 3, None, 4, 2], 3),
    ],
)
def test_goodNodes(root, expected):
    assert Solution().goodNodes(make_tree(root)) == expected
