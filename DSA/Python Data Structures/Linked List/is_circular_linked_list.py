# Check if a Linked List is Circular
# Check if a linked list is circular (last node points to head).
from linked_list_impl import Node, LinkedList

def is_circular(head):
    if not head:
        return False
    curr = head.next
    while curr and curr != head:
        curr = curr.next
    return curr == head

# Example usage:
ll = LinkedList()
ll.insert_values([1,2,3,4,5])
# Make it circular
last = ll.head
while last.next:
    last = last.next
last.next = ll.head
print('Is circular:', is_circular(ll.head))  # Output: True
