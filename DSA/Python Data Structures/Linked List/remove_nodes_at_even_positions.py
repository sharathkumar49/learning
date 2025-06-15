# Remove Nodes at Even Positions
from linked_list_impl import Node, LinkedList

def remove_nodes_at_even_positions(head):
    if not head:
        return None
    curr = head
    prev = None
    pos = 1
    while curr:
        if pos % 2 == 0:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
        pos += 1
    return head

# Example usage:
ll = LinkedList(); ll.insert_values([10, 20, 30, 40, 50, 60])
ll.head = remove_nodes_at_even_positions(ll.head)
ll.print()  # Output: 10 --> 30 --> 50
