# Detect Cycle Using Hashing (Set)
# Detect a cycle using a hash set to store visited nodes.
from linked_list_impl import Node, LinkedList

def has_cycle_hashing(head):
    visited = set()
    curr = head
    while curr:
        if id(curr) in visited:
            return True
        visited.add(id(curr))
        curr = curr.next
    return False

# Example usage:
ll = LinkedList()
ll.insert_values([1,2,3,4,5])
ll.create_cycle(0)
print('Cycle detected (hashing):', has_cycle_hashing(ll.head))  # Output: True
