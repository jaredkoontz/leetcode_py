# https://leetcode.com/problems/serialize-and-deserialize-binary-tree
from collections import deque

import pytest

from helpers.bin_tree import compare_trees
from helpers.bin_tree import make_tree
from helpers.bin_tree import TreeNode


class Codec:
    spliter = ","
    NN = "X"

    def serialize(self, root: TreeNode) -> str:
        def build_string(node, string_builder):
            if not node:
                string_builder.append(self.NN)
            else:
                string_builder.append(str(node.val))
                build_string(node.left, string_builder)
                build_string(node.right, string_builder)

        sb = []
        build_string(root, sb)
        return self.spliter.join(sb)

    def deserialize(self, data: str) -> TreeNode:
        def build_tree(my_nodes):
            val = my_nodes.popleft()
            if val == self.NN:
                return None
            node = TreeNode(int(val))
            node.left = build_tree(my_nodes)
            node.right = build_tree(my_nodes)
            return node

        nodes = deque(data.split(self.spliter))
        return build_tree(nodes)


@pytest.mark.parametrize(
    "arr, expected", [([1, 2, 3, None, None, 4, 5], "1,2,X,X,3,4,X,X,5,X,X"), ([], "X")]
)
def test_codec(arr, expected):
    codec = Codec()
    tree = make_tree(arr)
    serialized = codec.serialize(tree)
    assert serialized == expected
    assert compare_trees(tree, codec.deserialize(serialized))
