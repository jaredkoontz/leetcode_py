import pytest

from helpers.ll import ListNode
from helpers.ll import make_ll


class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        return self.isPalindrome_reverse(head)

    @staticmethod
    def isPalindrome_reverse(head: ListNode | None) -> bool:
        fast = slow = head

        # find middle(slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # check
        left, right = head, prev
        while right:
            if right.val != left.val:
                return False
            left = left.next
            right = right.next
        return True

    @staticmethod
    def isPalindrome_arr_mine(head: ListNode | None) -> bool:
        arr = []
        if not head:
            return True

        while head:
            arr.append(head.val)
            head = head.next

        length = len(arr) // 2
        for i in range(0, length):
            if arr[i] != arr[-i - 1]:
                return False
        return True

    @staticmethod
    def isPalindrome_arr_neet(head: ListNode | None) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        left, right = 0, len(arr) - 1
        while left < right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1
        return True


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([2, 4, 3, 3], False),
        ([3, 4, 3], True),
        ([0], True),
        ([7], True),
        ([9, 9, 9, 9, 9, 9, 9], True),
    ],
)
def test_palindrome_ll(l1, expected):
    assert Solution().isPalindrome(make_ll(l1)) == expected
