# Merge k Sorted Linked Lists
# Merge k sorted linked lists into one sorted linked list.
from linked_list_impl import Node, LinkedList
import heapq

def merge_k_lists(lists):
    min_heap = []
    for idx, node in enumerate(lists):
        if node:
            heapq.heappush(min_heap, (node.data, idx, node))
    dummy = Node(0)
    curr = dummy
    while min_heap:
        val, idx, node = heapq.heappop(min_heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(min_heap, (node.next.data, idx, node.next))
    return dummy.next

# Example usage:
ll1 = LinkedList(); ll1.insert_values([1,4,5])
ll2 = LinkedList(); ll2.insert_values([1,3,4])
ll3 = LinkedList(); ll3.insert_values([2,6])
result_head = merge_k_lists([ll1.head, ll2.head, ll3.head])
result = LinkedList(); result.head = result_head
result.print()  # Output: 1 --> 1 --> 2 --> 3 --> 4 --> 4 --> 5 --> 6
