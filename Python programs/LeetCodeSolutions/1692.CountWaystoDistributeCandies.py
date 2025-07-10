"""
LeetCode 1692. Count Ways to Distribute Candies

Given n candies and k boxes, return the number of ways to distribute the candies such that no box is empty.

Example 1:
Input: n = 3, k = 2
Output: 2

Constraints:
- 1 <= k <= n <= 1000
"""

def waysToDistribute(n, k):
    from math import comb
    return comb(n-1, k-1)

# Example usage:
# n = 3
# k = 2
# print(waysToDistribute(n, k))  # Output: 2
