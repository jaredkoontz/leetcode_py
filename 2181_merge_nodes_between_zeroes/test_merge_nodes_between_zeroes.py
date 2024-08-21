# https://leetcode.com/problems/merge-nodes-in-between-zeros
import pytest

from helpers.ll import ListNode
from helpers.ll import make_ll


class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        return self.mergeNodes_no_dummy(head)

    @staticmethod
    def mergeNodes_no_dummy(head: ListNode | None) -> ListNode | None:
        pointer_1 = head
        pointer_2 = head.next
        curr_sum = 0
        while pointer_2:
            if pointer_2.val == 0:
                pointer_1 = pointer_1.next
                pointer_1.val = curr_sum
                curr_sum = 0
            else:
                curr_sum += pointer_2.val
            pointer_2 = pointer_2.next
        pointer_1.next = None
        return head.next

    @staticmethod
    def mergeNodes_dummy(head: ListNode | None) -> ListNode | None:
        ret_list = ListNode(0)
        ret_list_next = ret_list
        node = head.next
        while node:
            curr_sum = 0
            while node.val != 0:
                curr_sum += node.val
                node = node.next
            ret_list_next.next = ListNode(curr_sum)
            ret_list_next = ret_list_next.next
            node = node.next

        return ret_list.next


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([0, 3, 1, 0, 4, 5, 2, 0], [4, 11]),
        ([0, 1, 0, 3, 0, 2, 2, 0], [1, 3, 4]),
    ],
)
def test_mergeNodes(l1, expected):
    assert Solution().mergeNodes(make_ll(l1)) == make_ll(expected)
