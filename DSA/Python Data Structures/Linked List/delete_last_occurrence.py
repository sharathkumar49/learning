# Delete the Last Occurrence of a Given Value
from linked_list_impl import Node, LinkedList

def delete_last_occurrence(head, x):
    last = None
    last_prev = None
    prev = None
    curr = head
    while curr:
        if curr.data == x:
            last_prev = prev
            last = curr
        prev = curr
        curr = curr.next
    if last:
        if last_prev:
            last_prev.next = last.next
        else:
            head = head.next
    return head

# Example usage:
ll = LinkedList(); ll.insert_values([1, 2, 3, 2, 4, 2, 5])
ll.head = delete_last_occurrence(ll.head, 2)
ll.print()  # Output: 1 --> 2 --> 3 --> 2 --> 4 --> 5
