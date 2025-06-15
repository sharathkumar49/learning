# Move All Even Nodes to the End of the List in Original Order
from linked_list_impl import Node, LinkedList

def move_even_nodes_to_end(head):
    if not head or not head.next:
        return head
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
ll = LinkedList(); ll.insert_values([1,2,3,4,5,6,7,8])
ll.head = move_even_nodes_to_end(ll.head)
ll.print()  # Output: 1 --> 3 --> 5 --> 7 --> 2 --> 4 --> 6 --> 8
