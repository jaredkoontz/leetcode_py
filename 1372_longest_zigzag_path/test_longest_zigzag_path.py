from collections import deque

import pytest

from helpers.bin_tree import make_tree
from helpers.bin_tree import TreeNode


class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        return self.longestZigZag_queue(root)

    @staticmethod
    def longestZigZag_stack(root: TreeNode | None) -> int:
        ans = 0
        stack = [(root, 0, None)]
        while stack:
            node, n, left = stack.pop()
            if node:
                ans = max(ans, n)
                stack.append((node.left, 1 if left else n + 1, 1))
                stack.append((node.right, n + 1 if left else 1, 0))
        return ans

    @staticmethod
    def longestZigZag_rec(root: TreeNode | None) -> int:
        path_length = 0

        def dfs(node, goLeft, steps):
            nonlocal path_length
            if node:
                path_length = max(path_length, steps)
                if goLeft:
                    dfs(node.left, False, steps + 1)
                    dfs(node.right, True, 1)
                else:
                    dfs(node.left, False, 1)
                    dfs(node.right, True, steps + 1)

        dfs(root, False, 0)
        dfs(root, True, 0)
        return path_length

    @staticmethod
    def longestZigZag_queue(root: TreeNode | None) -> int:
        if not root:
            return 0

        left = 0
        right = 1

        longest_zig_zag = 0

        queue = deque()
        queue.append((root, None, 0))

        while queue:
            node, last_move, curr_zig = queue.popleft()
            longest_zig_zag = max(curr_zig, longest_zig_zag)
            if node.left:
                if last_move is None or last_move is right:
                    queue.append((node.left, left, curr_zig + 1))
                queue.append((node.left, None, 0))
            if node.right:
                if last_move is None or last_move is left:
                    queue.append((node.right, right, curr_zig + 1))
                queue.append((node.right, None, 0))

        return longest_zig_zag


@pytest.mark.parametrize(
    "root,expected",
    [
        ([0, None, 1, 2, 3, None, None, 4, 5, None, 6, None, None, None, 7], 3),
        ([0, None, 1, 2, 3, None, None, 4, None, None, 6, None, None, None, 7], 3),
        ([1, 1, 1, None, 1, None, None, 1, 1, None, 1], 4),
        ([1], 0),
    ],
)
def test_longestZigZag(root, expected):
    assert Solution().longestZigZag(make_tree(root)) == expected
