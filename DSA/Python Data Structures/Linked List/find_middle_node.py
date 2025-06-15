# Find the Middle Node of a Linked List (Two-Pointer)
# Return the middle node. If two, return the second one.
from linked_list_impl import Node, LinkedList

def find_middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Example usage:
ll = LinkedList()
ll.insert_values([1,2,3,4,5])
mid = find_middle_node(ll.head)
print('Middle node:', mid.data if mid else None)  # Output: 3
