"""
LeetCode 2064. Minimized Maximum of Products Distributed to Any Store

Given n stores and quantities of products, return the minimized maximum number of products in any store after distributing them.

Example:
Input: n = 6, quantities = [11,6]
Output: 3

Constraints:
- 1 <= n <= 10^5
- 1 <= quantities.length <= 10^5
- 1 <= quantities[i] <= 10^9
"""

def minimizedMaximum(n, quantities):
    def check(x):
        return sum((q + x - 1) // x for q in quantities) <= n
    l, r = 1, max(quantities)
    while l < r:
        m = (l + r) // 2
        if check(m):
            r = m
        else:
            l = m + 1
    return l

# Example usage:
# print(minimizedMaximum(6, [11,6]))  # Output: 3
