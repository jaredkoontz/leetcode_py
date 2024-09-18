import pytest

from helpers.bin_tree import make_tree


def preorderTraversal(root):
    if not root:
        return []

    stack, output = [root], []

    while stack:
        node = stack.pop()
        if node:
            output.append(node.val)
            stack.append(node.right)  # Right child pushed first
            stack.append(node.left)  # Left child pushed second

    return output


def inorderTraversal(root):
    stack, output = [], []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        output.append(current.val)
        current = current.right

    return output


def postorderTraversal_no_reverse(root):
    if not root:
        return []

    stack, output = [], []
    last_visited = None
    current = root

    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            peek_node = stack[-1]
            # if right child exists and hasn't been visited yet, visit it
            if peek_node.right and last_visited != peek_node.right:
                current = peek_node.right
            else:
                output.append(peek_node.val)
                last_visited = stack.pop()

    return output


def postorderTraversal(root):
    if not root:
        return []

    stack, output = [root], []

    while stack:
        node = stack.pop()
        if node:
            output.append(node.val)
            stack.append(node.left)  # Left child pushed first
            stack.append(node.right)  # Right child pushed second

    return output[::-1]  # Reverse the output to get left-right-root


@pytest.mark.parametrize(
    "root,expected",
    [
        ([1, 2, 5, 3, 4, None, 6], [1, 2, 3, 4, 5, 6]),
    ],
)
def test_preorder(root, expected):
    assert preorderTraversal(make_tree(root)) == (expected)


@pytest.mark.parametrize(
    "root,expected",
    [
        ([1, 2, 5, 3, 4, None, 6], [3, 2, 4, 1, 5, 6]),
    ],
)
def test_inorder(root, expected):
    assert inorderTraversal(make_tree(root)) == (expected)


@pytest.mark.parametrize(
    "root,expected",
    [
        ([1, 2, 5, 3, 4, None, 6], [3, 4, 2, 6, 5, 1]),
    ],
)
def test_postorder(root, expected):
    assert postorderTraversal(make_tree(root)) == (expected)


@pytest.mark.parametrize(
    "root,expected",
    [
        ([1, 2, 5, 3, 4, None, 6], [3, 4, 2, 6, 5, 1]),
    ],
)
def test_postorder_no_reverse(root, expected):
    assert postorderTraversal_no_reverse(make_tree(root)) == (expected)
