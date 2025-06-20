"""
331. Verify Preorder Serialization of a Binary Tree

One way to serialize a binary tree is to use preorder traversal. Given a string of comma-separated values representing this traversal, return true if it is a correct preorder serialization of a binary tree.

Constraints:
- 1 <= preorder.length <= 10^4
- Each comma-separated value is either an integer or '#'.
- It is guaranteed that each comma is followed by a value.
"""
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')
        slots = 1
        for node in nodes:
            slots -= 1
            if slots < 0:
                return False
            if node != '#':
                slots += 2
        return slots == 0

# Example usage:
preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
print(Solution().isValidSerialization(preorder))  # Output: True
