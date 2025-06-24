"""
LeetCode 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree

Given two binary trees original and cloned and given a reference to a node target in the original tree.

Return a reference to the same node in the cloned tree.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- The values of the nodes of the tree are unique.
- target node is a node from the original tree and is not null.

Example:
Input: original = [7,4,3,null,null,6,19], cloned = [7,4,3,null,null,6,19], target = Node with value 3
Output: Node with value 3
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getTargetCopy(original, cloned, target):
    if not original:
        return None
    if original is target:
        return cloned
    left = getTargetCopy(original.left, cloned.left, target)
    if left:
        return left
    return getTargetCopy(original.right, cloned.right, target)

# Example usage:
# Build trees and call getTargetCopy as needed.
