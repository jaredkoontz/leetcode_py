# https://leetcode.com/problems/maximum-depth-of-n-ary-tree
import pytest

from helpers.nary_tree import make_nary_tree
from helpers.nary_tree import NAryNode


class Solution:
    def maxDepth(self, root: NAryNode) -> int:
        return self.maxDepth_iter(root)

    @staticmethod
    def maxDepth_iter(root: NAryNode) -> int:
        max_depth = 0
        traverse_stack = [(root, 1)]

        while traverse_stack:
            node, level = traverse_stack.pop()
            max_depth = max(level, max_depth)
            for n in node.children:
                traverse_stack.append((n, level + 1))

        return max_depth

    @staticmethod
    def maxDepth_rec(root: NAryNode) -> int:
        def dfs(node):
            if node is None:
                return 0
            if not node.children:
                return 1
            max_depth = 0
            for child in node.children:
                max_depth = max(max_depth, dfs(child))
            return 1 + max_depth

        return dfs(root)


@pytest.mark.parametrize(
    "root,expected",
    [
        ([1, None, 3, 2, 4, None, 5, 6], 3),
        (
            [
                1,
                None,
                2,
                3,
                4,
                5,
                None,
                None,
                6,
                7,
                None,
                8,
                None,
                9,
                10,
                None,
                None,
                11,
                None,
                12,
                None,
                13,
                None,
                None,
                14,
            ],
            5,
        ),
    ],
)
def test_maxDepth(root, expected):
    assert Solution().maxDepth(make_nary_tree(root)) == expected
