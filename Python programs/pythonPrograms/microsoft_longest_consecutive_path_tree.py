# Microsoft: Find the Longest Consecutive Path in a Binary Tree
# Given a binary tree, find the length of the longest consecutive path (parent to child, increasing by 1).
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def longest_consecutive(root):
    def dfs(node, parent_val, length):
        if not node:
            return length
        if node.val == parent_val + 1:
            left = dfs(node.left, node.val, length + 1)
            right = dfs(node.right, node.val, length + 1)
            return max(left, right)
        else:
            left = dfs(node.left, node.val, 1)
            right = dfs(node.right, node.val, 1)
            return max(length, left, right)
    if not root:
        return 0
    return max(dfs(root, root.val - 1, 0), 1)

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)
    print(longest_consecutive(root))  # Output: 3
