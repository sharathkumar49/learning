"""
LeetCode 1823. Find the Winner of the Circular Game

Given n friends in a circle and an integer k, return the winner of the game as described in the problem.

Example 1:
Input: n = 5, k = 2
Output: 3

Constraints:
- 1 <= k <= n <= 500
"""

def findTheWinner(n, k):
    friends = list(range(1, n+1))
    idx = 0
    while len(friends) > 1:
        idx = (idx + k - 1) % len(friends)
        friends.pop(idx)
    return friends[0]

# Example usage:
# n = 5
# k = 2
# print(findTheWinner(n, k))  # Output: 3
