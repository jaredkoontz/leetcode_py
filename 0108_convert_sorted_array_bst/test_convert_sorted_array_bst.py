import pytest

from helpers.bin_tree import create_array_from_tree
from helpers.bin_tree import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        return self.sortedArrayToBST_mine(nums)

    @staticmethod
    def sortedArrayToBST_mine(nums: list[int]) -> TreeNode | None:
        def bst_helper(left, right):
            if left > right:
                return None
            middle = (left + right) // 2
            root = TreeNode(nums[middle])
            root.left = bst_helper(left, middle - 1)
            root.right = bst_helper(middle + 1, right)
            return root

        return bst_helper(0, len(nums) - 1)


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([-10, -3, 0, 5, 9], [0, -10, 5, -3, 9]),
        ([1, 3], [1, 3]),
    ],
)
def test_sortedArrayToBST(l1, expected):
    assert create_array_from_tree(Solution().sortedArrayToBST(l1)) == expected
