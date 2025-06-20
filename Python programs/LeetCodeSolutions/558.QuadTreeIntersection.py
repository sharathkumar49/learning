'''
558. Quad Tree Intersection
 Difficulty: Medium

 Given two quad trees, each representing a n * n boolean grid, return a quad tree that represents the intersection (logical OR) of the two grids.

 Each node in the quad tree has the following attributes:
 - val: bool
 - isLeaf: bool
 - topLeft: Node
 - topRight: Node
 - bottomLeft: Node
 - bottomRight: Node

 The intersection should be a new quad tree representing the OR of the two input trees.

 Example:
 Input: quadTree1 and quadTree2
 Output: quadTree representing their intersection

 Constraints:
 quadTree1 and quadTree2 are both valid quad trees.

 Note: This problem requires a Node class definition for the quad tree.
'''

class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

def intersect(quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
    if quadTree1.isLeaf:
        return Node(quadTree1.val or quadTree2.val, True)
    if quadTree2.isLeaf:
        return Node(quadTree1.val or quadTree2.val, True) if quadTree2.val else quadTree1
    tl = intersect(quadTree1.topLeft, quadTree2.topLeft)
    tr = intersect(quadTree1.topRight, quadTree2.topRight)
    bl = intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
    br = intersect(quadTree1.bottomRight, quadTree2.bottomRight)
    if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val == tr.val == bl.val == br.val:
        return Node(tl.val, True)
    return Node(False, False, tl, tr, bl, br)

# Example usage
# (See LeetCode for quad tree construction examples)
