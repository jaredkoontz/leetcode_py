import pytest

from helpers.bin_tree import make_tree
from helpers.bin_tree import TreeNode
from helpers.ll import ListNode
from helpers.ll import make_ll


class Solution:
    def isSubPath(self, head: ListNode | None, root: TreeNode | None) -> bool:
        return self.isSubPath_dfs_iter(head, root)

    @staticmethod
    def isSubPath_KMP(head: ListNode | None, root: TreeNode | None) -> bool:
        def _search_in_tree(
            node: TreeNode | None,
            pattern_index: int,
            pattern: list[int],
            prefix_table: list[int],
        ) -> bool:
            if not node:
                return False

            while pattern_index > 0 and node.val != pattern[pattern_index]:
                pattern_index = prefix_table[pattern_index - 1]
            pattern_index += 1 if node.val == pattern[pattern_index] else 0

            # Check if the pattern is fully matched
            if pattern_index == len(pattern):
                return True

            # Recursively search left and right subtrees
            return _search_in_tree(
                node.left, pattern_index, pattern, prefix_table
            ) or _search_in_tree(node.right, pattern_index, pattern, prefix_table)

        # Build the pattern and prefix table from the linked list
        my_pattern = [head.val]
        my_prefix_table = [0]
        my_pattern_index = 0
        head = head.next

        while head:
            while my_pattern_index > 0 and head.val != my_pattern[my_pattern_index]:
                my_pattern_index = my_prefix_table[my_pattern_index - 1]
            my_pattern_index += 1 if head.val == my_pattern[my_pattern_index] else 0
            my_pattern.append(head.val)
            my_prefix_table.append(my_pattern_index)
            head = head.next

        # Perform DFS to search for the pattern in the tree
        return _search_in_tree(root, 0, my_pattern, my_prefix_table)

    @staticmethod
    def isSubPath_dfs_rec(head: ListNode | None, root: TreeNode | None) -> bool:
        def _dfs(node: TreeNode | None, list_node: ListNode | None) -> bool:
            if list_node is None:
                return True  # All nodes in the list matched
            if node is None:
                return False  # Reached end of tree without matching all nodes
            if node.val != list_node.val:
                return False  # Value mismatch
            return _dfs(node.left, list_node.next) or _dfs(node.right, list_node.next)

        def _check_path(node: TreeNode | None, list_node: ListNode | None) -> bool:
            if node is None:
                return False
            if _dfs(node, list_node):
                return True  # If a matching path is found

            # Recursively check left and right subtrees
            return _check_path(node.left, list_node) or _check_path(node.right, list_node)

        if root is None:
            return False
        return _check_path(root, head)

    @staticmethod
    def isSubPath_dfs_iter(head: ListNode | None, root: TreeNode | None) -> bool:
        if not head or not root:
            return False

        stack = [root]
        found = False

        def _traverse_tree_and_ll(tree_node):
            path_stack = [(tree_node, head)]

            while path_stack:
                current_node, current_list = path_stack.pop()

                while current_node and current_list:
                    if current_node.val != current_list.val:
                        break
                    current_list = current_list.next

                    # Continue to the next tree_node in the tree, left or right
                    if current_list:
                        if current_node.left:
                            path_stack.append((current_node.left, current_list))
                        if current_node.right:
                            path_stack.append((current_node.right, current_list))
                        break
                if not current_list:
                    return True
            return False

        while stack:
            node = stack.pop()
            if node.val == head.val:
                found = _traverse_tree_and_ll(node)
                if found:
                    break
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return found


@pytest.mark.parametrize(
    "head,root,expected",
    [
        (
            [4, 2, 8],
            [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3],
            True,
        ),
        (
            [1, 4, 2, 6],
            [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3],
            True,
        ),
        (
            [1, 4, 2, 6, 8],
            [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3],
            False,
        ),
    ],
)
def test_isSubPath(head, root, expected):
    assert Solution().isSubPath(make_ll(head), make_tree(root)) == expected
