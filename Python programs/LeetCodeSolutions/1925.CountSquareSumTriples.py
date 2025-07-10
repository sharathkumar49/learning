"""
LeetCode 1925. Count Square Sum Triples

Given an integer n, return the number of square sum triples (a, b, c) such that a^2 + b^2 = c^2 and 1 <= a, b, c <= n.

Example:
Input: n = 5
Output: 2

Constraints:
- 1 <= n <= 250
"""

def countTriples(n):
    res = 0
    for a in range(1, n+1):
        for b in range(1, n+1):
            c = (a*a + b*b) ** 0.5
            if c.is_integer() and c <= n:
                res += 1
    return res

# Example usage:
# print(countTriples(5))  # Output: 2
