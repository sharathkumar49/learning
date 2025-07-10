"""
LeetCode 2048. Next Greater Numerically Balanced Number

Given an integer n, return the smallest numerically balanced number strictly greater than n.
A numerically balanced number is an integer where, for every digit d in the number, the count of d in the number is exactly d.

Example:
Input: n = 1
Output: 22

Constraints:
- 0 <= n <= 10^6
"""

def nextBeautifulNumber(n):
    def is_balanced(x):
        from collections import Counter
        c = Counter(str(x))
        return all(c[str(d)] == d for d in c)
    x = n + 1
    while True:
        if is_balanced(x):
            return x
        x += 1

# Example usage:
# print(nextBeautifulNumber(1))  # Output: 22
