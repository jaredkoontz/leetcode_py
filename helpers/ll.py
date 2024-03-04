
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


def make_ll(arr):
    head = ListNode(arr[0])
    curr = head
    for val in range(1, len(arr)):
        curr.next = ListNode(arr[val])
        curr = curr.next
    return head