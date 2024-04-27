from collections import deque

import pytest

from helpers.bin_tree import make_tree
from helpers.bin_tree import TreeNode


class Solution:
    @staticmethod
    def levelOrder(root: TreeNode | None) -> list[int] | list[list[int]]:
        if not root:
            return []
        queue = deque([root])
        res = []
        even = False
        while queue:
            n = len(queue)
            level = []
            for i in range(n):
                if even:
                    # pop from right and append from left.
                    node = queue.pop()
                    # to maintain the order of nodes in the format of [left, right, left, right]
                    # we push right first since we are appending from left
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
                else:
                    # pop from left and append from right
                    node = queue.popleft()
                    # here the order is maintained in the format [left, right, left, right]
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                level.append(node.val)
            res.append(level)
            even = not even
        return res


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([1, 2, 3, 4, None, None, 5], [[1], [3, 2], [4, 5]]),
        ([3, 9, 20, None, None, 15, 7], [[3], [20, 9], [15, 7]]),
        ([1, 4, 2, 3], [[1], [2, 4], [3]]),
        ([1, 5, 2, 3, 4], [[1], [2, 5], [3, 4]]),
        ([], []),
        ([1], [[1]]),
    ],
)
def test_zigzag_levelOrder(l1, expected):
    assert Solution().levelOrder(make_tree(l1)) == expected
