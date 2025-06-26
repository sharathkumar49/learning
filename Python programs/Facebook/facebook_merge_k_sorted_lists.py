# Facebook: Merge k Sorted Lists
# Merge k sorted linked lists and return it as one sorted list.
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists):
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    dummy = ListNode()
    curr = dummy
    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next

if __name__ == "__main__":
    # Example usage
    a = ListNode(1, ListNode(4, ListNode(5)))
    b = ListNode(1, ListNode(3, ListNode(4)))
    c = ListNode(2, ListNode(6))
    res = merge_k_lists([a, b, c])
    out = []
    while res:
        out.append(res.val)
        res = res.next
    print(out)  # Output: [1,1,2,3,4,4,5,6]
