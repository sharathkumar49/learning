# Remove Nodes with Value Equal to Their Position from End (1-based)
from linked_list_impl import Node, LinkedList

def remove_nodes_with_value_equal_to_position_from_end(head):
    # First, get length
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    curr = head
    idx = 1
    while curr:
        if curr.data == (length - idx + 1):
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
        idx += 1
    return dummy.next

# Example usage:
ll = LinkedList(); ll.insert_values([5, 4, 3, 2, 1])
ll.head = remove_nodes_with_value_equal_to_position_from_end(ll.head)
ll.print()  # Output: 4 --> 3 --> 2 --> 1
