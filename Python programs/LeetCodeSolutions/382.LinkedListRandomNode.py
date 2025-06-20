"""
382. Linked List Random Node

Given a singly linked list, return a random node's value. Each node must have the same probability of being chosen.

Constraints:
- The number of nodes in the linked list is in the range [1, 10^4].
- -10^4 <= Node.val <= 10^4
- At most 10^4 calls will be made to getRandom.
"""
import random
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.nodes = []
        while head:
            self.nodes.append(head.val)
            head = head.next
    def getRandom(self) -> int:
        return random.choice(self.nodes)

# Example usage:
# head = ListNode(1, ListNode(2, ListNode(3)))
# obj = Solution(head)
# print(obj.getRandom())
