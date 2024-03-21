from typing import Optional

import pytest

from helpers.bin_tree import create_tree
from helpers.bin_tree import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[int] | list[list[int]]:
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
    assert Solution().levelOrder(create_tree(l1)) == expected
