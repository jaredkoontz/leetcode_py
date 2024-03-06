import math
from typing import Optional

import pytest

from helpers.ll import ListNode
from helpers.ll import make_ll


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        return self.insertGreatestCommonDivisors_mine(head)

    def insertGreatestCommonDivisors_theirs(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        cur = head.next
        prev = head

        while cur:
            gcd = math.gcd(cur.val, prev.val)
            gcd_node = ListNode(gcd)
            prev.next = gcd_node
            gcd_node.next = cur
            prev = cur
            cur = cur.next

        return head

    def insertGreatestCommonDivisors_mine(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            # find gcd
            gcd = math.gcd(curr.val, curr.next.val)
            gcd_node = ListNode(gcd)

            # update curr
            new_next = curr.next
            curr.next = gcd_node
            gcd_node.next = new_next

            curr = gcd_node.next
        return head


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([18, 6, 10, 3], [18, 6, 6, 2, 10, 1, 3]),
        ([7], [7]),
    ],
)
def test_add_two_numbers(l1, expected):
    assert Solution().insertGreatestCommonDivisors(make_ll(l1)) == make_ll(expected)
