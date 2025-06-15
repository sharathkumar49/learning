# Insert a Node After a Given Position (1-indexed)
from linked_list_impl import Node, LinkedList

def insert_after_position(head, value, pos):
    new_node = Node(value)
    curr = head
    count = 1
    while curr and count < pos:
        curr = curr.next
        count += 1
    if curr:
        new_node.next = curr.next
        curr.next = new_node
    return head

# Example usage:
ll = LinkedList(); ll.insert_values([10, 20, 30, 40])
ll.head = insert_after_position(ll.head, 25, 2)
ll.print()  # Output: 10 --> 20 --> 25 --> 30 --> 40
