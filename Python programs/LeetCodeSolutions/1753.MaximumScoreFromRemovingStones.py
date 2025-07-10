"""
LeetCode 1753. Maximum Score From Removing Stones

You are given three piles of stones. In each move, you can remove a stone from two different non-empty piles. Return the maximum score you can get.

Example 1:
Input: a = 2, b = 4, c = 6
Output: 6

Constraints:
- 1 <= a, b, c <= 10^5
"""

def maximumScore(a, b, c):
    arr = sorted([a, b, c])
    if arr[0] + arr[1] <= arr[2]:
        return arr[0] + arr[1]
    return (a + b + c) // 2

# Example usage:
# a = 2
# b = 4
# c = 6
# print(maximumScore(a, b, c))  # Output: 6
