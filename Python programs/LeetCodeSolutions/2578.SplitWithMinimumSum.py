"""
LeetCode 2578. Split With Minimum Sum

Given a number, split it into two numbers with minimum sum.

Constraints:
- 10 <= num <= 10^9
"""

def splitNum(num):
    digits = sorted(str(num))
    a, b = '', ''
    for i, d in enumerate(digits):
        if i%2==0:
            a += d
        else:
            b += d
    return int(a)+int(b)
# Example usage:
# print(splitNum(4325))  # Output: 59
