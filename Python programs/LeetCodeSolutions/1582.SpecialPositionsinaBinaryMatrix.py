"""
LeetCode 1582. Special Positions in a Binary Matrix

Given a rows x cols binary matrix mat, return the number of special positions in the matrix. A position (i, j) is special if mat[i][j] == 1 and all other elements in row i and column j are 0.

Example 1:
Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1

Constraints:
- 1 <= mat.length, mat[i].length <= 100
- mat[i][j] is either 0 or 1.
"""

def numSpecial(mat):
    rows = [sum(row) for row in mat]
    cols = [sum(col) for col in zip(*mat)]
    res = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                res += 1
    return res

# Example usage:
# mat = [[1,0,0],[0,0,1],[1,0,0]]
# print(numSpecial(mat))  # Output: 1
