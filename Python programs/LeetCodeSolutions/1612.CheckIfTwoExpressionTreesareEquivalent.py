"""
LeetCode 1612. Check If Two Expression Trees are Equivalent

Given the roots of two binary expression trees, return true if the two trees are equivalent.

Example 1:
Input: root1 = [+,a,+,null,null,b,c], root2 = [+,+,b,c,a]
Output: true

Constraints:
- The number of nodes in each tree is in the range [1, 100].
- Each node is either '+', a lowercase letter, or null.
"""

def checkEquivalence(root1, root2):
    def count(node):
        if not node:
            return [0]*26
        if node.val == '+':
            l = count(node.left)
            r = count(node.right)
            return [l[i]+r[i] for i in range(26)]
        else:
            arr = [0]*26
            arr[ord(node.val)-ord('a')] = 1
            return arr
    return count(root1) == count(root2)

# Example usage:
# (Assume Node class is defined)
# root1 = ...
# root2 = ...
# print(checkEquivalence(root1, root2))
