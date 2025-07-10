"""
LeetCode 2022. Convert 1D Array Into 2D Array

Given a 1D array and two integers m and n, reshape the array into a 2D array with m rows and n columns.

Example:
Input: original = [1,2,3,4], m = 2, n = 2
Output: [[1,2],[3,4]]

Constraints:
- 1 <= original.length <= 5 * 10^4
- 1 <= m, n <= 4 * 10^4
- original.length == m * n
"""

def construct2DArray(original, m, n):
    if len(original) != m * n:
        return []
    return [original[i*n:(i+1)*n] for i in range(m)]

# Example usage:
# print(construct2DArray([1,2,3,4], 2, 2))  # Output: [[1,2],[3,4]]
