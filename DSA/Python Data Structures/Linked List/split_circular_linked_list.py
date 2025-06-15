# Split a Circular Linked List into Two Halves
from linked_list_impl import Node, LinkedList

def split_circular_linked_list(head):
    if not head or not head.next:
        return head, None
    slow = head
    fast = head
    while fast.next != head and fast.next.next != head:
        slow = slow.next
        fast = fast.next.next
    head1 = head
    head2 = slow.next
    slow.next = head1
    curr = head2
    while curr.next != head:
        curr = curr.next
    curr.next = head2
    return head1, head2
# Example usage omitted for brevity
