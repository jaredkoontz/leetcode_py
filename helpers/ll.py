class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

    def __str__(self):
        result = "["
        head = self
        if head:
            result += str(head.val)
            head = head.next
            while head:
                result += ", " + str(head.val)
                head = head.next
        result += "]"
        return result

    def __eq__(self, other: "ListNode"):
        mine = self
        if mine and other:
            return mine.val == other.val
        return False


def compare_lls(l1: ListNode, l2: ListNode) -> bool:
    while l1 and l2:
        if l1 != l2:
            return False
        l1 = l1.next
        l2 = l2.next
    if l1 or l2:
        return False
    return True


def create_ll_cycle(head: ListNode, pos: int) -> ListNode:
    curr = head

    while curr.next:
        curr = curr.next

    # curr now points to last node
    new_curr = head
    for _ in range(pos):
        new_curr = new_curr.next
    curr.next = new_curr
    return head


def make_ll(arr: list[int]) -> ListNode | None:
    """makes a linked list from an array of integers"""
    if not arr:
        return None
    if len(arr) != 0:
        head = ListNode(arr[0])
        curr = head
        for val in range(1, len(arr)):
            curr.next = ListNode(arr[val])
            curr = curr.next
        return head
    return None
