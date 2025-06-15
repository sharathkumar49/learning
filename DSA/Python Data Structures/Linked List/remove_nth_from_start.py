# Remove the Nth Node from the Start of a Linked List
from linked_list_impl import Node, LinkedList

def remove_nth_from_start(head, n):
    if n <= 0:
        return head
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    curr = head
    count = 1
    while curr and count < n:
        prev = curr
        curr = curr.next
        count += 1
    if curr:
        prev.next = curr.next
    return dummy.next

# Example usage:
ll = LinkedList(); ll.insert_values([10,20,30,40,50])
ll.head = remove_nth_from_start(ll.head, 3)
ll.print()  # Output: 10 --> 20 --> 40 --> 50
