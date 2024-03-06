from typing import Optional

import pytest

from helpers.ll import ListNode
from helpers.ll import make_ll


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse_recurse(head)

    def reverse_recurse(self, head):
        def reverse(cur, prev):
            # reached the end of the list, return previous
            if cur is None:
                return prev
            else:
                # grab the next node
                next_node = cur.next

                cur.next = prev
                return reverse(next_node, cur)

        return reverse(head, None)


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([], []),
    ],
)
def test_add_two_numbers(l1, expected):
    assert Solution().reverseList(make_ll(l1)) == make_ll(expected)
