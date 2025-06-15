# Find the First Non-Repeating Node
# Find the first node in a linked list whose value does not repeat anywhere else in the list.
from linked_list_impl import Node, LinkedList
from collections import Counter

def first_non_repeating_node(head):
    values = []
    curr = head
    while curr:
        values.append(curr.data)
        curr = curr.next
    count = Counter(values)
    curr = head
    while curr:
        if count[curr.data] == 1:
            return curr
        curr = curr.next
    return None

# Example usage:
ll = LinkedList()
ll.insert_values([4,5,1,2,0,4])
node = first_non_repeating_node(ll.head)
print('First non-repeating node:', node.data if node else None)  # Output: 5
