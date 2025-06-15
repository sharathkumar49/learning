# Insert a Node After a Given Value
from linked_list_impl import Node, LinkedList

def insert_after_value(head, value, new_value):
    curr = head
    while curr:
        if curr.data == value:
            new_node = Node(new_value)
            new_node.next = curr.next
            curr.next = new_node
            break
        curr = curr.next
    return head

# Example usage:
ll = LinkedList(); ll.insert_values([1, 2, 3, 4])
ll.head = insert_after_value(ll.head, 2, 99)
ll.print()  # Output: 1 --> 2 --> 99 --> 3 --> 4
