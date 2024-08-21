# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii
import pytest

from helpers.ll import compare_lls
from helpers.ll import ListNode
from helpers.ll import make_ll


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        return self.deleteDuplicates_mine(head)

    @staticmethod
    def deleteDuplicates_mine(head: ListNode | None) -> ListNode | None:
        dummy = ListNode()

        dummy.next = head
        cur = dummy

        while cur:
            # if the next two are dupes, move forward
            if cur.next and cur.next.next and cur.next.val == cur.next.next.val:
                tmp = cur.next.next
                while tmp and tmp.next and tmp.val == tmp.next.val:
                    tmp = tmp.next
                cur.next = tmp.next
            else:
                cur = cur.next

        return dummy.next


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]),
        ([1, 1, 2], [2]),
        ([1, 1, 2, 3, 3], [2]),
        ([1, 1, 2, 3], [2, 3]),
        ([], []),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([0], [0]),
    ],
)
def test_remove_duplicates_ll(l1, expected):
    assert compare_lls(Solution().deleteDuplicates(make_ll(l1)), make_ll(expected))
