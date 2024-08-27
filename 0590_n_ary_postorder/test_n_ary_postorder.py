# https://leetcode.com/problems/n-ary-tree-postorder-traversal/
import pytest

from helpers.nary_tree import make_nary_tree
from helpers.nary_tree import NAryNode


class Solution:
    def postorder(self, root: NAryNode) -> list[int]:
        return self.postorder_iter(root)

    @staticmethod
    def postorder_iter(root: NAryNode) -> list[int]:
        ret_stack = []
        traverse_stack = [root]

        while traverse_stack:
            node = traverse_stack.pop()
            ret_stack.append(node)

            for n in node.children:
                traverse_stack.append(n)

        ret = []
        while ret_stack:
            ret.append(ret_stack.pop().val)
        return ret

    @staticmethod
    def postorder_rec(root: NAryNode) -> list[int]:
        ret = []

        def dfs(node: NAryNode):
            if node:
                for n in node.children:
                    dfs(n)
                ret.append(node.val)

        dfs(root)
        return ret


@pytest.mark.parametrize(
    "root,expected",
    [
        ([1, None, 3, 2, 4, None, 5, 6], [5, 6, 3, 2, 4, 1]),
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
            [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1],
        ),
    ],
)
def test_postorder(root, expected):
    assert Solution().postorder(make_nary_tree(root)) == expected
