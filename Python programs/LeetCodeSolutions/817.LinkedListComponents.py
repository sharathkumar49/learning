"""
817. Linked List Components

Given the head of a linked list and an array of integers G, return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.

Example 1:
Input: head = [0,1,2,3], G = [0,1,3]
Output: 2

Example 2:
Input: head = [0,1,2,3,4], G = [0,3,1,4]
Output: 2

Constraints:
- The number of nodes in the linked list is between 1 and 10000.
- 0 <= Node.val < 10000
- 1 <= G.length <= 10000
- G is a subset of the values in the linked list.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def numComponents(head, G):
    Gset = set(G)
    ans = 0
    in_component = False
    while head:
        if head.val in Gset:
            if not in_component:
                ans += 1
                in_component = True
        else:
            in_component = False
        head = head.next
    return ans

# Example usage:
# Helper function to build a linked list from list
# ...omitted for brevity...
