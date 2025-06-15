# Remove Nth Node From End of List
# Given a linked list, remove the n-th node from the end of list and return its head.
# LeetCode 19
from linked_list_impl import LinkedList, Node

def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    first = dummy
    second = dummy
    for _ in range(n+1):
        if first:
            first = first.next
        else:
            return head
    while first:
        first = first.next
        second = second.next
    second.next = second.next.next if second.next else None
    return dummy.next

# Example usage:
ll = LinkedList()
ll.insert_values([1,2,3,4,5])
ll.head = remove_nth_from_end(ll.head, 2)
ll.print()  # Output: 1 --> 2 --> 3 --> 5
