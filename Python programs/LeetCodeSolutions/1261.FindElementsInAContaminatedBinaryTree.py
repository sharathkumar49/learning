"""
1261. Find Elements in a Contaminated Binary Tree

Given a contaminated binary tree, recover it and implement a find method to check if a target exists in the tree.

Constraints:
- Tree nodes: 1 <= nodes <= 10^4
- -1 <= node.val <= 10^6
- 1 <= target <= 10^6

Example:
Input: root = [-1,null,-1], findElements = FindElements(root), findElements.find(1)
Output: False

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    def __init__(self, root):
        self.values = set()
        def recover(node, val):
            if not node:
                return
            node.val = val
            self.values.add(val)
            recover(node.left, 2*val+1)
            recover(node.right, 2*val+2)
        recover(root, 0)
    def find(self, target: int) -> bool:
        return target in self.values

# Example usage
if __name__ == "__main__":
    root = TreeNode(-1, None, TreeNode(-1))
    fe = FindElements(root)
    print(fe.find(1))  # Output: False
