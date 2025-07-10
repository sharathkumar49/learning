"""
LeetCode 1884. Egg Drop With 2 Eggs and N Floors

You are given two eggs and n floors. Return the minimum number of moves required to find the critical floor.

Example:
Input: n = 100
Output: 14

Constraints:
- 1 <= n <= 1000
"""

def twoEggDrop(n):
    # Find the smallest x such that x + (x-1) + ... + 1 >= n
    x = 0
    while x * (x + 1) // 2 < n:
        x += 1
    return x

# Example usage:
# print(twoEggDrop(100))  # Output: 14
