# Check if a Linked List is Rotated Sorted
from linked_list_impl import Node, LinkedList

def is_rotated_sorted(head):
    if not head or not head.next:
        return True
    count = 0
    curr = head
    while curr.next:
        if curr.data > curr.next.data:
            count += 1
        curr = curr.next
    # Check last to first
    if curr.data > head.data:
        count += 1
    return count <= 1

# Example usage:
ll = LinkedList(); ll.insert_values([4,5,1,2,3])
print('Is rotated sorted:', is_rotated_sorted(ll.head))  # Output: True
