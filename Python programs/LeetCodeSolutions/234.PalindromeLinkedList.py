# 234. Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome.
#
# Example 1:
# Input: head = [1,2,2,1]
# Output: true
#
# Example 2:
# Input: head = [1,2]
# Output: false
#
# Constraints:
# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 9

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals == vals[::-1]

# Example usage
head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
print("Is palindrome:", isPalindrome(head))  # Output: True
