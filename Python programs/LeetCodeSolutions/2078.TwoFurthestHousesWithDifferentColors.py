"""
LeetCode 2078. Two Furthest Houses With Different Colors

Given an array colors, return the maximum distance between two houses with different colors.

Example:
Input: colors = [1,1,1,6,1,1,1]
Output: 3

Constraints:
- 2 <= colors.length <= 100
- 1 <= colors[i] <= 100
"""

def maxDistance(colors):
    n = len(colors)
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            if colors[i] != colors[j]:
                res = max(res, j-i)
    return res

# Example usage:
# print(maxDistance([1,1,1,6,1,1,1]))  # Output: 3
