# Add One to a Number Represented by Linked List
# Each node contains a single digit. Add one to the number represented by the linked list.
from linked_list_impl import Node, LinkedList

def reverse(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def add_one(head):
    head = reverse(head)
    curr = head
    carry = 1
    prev = None
    while curr and carry:
        curr.data += carry
        carry = curr.data // 10
        curr.data = curr.data % 10
        prev = curr
        curr = curr.next
    if carry:
        prev.next = Node(carry)
    return reverse(head)

# Example usage:
ll = LinkedList()
ll.insert_values([9,9,9])
ll.head = add_one(ll.head)
ll.print()  # Output: 1 --> 0 --> 0 --> 0
