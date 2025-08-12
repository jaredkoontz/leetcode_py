# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
import pytest

from helpers.bin_tree import TreeNode
from helpers.bin_tree import compare_trees
from helpers.bin_tree import make_tree


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        return self.buildTree_mine(inorder, postorder)

    @staticmethod
    def buildTree_mine(inorder: list[int], postorder: list[int]) -> TreeNode | None:
        inorder_map = {node: index for index, node in enumerate(inorder)}

        # the root is always the last in a post order, then we can figure out the left and right subtrees
        def helper(left_index, right_index):
            if left_index > right_index:
                return None
            if postorder:
                root = TreeNode(postorder.pop())

                root_index = inorder_map[root.val]

                root.right = helper(root_index + 1, right_index)
                root.left = helper(left_index, root_index - 1)
                return root

            return None

        return helper(0, len(inorder) - 1)

    @staticmethod
    def buildTree_neet(inorder: list[int], postorder: list[int]) -> TreeNode | None:
        def helper(my_inorder, my_postorder):
            if not my_inorder:
                return None
            if my_postorder:
                root = TreeNode(my_postorder.pop())

                idx = inorder.index(root.val)
                root.right = helper(my_inorder[idx + 1:], my_postorder)
                root.left = helper(my_inorder[:idx], my_postorder)
                return root
            return None

        return helper(inorder, postorder)


@pytest.mark.parametrize(
    "inorder,postorder,expected",
    [
        (
                [9, 3, 15, 20, 7],
                [9, 15, 7, 20, 3],
                [3, 9, 20, None, None, 15, 7],
        ),
        (
                [-1],
                [-1],
                [-1],
        ),
    ],
)
def test_build_tree(inorder, postorder, expected):
    given_tree = make_tree(expected)
    created_tree = Solution().buildTree(inorder, postorder)
    assert compare_trees(given_tree, created_tree)
