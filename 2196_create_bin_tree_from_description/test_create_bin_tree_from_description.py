# https://leetcode.com/problems/create-binary-tree-from-descriptions
import pytest

from helpers.bin_tree import compare_trees
from helpers.bin_tree import make_tree
from helpers.bin_tree import TreeNode


class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode | None:
        return self.createBinaryTree_mine(descriptions)

    @staticmethod
    def createBinaryTree_mine(descriptions: list[list[int]]) -> TreeNode | None:
        bin_map = {}
        for parent, child, is_left in descriptions:
            bin_map[child] = (parent, is_left, TreeNode(child))
        root = None
        for key, val in bin_map.items():
            parent, is_left, node = val
            if bin_map.get(parent) is None:
                if not root:
                    root = TreeNode(parent)
                if is_left:
                    root.left = node
                else:
                    root.right = node
            else:
                parent_tuple = bin_map.get(parent)
                parent_node = parent_tuple[2]
                if is_left:
                    parent_node.left = node
                else:
                    parent_node.right = node
        return root

    @staticmethod
    def createBinaryTree_one_pass(descriptions: list[list[int]]) -> TreeNode | None:
        nodes = {}
        children = set()
        for parent, child, is_left in descriptions:
            children.add(child)

            if child not in nodes.keys():
                nodes[child] = TreeNode(child)
            if parent not in nodes.keys():
                nodes[parent] = TreeNode(parent)

            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

        for n, v in nodes.items():
            if n not in children:
                return nodes[n]


@pytest.mark.parametrize(
    "descriptions, expected",
    [
        (
            [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]],
            [50, 20, 80, 15, 17, 19],
        ),
        ([[1, 2, 1], [2, 3, 0], [3, 4, 1]], [1, 2, None, None, 3, 4]),
    ],
)
def test_create_binary_tree_from_description(descriptions, expected):
    assert compare_trees(Solution().createBinaryTree(descriptions), make_tree(expected))
