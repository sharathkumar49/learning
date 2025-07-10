"""
LeetCode 1533. Find the Index of the Large Integer

This is an interactive problem. Given an array of n elements, you can compare the sum of elements in two subarrays. Return the index of the largest integer.

Constraints:
- 1 <= n <= 100

Example:
Input: n = 3, arr = [1,2,3]
Output: 2
"""
# This is a placeholder for the interactive problem. In practice, you would use the provided API to compare subarrays.
def getIndex(n, compareSub):
    l, r = 0, n-1
    while l < r:
        m = (l + r) // 2
        if (r - l + 1) % 2 == 0:
            res = compareSub(l, m, m+1, r)
            if res == 1:
                r = m
            else:
                l = m+1
        else:
            res = compareSub(l, m-1, m+1, r)
            if res == 1:
                r = m-1
            elif res == -1:
                l = m+1
            else:
                return m
    return l

# Example usage:
# def compareSub(l1, r1, l2, r2): ...
# print(getIndex(n, compareSub))
