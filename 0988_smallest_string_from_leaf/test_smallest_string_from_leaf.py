# https://leetcode.com/problems/smallest-string-starting-from-leaf
import string
from collections import deque

import pytest

from helpers.bin_tree import make_tree
from helpers.bin_tree import TreeNode

LETTER_MAPPING = {x: y for x, y in zip(range(0, 26), string.ascii_lowercase)}


class Solution:
    @staticmethod
    def smallestFromLeaf(root: TreeNode | None) -> str:
        def _calculate_lex_path(path: list[int]) -> str:
            my_str = ""
            for char in reversed(path):
                my_str += LETTER_MAPPING[char]
            return my_str

        min_str = "zzzzzzzzzzzzzzzzzzzzzzzzzz"

        if not root:
            return ""

        queue = deque()
        queue.append((root, root.val, [root.val]))
        while queue:
            node, val, curr_path = queue.popleft()
            if not node.left and not node.right:
                curr_lex_path = _calculate_lex_path(curr_path)
                if curr_lex_path < min_str:
                    min_str = curr_lex_path
            if node.left:
                queue.append((node.left, node.val, curr_path + [node.left.val]))
            if node.right:
                queue.append((node.right, node.val, curr_path + [node.right.val]))
        return min_str


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([0, 1, 2, 3, 4, 3, 4], "dba"),
        ([25, 1, 3, 1, 3, 0, 2], "adz"),
        ([2, 2, 1, None, 1, 0, None, 0], "abc"),
    ],
)
def test_smallest_from_leaf(l1, expected):
    assert Solution().smallestFromLeaf(make_tree(l1)) == expected
