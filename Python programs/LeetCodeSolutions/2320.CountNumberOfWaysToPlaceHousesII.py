"""
LeetCode 2320. Count Number of Ways to Place Houses II

Given n, return the number of ways to place houses on both sides of the street.

Example:
Input: n = 2
Output: 9

Constraints:
- 1 <= n <= 1000
"""

def countHousePlacements(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return b * b

# Example usage:
# print(countHousePlacements(2))  # Output: 9
