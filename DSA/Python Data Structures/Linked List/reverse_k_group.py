# Reverse Nodes in k-Group
# Given a linked list, reverse the nodes of a list k at a time and return its modified list.
from linked_list_impl import Node, LinkedList

def reverse_k_group(head, k):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    while True:
        node = prev
        for _ in range(k):
            node = node.next
            if not node:
                return dummy.next
        curr = prev.next
        next_prev = curr
        prev_sub = None
        for _ in range(k):
            nxt = curr.next
            curr.next = prev_sub
            prev_sub = curr
            curr = nxt
        prev.next = prev_sub
        next_prev.next = curr
        prev = next_prev

# Example usage:
ll = LinkedList()
ll.insert_values([1,2,3,4,5])
ll.head = reverse_k_group(ll.head, 3)
ll.print()  # Output: 3 --> 2 --> 1 --> 4 --> 5
