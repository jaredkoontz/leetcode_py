# https://leetcode.com/problems/sort-list
import pytest

from helpers.ll import compare_lls
from helpers.ll import ListNode
from helpers.ll import make_ll


class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        # split the linked list into halves
        left = head
        right = self.get_middle_node(head)

        tmp = right.next
        right.next = None
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)

    @staticmethod
    def get_middle_node(head: ListNode) -> ListNode:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    @staticmethod
    def merge(left: ListNode, right: ListNode) -> ListNode:
        tail = dummy = ListNode(0)

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        if left:
            tail.next = left
        if right:
            tail.next = right

        return dummy.next


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([4, 2, 1, 3], [1, 2, 3, 4]),
        ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5]),
        ([0], [0]),
        ([], []),
    ],
)
def test_sort_ll(l1, expected):
    assert compare_lls(Solution().sortList(make_ll(l1)), make_ll(expected))
