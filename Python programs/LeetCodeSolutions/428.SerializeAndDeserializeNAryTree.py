"""
428. Serialize and Deserialize N-ary Tree

Design an algorithm to serialize and deserialize an N-ary tree.
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- 0 <= Node.val <= 10^4
- The height of the n-ary tree is less than or equal to 1000
- Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.

Example:
Input: root = [1,null,3,2,4,null,5,6]
Output: The encoded data and the decoded tree should be the same as the input tree.

"""

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Codec:
    def serialize(self, root: 'Node') -> str:
        serial = []
        def dfs(node):
            if not node:
                return
            serial.append(str(node.val))
            serial.append(str(len(node.children)))
            for child in node.children:
                dfs(child)
        dfs(root)
        return ','.join(serial)

    def deserialize(self, data: str) -> 'Node':
        if not data:
            return None
        vals = iter(data.split(','))
        def dfs():
            val = int(next(vals))
            size = int(next(vals))
            node = Node(val)
            for _ in range(size):
                node.children.append(dfs())
            return node
        return dfs()

# Example usage:
# Construct N-ary tree: 1,[3,2,4],[5,6]
root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
codec = Codec()
data = codec.serialize(root)
print("Serialized:", data)
restored = codec.deserialize(data)
print("Restored root value:", restored.val)  # Output: 1
