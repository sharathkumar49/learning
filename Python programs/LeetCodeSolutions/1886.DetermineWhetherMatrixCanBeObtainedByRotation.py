"""
LeetCode 1886. Determine Whether Matrix Can Be Obtained By Rotation

Given two n x n binary matrices mat and target, return true if mat can be obtained by rotating target 0, 90, 180, or 270 degrees.

Example:
Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true

Constraints:
- n == mat.length == target.length
- 1 <= n <= 10
- mat[i][j], target[i][j] is 0 or 1
"""

def findRotation(mat, target):
    for _ in range(4):
        if mat == target:
            return True
        mat = [list(row) for row in zip(*mat[::-1])]
    return False

# Example usage:
# print(findRotation([[0,1],[1,0]], [[1,0],[0,1]]))  # Output: True
