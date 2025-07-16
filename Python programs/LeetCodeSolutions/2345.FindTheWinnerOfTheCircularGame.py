"""
LeetCode 2345. Find the Winner of the Circular Game

Given n and k, return the winner of the circular game.

Example:
Input: n = 5, k = 2
Output: 3

Constraints:
- 1 <= n <= 1000
- 1 <= k <= n
"""

def findTheWinner(n, k):
    res = 0
    for i in range(1, n+1):
        res = (res + k) % i
    return res + 1

# Example usage:
# print(findTheWinner(5, 2))  # Output: 3
