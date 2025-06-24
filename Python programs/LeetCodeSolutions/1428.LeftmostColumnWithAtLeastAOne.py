"""
LeetCode 1428. Leftmost Column with at Least a One

(This is a binary matrix problem with a custom interface, but here is a simplified version for practice.)
Given a binary matrix, return the index of the leftmost column with at least a one. If such a column doesn't exist, return -1.

Constraints:
- 1 <= matrix.length, matrix[i].length <= 100
- matrix[i][j] is 0 or 1

Example:
Input: matrix = [[0,0],[1,1]]
Output: 0
"""
def leftMostColumnWithOne(matrix):
    m, n = len(matrix), len(matrix[0])
    res = n
    for row in matrix:
        for j in range(n):
            if row[j] == 1:
                res = min(res, j)
                break
    return res if res < n else -1

# Example usage:
matrix = [[0,0],[1,1]]
print(leftMostColumnWithOne(matrix))  # Output: 0
