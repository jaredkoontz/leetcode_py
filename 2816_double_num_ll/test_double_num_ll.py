# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list
import pytest

from helpers.ll import compare_lls
from helpers.ll import ListNode
from helpers.ll import make_ll


class Solution:
    def doubleIt(self, head: ListNode | None) -> ListNode | None:
        return self.doubleIt_optimal(head)

    @staticmethod
    def doubleIt_optimal(head: ListNode | None) -> ListNode | None:
        if not head:
            return None
        # are we going to need a new a tens place?
        if head.val > 4:
            head = ListNode(0, head)
        node = head
        while node:
            node.val = (2 * node.val) % 10
            if node.next and node.next.val > 4:
                # carry the one
                node.val += 1
            node = node.next
        return head

    @staticmethod
    def doubleIt_first_try(head: ListNode | None) -> ListNode | None:
        if not head:
            return None
        val = 0
        nums_list = []
        while head:
            nums_list.append(head.val)
            head = head.next
        tens_place = 1
        # create int
        for i in range(len(nums_list) - 1, -1, -1):
            val += nums_list[i] * tens_place
            tens_place *= 10
        # double it
        val *= 2
        # turn back into list
        new_list = map(int, str(val))
        new_list = [x for x in new_list]
        if len(new_list) != 0:
            new_head = ListNode(new_list[0])
            curr = new_head
            for val in range(1, len(new_list)):
                curr.next = ListNode(new_list[val])
                curr = curr.next
            return new_head


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([1, 8, 9], [3, 7, 8]),
        ([9, 9, 9], [1, 9, 9, 8]),
        ([1], [2]),
        ([2], [4]),
        ([5], [1, 0]),
        ([5], [1, 0]),
    ],
)
def test_doubleIt(l1, expected):
    assert compare_lls(Solution().doubleIt(make_ll(l1)), make_ll(expected))
