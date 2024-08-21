# https://leetcode.com/problems/reverse-linked-list
import pytest

from helpers.ll import compare_lls
from helpers.ll import ListNode
from helpers.ll import make_ll


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        return self.reverse_iterative(head)

    @staticmethod
    def reverse_iterative(head: ListNode | None) -> ListNode | None:
        curr = head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    @staticmethod
    def reverse_recurse(head: ListNode | None) -> ListNode | None:
        def reverse(cur: ListNode | None, prev: ListNode | None):
            # reached the end of the list, return previous
            if cur is None:
                return prev
            else:
                # grab the next node
                next_node = cur.next

                cur.next = prev
                return reverse(next_node, cur)

        return reverse(head, None)


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([], []),
    ],
)
def test_reverse_ll(l1, expected):
    assert compare_lls(Solution().reverseList(make_ll(l1)), make_ll(expected))
