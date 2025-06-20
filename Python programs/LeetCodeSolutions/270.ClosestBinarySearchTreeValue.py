"""
270. Closest Binary Search Tree Value
https://leetcode.com/problems/closest-binary-search-tree-value/

Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- 0 <= Node.val <= 10^9
- -10^9 <= target <= 10^9

Example 1:
Input: root = [4,2,5,1,3], target = 3.714286
Output: 4

Example 2:
Input: root = [1], target = 4.428571
Output: 1
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def closestValue(root, target):
    closest = root.val
    while root:
        if abs(root.val - target) < abs(closest - target):
            closest = root.val
        root = root.left if target < root.val else root.right
    return closest

# Example usage:
if __name__ == "__main__":
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
    print(closestValue(root, 3.714286))  # Output: 4
    root2 = TreeNode(1)
    print(closestValue(root2, 4.428571)) # Output: 1
