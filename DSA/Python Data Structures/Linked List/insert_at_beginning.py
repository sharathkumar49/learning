# Insert a Node at the Beginning of a Linked List
from linked_list_impl import Node, LinkedList

def insert_at_beginning(head, value):
    new_node = Node(value)
    new_node.next = head
    return new_node

# Example usage:
ll = LinkedList(); ll.insert_values([2, 3, 4])
ll.head = insert_at_beginning(ll.head, 1)
ll.print()  # Output: 1 --> 2 --> 3 --> 4
