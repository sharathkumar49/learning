"""
LeetCode 2624. Snail Traversal

Given a matrix, return its snail traversal.

Constraints:
- 1 <= matrix.length, matrix[0].length <= 100
"""

def snail(matrix):
    res = []
    while matrix:
        res += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                res.append(row.pop())
        if matrix:
            res += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                res.append(row.pop(0))
    return res
# Example usage:
# print(snail([[1,2,3],[4,5,6],[7,8,9]]))  # Output: [1,2,3,6,9,8,7,4,5]
