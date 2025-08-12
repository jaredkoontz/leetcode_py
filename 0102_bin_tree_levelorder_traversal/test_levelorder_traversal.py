# https://leetcode.com/problems/binary-tree-level-order-traversal
import pytest

from helpers.bin_tree import TreeNode
from helpers.bin_tree import make_tree


class Solution:
    @staticmethod
    def levelOrder(root: TreeNode | None) -> list[int] | list[list[int]]:
        if not root:
            return []

        queue = [root]
        result = []

        while queue:
            next_queue = []
            level = []
            for root in queue:
                level.append(root.val)
                if root.left:
                    next_queue.append(root.left)
                if root.right:
                    next_queue.append(root.right)
            result.append(level)
            queue = next_queue

        return result


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([1, 2, 3, 4, None, None, 5], [[1], [2, 3], [4, 5]]),
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1, 4, 2, 3], [[1], [4, 2], [3]]),
        ([1, 5, 2, 3, 4], [[1], [5, 2], [3, 4]]),
        ([], []),
        ([1], [[1]]),
    ],
)
def test_levelOrder(l1, expected):
    assert Solution().levelOrder(make_tree(l1)) == expected
