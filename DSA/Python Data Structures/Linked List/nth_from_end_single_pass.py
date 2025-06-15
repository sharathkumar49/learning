# Find the Nth Node from the End (Single Pass)
# Return the nth node from the end in a single traversal.
from linked_list_impl import Node, LinkedList

def nth_from_end(head, n):
    first = second = head
    for _ in range(n):
        if not first:
            return None
        first = first.next
    while first:
        first = first.next
        second = second.next
    return second

# Example usage:
ll = LinkedList()
ll.insert_values([10,20,30,40,50])
node = nth_from_end(ll.head, 2)
print('2nd from end:', node.data if node else None)  # Output: 40
