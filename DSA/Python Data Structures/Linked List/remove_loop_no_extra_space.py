# Remove Loop Without Extra Space
# Remove a cycle from a linked list if present, without using extra space.
from linked_list_impl import Node, LinkedList

def remove_loop(head):
    slow = fast = head
    # Detect loop
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return head  # No loop
    # Find start of loop
    slow = head
    prev = None
    while slow != fast:
        prev = fast
        slow = slow.next
        fast = fast.next
    # prev is the node before loop start
    if prev:
        prev.next = None
    return head

# Example usage:
ll = LinkedList()
ll.insert_values([1,2,3,4,5])
ll.create_cycle(2)
ll.head = remove_loop(ll.head)
# Now ll.print() will terminate
ll.print()  # Output: 1 --> 2 --> 3 --> 4 --> 5
