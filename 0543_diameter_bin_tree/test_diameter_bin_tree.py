# https://leetcode.com/problems/diameter-of-binary-tree
import pytest

from helpers.bin_tree import TreeNode
from helpers.bin_tree import make_tree


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        return self.diameterOfBinaryTree_dfs_iter(root)

    @staticmethod
    def diameterOfBinaryTree_dfs_rec(root: TreeNode | None) -> int:
        max_all = [0]

        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            m = left + right
            max_all[0] = max(max_all[0], m)
            return 1 + max(left, right)

        depth(root)
        return max_all[0]

    @staticmethod
    def diameterOfBinaryTree_dfs_iter(root: TreeNode | None) -> int:
        if not root:
            return 0
        stack = []
        depths = {}
        max_diameter = 0

        # Traverse using an iterative postorder
        node = root
        while stack or node:
            # Go to the leftmost node
            while node:
                stack.append(node)
                node = node.left

            temp = stack[-1]

            # If we have visited the right node already, process the current node
            if temp.right and temp.right not in depths:
                node = temp.right
            else:
                # Pop and process the node
                node = stack.pop()

                # Get the left and right depths
                left_depth = depths.get(node.left, 0)
                right_depth = depths.get(node.right, 0)

                # Update the max diameter
                max_diameter = max(max_diameter, left_depth + right_depth)

                # Store the depth of the current node
                depths[node] = max(left_depth, right_depth) + 1

                node = None  # Reset to None to stop reprocessing this node

        return max_diameter


@pytest.mark.parametrize(
    "root,expected",
    [
        (
                [
                    4,
                    -7,
                    -3,
                    None,
                    None,
                    -9,
                    -3,
                    9,
                    -7,
                    -4,
                    None,
                    6,
                    None,
                    -6,
                    -6,
                    None,
                    None,
                    0,
                    6,
                    5,
                    None,
                    9,
                    None,
                    None,
                    -1,
                    -4,
                    None,
                    None,
                    None,
                    -2,
                ],
                8,
        ),
        ([1, 2, 3, 4, 5], 3),
        ([1, 2], 1),
    ],
)
def test_diameterOfBinaryTree(root, expected):
    assert Solution().diameterOfBinaryTree(make_tree(root)) == expected
