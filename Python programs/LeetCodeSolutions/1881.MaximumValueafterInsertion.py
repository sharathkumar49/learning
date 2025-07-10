"""
LeetCode 1881. Maximum Value after Insertion

Given a string n representing an integer and an integer x, insert x into n to maximize the value of the resulting integer.

Example:
Input: n = "99", x = 9
Output: "999"

Constraints:
- 1 <= n.length <= 10^5
- 1 <= x <= 9
- n consists of digits and may be negative.
"""

def maxValue(n, x):
    x = str(x)
    if n[0] == '-':
        for i in range(1, len(n)):
            if n[i] > x:
                return n[:i] + x + n[i:]
        return n + x
    else:
        for i in range(len(n)):
            if n[i] < x:
                return n[:i] + x + n[i:]
        return n + x

# Example usage:
# print(maxValue("99", 9))  # Output: "999"
