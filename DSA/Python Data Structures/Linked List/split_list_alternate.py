# Split a Linked List into Two Lists by Alternating Nodes
from linked_list_impl import Node, LinkedList

def split_list_alternate(head):
    head1 = head2 = None
    tail1 = tail2 = None
    curr = head
    toggle = True
    while curr:
        if toggle:
            if not head1:
                head1 = tail1 = curr
            else:
                tail1.next = curr
                tail1 = curr
        else:
            if not head2:
                head2 = tail2 = curr
            else:
                tail2.next = curr
                tail2 = curr
        curr = curr.next
        toggle = not toggle
    if tail1:
        tail1.next = None
    if tail2:
        tail2.next = None
    return head1, head2

# Example usage:
ll = LinkedList(); ll.insert_values([1,2,3,4,5,6,7])
h1, h2 = split_list_alternate(ll.head)
l1 = LinkedList(); l1.head = h1
l2 = LinkedList(); l2.head = h2
print('List 1:', l1.to_list())  # Output: [1,3,5,7]
print('List 2:', l2.to_list())  # Output: [2,4,6]
