# Find the Node Before the Start of Cycle
# Return the node just before the start of the cycle (if any).
from linked_list_impl import Node, LinkedList

def node_before_cycle_start(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # Find start
            ptr1 = head
            ptr2 = slow
            prev = None
            while ptr1 != ptr2:
                prev = ptr2
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            # prev is the node before cycle start
            return prev
    return None

# Example usage:
ll = LinkedList()
ll.insert_values([1,2,3,4,5])
ll.create_cycle(2)
node = node_before_cycle_start(ll.head)
print('Node before cycle start:', node.data if node else None)  # Output: 5
