# Find Intersection Node in Y-Shaped Linked Lists
# Given two singly linked lists that merge at some point (Y-shaped), find the intersection node.
from linked_list_impl import Node, LinkedList

def get_length(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length

def find_intersection(head1, head2):
    len1, len2 = get_length(head1), get_length(head2)
    # Align heads
    while len1 > len2:
        head1 = head1.next
        len1 -= 1
    while len2 > len1:
        head2 = head2.next
        len2 -= 1
    # Find intersection
    while head1 and head2:
        if head1 == head2:
            return head1
        head1 = head1.next
        head2 = head2.next
    return None

# Example usage:
ll1 = LinkedList()
ll2 = LinkedList()
ll1.insert_values([1,2,3])
ll2.insert_values([4,5])
common = LinkedList()
common.insert_values([6,7,8])
# Attach common part
last1 = ll1.head
while last1.next:
    last1 = last1.next
last1.next = common.head
last2 = ll2.head
while last2.next:
    last2 = last2.next
last2.next = common.head

result = find_intersection(ll1.head, ll2.head)
print('Intersection at:', result.data if result else None)  # Output: 6
