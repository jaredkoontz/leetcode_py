from collections import deque

import pytest

from helpers.bin_tree import create_tree
from helpers.bin_tree import TreeNode


class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        # assert (
        #     self.sumNumbers_mine(root)
        #     == self.sumNumbers_iterative(root)
        #     == self.sumNumbers_bfs(root)
        #     == self.sumNumbers_morris(root)
        #     == self.sumNumbers_one_line(root)
        #     == self.sumNumbers_one_line_unwrapped(root)
        # )
        return self.sumNumbers_mine(root)

    @staticmethod
    def sumNumbers_mine(root: TreeNode | None) -> int:
        def preorder(node: TreeNode, curr: int):
            if not node:
                return 0
            curr = curr * 10 + node.val
            if not node.left and not node.right:
                return curr
            return preorder(node.left, curr) + preorder(node.right, curr)

        return preorder(root, 0)

    @staticmethod
    def sumNumbers_iterative(root: TreeNode | None) -> int:
        if not root:
            return 0
        queue, total_sum = deque([(root, 0)]), 0
        while len(queue):
            root, cur = queue.pop()
            cur = cur * 10 + root.val
            if not root.left and not root.right:
                total_sum += cur
            if root.right:
                queue.append((root.right, cur))
            if root.left:
                queue.append((root.left, cur))
        return total_sum

    @staticmethod
    def sumNumbers_bfs(root: TreeNode | None) -> int:
        if not root:
            return 0
        q, total_sum = deque([(root, 0)]), 0
        while len(q):
            root, cur = q.pop()
            cur = cur * 10 + root.val
            if root.left:
                q.append((root.left, cur))
            if root.right:
                q.append((root.right, cur))
            if not root.left and not root.right:
                total_sum += cur

        return total_sum

    @staticmethod
    def sumNumbers_morris(root: TreeNode | None) -> int:
        tot_sum, cur, depth = 0, 0, 0
        while root:
            if root.left:
                pre, depth = root.left, 1
                while pre.right and pre.right != root:
                    pre, depth = pre.right, depth + 1
                if not pre.right:
                    pre.right = root
                    cur = cur * 10 + root.val
                    root = root.left
                else:
                    pre.right = None
                    if not pre.left:
                        tot_sum += cur
                    cur //= 10**depth
                    root = root.right
            else:
                cur = cur * 10 + root.val
                if not root.right:
                    tot_sum += cur
                root = root.right
        return tot_sum

    @staticmethod
    def sumNumbers_one_line(root: TreeNode | None) -> int:
        return (
            f := lambda n, q: n
            and (f(n.left, q := 10 * q + n.val) + f(n.right, q) or q)
            or 0
        )(root, 0)

    @staticmethod
    def sumNumbers_one_line_unwrapped(root: TreeNode | None) -> int:
        def f(n, q):
            if n:
                q = 10 * q + n.val
                if result := f(n.left, q) + f(n.right, q):
                    return result

                return q

            return 0

        return f(root, 0)


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([4, 9, 0, 5, 1], 1026),
        ([1, 2, 3], 25),
        ([1, 5, 2, 3, 4], 319),
        ([], 0),
        ([1], 1),
    ],
)
def test_sumNumbers(l1, expected):
    assert Solution().sumNumbers(create_tree(l1)) == expected
