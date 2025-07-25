# https://leetcode.com/problems/swap-nodes-in-pairs
import pytest

from helpers.ll import compare_lls
from helpers.ll import ListNode
from helpers.ll import make_ll


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        return self.swapPairs_rec(head)

    @staticmethod
    def swapPairs_rec(head: ListNode | None) -> ListNode | None:
        def helper(node: ListNode) -> ListNode:
            if node is None or node.next is None:
                return node

            first = node
            second = node.next

            # Recursively swap the rest
            first.next = helper(second.next)
            second.next = first

            return second

        return helper(head)

    @staticmethod
    def swapPairs_iter(head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            first = head
            second = head.next

            # Swapping
            prev.next = second
            first.next = second.next
            second.next = first

            # Move pointers
            prev = first
            head = first.next

        return dummy.next


@pytest.mark.parametrize(
    "head,expected",
    [
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [2, 1, 3]),
        ([1, 2, 3, 4], [2, 1, 4, 3]),
    ],
)
def test_swapPairs(head, expected):
    assert compare_lls(Solution().swapPairs(make_ll(head)), make_ll(expected))
