# Reverse Nodes in Pairs
from linked_list_impl import Node, LinkedList

def reverse_nodes_in_pairs(head):
    if not head or not head.next:
        return head
    prev = None
    curr = head
    new_head = head.next
    while curr and curr.next:
        nxt = curr.next
        temp = nxt.next
        nxt.next = curr
        if prev:
            prev.next = nxt
        curr.next = temp
        prev = curr
        curr = temp
    return new_head

# Example usage:
ll = LinkedList(); ll.insert_values([1,2,3,4,5])
ll.head = reverse_nodes_in_pairs(ll.head)
ll.print()  # Output: 2 --> 1 --> 4 --> 3 --> 5
