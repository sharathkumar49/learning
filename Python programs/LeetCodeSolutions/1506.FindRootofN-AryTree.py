"""
LeetCode 1506. Find Root of N-Ary Tree

Given all the nodes of an N-ary tree as an array Node[], return the root node of the tree.

Constraints:
- The total number of nodes is between [1, 10^4].
- Each node has a unique value.

Example:
Input: nodes = [1,2,3,4,5,6]
Output: root node
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def findRoot(tree):
    seen = set()
    for node in tree:
        for child in node.children:
            seen.add(child)
    for node in tree:
        if node not in seen:
            return node

# Example usage:
# nodes = [Node(1), Node(2), Node(3)]
# ... (set up children)
# root = findRoot(nodes)
