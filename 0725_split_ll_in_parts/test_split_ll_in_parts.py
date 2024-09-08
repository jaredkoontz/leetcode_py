from typing import List

import pytest

from helpers.ll import ListNode
from helpers.ll import make_ll


class Solution:
    def splitListToParts(self, head: ListNode | None, k: int) -> List[ListNode | None]:
        return self.splitListToParts_split(head, k)

    @staticmethod
    def splitListToParts_split(head: ListNode | None, k: int) -> List[ListNode | None]:
        size = 0
        nodes = [None] * k
        node = head
        while node:
            size += 1
            node = node.next
        node = head
        num_nodes, remain = divmod(size, k)
        index = 0
        prev = node
        while node:
            # this will loop k times so we could do a forloop for readability

            new_part = node
            curr_count = num_nodes

            if remain:
                curr_count += 1
                remain -= 1

            while curr_count:
                prev = node
                if node is not None:
                    node = node.next
                curr_count -= 1

            # cut off the rest of linked list
            if prev is not None:
                prev.next = None

            nodes[index] = new_part
            index += 1

        return nodes

    @staticmethod
    def splitListToParts_split_copy(
        head: ListNode | None, k: int
    ) -> List[ListNode | None]:
        size = 0
        nodes = [None] * k
        node = head
        while node:
            size += 1
            node = node.next
        node = head
        num_nodes, remain = divmod(size, k)
        index = 0
        while node:
            new_part = ListNode()
            tail = new_part
            curr_count = num_nodes

            if remain:
                curr_count += 1
                remain -= 1

            while curr_count:
                tail.next = ListNode(node.val)
                tail = tail.next
                node = node.next
                curr_count -= 1
            nodes[index] = new_part.next
            index += 1

        return nodes

    @staticmethod
    def splitListToParts_wrong_directions(
        head: ListNode | None, k: int
    ) -> List[ListNode | None]:
        """
        read the instructions wrong 😭
        """
        nodes = [None] * k
        node = head
        index = 0
        while node:
            if not nodes[index]:
                nodes[index] = ListNode(node.val)
            else:
                to_insert = nodes[index]
                while to_insert.next:
                    to_insert = to_insert.next
                to_insert.next = ListNode(node.val)
            index = (index + 1) % k
            node = node.next

        return nodes


@pytest.mark.parametrize(
    "head,k,expected",
    [
        ([1, 2, 3], 5, [[1], [2], [3], [], []]),
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            3,
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11]],
        ),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]),
    ],
)
def test_splitListToParts(head, k, expected):
    as_ll = []
    for i in range(len(expected)):
        as_ll.append(make_ll(expected[i]))
    assert Solution().splitListToParts(make_ll(head), k) == as_ll
