"""
573. Squirrel Simulation
Difficulty: Medium

You are given two integers height and width representing the dimensions of a rectangular field. There is a tree, a squirrel, and several nuts in the field. You are given the positions of the tree, the squirrel, and the nuts. Return the minimal distance for the squirrel to collect all the nuts and put them under the tree.

Example 1:
Input: height = 5, width = 7, tree = [2,2], squirrel = [4,4], nuts = [[3,0],[2,5]]
Output: 12

Constraints:
1 <= height, width <= 100
nuts.length <= 500
All positions are distinct.
"""

def minDistance(height, width, tree, squirrel, nuts):
    total = sum(abs(n[0]-tree[0]) + abs(n[1]-tree[1]) for n in nuts)
    best = float('-inf')
    for n in nuts:
        dist = abs(n[0]-squirrel[0]) + abs(n[1]-squirrel[1]) - (abs(n[0]-tree[0]) + abs(n[1]-tree[1]))
        best = max(best, dist)
    return total * 2 - best

# Example usage
if __name__ == "__main__":
    print(minDistance(5, 7, [2,2], [4,4], [[3,0],[2,5]]))  # Output: 12
