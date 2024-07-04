import pytest

from helpers.bin_tree import make_tree
from helpers.bin_tree import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        return self.isSymmetric_mine(root)

    @staticmethod
    def isSymmetric_mine(root: TreeNode | None) -> bool:
        def recurse(left, right):
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False

            return recurse(left.left, right.right) and recurse(left.right, right.left)

        return recurse(root.left, root.right)


@pytest.mark.parametrize(
    "root1, expected",
    [
        ([1, 2, 2, 3, 4, 4, 3], True),
        ([1, 2, 2, None, 3, None, 3], False),
    ],
)
def test_isSymmetric(root1, expected):
    assert Solution().isSymmetric(make_tree(root1)) == expected
