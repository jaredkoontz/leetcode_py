import pytest

from helpers.ll import create_ll_cycle
from helpers.ll import ListNode
from helpers.ll import make_ll


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode | None:
        return self.detectCycle_tortise_hare(head)

    @staticmethod
    def detectCycle_tortise_hare(head: ListNode) -> ListNode | None:
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
    "l1,pos,expected_val,expected_index",
    [
        ([3, 2, 0, -4], 1, 2, 1),
        ([1, 2], 0, 1, 0),
        ([1], -1, None, None),
    ],
)
def test_ll_cycle2(l1, pos, expected_val, expected_index):
    linked_list = make_ll(l1)
    if pos >= 0:
        create_ll_cycle(linked_list, pos)
    expected_node = ListNode(expected_val) if expected_val else None
    node = Solution().detectCycle(linked_list)
    my_index = None
    for i, arr_val in enumerate(l1):
        if arr_val == expected_val:
            my_index = i
            break
    assert node == expected_node
    assert my_index == expected_index
