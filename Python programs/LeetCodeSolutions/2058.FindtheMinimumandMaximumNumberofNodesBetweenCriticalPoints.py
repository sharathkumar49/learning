"""
LeetCode 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points

Given the head of a linked list, return the minimum and maximum number of nodes between critical points.

Example:
Input: head = [5,3,1,2,5,1,2]
Output: [1,3]

Constraints:
- The number of nodes in the list is in the range [2, 10^5].
- -10^5 <= Node.val <= 10^5
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nodesBetweenCriticalPoints(head):
    idxs = []
    prev, curr, idx = head, head.next, 1
    while curr and curr.next:
        if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
            idxs.append(idx)
        prev, curr = curr, curr.next
        idx += 1
    if len(idxs) < 2:
        return [-1, -1]
    return [min(b-a for a, b in zip(idxs, idxs[1:])), idxs[-1] - idxs[0]]

# Example usage:
# # Build linked list: 5 -> 3 -> 1 -> 2 -> 5 -> 1 -> 2
# head = ListNode(5, ListNode(3, ListNode(1, ListNode(2, ListNode(5, ListNode(1, ListNode(2)))))))
# print(nodesBetweenCriticalPoints(head))  # Output: [1,3]
