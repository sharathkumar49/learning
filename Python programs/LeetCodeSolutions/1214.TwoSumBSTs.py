"""
1214. Two Sum BSTs

Given two binary search trees, return True if there exists a node from each tree such that their values sum up to a target.

Constraints:
- The number of nodes in each tree is between 1 and 5000.
- -10^9 <= Node.val <= 10^9
- -10^9 <= target <= 10^9

Example:
Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: True

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def twoSumBSTs(root1, root2, target):
    def inorder(node):
        if not node:
            return set()
        return inorder(node.left) | {node.val} | inorder(node.right)
    s1 = inorder(root1)
    s2 = inorder(root2)
    for v in s1:
        if target - v in s2:
            return True
    return False

# Example usage
if __name__ == "__main__":
    r1 = TreeNode(2, TreeNode(1), TreeNode(4))
    r2 = TreeNode(1, TreeNode(0), TreeNode(3))
    print(twoSumBSTs(r1, r2, 5))  # Output: True
