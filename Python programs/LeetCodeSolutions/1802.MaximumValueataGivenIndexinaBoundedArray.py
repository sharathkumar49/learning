"""
LeetCode 1802. Maximum Value at a Given Index in a Bounded Array

Given n, index, and maxSum, return the maximum value at index such that the sum of the array does not exceed maxSum and all elements are positive integers.

Example 1:
Input: n = 4, index = 2, maxSum = 6
Output: 2

Constraints:
- 1 <= n <= maxSum <= 10^9
- 0 <= index < n
"""

def maxValue(n, index, maxSum):
    def calc(x, cnt):
        if x > cnt:
            return (x+cnt)*(cnt+1)//2 - cnt*(cnt+1)//2
        else:
            return (x+1)*x//2 + cnt-x
    l, r = 1, maxSum
    while l < r:
        m = (l+r+1)//2
        if calc(m-1, index) + calc(m-1, n-index-1) + m > maxSum:
            r = m-1
        else:
            l = m
    return l

# Example usage:
# n = 4
# index = 2
# maxSum = 6
# print(maxValue(n, index, maxSum))  # Output: 2
