# Remove All Occurrences of a Given Value
# Remove all nodes with a specific value from the linked list.
from linked_list_impl import Node, LinkedList

def remove_all_occurrences(head, val):
    dummy = Node(0)
    dummy.next = head
    prev, curr = dummy, head
    while curr:
        if curr.data == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return dummy.next

# Example usage:
ll = LinkedList()
ll.insert_values([1,2,6,3,4,5,6])
ll.head = remove_all_occurrences(ll.head, 6)
ll.print()  # Output: 1 --> 2 --> 3 --> 4 --> 5
