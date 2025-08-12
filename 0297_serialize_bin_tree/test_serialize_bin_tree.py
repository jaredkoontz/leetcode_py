# https://leetcode.com/problems/serialize-and-deserialize-binary-tree
import pytest

from helpers.bin_tree import TreeCodec
from helpers.bin_tree import compare_trees
from helpers.bin_tree import make_tree

Codec = TreeCodec


@pytest.mark.parametrize(
    "arr, expected", [([1, 2, 3, None, None, 4, 5], "1,2,X,X,3,4,X,X,5,X,X"), ([], "X")]
)
def test_codec(arr, expected):
    codec = Codec()
    tree = make_tree(arr)
    serialized = codec.serialize(tree)
    assert serialized == expected
    assert compare_trees(tree, codec.deserialize(serialized))
