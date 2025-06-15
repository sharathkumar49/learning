# Find the Intersection Point of Two Linked Lists Using Cycle Trick
from linked_list_impl import Node, LinkedList

def get_intersection_cycle_trick(headA, headB):
    # Make list A circular
    if not headA or not headB:
        return None
    tailA = headA
    while tailA.next:
        tailA = tailA.next
    tailA.next = headA
    # Detect cycle in B
    slow = fast = headB
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        tailA.next = None
        return None
    # Find entry
    slow = headB
    while slow != fast:
        slow = slow.next
        fast = fast.next
    tailA.next = None
    return slow

# Example usage:
ll1 = LinkedList(); ll1.insert_values([1,2,3])
ll2 = LinkedList(); ll2.insert_values([4,5])
common = LinkedList(); common.insert_values([6,7,8])
last1 = ll1.head
while last1.next:
    last1 = last1.next
last1.next = common.head
last2 = ll2.head
while last2.next:
    last2 = last2.next
last2.next = common.head
result = get_intersection_cycle_trick(ll1.head, ll2.head)
print('Intersection at:', result.data if result else None)  # Output: 6
