"""
LeetCode 1981. Minimizing the Difference of Sums

Given a matrix mat, return the minimum absolute difference between the sum of elements chosen from each row and a target.

Example:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], target = 13
Output: 0

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 70
- 1 <= mat[i][j] <= 70
- 1 <= target <= 800
"""

def minimizeTheDifference(mat, target):
    m, n = len(mat), len(mat[0])
    dp = {0}
    for row in mat:
        ndp = set()
        for x in row:
            for s in dp:
                ndp.add(s + x)
        dp = set(sorted(ndp)[:target+1])
    return min(abs(s - target) for s in dp)

# Example usage:
# print(minimizeTheDifference([[1,2,3],[4,5,6],[7,8,9]], 13))  # Output: 0
