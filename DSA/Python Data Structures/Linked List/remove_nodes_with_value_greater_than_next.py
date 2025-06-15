# Remove Nodes with Value Greater Than Next Node
from linked_list_impl import Node, LinkedList

def remove_nodes_with_value_greater_than_next(head):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    curr = head
    while curr and curr.next:
        if curr.data > curr.next.data:
            prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next
    return dummy.next

# Example usage:
ll = LinkedList(); ll.insert_values([12, 15, 10, 11, 5, 6, 2, 3])
ll.head = remove_nodes_with_value_greater_than_next(ll.head)
ll.print()  # Output: 12 --> 10 --> 5 --> 2 --> 3
