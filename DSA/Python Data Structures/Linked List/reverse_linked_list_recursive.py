# Reverse a Linked List Recursively
from linked_list_impl import Node, LinkedList

def reverse_recursive(head):
    if not head or not head.next:
        return head
    rest = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return rest

# Example usage:
ll = LinkedList(); ll.insert_values([1,2,3,4,5])
ll.head = reverse_recursive(ll.head)
ll.print()  # Output: 5 --> 4 --> 3 --> 2 --> 1
