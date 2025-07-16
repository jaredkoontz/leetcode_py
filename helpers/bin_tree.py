import dataclasses

import pytest


@dataclasses.dataclass
class TreeNode:
    val: int = 0
    left: "TreeNode" = None
    right: "TreeNode" = None

    def __str__(self):
        left_val = self.left.val if self.left is not None else "None"
        right_val = self.right.val if self.right is not None else "None"
        return f"{self.val} l={left_val} r={right_val}"

    # does not check for children, as no question has asked for it yet
    def __eq__(self, other):
        if isinstance(other, TreeNode):
            return self.val == other.val
        elif isinstance(other, int):
            return self.val == other
        return None

    def __hash__(self):
        return hash((self.val, self.left, self.right))


def make_tree(tree_array: list[int]) -> TreeNode | None:
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


def make_array_from_tree(root: TreeNode | None) -> list[int]:
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


def compare_trees(root1: TreeNode | None, root2: TreeNode | None) -> bool:
    stack = [(root1, root2)]
    while stack:
        n1, n2 = stack.pop()
        if n1 and n2 and n1.val == n2.val:
            stack.append((n1.right, n2.right))
            stack.append((n1.left, n2.left))
        elif n1 != n2:
            return False
    return True


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
    assert make_array_from_tree(make_tree(l1)) == l1
