"""
272. Closest Binary Search Tree Value II
https://leetcode.com/problems/closest-binary-search-tree-value-ii/

Given the root of a binary search tree, a target value, and an integer k, return the k values in the BST that are closest to the target. You may return the answer in any order.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- 0 <= Node.val <= 10^9
- -10^9 <= target <= 10^9
- 1 <= k <= n <= 10^4

Example 1:
Input: root = [4,2,5,1,3], target = 3.714286, k = 2
Output: [4,3]

Example 2:
Input: root = [1], target = 0.000000, k = 1
Output: [1]
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def closestKValues(root, target, k):
    vals = []
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        vals.append(node.val)
        inorder(node.right)
    inorder(root)
    vals.sort(key=lambda x: abs(x - target))
    return vals[:k]

# Example usage:
if __name__ == "__main__":
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
    print(closestKValues(root, 3.714286, 2))  # Output: [4,3]
    root2 = TreeNode(1)
    print(closestKValues(root2, 0.0, 1))     # Output: [1]
