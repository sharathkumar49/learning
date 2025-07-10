"""
LeetCode 1522. Diameter of N-Ary Tree

Given the root of an N-ary tree, return the diameter of the tree.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- Each node's value is between [1, 10^4].

Example:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,9,10,null,null,11,12,null,13,null,14]
Output: 7
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def diameter(root):
    res = 0
    def dfs(node):
        nonlocal res
        if not node:
            return 0
        max1 = max2 = 0
        for child in node.children:
            d = dfs(child)
            if d > max1:
                max1, max2 = d, max1
            elif d > max2:
                max2 = d
        res = max(res, max1 + max2)
        return max1 + 1
    dfs(root)
    return res

# Example usage:
# root = Node(1, [Node(2), Node(3), Node(4), Node(5)])
# print(diameter(root))
