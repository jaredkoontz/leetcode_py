# https://leetcode.com/problems/remove-nodes-from-linked-list
import pytest

from helpers.ll import compare_lls
from helpers.ll import ListNode
from helpers.ll import make_ll


class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        # assert (
        #     self.removeNodes_reverse_and_filter_optimal(head)
        #     == self.removeNodes_reverse_and_filter(head)
        #     == self.removeNodes_stack(head)
        #     == self.removeNodes_rec(head)
        # )
        return self.removeNodes_reverse_and_filter_optimal(head)

    @staticmethod
    def removeNodes_reverse_and_filter_optimal(
        head: ListNode | None,
    ) -> ListNode | None:
        if not head or not head.next:
            return head

        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        curr, prev.next = prev.next, None
        while curr:
            temp = curr.next
            if curr.val >= prev.val:
                curr.next = prev
                prev = curr
            curr = temp

        return prev

    @staticmethod
    def removeNodes_reverse_and_filter(head: ListNode | None) -> ListNode | None:
        # Reverse the list
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # Initialize a dummy node to hold the result
        dummy_head = ListNode(-1)
        temp_prev, curr = dummy_head, prev
        # Traverse the reversed list, keeping nodes greater or equal to previous
        while curr:
            if curr.val >= temp_prev.val:
                temp_prev.next = curr
                temp_prev = curr
                curr = curr.next
            else:
                curr = curr.next
        temp_prev.next = None

        # Reverse the result list again
        new_prev = None
        curr = dummy_head.next
        while curr:
            curr.next, new_prev, curr = new_prev, curr, curr.next

        return new_prev

    @staticmethod
    def removeNodes_stack(head: ListNode | None) -> ListNode | None:
        cur = head
        stack = []
        while cur:
            while stack and stack[-1].val < cur.val:
                stack.pop()
            stack.append(cur)
            cur = cur.next

        nxt = None
        while stack:
            cur = stack.pop()
            cur.next = nxt
            nxt = cur

        return cur

    def removeNodes_rec(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None
        node = head
        # Gives next greater node
        nxt_greater = self.removeNodes_rec(node.next)

        node.next = nxt_greater
        if not nxt_greater or node.val >= nxt_greater.val:
            return node
        return nxt_greater


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([5, 2, 13, 3, 8], [13, 8]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
        ([1, 1, 0, 1], [1, 1, 1]),
        ([1, 2, 1, 1], [2, 1, 1]),
    ],
)
def test_remove_nodes(l1, expected):
    assert compare_lls(Solution().removeNodes(make_ll(l1)), make_ll(expected))
