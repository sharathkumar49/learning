# Check if Two Linked Lists Form a Cycle Together
# Given two singly linked lists, check if they merge and form a cycle together.
from linked_list_impl import Node, LinkedList

def two_lists_form_cycle(head1, head2):
    # Find tail of first list
    tail1 = head1
    while tail1 and tail1.next:
        tail1 = tail1.next
    # Connect tail1 to head2 temporarily
    if tail1:
        tail1.next = head2
    # Check for cycle
    slow = fast = head1
    has_cycle = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break
    # Restore original structure
    if tail1:
        tail1.next = None
    return has_cycle

# Example usage:
ll1 = LinkedList()
ll2 = LinkedList()
ll1.insert_values([1,2,3])
ll2.insert_values([4,5,6])
# Create a cycle by connecting ll2's tail to ll1's head
last2 = ll2.head
while last2.next:
    last2 = last2.next
last2.next = ll1.head
print('Two lists form cycle:', two_lists_form_cycle(ll1.head, ll2.head))  # Output: True
