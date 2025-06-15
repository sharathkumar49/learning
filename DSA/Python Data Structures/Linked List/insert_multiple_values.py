# Insert Multiple Values into a Linked List
from linked_list_impl import Node, LinkedList

def insert_multiple_values(head, values):
    for value in values:
        head = insert_at_end(head, value)
    return head

def insert_at_end(head, value):
    new_node = Node(value)
    if not head:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    return head

# Example usage:
ll = LinkedList(); ll.head = None
ll.head = insert_multiple_values(ll.head, [1, 2, 3, 4, 5])
ll.print()  # Output: 1 --> 2 --> 3 --> 4 --> 5
