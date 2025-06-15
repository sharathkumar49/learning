# Remove Nodes with Value Equal to Sum of Previous and Next Node
from linked_list_impl import Node, LinkedList

def remove_nodes_with_value_equal_to_sum_of_prev_next(head):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    curr = head
    while curr and curr.next:
        if prev != dummy and curr.data == prev.data + curr.next.data:
            prev.next = curr.next
            curr = prev.next
        else:
            prev = curr
            curr = curr.next
    return dummy.next

# Example usage:
ll = LinkedList(); ll.insert_values([1, 3, 4, 7, 11, 18])
ll.head = remove_nodes_with_value_equal_to_sum_of_prev_next(ll.head)
ll.print()  # Output: 1 --> 3 --> 4 --> 7 --> 11
