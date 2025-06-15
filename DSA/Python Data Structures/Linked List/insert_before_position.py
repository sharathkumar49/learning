# Insert a Node Before a Given Position (1-indexed)
from linked_list_impl import Node, LinkedList

def insert_before_position(head, value, pos):
    new_node = Node(value)
    if pos <= 1 or not head:
        new_node.next = head
        return new_node
    curr = head
    count = 1
    while curr.next and count < pos - 1:
        curr = curr.next
        count += 1
    new_node.next = curr.next
    curr.next = new_node
    return head

# Example usage:
ll = LinkedList(); ll.insert_values([10, 20, 30, 40])
ll.head = insert_before_position(ll.head, 15, 2)
ll.print()  # Output: 10 --> 15 --> 20 --> 30 --> 40
