# Remove Nodes at Odd Positions
from linked_list_impl import Node, LinkedList

def remove_nodes_at_odd_positions(head):
    if not head:
        return None
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    curr = head
    pos = 1
    while curr:
        if pos % 2 == 1:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
        pos += 1
    return dummy.next

# Example usage:
ll = LinkedList(); ll.insert_values([10, 20, 30, 40, 50, 60])
ll.head = remove_nodes_at_odd_positions(ll.head)
ll.print()  # Output: 20 --> 40 --> 60
