"""
1145. Binary Tree Coloring Game

Two players play a coloring game on a binary tree. The first player colors a node with value x, and the second player colors another node. Players alternate turns coloring uncolored neighbors. Return True if the second player can win, else False.

Constraints:
- The number of nodes in the tree is between 1 and 100.
- Node values are unique and range from 1 to n.
- 1 <= x <= n <= 100

Example:
Input: root = [1,2,3,4,5,6,7], n = 7, x = 3
Output: True

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def btreeGameWinningMove(root, n, x):
    def count(node):
        if not node:
            return 0
        return 1 + count(node.left) + count(node.right)
    def find(node):
        if not node:
            return None
        if node.val == x:
            return node
        return find(node.left) or find(node.right)
    xNode = find(root)
    left = count(xNode.left)
    right = count(xNode.right)
    parent = n - (left + right + 1)
    return max(left, right, parent) > n // 2

# Example usage
if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)),
                       TreeNode(3, TreeNode(6), TreeNode(7)))
    print(btreeGameWinningMove(root, 7, 3))  # Output: True
