# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
import pytest

from helpers.bin_tree import make_tree
from helpers.bin_tree import TreeNode


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        return self.lowestCommonAncestor_simple(root, p, q)

    @staticmethod
    def lowestCommonAncestor_simple(
        root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr

    @staticmethod
    def lowestCommonAncestor_stack(
        root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        stack = [root]
        while stack:
            node = stack.pop()
            if (p.val >= node.val >= q.val) or (p.val <= node.val <= q.val):
                return node
            if node.val >= p.val and node.val >= q.val and node.left:
                stack.append(node.left)
            else:
                stack.append(node.right)

        return root

    @staticmethod
    def lowestCommonAncestor_recursive(
        root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        def lca(node: TreeNode, first: TreeNode, second: TreeNode) -> TreeNode:
            if node:
                node_value = node.val
                if (
                    first.val >= node_value >= second.val
                    or first.val <= node_value <= second.val
                ):
                    return node
                elif node_value > first.val and node_value > second.val:
                    return lca(node.left, first, second)
                else:
                    return lca(node.right, first, second)

        return lca(root, p, q)


@pytest.mark.parametrize(
    "root,p,q,expected",
    [
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6),
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2),
        ([2, 1], 2, 1, 2),
    ],
)
def test_lowestCommonAncestor(root, p, q, expected):
    assert (
        Solution().lowestCommonAncestor(make_tree(root), TreeNode(p), TreeNode(q))
        == expected
    )
