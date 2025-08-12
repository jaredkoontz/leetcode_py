# https://leetcode.com/problems/rotate-list
import pytest

from helpers.ll import compare_lls
from helpers.ll import ListNode
from helpers.ll import make_ll


class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        return self.rotateRight_one_rotation(head, k)

    @staticmethod
    def rotateRight_one_rotation_explanation(
        head: ListNode | None, k: int
    ) -> ListNode | None:
        if not head:
            return None

        last_element = head
        length = 1
        # get the length of the list and the last node in the list
        while last_element.next:
            last_element = last_element.next
            length += 1

        # If k is equal to the length of the list then k == 0
        # ElIf k is greater than the length of the list then k = k % length
        k = k % length

        # Set the last node to point to head node
        # The list is now a circular linked list with last node pointing to first node
        last_element.next = head

        # Traverse the list to get to the node just before the ( length - k )th node.
        # Example: In 1->2->3->4->5, and k = 2
        #          we need to get to the Node(3)
        temp_node = head
        for _ in range(length - k - 1):
            temp_node = temp_node.next

        # Get the next node from the temp_node and then set the temp_node.next as None
        # Example: In 1->2->3->4->5, and k = 2
        #          temp_node = Node(3)
        #          answer = Node(3).next => Node(4)
        #          Node(3).next = None ( cut the linked list from here )
        answer = temp_node.next
        temp_node.next = None

        return answer

    @staticmethod
    def rotateRight_one_rotation(head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next:
            return head
        node, length = head, 1
        while node.next:
            length += 1
            node = node.next

        k %= length
        if k == 0:
            return head

        fast = head
        for _ in range(length - k - 1):
            fast = fast.next
        new_head = fast.next
        node.next = head
        fast.next = None

        return new_head

    @staticmethod
    def rotateRight_mine(head: ListNode | None, k: int) -> ListNode | None:
        def _rotate_list(my_head: ListNode | None):
            node = my_head
            new_tail_node = None
            while node.next:
                if not node.next.next:
                    new_tail_node = node

                node = node.next

            if new_tail_node:
                new_tail_node.next = None
                last = node
                last.next = my_head
                return last
            else:
                # ll of len 1
                return head

        def _get_ll_len(my_head: ListNode | None) -> int:
            length = 1
            node = my_head
            while node.next:
                length += 1
                node = node.next
            return length

        if not head or not head.next:
            return head

        num_rotations = k % _get_ll_len(head)

        new_head = head
        for _ in range(num_rotations):
            new_head = _rotate_list(new_head)
        return new_head


@pytest.mark.parametrize(
    "l1,k,expected",
    [
        ([], 3, []),
        ([0], 4, [0]),
        ([0], 30000, [0]),
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
        ([0, 1, 2], 4, [2, 0, 1]),
        ([0, 1], 4, [0, 1]),
        ([0, 1], 5, [1, 0]),
    ],
)
def test_rotate_ll(l1, k, expected):
    assert compare_lls(Solution().rotateRight(make_ll(l1), k), make_ll(expected))
