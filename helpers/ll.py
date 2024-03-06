class ListNode(object):
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = "["
        node = self
        if node is not None:
            result += str(node.val)
            node = node.next
            while node:
                result += ", " + str(node.val)
                node = node.next
        result += "]"
        return result

    def __eq__(self, other):
        mine = self
        while mine and other:
            if mine.val != other.val:
                return False
            mine = mine.next
            other = other.next
        return True


def make_ll(arr):
    if len(arr) != 0:
        head = ListNode(arr[0])
        curr = head
        for val in range(1, len(arr)):
            curr.next = ListNode(arr[val])
            curr = curr.next
        return head
