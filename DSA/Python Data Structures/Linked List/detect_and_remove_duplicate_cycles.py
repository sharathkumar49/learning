# Detect and Remove Duplicate Cycles
# If a linked list contains multiple cycles, detect and remove all cycles.
from linked_list_impl import Node, LinkedList

def remove_all_cycles(head):
    visited = set()
    prev = None
    curr = head
    while curr:
        if id(curr) in visited:
            if prev:
                prev.next = None
            break
        visited.add(id(curr))
        prev = curr
        curr = curr.next
    return head

# Example usage:
ll = LinkedList()
ll.insert_values([1,2,3,4,5])
ll.create_cycle(1)
# Manually create another cycle for demonstration (not typical)
# Remove all cycles
ll.head = remove_all_cycles(ll.head)
ll.print()  # Output: 1 --> 2 --> 3 --> 4 --> 5
