from typing import Optional

import pytest

from helpers.ll import compare_lls
from helpers.ll import ListNode
from helpers.ll import make_ll


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.removeZeroSumSublists_mine(head)

    def removeZeroSumSublists_mine(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        # store the cumulative sum and corresponding node
        prefix_sum_map = {}

        prefix_sum = 0
        current = dummy

        # calculate the cumulative sum and store it in dict
        while current:
            prefix_sum += current.val
            prefix_sum_map[prefix_sum] = current
            current = current.next

        prefix_sum = 0
        current = dummy

        # Update the next pointers of each node based on the cumulative sum stored in the dict
        # effectively removing zero-sum sublists.
        while current:
            prefix_sum += current.val
            current.next = prefix_sum_map[prefix_sum].next
            current = current.next

        return dummy.next

    def removeZeroSumSublists_theirs(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        prefix_sums = {0: dummy}
        curr = head

        while curr:
            prefix_sum += curr.val
            if prefix_sum in prefix_sums:
                to_delete = prefix_sums[prefix_sum].next
                temp_sum = prefix_sum + to_delete.val
                while to_delete != curr:
                    del prefix_sums[temp_sum]
                    to_delete = to_delete.next
                    temp_sum += to_delete.val
                prefix_sums[prefix_sum].next = curr.next
            else:
                prefix_sums[prefix_sum] = curr
            curr = curr.next

        return dummy.next


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([1, 2, -3, 3, 1], [3, 1]),
        ([1, 2, 3, -3, 4], [1, 2, 4]),
        ([1, 2, 3, -3, -2], [1]),
        ([], []),
        ([1], [1]),
        ([0], []),
    ],
)
def test_remove_duplicates_ll(l1, expected):
    assert compare_lls(Solution().removeZeroSumSublists(make_ll(l1)), make_ll(expected))
