import pytest

from helpers.ll import create_ll_cycle
from helpers.ll import ListNode
from helpers.ll import make_ll


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        return self.hasCycle_tortise_hare(head)

    def hasCycle_tortise_hare(self, head: ListNode) -> bool:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast.val == slow.val:
                return True
        return False

    def hasCycle_hash_map(self, head: ListNode) -> bool:
        # relies on distinct nodes and uses extra space 😭
        h_map = {}
        curr = head
        while curr:
            if curr.val in h_map:
                return True
            else:
                h_map[curr.val] = True
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
    if pos >= 0:
        create_ll_cycle(linked_list, pos)

    assert Solution().hasCycle(linked_list) == expected
