# Delete Without Head Pointer
# Given only a pointer to a node to be deleted (not the head), delete the node from the linked list.
from linked_list_impl import Node, LinkedList

def delete_node(node):
    if node is None or node.next is None:
        return False  # Can't delete last node or None
    node.data = node.next.data
    node.next = node.next.next
    return True

# Example usage:
ll = LinkedList()
ll.insert_values([1,2,3,4,5])
# Delete node with value 3 (not head)
target = ll.head.next.next  # Node with value 3
delete_node(target)
ll.print()  # Output: 1 --> 2 --> 4 --> 5
