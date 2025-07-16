"""
LeetCode 2387. Median of a Matrix

Given a matrix, return its median value.

Constraints:
- 1 <= matrix.length, matrix[0].length <= 100
"""

def matrixMedian(matrix):
    arr = [x for row in matrix for x in row]
    arr.sort()
    n = len(arr)
    return arr[n//2]

# Example usage:
# print(matrixMedian([[1,3,5],[2,6,9],[3,6,9]]))  # Output: 5
