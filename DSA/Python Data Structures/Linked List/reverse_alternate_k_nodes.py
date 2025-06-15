# Reverse Alternate k Nodes in a Linked List
# Reverse every alternate k nodes in a linked list.
from linked_list_impl import Node, LinkedList

def reverse_alternate_k_nodes(head, k):
    curr = head
    prev = None
    count = 0
    # Reverse first k nodes
    while curr and count < k:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        count += 1
    if head:
        head.next = curr
    # Skip next k nodes
    count = 0
    temp = curr
    while temp and count < k - 1:
        temp = temp.next
        count += 1
    if temp:
        temp.next = reverse_alternate_k_nodes(temp.next, k)
    return prev

# Example usage:
ll = LinkedList()
ll.insert_values([1,2,3,4,5,6,7,8,9])
ll.head = reverse_alternate_k_nodes(ll.head, 3)
ll.print()  # Output: 3 --> 2 --> 1 --> 4 --> 5 --> 6 --> 9 --> 8 --> 7
