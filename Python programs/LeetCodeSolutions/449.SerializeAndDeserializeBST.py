"""
449. Serialize and Deserialize BST

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a BST can be serialized to a string and this string can be deserialized to the original tree structure.

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- 0 <= Node.val <= 10^4
- The input tree is guaranteed to be a binary search tree.

Example:
Input: root = [2,1,3]
Output: The encoded data and the decoded tree should be the same as the input tree.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: TreeNode) -> str:
        vals = []
        def preorder(node):
            if node:
                vals.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return ' '.join(vals)

    def deserialize(self, data: str) -> TreeNode:
        vals = list(map(int, data.split()))
        def build(lower, upper):
            if vals and lower < vals[0] < upper:
                val = vals.pop(0)
                node = TreeNode(val)
                node.left = build(lower, val)
                node.right = build(val, upper)
                return node
            return None
        return build(float('-inf'), float('inf'))

# Example usage:
# Construct BST: 2,1,3
root = TreeNode(2, TreeNode(1), TreeNode(3))
codec = Codec()
data = codec.serialize(root)
print("Serialized:", data)
restored = codec.deserialize(data)
print("Restored root value:", restored.val)  # Output: 2
