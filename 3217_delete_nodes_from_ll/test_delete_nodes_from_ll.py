# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array
import pytest

from helpers.ll import ListNode
from helpers.ll import make_ll


class Solution:
    def modifiedList(self, nums: list[int], head: ListNode | None) -> ListNode | None:
        return self.modifiedList_dummy(nums, head)

    @staticmethod
    def modifiedList_no_dummy(
            nums: list[int], head: ListNode | None
    ) -> ListNode | None:
        nums = set(nums)
        prev = None
        cur = head
        while cur:
            if cur.val in nums:
                if prev:
                    prev.next = cur.next
                else:
                    head = cur.next
            else:
                prev = cur
            cur = cur.next
        return head

    @staticmethod
    def modifiedList_dummy(nums: list[int], head: ListNode | None) -> ListNode | None:
        nums = set(nums)
        dummy = ListNode()
        dummy.next = head
        node = dummy

        while node.next:
            if node.next.val in nums:
                node.next = node.next.next
            else:
                node = node.next
        return dummy.next


@pytest.mark.parametrize(
    "nums,head,expected",
    [
        ([1, 2, 3], [1, 2, 3, 4, 5], [4, 5]),
        ([1], [1, 2, 1, 2, 1, 2], [2, 2, 2]),
        ([5], [1, 2, 3, 4], [1, 2, 3, 4]),
        ([], [], None),
    ],
)
def test_modifiedList(nums, head, expected):
    assert Solution().modifiedList(nums, make_ll(head)) == make_ll(expected)
