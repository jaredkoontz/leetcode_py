# https://leetcode.com/problems/binary-tree-postorder-traversal
import pytest

from helpers.bin_tree import TreeNode
from helpers.bin_tree import make_tree


class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        return self.postorderTraversal_recursive(root)

    @staticmethod
    def postorderTraversal_stack(root: TreeNode | None) -> list[int]:
        result = []

        # If the root is null, return an empty list
        if root is None:
            return result

        # To keep track of the previously processed node
        previous_node = None
        # Stack to manage the traversal
        traversal_stack = []

        # Process nodes until both the root is null and the stack is empty
        while root is not None or len(traversal_stack) > 0:
            # Traverse to the leftmost node
            if root is not None:
                traversal_stack.append(root)
                root = root.left
            else:
                # Peek at the top node of the stack
                root = traversal_stack[-1]

                # If there is no right child or the right child was already processed
                if root.right is None or root.right == previous_node:
                    result.append(root.val)
                    traversal_stack.pop()
                    previous_node = root
                    root = None  # Ensure we don’t traverse again from this node
                else:
                    # Move to the right child
                    root = root.right

        return result

    @staticmethod
    def postorderTraversal_two_stack(root: TreeNode | None) -> list[int]:
        result = []

        # If the root is null, return an empty list
        if root is None:
            return result

        # Stack to manage the traversal
        main_stack = []
        # Stack to manage the path
        path_stack = []

        # Start with the root node
        main_stack.append(root)

        # Process nodes until the main stack is empty
        while main_stack:
            root = main_stack[-1]

            # If the node is in the path stack and it's the top, add its value
            if path_stack and path_stack[-1] == root:
                result.append(root.val)
                main_stack.pop()
                path_stack.pop()
            else:
                # Push the current node to the path stack
                path_stack.append(root)
                # Push right child if it exists
                if root.right is not None:
                    main_stack.append(root.right)
                # Push left child if it exists
                if root.left is not None:
                    main_stack.append(root.left)

        return result

    @staticmethod
    def postorderTraversal_stack_trick(root: TreeNode | None) -> list[int]:
        # List to store the result of postorder traversal
        result = []
        # Stack to facilitate the traversal of nodes
        traversal_stack = []
        current_node = root

        # Traverse the tree while there are nodes to process
        while current_node or traversal_stack:
            if current_node:
                # Add current node's value to result list before going to its children
                result.append(current_node.val)
                # Push current node onto the stack
                traversal_stack.append(current_node)
                # Move to the right child
                current_node = current_node.right
            else:
                # Pop the node from the stack and move to its left child
                current_node = traversal_stack.pop()
                current_node = current_node.left
        # Reverse the result list to get the correct postorder sequence
        result.reverse()
        return result

    @staticmethod
    def postorderTraversal_recursive(root: TreeNode | None) -> list[int]:
        nodes = []

        def post_order(node):
            if node:
                post_order(node.left)
                post_order(node.right)
                nodes.append(node.val)
            return

        post_order(root)
        return nodes


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
    assert Solution().postorderTraversal(make_tree(l1)) == expected
