import copy
from typing import Optional

import pytest

from helpers.bin_tree import TreeNode
from helpers.bin_tree import create_tree


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[int] | list[list[int]]:
        if not root:
            return []

        level, queue, node = [], [], root
        level.append([root.val])
        while node:
            my_list = []
            left, right = node.left, node.right
            if left:
                queue.insert(0, left)
                my_list.append(left.val)
            if right:
                queue.insert(0, right)
                my_list.append(right.val)
            node = None if not queue else queue.pop()
            level.append(copy.copy(my_list)) if my_list else ...
            my_list.clear()
        return level


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([1, 2, 3, 4, None, None, 5], [[1], [2, 3], [4, 5]]),
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1, 4, 2, 3], [[1], [4, 2], [3]]),
        ([1, 5, 2, 3, 4], [[1], [5, 2], [3, 4]]),
        ([], []),
        ([[1]], [[1]]),
    ],
)
def test_levelOrder(l1, expected):
    assert Solution().levelOrder(create_tree(l1)) == expected
