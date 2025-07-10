"""
LeetCode 2096. Step-By-Step Directions From a Binary Tree Node to Another

Given the root of a binary tree and two nodes, return the directions to get from one node to another.

Example:
Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"

Constraints:
- The number of nodes in the tree is in the range [2, 10^5].
- 1 <= Node.val <= 10^5
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getDirections(root, startValue, destValue):
    def findPath(node, val, path):
        if not node:
            return False
        if node.val == val:
            return True
        path.append('L')
        if findPath(node.left, val, path):
            return True
        path.pop()
        path.append('R')
        if findPath(node.right, val, path):
            return True
        path.pop()
        return False
    path1, path2 = [], []
    findPath(root, startValue, path1)
    findPath(root, destValue, path2)
    i = 0
    while i < len(path1) and i < len(path2) and path1[i] == path2[i]:
        i += 1
    return 'U' * (len(path1) - i) + ''.join(path2[i:])

# Example usage:
# # Build tree and call getDirections as needed
