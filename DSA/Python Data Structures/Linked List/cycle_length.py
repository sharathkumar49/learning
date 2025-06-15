# Find Length of Cycle in a Linked List
# If a cycle exists, return its length. Otherwise, return 0.
from linked_list_impl import Node, LinkedList

def cycle_length(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # Cycle detected, count length
            count = 1
            curr = slow.next
            while curr != slow:
                curr = curr.next
                count += 1
            return count
    return 0

# Example usage:
ll = LinkedList()
ll.insert_values([1,2,3,4,5])
ll.create_cycle(1)  # Cycle at node with value 2
print('Cycle length:', cycle_length(ll.head))  # Output: 4
