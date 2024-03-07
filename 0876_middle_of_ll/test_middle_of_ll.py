from typing import Optional

import pytest

from helpers.ll import make_ll, ListNode, compare_lls


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([1, 2, 3, 4, 5], [3, 4, 5]),
        ([1, 2, 3, 4, 5, 6], [4, 5, 6]),
    ],
)
def test_ll_middle(l1, expected):
    linked_list1 = make_ll(l1)
    linked_list2 = make_ll(expected)
    assert compare_lls(Solution().middleNode(linked_list1), linked_list2)
