# Find the Intersection Node of Two Linked Lists Without Extra Space
# O(1) space, O(n) time
from linked_list_impl import Node, LinkedList

def get_intersection_node(headA, headB):
    if not headA or not headB:
        return None
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a

# Example usage:
ll1 = LinkedList(); ll1.insert_values([1,2,3])
ll2 = LinkedList(); ll2.insert_values([4,5])
common = LinkedList(); common.insert_values([6,7,8])
# Attach common part
last1 = ll1.head
while last1.next:
    last1 = last1.next
last1.next = common.head
last2 = ll2.head
while last2.next:
    last2 = last2.next
last2.next = common.head
result = get_intersection_node(ll1.head, ll2.head)
print('Intersection at:', result.data if result else None)  # Output: 6
