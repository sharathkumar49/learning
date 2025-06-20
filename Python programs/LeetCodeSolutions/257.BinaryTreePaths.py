"""
257. Binary Tree Paths
https://leetcode.com/problems/binary-tree-paths/

Given the root of a binary tree, return all root-to-leaf paths in any order.

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:
Input: root = [1]
Output: ["1"]
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreePaths(root):
    res = []
    def dfs(node, path):
        if not node:
            return
        if not node.left and not node.right:
            res.append(path + str(node.val))
        else:
            dfs(node.left, path + str(node.val) + '->')
            dfs(node.right, path + str(node.val) + '->')
    dfs(root, '')
    return res

# Example usage:
if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
    print(binaryTreePaths(root))  # Output: ['1->2->5', '1->3']
    root2 = TreeNode(1)
    print(binaryTreePaths(root2)) # Output: ['1']
