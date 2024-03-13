from typing import List
from typing import Optional

import pytest

from helpers.bin_tree import create_tree
from helpers.bin_tree import TreeNode


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        my_list = []
        self.postorder(root, my_list)
        return my_list

    def postorder(self, root, my_list):
        if root:
            self.postorder(root.left, my_list)
            self.postorder(root.right, my_list)
            my_list.append(root.val)


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([1, None, 2, 3], [3, 2, 1]),
        ([1, 4, 2, 3], [3, 4, 2, 1]),
        ([1, 5, 2, 3, 4], [3, 4, 5, 2, 1]),
        ([], []),
        ([1], [1]),
    ],
)
def test_postorderTraversal(l1, expected):
    assert Solution().postorderTraversal(create_tree(l1)) == expected
