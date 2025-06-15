# Remove Nodes with Value Less Than Previous Node
from linked_list_impl import Node, LinkedList

def remove_nodes_with_value_less_than_prev(head):
    if not head or not head.next:
        return head
    dummy = Node(0)
    dummy.next = head
    prev = head
    curr = head.next
    while curr:
        if curr.data < prev.data:
            prev.next = curr.next
            curr = prev.next
        else:
            prev = curr
            curr = curr.next
    return dummy.next

# Example usage:
ll = LinkedList(); ll.insert_values([1, 3, 2, 4, 3, 5])
ll.head = remove_nodes_with_value_less_than_prev(ll.head)
ll.print()  # Output: 1 --> 3 --> 4 --> 5
