"""
427. Construct Quad Tree

Given a n * n matrix grid of 0's and 1's only. We want to represent grid with a Quad-Tree.
Return the root of the Quad-Tree representing grid.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Each node has a value (True/False) and a flag to indicate if it is a leaf node.

Constraints:
- n == grid.length == grid[i].length
- n == 2^x where 0 <= x <= 6

Example:
Input: grid = [[0,1],[1,0]]
Output: Quad-Tree representation

"""

class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid):
        def isLeaf(x0, y0, length):
            val = grid[x0][y0]
            for i in range(x0, x0+length):
                for j in range(y0, y0+length):
                    if grid[i][j] != val:
                        return False, None
            return True, val
        def build(x0, y0, length):
            leaf, val = isLeaf(x0, y0, length)
            if leaf:
                return Node(bool(val), True)
            half = length // 2
            return Node(
                True,
                False,
                build(x0, y0, half),
                build(x0, y0+half, half),
                build(x0+half, y0, half),
                build(x0+half, y0+half, half)
            )
        n = len(grid)
        return build(0, 0, n)

# Example usage:
grid = [[0,1],[1,0]]
sol = Solution()
root = sol.construct(grid)
# The returned root is the root of the constructed Quad-Tree.
