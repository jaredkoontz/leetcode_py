# https://leetcode.com/problems/balance-a-binary-search-tree
import pytest

from helpers.bin_tree import compare_trees
from helpers.bin_tree import create_array_from_tree
from helpers.bin_tree import make_tree
from helpers.bin_tree import TreeNode


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        return self.balanceBST_bin_search(root)

    @staticmethod
    def balanceBST_dsw(root: TreeNode) -> TreeNode:
        def makeVine(grand: TreeNode) -> int:
            count = 0
            n = grand.right
            while n is not None:
                if n.left is not None:
                    old_n = n
                    n = n.left
                    old_n.left = n.right
                    n.right = old_n
                    grand.right = n
                else:
                    count += 1
                    grand = n
                    n = n.right
            return count

        def compress(grand: TreeNode, m: int) -> None:
            n = grand.right
            while m > 0:
                old_n = n
                n = n.right
                grand.right = n
                old_n.right = n.left
                n.left = old_n
                grand = n
                n = n.right
                m -= 1

        grandparent = TreeNode(0)
        grandparent.right = root
        cnt = makeVine(grandparent)
        m = (2 ** int((cnt + 1).bit_length() - 1)) - 1
        compress(grandparent, cnt - m)
        m //= 2
        while m > 0:
            compress(grandparent, m)
            m //= 2
        return grandparent.right

    @staticmethod
    def balanceBST_bin_search(root: TreeNode) -> TreeNode:
        nodes = []

        def in_order_traverse(node: TreeNode):
            if node is None:
                return
            in_order_traverse(node.left)
            nodes.append(node)
            in_order_traverse(node.right)

        def build_balanced_tree(left: int, right: int):
            if left > right:
                return None
            mid = (left + right) // 2
            new_root = nodes[mid]
            new_root.left = build_balanced_tree(left, mid - 1)
            new_root.right = build_balanced_tree(mid + 1, right)
            return new_root

        in_order_traverse(root)
        return build_balanced_tree(0, len(nodes) - 1)


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([1, None, 2, None, 3, None, 4, None, None], [2, 1, 3, None, None, None, 4]),
        ([2, 1, 3], [2, 1, 3]),
    ],
)
def test_balance_bst(l1, expected):
    tree_given = make_tree(l1)
    tree_expected = make_tree(expected)
    balanced = Solution().balanceBST(tree_given)
    assert create_array_from_tree(balanced) == create_array_from_tree(tree_expected)
    assert compare_trees(balanced, tree_expected)
