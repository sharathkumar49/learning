# Detect Cycle and Return the Starting Node
# Given a linked list, return the node where the cycle begins. If there is no cycle, return None.
from linked_list_impl import Node, LinkedList

def detect_cycle_start(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # Cycle detected, find entry
            ptr1 = head
            ptr2 = slow
            while ptr1 != ptr2:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            return ptr1
    return None

# Example usage:
ll = LinkedList()
ll.insert_values([1,2,3,4,5])
ll.create_cycle(2)  # Cycle at node with value 3
start = detect_cycle_start(ll.head)
print('Cycle starts at:', start.data if start else None)  # Output: 3
