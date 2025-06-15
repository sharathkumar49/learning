# Segregate Even and Odd Nodes
# Rearrange the linked list so that all even nodes appear after all odd nodes, preserving their original order.
from linked_list_impl import Node, LinkedList

def segregate_even_odd(head):
    if not head:
        return None
    odd_head = odd_tail = None
    even_head = even_tail = None
    curr = head
    while curr:
        if curr.data % 2 == 0:
            if not even_head:
                even_head = even_tail = curr
            else:
                even_tail.next = curr
                even_tail = curr
        else:
            if not odd_head:
                odd_head = odd_tail = curr
            else:
                odd_tail.next = curr
                odd_tail = curr
        curr = curr.next
    if odd_tail:
        odd_tail.next = even_head
    if even_tail:
        even_tail.next = None
    return odd_head if odd_head else even_head

# Example usage:
ll = LinkedList()
ll.insert_values([17,15,8,12,10,5,4])
ll.head = segregate_even_odd(ll.head)
ll.print()  # Output: 17 --> 15 --> 5 --> 8 --> 12 --> 10 --> 4
