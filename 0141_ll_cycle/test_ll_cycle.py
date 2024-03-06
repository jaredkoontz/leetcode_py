from typing import Optional

import pytest

from helpers.ll import ListNode
from helpers.ll import make_ll


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return self.hasCycle_hash_map(head)

    def hasCycle_tortise_hare(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    def hasCycle_hash_map(self, head: Optional[ListNode]) -> bool:
        # relies on distinct nodes and uses extra space 😭
        map = {}
        curr = head
        while curr:
            if curr.val in map:
                return True
            else:
                map[curr.val] = True
                curr = curr.next

        return False


@pytest.mark.parametrize(
    "l1,pos,expected",
    [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
    ],
)
def test_ll_cycle(l1, pos, expected):
    linked_list = make_ll(l1)
    if pos > 0:
        curr = linked_list

        while curr.next:
            curr = curr.next

        # curr now points to last node
        new_curr = linked_list
        for _ in range(pos):
            new_curr = new_curr.next
        curr.next = new_curr

    assert Solution().hasCycle(make_ll(l1)) == expected
