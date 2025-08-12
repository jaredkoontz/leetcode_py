# https://leetcode.com/problems/binary-tree-right-side-view
import pytest

from helpers.bin_tree import make_tree
from helpers.bin_tree import TreeNode


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        return self.rightSideView_rec(root)

    @staticmethod
    def rightSideView_rec(root: TreeNode | None) -> list[int]:
        result = []

        def rightView(node, depth):
            if not node:
                return
            if depth == len(result):
                result.append(node.val)
            rightView(node.right, depth + 1)
            rightView(node.left, depth + 1)

        rightView(root, 0)
        return result


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
        ([1, 2, 3, 4, None, None, None, 5], [1, 3, 4, 5]),
    ],
)
def test_rightSideView(l1, expected):
    assert Solution().rightSideView(make_tree(l1)) == expected
