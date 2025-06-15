# Delete All Nodes with Odd Values
from linked_list_impl import Node, LinkedList

def delete_nodes_with_odd_values(head):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    curr = head
    while curr:
        if curr.data % 2 == 1:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return dummy.next

# Example usage:
ll = LinkedList(); ll.insert_values([1,2,3,4,5,6])
ll.head = delete_nodes_with_odd_values(ll.head)
ll.print()  # Output: 2 --> 4 --> 6
