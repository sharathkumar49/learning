"""
LeetCode 2554. Maximum Number of Integers to Choose From a Range I

Given banned numbers and a range, return the maximum number of integers to choose.

Constraints:
- 1 <= banned.length <= 10^5
- 1 <= n, maxSum <= 10^9
"""

def maxCount(banned, n, maxSum):
    banned = set(banned)
    res = s = 0
    for i in range(1, n+1):
        if i in banned:
            continue
        if s+i > maxSum:
            break
        s += i
        res += 1
    return res
# Example usage:
# print(maxCount([1,6,5], 5, 6))  # Output: 2
