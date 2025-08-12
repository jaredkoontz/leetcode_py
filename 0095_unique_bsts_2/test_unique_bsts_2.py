# https://leetcode.com/problems/unique-binary-search-trees-ii
import pytest

from helpers.bin_tree import make_tree
from helpers.bin_tree import TreeCodec
from helpers.bin_tree import TreeNode


class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        return self.generateTrees_rec_naive(n)

    @staticmethod
    def generateTrees_memo(n: int) -> list[TreeNode | None]:
        if n == 0:
            return []

        memo = {}

        def generate_trees(start, end):
            if (start, end) in memo:
                return memo[(start, end)]

            trees = []
            if start > end:
                trees.append(None)
                return trees

            for root_val in range(start, end + 1):
                left_trees = generate_trees(start, root_val - 1)
                right_trees = generate_trees(root_val + 1, end)

                for left_tree in left_trees:
                    for right_tree in right_trees:
                        root = TreeNode(root_val, left_tree, right_tree)
                        trees.append(root)

            memo[(start, end)] = trees
            return trees

        return generate_trees(1, n)

    @staticmethod
    def generateTrees_rec_naive(n: int) -> list[TreeNode | None]:
        def dfs(start, end):
            nodes = []
            if start > end:
                nodes.append(None)
                return nodes
            if start == end:
                nodes.append(TreeNode(start))
                return nodes
            for index in range(start, end + 1):
                left = dfs(start, index - 1)
                right = dfs(index + 1, end)
                for left_node in left:
                    for right_node in right:
                        root = TreeNode(index)
                        root.left = left_node
                        root.right = right_node
                        nodes.append(root)
            return nodes

        return dfs(1, n)


@pytest.mark.parametrize(
    "n, expected",
    [
        (
            3,
            [
                [1, None, 2, None, 3],
                [1, None, 3, 2],
                [2, 1, 3],
                [3, 1, None, None, 2],
                [3, 2, None, 1],
            ],
        ),
        (1, [[1]]),
    ],
)
def test_generateTrees(n, expected):
    trees = Solution().generateTrees(n)
    given_trees = [TreeCodec().serialize(make_tree(x)) for x in expected]
    for tree in trees:
        assert TreeCodec().serialize(tree) in given_trees
