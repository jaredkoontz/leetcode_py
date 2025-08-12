# https://leetcode.com/problems/n-ary-tree-preorder-traversal
import pytest

from helpers.nary_tree import NAryNode
from helpers.nary_tree import make_nary_tree


class Solution:
    def preorder(self, root: NAryNode) -> list[int]:
        return self.preorder_iter(root)

    @staticmethod
    def preorder_iter(root: NAryNode) -> list[int]:
        ret = []
        traverse_stack = [root]

        while traverse_stack:
            node = traverse_stack.pop()
            ret.append(node.val)

            for n in reversed(node.children):
                traverse_stack.append(n)

        return ret

    @staticmethod
    def preorder_rec(root: NAryNode) -> list[int]:
        ret = []

        def dfs(node: NAryNode):
            if node:
                ret.append(node.val)
                for n in node.children:
                    dfs(n)

        dfs(root)
        return ret


@pytest.mark.parametrize(
    "root,expected",
    [
        ([1, None, 3, 2, 4, None, 5, 6], [1, 3, 5, 6, 2, 4]),
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
                [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10],
        ),
    ],
)
def test_preorder(root, expected):
    assert Solution().preorder(make_nary_tree(root)) == expected
