import pytest

from helpers.bin_tree import create_tree
from helpers.bin_tree import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        my_list = []
        self.inorder(root, my_list)
        return my_list

    def inorder(self, root, my_list):
        if root:
            self.inorder(root.left, my_list)
            my_list.append(root.val)
            self.inorder(root.right, my_list)


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([1, None, 2, 3], [1, 3, 2]),
        ([1, 4, 2, 3], [3, 4, 1, 2]),
        ([1, 5, 2, 3, 4], [3, 5, 4, 1, 2]),
        ([], []),
        ([1], [1]),
    ],
)
def test_inorderTraversal(l1, expected):
    assert Solution().inorderTraversal(create_tree(l1)) == expected
