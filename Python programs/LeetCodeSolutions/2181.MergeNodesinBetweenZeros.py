"""
LeetCode 2181. Merge Nodes in Between Zeros

Given the head of a linked list, which contains sequences of non-zero values separated by zeroes, merge the nodes between every two zeros into a single node and return the new list (excluding zeros).

Example:
Input: head = [0,3,1,0,4,5,2,0]
Output: [4,11]

Constraints:
- The list contains at least three nodes.
- 0 <= Node.val <= 1000
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeNodes(head):
    dummy = ListNode(0)
    cur = dummy
    s = 0
    node = head.next
    while node:
        if node.val == 0:
            cur.next = ListNode(s)
            cur = cur.next
            s = 0
        else:
            s += node.val
        node = node.next
    return dummy.next

# Example usage:
# (You would need to build a linked list from [0,3,1,0,4,5,2,0] and print the result)
