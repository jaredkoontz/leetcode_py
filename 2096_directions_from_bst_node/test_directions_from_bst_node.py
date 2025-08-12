# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another
import pytest

from helpers.bin_tree import TreeNode
from helpers.bin_tree import make_tree


class Solution:
    def getDirections(
            self, root: TreeNode | None, startValue: int, destValue: int
    ) -> str:
        return self.getDirections_mine(root, startValue, destValue)

    @staticmethod
    def getDirections_mine(
            root: TreeNode | None, startValue: int, destValue: int
    ) -> str:
        route = ""
        stack = [(root, "")]
        root_to_start = ""
        root_to_dest = ""
        while stack and not (root_to_start and root_to_dest):
            node, curr_path = stack.pop()
            if node.val == startValue:
                root_to_start = curr_path
            if node.val == destValue:
                root_to_dest = curr_path
            if node.left:
                stack.append((node.left, curr_path + "L"))
            if node.right:
                stack.append((node.right, curr_path + "R"))

        # remove prefix string in case we go to the same path:
        while (
                len(root_to_start)
                and len(root_to_dest)
                and root_to_start[0] == root_to_dest[0]
        ):
            root_to_start = root_to_start[1:]
            root_to_dest = root_to_dest[1:]

        # everything left in start now becomes going to the parent
        route += "U" * len(root_to_start)
        return route + root_to_dest

    @staticmethod
    def getDirections_lca(
            root: TreeNode | None, startValue: int, destValue: int
    ) -> str:
        def lca(node):
            if not node:
                return None

            if node.val == startValue or node.val == destValue:
                return node

            left = lca(node.left)
            right = lca(node.right)
            if left and right:
                return node
            else:
                return left or right

        def dfs(node, target, path):
            if not node:
                return []

            if node.val == target:
                return path
            path.append("L")
            left = dfs(node.left, target, path)
            if not left:
                path.pop()

            path.append("R")
            right = dfs(node.right, target, path)
            if not right:
                path.pop()
            return left or right

        ro = lca(root)

        left_path = dfs(ro, startValue, [])
        right_path = dfs(ro, destValue, [])

        return len(left_path) * "U" + "".join(right_path)


@pytest.mark.parametrize(
    "root,start,dest,expected",
    [
        ([3, 1, 2], 2, 1, "UL"),
        ([5, 1, 2, 3, None, 6, 4], 3, 6, "UURL"),
        ([2, 1], 2, 1, "L"),
    ],
)
def test_getDirections(root, start, dest, expected):
    assert Solution().getDirections(make_tree(root), start, dest) == expected
