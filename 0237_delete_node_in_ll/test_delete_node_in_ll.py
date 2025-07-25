# https://leetcode.com/problems/delete-node-in-a-linked-list
import pytest

from helpers.ll import compare_lls
from helpers.ll import make_ll


class Solution:
    def deleteNode(self, node) -> None:
        return self.deleteNode_mine(node)

    @staticmethod
    def deleteNode_mine(node) -> None:
        """delete the node by just making the next one this one"""
        if not node or not node.next:
            return

        node.val = node.next.val  # Copy next node's value
        node.next = node.next.next  # Skip the next node, effectively deleting it


@pytest.mark.parametrize(
    "l1,node,expected",
    [
        ([4, 5, 1, 9], 5, [4, 1, 9]),
        ([4, 5, 1, 9], 1, [4, 5, 9]),
    ],
)
def test_deleteNode(l1, node, expected):
    head = make_ll(l1)
    pointer = head
    while pointer.val != node:
        pointer = pointer.next
    Solution().deleteNode_mine(pointer)
    assert compare_lls(head, make_ll(expected))
