"""
431. Encode N-ary Tree to Binary Tree

Design an algorithm to encode an N-ary tree into a binary tree and decode the binary tree to get the original N-ary tree.

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- 0 <= Node.val <= 10^4
- The height of the n-ary tree is less than or equal to 1000
- Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.

Example:
Input: root = [1,null,3,2,4,null,5,6]
Output: The encoded binary tree and the decoded N-ary tree should be the same as the input tree.
"""

class NAryNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class BinaryNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def encode(self, root: 'NAryNode') -> 'BinaryNode':
        if not root:
            return None
        bRoot = BinaryNode(root.val)
        if root.children:
            bRoot.left = self.encode(root.children[0])
        curr = bRoot.left
        for child in root.children[1:]:
            curr.right = self.encode(child)
            curr = curr.right
        return bRoot

    def decode(self, data: 'BinaryNode') -> 'NAryNode':
        if not data:
            return None
        nRoot = NAryNode(data.val)
        curr = data.left
        while curr:
            nRoot.children.append(self.decode(curr))
            curr = curr.right
        return nRoot

# Example usage:
# Construct N-ary tree: 1,[3,2,4],[5,6]
nroot = NAryNode(1, [NAryNode(3, [NAryNode(5), NAryNode(6)]), NAryNode(2), NAryNode(4)])
codec = Codec()
broot = codec.encode(nroot)
restored = codec.decode(broot)
print(restored.val)  # Output: 1
