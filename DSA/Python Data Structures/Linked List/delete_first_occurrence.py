# Delete the First Occurrence of a Given Value
from linked_list_impl import Node, LinkedList

def delete_first_occurrence(head, x):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    curr = head
    while curr:
        if curr.data == x:
            prev.next = curr.next
            break
        prev = curr
        curr = curr.next
    return dummy.next

# Example usage:
ll = LinkedList(); ll.insert_values([1, 2, 3, 2, 4, 2, 5])
ll.head = delete_first_occurrence(ll.head, 2)
ll.print()  # Output: 1 --> 3 --> 2 --> 4 --> 2 --> 5
