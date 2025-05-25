# Amazon: Serialize and Deserialize Binary Tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def serialize(root):
    vals = []
    def helper(node):
        if node:
            vals.append(str(node.val))
            helper(node.left)
            helper(node.right)
        else:
            vals.append('#')
    helper(root)
    return ' '.join(vals)

def deserialize(data):
    vals = iter(data.split())
    def helper():
        val = next(vals)
        if val == '#':
            return None
        node = Node(int(val))
        node.left = helper()
        node.right = helper()
        return node
    return helper()

if __name__ == "__main__":
    a = Node(1); b = Node(2); c = Node(3)
    a.left = b; a.right = c
    s = serialize(a)
    print("Serialized:", s)
    root = deserialize(s)
    print("Root value after deserialization:", root.val)
