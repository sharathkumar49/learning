"""
237. Delete Node in a Linked List
https://leetcode.com/problems/delete-node-in-a-linked-list/

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Constraints:
- The linked list will have at least two elements.
- The value of each node in the linked list is unique.
- The node to be deleted is not a tail node in the list.

Example 1:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]

Example 2:
Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next

# Example usage:
if __name__ == "__main__":
    def to_list(head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res
    n = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
    node = n.next  # Node with value 5
    deleteNode(node)
    print(to_list(n))  # Output: [4,1,9]
    n2 = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
    node2 = n2.next.next  # Node with value 1
    deleteNode(node2)
    print(to_list(n2))  # Output: [4,5,9]
