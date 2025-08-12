# https://leetcode.com/problems/leaf-similar-trees
from collections import deque

import pytest

from helpers.bin_tree import make_tree
from helpers.bin_tree import TreeNode


class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        return self.leafSimilar_stack(root1, root2)

    @staticmethod
    def leafSimilar_stack(root1: TreeNode | None, root2: TreeNode | None) -> bool:
        def helper(root):
            leaf_vals = []
            my_stack = [root]
            while my_stack:
                node = my_stack.pop()
                if not node.left and not node.right:
                    leaf_vals.append(node.val)
                if node.left:
                    my_stack.append(node.left)
                if node.right:
                    my_stack.append(node.right)
            return leaf_vals

        root1_leaves = helper(root1)
        root2_leaves = helper(root2)
        return root1_leaves == root2_leaves

    # todo fails because order matters
    @staticmethod
    def leafSimilar_queue(root1: TreeNode | None, root2: TreeNode | None) -> bool:
        def helper(root):
            leaf_vals = []
            my_queue = deque([root])
            while my_queue:
                node = my_queue.popleft()
                if not node.left and not node.right:
                    leaf_vals.append(node.val)
                if node.left:
                    my_queue.append(node.left)
                if node.right:
                    my_queue.append(node.right)
            return leaf_vals

        root1_leaves = helper(root1)
        root2_leaves = helper(root2)
        return root1_leaves == root2_leaves

    @staticmethod
    def leafSimilar_recursive(root1: TreeNode | None, root2: TreeNode | None) -> bool:
        def helper(root, arr=None):
            if not root:
                return
            if not root.left and not root.right:
                arr.append(root.val)
            helper(root.left, arr)
            helper(root.right, arr)

        root1_arr = []
        root2_arr = []
        helper(root1, root1_arr)
        helper(root2, root2_arr)
        print(f"{root1_arr=}{root2_arr=}")
        return root1_arr == root2_arr


@pytest.mark.parametrize(
    "l1,l2,expected",
    [
        (
            [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4],
            [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8],
            True,
        ),
        ([1, 2, 3], [1, 3, 2], False),
    ],
)
def test_leafSimilar(l1, l2, expected):
    assert Solution().leafSimilar(make_tree(l1), make_tree(l2)) == expected
