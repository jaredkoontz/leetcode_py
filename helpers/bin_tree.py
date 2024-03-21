import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        left_val = self.left.val if self.left is not None else "None"
        right_val = self.right.val if self.right is not None else "None"
        return f"{self.val} l={left_val} r={right_val}"


def create_tree(tree_array: list[int]) -> TreeNode | None:
    # array = [root, root.left, root.right, root.left.left, ...]
    if not tree_array:
        return None

    it = iter(tree_array)
    root = TreeNode(next(it))
    queue = [root]
    for node in queue:
        val = next(it, None)
        if val is not None:
            node.left = TreeNode(val)
            queue.append(node.left)
        val = next(it, None)
        if val is not None:
            node.right = TreeNode(val)
            queue.append(node.right)
    return root


def create_array_from_tree(root):
    if not root:
        return []

    # Level traverse
    my_list, q, node = [], [], root
    while node:
        my_list.append(node.val)
        left, right = node.left, node.right
        if left:
            q.insert(0, left)
        if right:
            q.insert(0, right)
        node = None if not q else q.pop()
    return my_list


@pytest.mark.parametrize(
    "l1",
    [
        ([1, None, 2, 3]),
        ([1, 2, None, 3]),
        ([1, 2, 3]),
        ([1, 4, 2, 3]),
        ([1, 5, 2, 3, 4]),
    ],
)
def test_bin_tree_maker(l1):
    # todo fails because of none
    assert create_array_from_tree(create_tree(l1)) == l1
