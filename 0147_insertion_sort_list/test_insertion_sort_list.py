# https://leetcode.com/problems/insertion-sort-list
import pytest

from helpers.ll import compare_lls
from helpers.ll import ListNode
from helpers.ll import make_ll


class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
        return self.insertionSortList_mine(head)

    @staticmethod
    def insertionSortList_mine(head: ListNode | None) -> ListNode | None:
        def insertion_sort(dummy_head: ListNode, val: int):
            while dummy_head.next and dummy_head.next.val < val:
                dummy_head = dummy_head.next
            if not dummy_head.next:
                dummy_head.next = ListNode(val)
            else:
                node = ListNode(val)
                old_next = dummy_head.next
                node.next = old_next
                dummy_head.next = node

        dummy = ListNode()
        while head:
            insertion_sort(dummy, head.val)
            head = head.next

        return dummy.next


@pytest.mark.parametrize(
    "head,expected",
    [
        ([1, 1], [1, 1]),
        ([4, 2, 1, 3], [1, 2, 3, 4]),
        ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5]),
    ],
)
def test_insertionSortList(head, expected):
    assert compare_lls(Solution().insertionSortList(make_ll(head)), make_ll(expected))
