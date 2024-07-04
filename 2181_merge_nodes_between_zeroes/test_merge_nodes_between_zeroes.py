import pytest

from helpers.ll import make_ll, ListNode


class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        ret_list = ListNode(0)
        ret_list_next = ret_list
        node = head.next
        while node:
            curr_sum = 0
            while node.val != 0:
                curr_sum += node.val
                node = node.next
            ret_list_next.next = ListNode(curr_sum)
            ret_list_next = ret_list_next.next
            node = node.next

        return ret_list.next


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([0, 3, 1, 0, 4, 5, 2, 0], [4, 11]),
        ([0, 1, 0, 3, 0, 2, 2, 0], [1, 3, 4]),
    ],
)
def test_mergeNodes(l1, expected):
    assert Solution().mergeNodes(make_ll(l1)) == make_ll(expected)
