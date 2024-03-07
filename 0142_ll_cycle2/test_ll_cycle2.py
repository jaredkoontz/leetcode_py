import pytest

from helpers.ll import create_ll_cycle
from helpers.ll import ListNode
from helpers.ll import make_ll


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode | None:
        return self.detectCycle_tortise_hare(head)

    def detectCycle_tortise_hare(self, head: ListNode) -> ListNode | None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # If the pointers meet, there is a cycle in the linked list.
                # Reset the slow pointer to the head of the linked list, and move both pointers one step at a time
                # until they meet again. The node where they meet is the starting point of the cycle.
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None


@pytest.mark.parametrize(
    "l1,pos,expected",
    [
        ([3, 2, 0, -4], 1, 2),
        ([1, 2], 0, 1),
        ([1], -1, None),
    ],
)
def test_ll_cycle(l1, pos, expected):
    # the official site will verify the index. for ease, we are just comparing node.val
    linked_list = make_ll(l1)
    if pos >= 0:
        create_ll_cycle(linked_list, pos)
    expected_node = ListNode(expected) if expected else None
    assert Solution().detectCycle(linked_list) == expected_node
