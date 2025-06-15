# Insert a Node Before a Given Value
from linked_list_impl import Node, LinkedList

def insert_before_value(head, value, new_value):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    curr = head
    while curr:
        if curr.data == value:
            new_node = Node(new_value)
            prev.next = new_node
            new_node.next = curr
            break
        prev = curr
        curr = curr.next
    return dummy.next

# Example usage:
ll = LinkedList(); ll.insert_values([1, 2, 3, 4])
ll.head = insert_before_value(ll.head, 3, 88)
ll.print()  # Output: 1 --> 2 --> 88 --> 3 --> 4
