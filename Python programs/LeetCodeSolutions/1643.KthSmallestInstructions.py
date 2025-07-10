"""
LeetCode 1643. Kth Smallest Instructions

Given two integers n and m and an integer k, return the kth lexicographically smallest instructions to reach (n, m) from (0, 0) by moving right (H) and down (V).

Example 1:
Input: n = 2, m = 3, k = 3
Output: "HHVHV"

Constraints:
- 1 <= n, m <= 15
- 1 <= k <= comb(n+m, n)
"""

def kthSmallestPath(destination, k):
    from math import comb
    n, m = destination
    res = []
    for _ in range(n+m):
        if m == 0:
            res.append('V')
            n -= 1
        elif n == 0:
            res.append('H')
            m -= 1
        else:
            c = comb(n+m-1, n)
            if k <= c:
                res.append('H')
                m -= 1
            else:
                res.append('V')
                n -= 1
                k -= c
    return ''.join(res)

# Example usage:
# destination = [2,3]
# k = 3
# print(kthSmallestPath(destination, k))  # Output: "HHVHV"
