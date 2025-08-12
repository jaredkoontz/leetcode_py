# https://leetcode.com/problems/n-ary-tree-level-order-traversal
from collections import defaultdict
from collections import deque

import pytest

from helpers.nary_tree import NAryNode
from helpers.nary_tree import make_nary_tree


class Solution:
    def levelOrder(self, root: NAryNode) -> list[list[int]]:
        return self.levelOrder_rec(root)

    @staticmethod
    def levelOrder_queue(root: NAryNode) -> list[list[int]]:
        ans = []
        queue = deque()
        if not root:
            return ans
        queue.append(root)

        while queue:
            level = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)
                for child in curr.children:
                    if child:
                        queue.append(child)

            ans.append(level)
        return ans

    @staticmethod
    def levelOrder_stack(root: NAryNode) -> list[list[int]]:
        levels = defaultdict(list)
        traverse_stack = [(root, 1)]

        while traverse_stack:
            node, level = traverse_stack.pop()
            levels[level].append(node.val)
            for n in reversed(node.children):
                traverse_stack.append((n, level + 1))

        return [x for x in levels.values()]

    @staticmethod
    def levelOrder_rec(root: NAryNode) -> list[list[int]]:
        dct = defaultdict(list)

        def dfs(node, depth=0):
            if node is None:
                return

            dct[depth].append(node.val)

            for i in node.children:
                dfs(i, depth + 1)

        dfs(root)

        return [val for val in dct.values()]


@pytest.mark.parametrize(
    "root,expected",
    [
        ([1, None, 3, 2, 4, None, 5, 6], [[1], [3, 2, 4], [5, 6]]),
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
                [[1], [2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13], [14]],
        ),
    ],
)
def test_levelOrder(root, expected):
    assert Solution().levelOrder(make_nary_tree(root)) == expected
