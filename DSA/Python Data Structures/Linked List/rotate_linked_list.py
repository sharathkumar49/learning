# Rotate Linked List Right by k Places
from linked_list_impl import Node, LinkedList

def rotate_linked_list(head, k):
    if not head or not head.next or k == 0:
        return head
    # Compute length and make it circular
    old_tail = head
    length = 1
    while old_tail.next:
        old_tail = old_tail.next
        length += 1
    old_tail.next = head
    k = k % length
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head

# Example usage:
ll = LinkedList(); ll.insert_values([1,2,3,4,5])
ll.head = rotate_linked_list(ll.head, 2)
ll.print()  # Output: 4 --> 5 --> 1 --> 2 --> 3
