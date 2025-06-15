# Find the Intersection Node of Two Linked Lists Using Stacks
from linked_list_impl import Node, LinkedList

def intersection_using_stacks(head1, head2):
    stack1, stack2 = [], []
    while head1:
        stack1.append(head1)
        head1 = head1.next
    while head2:
        stack2.append(head2)
        head2 = head2.next
    intersection = None
    while stack1 and stack2 and stack1[-1] == stack2[-1]:
        intersection = stack1.pop()
        stack2.pop()
    return intersection

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
result = intersection_using_stacks(ll1.head, ll2.head)
print('Intersection at:', result.data if result else None)  # Output: 6
