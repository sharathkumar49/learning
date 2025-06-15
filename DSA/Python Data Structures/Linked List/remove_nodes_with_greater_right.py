# Remove Nodes with Greater Value on Right
from linked_list_impl import Node, LinkedList

def reverse(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def remove_nodes_with_greater_right(head):
    head = reverse(head)
    max_val = head.data
    curr = head
    while curr and curr.next:
        if curr.next.data < max_val:
            curr.next = curr.next.next
        else:
            curr = curr.next
            max_val = curr.data
    return reverse(head)

# Example usage:
ll = LinkedList(); ll.insert_values([12,15,10,11,5,6,2,3])
ll.head = remove_nodes_with_greater_right(ll.head)
ll.print()  # Output: 15 --> 11 --> 6 --> 3
