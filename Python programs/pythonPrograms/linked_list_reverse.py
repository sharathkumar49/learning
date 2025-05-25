# Linked list reversal (iterative & recursive)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_iterative(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def reverse_recursive(head):
    if not head or not head.next:
        return head
    rest = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return rest

if __name__ == "__main__":
    a = Node(1); b = Node(2); c = Node(3)
    a.next = b; b.next = c
    head = reverse_iterative(a)
    while head:
        print(head.val, end=' ')
        head = head.next
