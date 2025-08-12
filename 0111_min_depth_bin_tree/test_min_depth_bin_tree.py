# https://leetcode.com/problems/minimum-depth-of-binary-tree
from collections import deque

import pytest

from helpers.bin_tree import TreeNode
from helpers.bin_tree import make_tree


class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        return self.minDepth_queue(root)

    @staticmethod
    def minDepth_queue(root: TreeNode | None) -> int:
        # If the tree is empty, return 0
        if root is None:
            return 0

        # Use BFS with a queue: each element is [node, depth]
        queue = deque([[root, 1]])

        while queue:
            # Pop the front of the queue
            u, d = queue.popleft()

            # If the node is a leaf, return its depth
            if u.left is None and u.right is None:
                return d

            # Add children to the queue if they exist
            if u.left is not None:
                queue.append([u.left, d + 1])
            if u.right is not None:
                queue.append([u.right, d + 1])

        # Should never reach here
        return -1

    @staticmethod
    def minDepth_rec(root: TreeNode | None) -> int:
        def helper(my_root):
            if not my_root:
                return 0

            if not my_root.left:
                return helper(my_root.right) + 1

            if not my_root.right:
                return helper(my_root.left) + 1

            return 1 + min(helper(my_root.left), helper(my_root.right))

        return helper(root)


@pytest.mark.parametrize(
    "s, expected",
    [
        ([3, 9, 20, None, None, 15, 7], 2),
        ([2, None, 3, None, 4, None, 5, None, 6], 5),
    ],
)
def test_findMinDepth(s, expected):
    root = make_tree(s)
    assert Solution().minDepth(root) == expected
