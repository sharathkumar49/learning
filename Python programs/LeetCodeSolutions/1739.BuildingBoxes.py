"""
LeetCode 1739. Building Boxes

Given n boxes, return the minimum number of boxes needed to build a pyramid with n boxes.

Example 1:
Input: n = 3
Output: 3

Constraints:
- 1 <= n <= 10^9
"""

def minimumBoxes(n):
    import math
    h = int((2*n)**(1/3))
    while h*(h+1)*(h+2)//6 > n:
        h -= 1
    left = n - h*(h+1)*(h+2)//6
    l = 0
    while l*(l+1)//2 < left:
        l += 1
    return h*(h+1)//2 + l

# Example usage:
# n = 3
# print(minimumBoxes(3))  # Output: 3
