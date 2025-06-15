# Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head.
from linked_list_impl import Node, LinkedList

def swap_pairs(head):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    while prev.next and prev.next.next:
        a = prev.next
        b = a.next
        prev.next, a.next, b.next = b, b.next, a
        prev = a
    return dummy.next

# Example usage:
ll = LinkedList()
ll.insert_values([1,2,3,4])
ll.head = swap_pairs(ll.head)
ll.print()  # Output: 2 --> 1 --> 4 --> 3
