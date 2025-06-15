# Insert a Node at the End of a Linked List
from linked_list_impl import Node, LinkedList

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
ll = LinkedList(); ll.insert_values([1, 2, 3])
ll.head = insert_at_end(ll.head, 99)
ll.print()  # Output: 1 --> 2 --> 3 --> 99
