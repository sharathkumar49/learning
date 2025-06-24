"""
1171. Remove Zero Sum Consecutive Nodes from Linked List

Given the head of a linked list, remove all consecutive sequences of nodes that sum to 0.

Constraints:
- The number of nodes in the list is between 1 and 1000.
- -1000 <= Node.val <= 1000

Example:
Input: head = [1,2,-3,3,1]
Output: [3,1]

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeZeroSumSublists(head):
    dummy = ListNode(0)
    dummy.next = head
    prefix = 0
    seen = {0: dummy}
    node = head
    while node:
        prefix += node.val
        seen[prefix] = node
        node = node.next
    prefix = 0
    node = dummy
    while node:
        prefix += node.val
        node.next = seen[prefix].next
        node = node.next
    return dummy.next

# Example usage
if __name__ == "__main__":
    def to_list(head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res
    # [1,2,-3,3,1] -> [3,1]
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(-3)
    n4 = ListNode(3)
    n5 = ListNode(1)
    n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n5
    result = removeZeroSumSublists(n1)
    print(to_list(result))  # Output: [3, 1]
