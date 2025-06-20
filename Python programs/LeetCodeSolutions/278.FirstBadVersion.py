"""
278. First Bad Version
https://leetcode.com/problems/first-bad-version/

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Given n versions [1, 2, ..., n], find the first bad one.

Constraints:
- 1 <= bad <= n <= 2^31 - 1

Example 1:
Input: n = 5, bad = 4
Output: 4

Example 2:
Input: n = 1, bad = 1
Output: 1
"""
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def firstBadVersion(n):
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left

# Example usage (requires isBadVersion API):
# Not executable as-is without isBadVersion() implementation.
