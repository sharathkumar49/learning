"""
445. Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

Constraints:
- The number of nodes in each linked list is in the range [1, 100]
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.

Example:
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        carry = 0
        head = None
        while stack1 or stack2 or carry:
            s = (stack1.pop() if stack1 else 0) + (stack2.pop() if stack2 else 0) + carry
            carry, val = divmod(s, 10)
            node = ListNode(val)
            node.next = head
            head = node
        return head

# Example usage:
def list_to_linked(lst):
    head = ListNode(lst[0])
    curr = head
    for x in lst[1:]:
        curr.next = ListNode(x)
        curr = curr.next
    return head

def linked_to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

l1 = list_to_linked([7,2,4,3])
l2 = list_to_linked([5,6,4])
sol = Solution()
result = sol.addTwoNumbers(l1, l2)
print(linked_to_list(result))  # Output: [7, 8, 0, 7]
