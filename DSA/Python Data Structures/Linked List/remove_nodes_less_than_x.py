# Remove All Nodes Less Than a Given Value x
from linked_list_impl import Node, LinkedList

def remove_nodes_less_than_x(head, x):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    curr = head
    while curr:
        if curr.data < x:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return dummy.next

# Example usage:
ll = LinkedList(); ll.insert_values([2, 7, 4, 9, 1, 5])
ll.head = remove_nodes_less_than_x(ll.head, 5)
ll.print()  # Output: 7 --> 9 --> 5
