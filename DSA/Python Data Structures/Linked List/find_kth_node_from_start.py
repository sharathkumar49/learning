# Find the k-th Node from the Start
from linked_list_impl import Node, LinkedList

def find_kth_node_from_start(head, k):
    curr = head
    count = 1
    while curr and count < k:
        curr = curr.next
        count += 1
    return curr

# Example usage:
ll = LinkedList(); ll.insert_values([10,20,30,40,50])
kth = find_kth_node_from_start(ll.head, 3)
print('3rd node from start:', kth.data if kth else None)  # Output: 30
