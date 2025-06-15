# Partition List
# Given a linked list and a value x, partition it so that all nodes less than x come before nodes greater than or equal to x.
from linked_list_impl import Node, LinkedList

def partition(head, x):
    before_head = Node(0)
    before = before_head
    after_head = Node(0)
    after = after_head
    while head:
        if head.data < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next
        head = head.next
    after.next = None
    before.next = after_head.next
    return before_head.next

# Example usage:
ll = LinkedList()
ll.insert_values([1,4,3,2,5,2])
ll.head = partition(ll.head, 3)
ll.print()  # Output: 1 --> 2 --> 2 --> 4 --> 3 --> 5
