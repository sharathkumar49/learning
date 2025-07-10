"""
LeetCode 1663. Smallest String With A Given Numeric Value

Given two integers n and k, return the lexicographically smallest string of length n and numeric value k.

Example 1:
Input: n = 3, k = 27
Output: "aay"

Constraints:
- 1 <= n <= 10^5
- n <= k <= 26 * n
"""

def getSmallestString(n, k):
    res = ['a'] * n
    k -= n
    i = n - 1
    while k > 0:
        add = min(25, k)
        res[i] = chr(ord('a') + add)
        k -= add
        i -= 1
    return ''.join(res)

# Example usage:
# n = 3
# k = 27
# print(getSmallestString(n, k))  # Output: "aay"
