# https://leetcode.com/problems/subtree-of-another-tree
from collections import deque

import pytest

from helpers.bin_tree import make_tree
from helpers.bin_tree import TreeNode


class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        return self.isSubtree_serialize(subRoot, root)

    @staticmethod
    def isSubtree_mine(root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def helper(my_root, my_subRoot):
            if not my_root:
                return False
            if my_root.val == my_subRoot.val and isIdentical(root, my_subRoot):
                return True
            return helper(my_root.left, my_subRoot) or helper(my_root.right, my_subRoot)

        def isIdentical(my_root, my_subRoot):
            if not my_root and not my_subRoot:
                return True
            elif not my_root or not my_subRoot or root.val != my_subRoot.val:
                return False
            if not isIdentical(my_root.left, my_subRoot.left):
                return False
            if not isIdentical(my_root.right, my_subRoot.right):
                return False
            return True

        return helper(root, subRoot)

    @staticmethod
    def isSubtree_serialize(root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def ser(n):
            if not n:
                return ",#"
            return "," + str(n.val) + ser(n.left) + ser(n.right)

        return ser(subRoot) in ser(root)

    @staticmethod
    def isSubtree_rec(root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        flag = [False]

        def traverse(my_root: TreeNode | None, my_sub_root: TreeNode | None):
            if not my_root:
                return None

            stack = deque()
            stack.append(my_root)

            while stack:
                curr = stack.pop()

                if traverse(curr, my_sub_root):
                    flag[0] = True

                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)
            return None

        traverse(root, subRoot)
        return flag[0]

    @staticmethod
    def isSameTree_queue(p: TreeNode | None, q: TreeNode | None) -> bool:
        stack1 = deque()
        stack2 = deque()
        stack1.append(p)
        stack2.append(q)

        while stack1 and stack2:
            curr1 = stack1.pop()
            curr2 = stack2.pop()

            if not curr1 and not curr2:
                continue
            if not curr1 or not curr2:
                return False
            if curr1.val != curr2.val:
                return False

            stack1.append(curr1.right)
            stack1.append(curr1.left)
            stack2.append(curr2.right)
            stack2.append(curr2.left)

        return not stack1 and not stack2


@pytest.mark.parametrize(
    "root,subroot,expected",
    [
        ([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2], False),
    ],
)
def test_isSubtree(root, subroot, expected: bool):
    assert Solution().isSubtree(make_tree(root), make_tree(subroot)) == expected
