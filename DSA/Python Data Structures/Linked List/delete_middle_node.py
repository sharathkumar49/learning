# Delete the Middle Node of a Linked List
from linked_list_impl import Node, LinkedList

def delete_middle_node(head):
    if not head or not head.next:
        return None
    slow = fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = slow.next
    return head

# Example usage:
ll = LinkedList(); ll.insert_values([1,2,3,4,5])
ll.head = delete_middle_node(ll.head)
ll.print()  # Output: 1 --> 2 --> 4 --> 5
