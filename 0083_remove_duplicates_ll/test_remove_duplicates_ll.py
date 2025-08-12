# https://leetcode.com/problems/remove-duplicates-from-sorted-list
import pytest

from helpers.ll import ListNode
from helpers.ll import compare_lls
from helpers.ll import make_ll


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        return self.deleteDuplicates_mine(head)

    @staticmethod
    def deleteDuplicates_mine(head: ListNode | None) -> ListNode | None:
        cur = head
        if head:
            while cur and cur.next:
                if cur.val == cur.next.val:
                    cur.next = cur.next.next
                else:
                    cur = cur.next
        return head

    @staticmethod
    def deleteDuplicates_theirs(head: ListNode | None) -> ListNode | None:
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([1, 1, 2], [1, 2]),
        ([1, 1, 2, 3, 3], [1, 2, 3]),
        ([], []),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([0], [0]),
    ],
)
def test_remove_duplicates_ll(l1, expected):
    result = Solution().deleteDuplicates(make_ll(l1))
    print(result)
    assert compare_lls(result, make_ll(expected))
