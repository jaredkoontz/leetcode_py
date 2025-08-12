# https://leetcode.com/problems/remove-nth-node-from-end-of-list
import pytest

from helpers.ll import ListNode
from helpers.ll import compare_lls
from helpers.ll import make_ll


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        return self.removeNthFromEnd_reverse(head, n)

    @staticmethod
    def removeNthFromEnd_reverse(head: ListNode | None, n: int) -> ListNode | None:
        def _reverse_ll(my_node):
            curr = my_node
            previous = None
            while curr:
                next_node = curr.next
                curr.next = previous
                previous = curr
                curr = next_node

            return previous

        reverse = _reverse_ll(head)

        index = 1
        node = reverse
        prev = None
        while index < n and reverse:
            prev = reverse
            reverse = reverse.next
            index += 1

        if not prev:
            return _reverse_ll(node.next)

        prev.next = prev.next.next
        return _reverse_ll(node)

    @staticmethod
    def removeNthFromEnd_fast(head: ListNode | None, n: int) -> ListNode | None:
        fast, slow = head, head
        index = 0
        while fast and index < n:
            fast = fast.next
            index += 1

        if not fast:
            return slow.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

    @staticmethod
    def removeNthFromEnd_mine(head: ListNode | None, n: int) -> ListNode | None:
        if not head.next:
            return None

        length = 0
        node = head

        while node:
            length += 1
            node = node.next

        node = head
        one_to_remove = length - n - 1

        if one_to_remove == -1:
            return head.next

        count = 0
        while node:
            if count == one_to_remove:
                node.next = node.next.next if node.next else None
                break
            count += 1
            node = node.next
        return head


@pytest.mark.parametrize(
    "l1, n ,expected",
    [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
        ([1, 2, 3], 3, [2, 3]),
    ],
)
def test_remove_nth_node_end(l1, n, expected):
    assert compare_lls(Solution().removeNthFromEnd(make_ll(l1), n), make_ll(expected))
