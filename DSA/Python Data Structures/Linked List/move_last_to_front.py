# Move Last Element to Front of Linked List
from linked_list_impl import Node, LinkedList

def move_last_to_front(head):
    if not head or not head.next:
        return head
    second_last = None
    last = head
    while last.next:
        second_last = last
        last = last.next
    second_last.next = None
    last.next = head
    return last

# Example usage:
ll = LinkedList(); ll.insert_values([1,2,3,4,5])
ll.head = move_last_to_front(ll.head)
ll.print()  # Output: 5 --> 1 --> 2 --> 3 --> 4
