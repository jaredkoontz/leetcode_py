import pytest

from helpers.bin_tree import make_tree
from helpers.bin_tree import TreeNode


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode | None, p: TreeNode | None, q: TreeNode | None
    ) -> TreeNode | None:
        return self.lowestCommonAncestor_recursive(root, p, q)

    @staticmethod
    def lowestCommonAncestor_recursive(
        root: TreeNode | None, p: TreeNode | None, q: TreeNode | None
    ) -> TreeNode | None:
        def lca(node, first, second):
            if not node:
                return
            # looking for me, return myself
            if first == node or second == node:
                return node

            # look in left and right child
            lca1 = lca(node.left, first, second)
            lca2 = lca(node.right, first, second)

            if lca1 and lca2:
                return node
            if lca1 is None:
                return lca2
            return lca1

        lowest_common = lca(root, p, q)
        return lowest_common

    @staticmethod
    def lowestCommonAncestor_stack(
        root: TreeNode | None, p: TreeNode | None, q: TreeNode | None
    ) -> TreeNode | None:
        stack = [(root, "")]
        p_path = ""
        q_path = ""

        while stack and not (p_path and q_path):
            node, path = stack.pop()
            if node == p:
                p_path = path
            if node == q:
                q_path = path
            if node.left:
                stack.append((node.left, path + "L"))
            if node.right:
                stack.append((node.right, path + "R"))
        node = root
        for left_path, right_path in zip(p_path, q_path):
            if left_path != right_path:
                return node
            else:
                if left_path == "L":
                    node = node.left
                else:
                    node = node.right
        return node


@pytest.mark.parametrize(
    "root,p,q,expected",
    [
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3),
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5),
        ([1, 2], 1, 2, 1),
    ],
)
def test_least_common_ancestor(root, p, q, expected):
    assert (
        Solution().lowestCommonAncestor(make_tree(root), TreeNode(p), TreeNode(q))
        == expected
    )
