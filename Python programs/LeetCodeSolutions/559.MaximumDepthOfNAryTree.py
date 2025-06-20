'''
 559. Maximum Depth of N-ary Tree
 Difficulty: Easy

 Given a root of an N-ary tree, return its maximum depth.

 An N-ary tree is a tree in which each node has no more than N children.

 Example:
 Input: root = [1,null,3,2,4,null,5,6]
 Output: 3

 Constraints:
 The total number of nodes is in the range [0, 10^4].
 The depth of the tree is no more than 1000.
'''

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def maxDepth(root: 'Node') -> int:
    if not root:
        return 0
    return 1 + max((maxDepth(child) for child in root.children), default=0)

# Example usage
# (See LeetCode for N-ary tree construction examples)
