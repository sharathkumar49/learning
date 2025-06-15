# Find the Intersection Point of Two Cyclic Linked Lists
# Given two singly linked lists that may have cycles, find their intersection node (if any).
from linked_list_impl import Node, LinkedList

def get_cycle_start(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None

def get_intersection_node(headA, headB):
    # Get cycle starts
    startA = get_cycle_start(headA)
    startB = get_cycle_start(headB)
    if not startA and not startB:
        # No cycles, use standard method
        nodes = set()
        curr = headA
        while curr:
            nodes.add(curr)
            curr = curr.next
        curr = headB
        while curr:
            if curr in nodes:
                return curr
            curr = curr.next
        return None
    if (startA and not startB) or (not startA and startB):
        return None  # One has cycle, other doesn't
    # Both have cycles
    ptr = startA
    while True:
        if ptr == startB:
            return startB
        ptr = ptr.next
        if ptr == startA:
            break
    return None
# Example usage omitted for brevity
