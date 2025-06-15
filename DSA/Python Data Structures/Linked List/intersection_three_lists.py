# Find the Intersection Node of Three Linked Lists
from linked_list_impl import Node, LinkedList

def get_length(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length

def intersection_three_lists(h1, h2, h3):
    l1, l2, l3 = get_length(h1), get_length(h2), get_length(h3)
    # Align all heads
    while l1 > l2 or l1 > l3:
        h1 = h1.next
        l1 -= 1
    while l2 > l1 or l2 > l3:
        h2 = h2.next
        l2 -= 1
    while l3 > l1 or l3 > l2:
        h3 = h3.next
        l3 -= 1
    # Find intersection
    while h1 and h2 and h3:
        if h1 == h2 == h3:
            return h1
        h1 = h1.next
        h2 = h2.next
        h3 = h3.next
    return None

# Example usage:
ll1 = LinkedList(); ll1.insert_values([1,2,3])
ll2 = LinkedList(); ll2.insert_values([4,5])
ll3 = LinkedList(); ll3.insert_values([6])
common = LinkedList(); common.insert_values([7,8,9])
# Attach common part
last1 = ll1.head
while last1.next:
    last1 = last1.next
last1.next = common.head
last2 = ll2.head
while last2.next:
    last2 = last2.next
last2.next = common.head
last3 = ll3.head
while last3.next:
    last3 = last3.next
last3.next = common.head
result = intersection_three_lists(ll1.head, ll2.head, ll3.head)
print('Intersection at:', result.data if result else None)  # Output: 7
