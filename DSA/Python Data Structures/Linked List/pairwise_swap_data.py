# Pairwise Swap Elements of a Linked List (Data Only)
# Swap data of every two adjacent nodes (not the nodes themselves).
from linked_list_impl import Node, LinkedList

def pairwise_swap_data(head):
    curr = head
    while curr and curr.next:
        curr.data, curr.next.data = curr.next.data, curr.data
        curr = curr.next.next
    return head

# Example usage:
ll = LinkedList()
ll.insert_values([1,2,3,4,5])
ll.head = pairwise_swap_data(ll.head)
ll.print()  # Output: 2 --> 1 --> 4 --> 3 --> 5
