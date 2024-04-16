from collections import deque

import pytest

from helpers.bin_tree import create_tree
from helpers.bin_tree import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        assert (
            self.hasPathSum_mine(root, targetSum)
            == self.hasPathSum_recursive(root, targetSum)
            # == self.hasPathSum_dfs(root, targetSum)
            == self.hasPathSum_dfs_stack(root, targetSum)
            == self.hasPathSum_bfs_queue(root, targetSum)
        )
        return self.hasPathSum_dfs(root, targetSum)

    @staticmethod
    def hasPathSum_mine(root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False
        queue = deque([(root, 0)])
        while len(queue):
            root, current_sum = queue.pop()
            current_sum = current_sum + root.val
            if not root.left and not root.right:
                if current_sum == targetSum:
                    return True
            if root.right:
                queue.append((root.right, current_sum))
            if root.left:
                queue.append((root.left, current_sum))
        return False

    def hasPathSum_recursive(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right and root.val == targetSum:
            return True

        targetSum -= root.val
        return self.hasPathSum_recursive(
            root.left, targetSum
        ) or self.hasPathSum_recursive(root.right, targetSum)

    @staticmethod
    def hasPathSum_dfs(root: TreeNode | None, targetSum: int) -> bool:
        result = []

        def dfs(node, target, res):
            if node:
                if not node.left and not node.right and node.val == target:
                    res.append(True)
                if node.left:
                    dfs(node.left, target - node.val, res)
                if node.right:
                    dfs(node.right, target - node.val, res)

        dfs(root, targetSum, result)
        return any(result)

    @staticmethod
    def hasPathSum_dfs_stack(root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            curr, val = stack.pop()
            if not curr.left and not curr.right and val == targetSum:
                return True
            if curr.right:
                stack.append((curr.right, val + curr.right.val))
            if curr.left:
                stack.append((curr.left, val + curr.left.val))
        return False

    @staticmethod
    def hasPathSum_bfs_queue(root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False
        queue = [(root, targetSum - root.val)]
        while queue:
            curr, val = queue.pop(0)
            if not curr.left and not curr.right and val == 0:
                return True
            if curr.left:
                queue.append((curr.left, val - curr.left.val))
            if curr.right:
                queue.append((curr.right, val - curr.right.val))
        return False


@pytest.mark.parametrize(
    "l1,leaf_sum,expected",
    [
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True),
        ([1, 2, 3], 5, False),
        ([4, 9, 0, 5, 1], 14, True),
        ([1, 2, 3], 4, True),
        ([1, 5, 2, 3, 4], 3, True),
        ([], 0, False),
        ([1], 1, True),
    ],
)
def test_sumNumbers(l1, leaf_sum, expected):
    assert Solution().hasPathSum(create_tree(l1), leaf_sum) == expected
