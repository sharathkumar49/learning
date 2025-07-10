"""
LeetCode 1530. Number of Good Leaf Nodes Pairs

Given the root of a binary tree and an integer distance, return the number of good leaf node pairs in the tree. A pair is good if the length of the shortest path between them is less than or equal to distance.

Constraints:
- The number of nodes in the tree is in the range [1, 2 * 10^4].
- 1 <= Node.val <= 100
- 1 <= distance <= 10

Example:
Input: root = [1,2,3,null,4], distance = 3
Output: 1
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countPairs(root, distance):
    res = 0
    def dfs(node):
        nonlocal res
        if not node:
            return []
        if not node.left and not node.right:
            return [1]
        L = dfs(node.left)
        R = dfs(node.right)
        for l in L:
            for r in R:
                if l + r <= distance:
                    res += 1
        return [n+1 for n in L+R if n+1 <= distance]
    dfs(root)
    return res

# Example usage:
# root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
# print(countPairs(root, 3))  # Output: 1
