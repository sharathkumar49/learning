"""
LeetCode 2485. Find the Pivot Integer

Given n, return the pivot integer such that the sum of all numbers to the left equals the sum to the right.

Constraints:
- 1 <= n <= 1000
"""

def pivotInteger(n):
    total = n*(n+1)//2
    curr = 0
    for x in range(1, n+1):
        curr += x
        if curr == total-curr+x:
            return x
    return -1

# Example usage:
# print(pivotInteger(8))  # Output: 6
