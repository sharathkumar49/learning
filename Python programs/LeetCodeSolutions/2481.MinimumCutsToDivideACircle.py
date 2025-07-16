"""
LeetCode 2481. Minimum Cuts to Divide a Circle

Given n, return the minimum cuts to divide a circle into n pieces.

Constraints:
- 1 <= n <= 100
"""

def minCuts(n):
    if n == 1:
        return 0
    if n%2 == 0:
        return n//2
    return n

# Example usage:
# print(minCuts(4))  # Output: 2
