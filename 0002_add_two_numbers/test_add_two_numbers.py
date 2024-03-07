import pytest

from helpers.ll import compare_lls
from helpers.ll import ListNode
from helpers.ll import make_ll


class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            new_dig = v1 + v2 + carry
            carry = new_dig // 10
            new_dig = new_dig % 10

            curr.next = ListNode(new_dig)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


@pytest.mark.parametrize(
    "l1,l2,expected",
    [
        ([2, 4, 3, 3], [5, 6, 4], [7, 0, 8, 3]),
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([7], [8], [5, 1]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ],
)
def test_add_two_numbers(l1, l2, expected):
    assert compare_lls(
        Solution().addTwoNumbers(make_ll(l1), make_ll(l2)), make_ll(expected)
    )
