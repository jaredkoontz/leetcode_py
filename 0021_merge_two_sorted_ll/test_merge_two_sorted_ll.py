from typing import Optional

import pytest

from helpers.ll import compare_lls
from helpers.ll import ListNode
from helpers.ll import make_ll


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        return self.mergeTwoLists_in_place(list1, list2)

    def mergeTwoLists_in_place(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        while list2:
            node1, node2 = list1, list2
            list2 = list2.next

            if node2.val <= node1.val:
                node2.next = node1
                list1 = node2
            else:
                prev = None
                while node1 and node2.val > node1.val:
                    prev = node1
                    node1 = node1.next

                temp = prev.next
                prev.next = node2
                node2.next = temp

        return list1

    def mergeTwoLists_extra(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        import sys

        max_size = sys.maxsize

        dummy_head = ListNode(0)
        dummy = dummy_head
        curr_list1, curr_list2 = list1, list2

        while curr_list1 or curr_list2:
            curr1_val = curr_list1.val if curr_list1 else max_size
            curr2_val = curr_list2.val if curr_list2 else max_size

            if curr1_val <= curr2_val:
                dummy.next = ListNode(curr1_val)
                curr_list1 = curr_list1.next
            else:
                dummy.next = ListNode(curr2_val)
                curr_list2 = curr_list2.next

            dummy = dummy.next

        return dummy_head.next


@pytest.mark.parametrize(
    "l1,l2,expected",
    [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
    ],
)
def test_merge_ll(l1, l2, expected):
    assert compare_lls(
        Solution().mergeTwoLists(make_ll(l1), make_ll(l2)), make_ll(expected)
    )
