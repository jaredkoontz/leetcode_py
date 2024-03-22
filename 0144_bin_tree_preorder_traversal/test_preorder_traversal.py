import pytest

from helpers.bin_tree import create_tree
from helpers.bin_tree import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        my_list = []
        self.preorder(root, my_list)
        return my_list

    def preorder(self, root, my_list):
        if root:
            my_list.append(root.val)
            self.preorder(root.left, my_list)
            self.preorder(root.right, my_list)


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([1, None, 2, 3], [1, 2, 3]),
        ([1, 4, 2, 3], [1, 4, 3, 2]),
        ([1, 5, 2, 3, 4], [1, 5, 3, 4, 2]),
        ([], []),
        ([1], [1]),
    ],
)
def test_preorderTraversal(l1, expected):
    assert Solution().preorderTraversal(create_tree(l1)) == expected
