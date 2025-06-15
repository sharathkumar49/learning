# Remove Nodes with Value Equal to Their Index (0-based)
from linked_list_impl import Node, LinkedList

def remove_nodes_with_value_equal_to_index(head):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    curr = head
    idx = 0
    while curr:
        if curr.data == idx:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
        idx += 1
    return dummy.next

# Example usage:
ll = LinkedList(); ll.insert_values([0, 2, 2, 3, 4, 5])
ll.head = remove_nodes_with_value_equal_to_index(ll.head)
ll.print()  # Output: 2 --> 2 --> 4 --> 5
