# Delete All Nodes with Even Values
from linked_list_impl import Node, LinkedList

def delete_nodes_with_even_values(head):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    curr = head
    while curr:
        if curr.data % 2 == 0:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return dummy.next

# Example usage:
ll = LinkedList(); ll.insert_values([1,2,3,4,5,6])
ll.head = delete_nodes_with_even_values(ll.head)
ll.print()  # Output: 1 --> 3 --> 5
