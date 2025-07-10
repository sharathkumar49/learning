"""
LeetCode 1727. Largest Submatrix With Rearrangements

Given a binary matrix, you can rearrange the columns of each row. Return the area of the largest submatrix containing only 1's after rearrangements.

Example 1:
Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
Output: 4

Constraints:
- 1 <= matrix.length, matrix[i].length <= 10^5
- matrix[i][j] is 0 or 1
"""

def largestSubmatrix(matrix):
    m, n = len(matrix), len(matrix[0])
    for i in range(1, m):
        for j in range(n):
            if matrix[i][j]:
                matrix[i][j] += matrix[i-1][j]
    res = 0
    for row in matrix:
        row.sort(reverse=True)
        for i, h in enumerate(row):
            res = max(res, h * (i+1))
    return res

# Example usage:
# matrix = [[0,0,1],[1,1,1],[1,0,1]]
# print(largestSubmatrix(matrix))  # Output: 4
