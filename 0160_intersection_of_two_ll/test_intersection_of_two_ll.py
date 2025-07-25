# https://leetcode.com/problems/intersection-of-two-linked-lists
import pytest

from helpers.ll import ListNode
from helpers.ll import make_ll


class Solution:
    def getIntersectionNode(
        self, head_a: ListNode, head_b: ListNode
    ) -> ListNode | None:
        return self.getIntersectionNode_mine(head_a, head_b)

    @staticmethod
    def getIntersectionNode_mine(head_a: ListNode, head_b: ListNode) -> ListNode | None:
        def ll_len(node: ListNode):
            length = 0
            while node:
                node = node.next
                length += 1
            return length

        len_a = ll_len(head_a)
        len_b = ll_len(head_b)

        # move head_a and head_b to the same start point
        while len_a > len_b:
            head_a = head_a.next
            len_a -= 1

        while len_a < len_b:
            head_b = head_b.next
            len_b -= 1

        # find the intersection until end
        while head_a != head_b:
            head_a = head_a.next
            head_b = head_b.next

        return head_a


@pytest.mark.parametrize(
    "head_a, head_b, expected",
    [
        ([4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 1),
        ([1, 9, 1, 2, 4], [3, 2, 4], 2),
        ([2, 6, 4], [1, 5], None),
    ],
)
def test_getIntersectionNode(head_a, head_b, expected):
    node = Solution().getIntersectionNode(make_ll(head_a), make_ll(head_b))
    assert node.val == expected if node else expected is None
