# Find the Node with Minimum Value in a Rotated Sorted Linked List
from linked_list_impl import Node, LinkedList

def min_in_rotated_sorted_list(head):
    if not head:
        return None
    min_node = head
    curr = head.next
    while curr and curr != head:
        if curr.data < min_node.data:
            min_node = curr
        curr = curr.next
    return min_node

# Example usage:
ll = LinkedList(); ll.insert_values([4,5,1,2,3])
# Make it circular
last = ll.head
while last.next:
    last = last.next
last.next = ll.head
min_node = min_in_rotated_sorted_list(ll.head)
print('Min node in rotated sorted list:', min_node.data if min_node else None)  # Output: 1
