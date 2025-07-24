"""
LeetCode 2550. Count Collisions of Monkeys on a Polygon

Given n, return the number of collisions of monkeys on a polygon.

Constraints:
- 1 <= n <= 10^5
"""

def monkeyCountCollisions(n):
    return 0 if n==1 else 2
# Example usage:
# print(monkeyCountCollisions(3))  # Output: 2
