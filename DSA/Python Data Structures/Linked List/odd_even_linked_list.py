# Odd Even Linked List
# Group all odd-indexed nodes together followed by even-indexed nodes.
from linked_list_impl import Node, LinkedList

def odd_even_list(head):
    if not head or not head.next:
        return head
    odd = head
    even = head.next
    even_head = even
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head
    return head

# Example usage:
ll = LinkedList()
ll.insert_values([1,2,3,4,5])
ll.head = odd_even_list(ll.head)
ll.print()  # Output: 1 --> 3 --> 5 --> 2 --> 4
