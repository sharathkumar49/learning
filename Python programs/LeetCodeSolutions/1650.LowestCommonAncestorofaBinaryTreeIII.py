"""
LeetCode 1650. Lowest Common Ancestor of a Binary Tree III

Given two nodes of a binary tree, return their lowest common ancestor. Each node has a parent pointer.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3

Constraints:
- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
"""

def lowestCommonAncestor(p, q):
    seen = set()
    while p:
        seen.add(p)
        p = p.parent
    while q:
        if q in seen:
            return q
        q = q.parent
    return None

# Example usage:
# (Assume Node class with parent pointer is defined)
# p = ...
# q = ...
# print(lowestCommonAncestor(p, q))
