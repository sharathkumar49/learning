# Find the Second Largest Element in a Linked List
from linked_list_impl import Node, LinkedList

def second_largest(head):
    if not head or not head.next:
        return None
    first = second = float('-inf')
    curr = head
    while curr:
        if curr.data > first:
            second = first
            first = curr.data
        elif curr.data > second and curr.data != first:
            second = curr.data
        curr = curr.next
    return second if second != float('-inf') else None

# Example usage:
ll = LinkedList(); ll.insert_values([1, 3, 5, 2, 4])
print('Second largest:', second_largest(ll.head))  # Output: 4
