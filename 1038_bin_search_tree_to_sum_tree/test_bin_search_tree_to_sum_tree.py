# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree
import pytest

from helpers.bin_tree import compare_trees
from helpers.bin_tree import make_array_from_tree
from helpers.bin_tree import make_tree
from helpers.bin_tree import TreeNode


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        return self.bstToGst_bfs(root)

    @staticmethod
    def bstToGst_bfs(root: TreeNode) -> TreeNode:
        def reversed_inorder_traversal(curr: TreeNode):
            if not curr:
                # empty node or empty tree
                return
            else:
                # DFS to next level
                yield from reversed_inorder_traversal(curr.right)
                yield curr
                yield from reversed_inorder_traversal(curr.left)

        accumulation_sum = 0

        for node in reversed_inorder_traversal(root):
            accumulation_sum += node.val
            node.val = accumulation_sum

        return root

    @staticmethod
    def bstToGst_dfs(root: TreeNode) -> TreeNode:
        def reversedInorder(node, total):
            if not node:
                return total
            node.val += reversedInorder(node.right, total)
            return reversedInorder(node.left, node.val)

        reversedInorder(root, 0)
        return root

    @staticmethod
    def bstToGst_iterative(root: TreeNode) -> TreeNode:
        cur = root
        total = 0
        while cur is not None:
            if cur.right is not None:  # traverse right subtree
                left_most = cur.right
                # locate the left-most node of cur's right subtree
                while left_most.left is not None and left_most.left != cur:
                    left_most = left_most.left
                if left_most.left is None:  # never visit the left-most node yet
                    left_most.left = cur  # construct a way back to cur
                    cur = cur.right  # explore right
                else:  # visited left_most already, which implies now on way back
                    left_most.left = None  # cut off the fabricated link
                    total += cur.val  # update total
                    cur.val = total  # update node value
                    cur = cur.left  # continue on way back
            else:  # no right child: 1) cur is the right-most of unvisited nodes; 2) must traverse left
                total += cur.val  # update total
                cur.val = total  # update node value
                cur = cur.left  # continue on way back
        return root

    @staticmethod
    def bstToGst_stack(root: TreeNode) -> TreeNode:
        if root:
            node, stack, total = root, [], 0
            while node or stack:
                while node:
                    stack.append(node)
                    node = node.right
                node = stack.pop()
                node.val += total
                total = node.val
                node = node.left
        return root


@pytest.mark.parametrize(
    "l1,expected",
    [
        (
            [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8],
            [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8],
        ),
        ([0, None, 1], [1, None, 1]),
    ],
)
def test_bstToGst(l1, expected):
    tree_given = make_tree(l1)
    tree_expected = make_tree(expected)
    assert make_array_from_tree(
        Solution().bstToGst(tree_given)
    ) == make_array_from_tree(tree_expected)
    assert compare_trees(tree_given, tree_expected)
