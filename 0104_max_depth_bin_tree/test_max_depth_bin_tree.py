# https://leetcode.com/problems/maximum-depth-of-binary-tree
import collections

import pytest

from helpers.bin_tree import TreeNode
from helpers.bin_tree import make_tree


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        assert (
                self.maxDepth_bfs(root)
                == self.maxDepth_dfs(root)
                == self.maxDepth_rec(root)
        )
        return self.maxDepth_bfs(root)

    @staticmethod
    def maxDepth_bfs(root: TreeNode | None) -> int:
        if not root:
            return 0

        queue = collections.deque()
        curr_max = -1
        if root:
            queue.append((root, 1))

        while queue:
            node, depth = queue.popleft()
            curr_max = max(curr_max, depth)

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.appendleft((node.right, depth + 1))

        return curr_max

    @staticmethod
    def maxDepth_dfs(root: TreeNode | None) -> int:
        if not root:
            return 0

        stack = [(root, 1)]
        max_depth = 0

        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)

            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return max_depth

    @staticmethod
    def maxDepth_rec(root: TreeNode | None) -> int:
        def helper(node):
            if not node:
                return 0
            return 1 + max(helper(node.left), helper(node.right))

        return helper(root)


@pytest.mark.parametrize(
    "input_list,expected",
    [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
        ([1, 2, 3, 4, None, None, 5], 3),
    ],
)
def test_maxDepth(input_list, expected):
    assert Solution().maxDepth(make_tree(input_list)) == expected
